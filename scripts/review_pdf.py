#!/usr/bin/env python3
"""Render book pages or figure assets into bounded, labelled contact sheets."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader


def selected_pages(spec, total):
    if not spec:
        return list(range(1, total + 1))
    result = set()
    for term in spec.split(','):
        parts = term.strip().split('-')
        if len(parts) == 1:
            first = last = int(parts[0])
        elif len(parts) == 2:
            first, last = map(int, parts)
        else:
            raise ValueError(f'Invalid page selection: {term}')
        if not 1 <= first <= last <= total:
            raise ValueError(f'Page range {term} is outside 1..{total}.')
        result.update(range(first, last + 1))
    return sorted(result)


def sheets(items, out, per_sheet=16):
    try:
        font = ImageFont.load_default(size=14)
    except TypeError:
        font = ImageFont.load_default()
    paths = []
    for old in out.glob('review-sheet-*.jpg'):
        old.unlink()
    for start in range(0, len(items), per_sheet):
        group = items[start:start + per_sheet]
        columns = 4
        cw, ch = 300, 450
        canvas = Image.new('RGB', (columns * cw, ((len(group) + columns - 1) // columns) * ch), '#e6ebee')
        draw = ImageDraw.Draw(canvas)
        for i, (label, path) in enumerate(group):
            with Image.open(path) as source:
                im = source.convert('RGB')
            im.thumbnail((cw - 16, ch - 38))
            x, y = i % columns * cw, i // columns * ch
            canvas.paste(im, (x + (cw - im.width) // 2, y + 32))
            draw.text((x + 8, y + 8), label[:38], fill='#203443', font=font)
        target = out / f'review-sheet-{start // per_sheet + 1:03d}.jpg'
        canvas.save(target, quality=90)
        paths.append(str(target))
    return paths


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path, nargs='?')
    parser.add_argument('--images', type=Path, nargs='+', help='Review actual crop/new-figure raster assets instead of a book.')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--pages', help='1-based selection, e.g. 1,3-8; default all PDF pages.')
    parser.add_argument('--scale', type=int, default=1100)
    args = parser.parse_args()
    if bool(args.pdf) == bool(args.images):
        parser.error('Provide either a PDF or --images, but not both.')
    if args.scale < 300:
        parser.error('--scale must be at least 300 pixels.')
    if args.images and args.pages:
        parser.error('--pages applies only to a PDF.')
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    try:
        items = []
        if args.images:
            items = [(path.name, path.resolve(strict=True)) for path in args.images]
            report = {'mode': 'images', 'assets': [str(p) for _, p in items]}
        else:
            renderer = shutil.which('pdftoppm')
            if not renderer:
                raise RuntimeError('pdftoppm is required to render PDF pages.')
            pdf = args.pdf.resolve(strict=True)
            reader = PdfReader(pdf)
            pages = selected_pages(args.pages, len(reader.pages))
            report = {'mode': 'pdf', 'pdf': str(pdf), 'total_pages': len(reader.pages),
                      'rendered_pages': pages, 'bytes': pdf.stat().st_size,
                      'text_diagnostics_are_heuristics': True, 'pages': []}
            for page_number in pages:
                page = reader.pages[page_number - 1]
                text = page.extract_text() or ''
                report['pages'].append({'pdf_page': page_number, 'text_characters': len(text.strip()),
                                        'replacement_characters': text.count('\ufffd'),
                                        'double_question_marks': text.count('??'),
                                        'short_searchable_text': len(text.strip()) < 150})
                base = out / f'page-{page_number:04d}'
                subprocess.run([renderer, '-f', str(page_number), '-l', str(page_number),
                                '-scale-to', str(args.scale), '-singlefile', '-png', str(pdf), str(base)],
                               check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
                items.append((f'PDF page {page_number}', base.with_suffix('.png')))
        report['contact_sheets'] = sheets(items, out)
        report['visual_review'] = 'pending: rendering does not establish visual inspection or technical correctness'
        report['review_required'] = 'Open all contact sheets and inspect dense/new/suspicious pages or assets at readable resolution.'
        target = out / 'review-report.json'
        target.write_text(json.dumps(report, indent=2), encoding='utf-8')
        print(json.dumps({'report': str(target), 'rendered_items': len(items), 'contact_sheets': report['contact_sheets']}, indent=2))
        return 0
    except (ValueError, OSError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f'Error: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
