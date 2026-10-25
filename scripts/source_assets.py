#!/usr/bin/env python3
"""Inventory immutable PDF sources and create provenance-linked upright crops."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def slug(value: str) -> str:
    return re.sub(r'[^a-zA-Z0-9-]+', '-', value).strip('-')[:60] or 'source'


def read_pdf(path: Path):
    reader = PdfReader(path)
    if reader.is_encrypted and not reader.decrypt(''):
        raise ValueError(f'Password-protected PDF requires an authorized decrypted working copy: {path}')
    return reader


def inventory(args):
    out = args.out.resolve()
    if (out / 'inventory.json').exists():
        raise FileExistsError('Inventory baseline already exists; use a new output directory to preserve it.')
    sources = list(dict.fromkeys(p.resolve(strict=True) for p in args.sources))
    records = []
    out.mkdir(parents=True, exist_ok=True)
    for source in sources:
        source_hash = digest(source)
        source_id = f'{slug(source.stem)}-{source_hash[:8]}'
        reader = read_pdf(source)
        text_parts, pages = [], []
        for number, page in enumerate(reader.pages, 1):
            text = page.extract_text() or ''
            text_parts.append(f'\n=== SOURCE {source.name} | PDF PAGE {number} ===\n{text}\n')
            pages.append({'pdf_page': number, 'rotation': page.rotation,
                          'media_box': [float(x) for x in page.mediabox],
                          'visible_crop_box': [float(x) for x in page.cropbox],
                          'text_characters': len(text.strip()),
                          'needs_visual_or_ocr_review': len(text.strip()) < 30})
        text_path = out / f'{source_id}.txt'
        text_path.write_text(''.join(text_parts), encoding='utf-8')
        records.append({'id': source_id, 'path': str(source), 'sha256': source_hash,
                        'bytes': source.stat().st_size, 'page_count': len(reader.pages),
                        'numbered_text': text_path.name, 'pages': pages})
    target = out / 'inventory.json'
    target.write_text(json.dumps({'schema_version': 1, 'sources': records}, indent=2), encoding='utf-8')
    print(json.dumps({'inventory': str(target), 'sources': len(records),
                      'total_pages': sum(r['page_count'] for r in records)}, indent=2))


def verify(args):
    data = json.loads(args.inventory.read_text(encoding='utf-8'))
    failures = []
    for source in data['sources']:
        path = Path(source['path'])
        if not path.is_file() or digest(path) != source['sha256']:
            failures.append(str(path))
    print(json.dumps({'verified_sources': len(data['sources']) - len(failures),
                      'changed_or_missing': failures}, indent=2))
    return bool(failures)


def crop(args):
    source = args.source.resolve(strict=True)
    left, top, right, bottom = args.bounds
    if not (0 <= left < right <= 1 and 0 <= top < bottom <= 1):
        raise ValueError('Bounds must satisfy 0 <= left < right <= 1 and 0 <= top < bottom <= 1.')
    if args.dpi < 72 or args.dpi > 1200:
        raise ValueError('DPI must be between 72 and 1200.')
    renderer = shutil.which('pdftoppm')
    if not renderer:
        raise RuntimeError('pdftoppm is required to produce and verify the crop PNG.')
    reader = read_pdf(source)
    if not 1 <= args.page <= len(reader.pages):
        raise ValueError(f'Page must be 1..{len(reader.pages)} (1-based PDF page).')
    page = reader.pages[args.page - 1]
    original_rotation = page.rotation
    if original_rotation:
        page.transfer_rotation_to_content()
    base = page.cropbox
    x0, y0, width, height = float(base.left), float(base.bottom), float(base.width), float(base.height)
    rect = RectangleObject([x0 + left * width, y0 + (1 - bottom) * height,
                            x0 + right * width, y0 + (1 - top) * height])
    page.mediabox = rect
    page.cropbox = rect
    source_hash = digest(source)
    signature = hashlib.sha256(json.dumps([source_hash, args.page, args.bounds, args.dpi]).encode()).hexdigest()[:12]
    stem = f'{slug(source.stem)}-p{args.page:04d}-{signature}'
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    pdf_path, png_path = out / f'{stem}.pdf', out / f'{stem}.png'
    if pdf_path == source:
        raise ValueError('A crop output must not overwrite its source.')
    writer = PdfWriter()
    writer.add_page(page)
    with pdf_path.open('wb') as stream:
        writer.write(stream)
    subprocess.run([renderer, '-cropbox', '-r', str(args.dpi), '-singlefile', '-png',
                    str(pdf_path), str(out / stem)], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    record = {'source': str(source), 'source_sha256': source_hash, 'pdf_page': args.page,
              'bounds': args.bounds, 'bounds_basis': 'upright visible CropBox, normalized left/top/right/bottom',
              'original_rotation': original_rotation, 'crop_size_pt': [float(rect.width), float(rect.height)],
              'dpi': args.dpi, 'crop_pdf': str(pdf_path), 'png': str(png_path),
              'visual_review': 'pending: inspect actual PNG and final display size'}
    record_path = out / f'{stem}.json'
    record_path.write_text(json.dumps(record, indent=2), encoding='utf-8')
    print(json.dumps({'record': str(record_path), **record}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('inventory', help='Create a hash baseline and page-numbered text for explicit source PDFs.')
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('sources', type=Path, nargs='+')
    p.set_defaults(run=inventory)
    p = sub.add_parser('verify', help='Check source hashes against the initial inventory.')
    p.add_argument('inventory', type=Path)
    p.set_defaults(run=verify)
    p = sub.add_parser('crop', help='Render a measured crop from an upright visible source page.')
    p.add_argument('--source', type=Path, required=True)
    p.add_argument('--page', type=int, required=True)
    p.add_argument('--bounds', type=float, nargs=4, metavar=('LEFT', 'TOP', 'RIGHT', 'BOTTOM'), required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--dpi', type=int, default=300)
    p.set_defaults(run=crop)
    args = parser.parse_args()
    try:
        return int(args.run(args) or 0)
    except (ValueError, OSError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f'Error: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
