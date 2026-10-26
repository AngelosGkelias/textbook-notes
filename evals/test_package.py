#!/usr/bin/env python3
"""Mechanical package/helper regressions. These do not grade teaching quality."""
from __future__ import annotations
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

SKILL=Path(__file__).resolve().parents[1]
PDF_DEPS=all(importlib.util.find_spec(x) for x in ('pypdf','PIL','reportlab'))


class PackageTests(unittest.TestCase):
    def test_local_references_resolve(self):
        for path in SKILL.rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
                if '://' in target or target.startswith('#'): continue
                self.assertTrue((path.parent/target.split('#')[0]).exists(),f'{path}: {target}')

    def test_references_are_discoverable(self):
        reached={SKILL/'SKILL.md'}
        pending=list(reached)
        while pending:
            p=pending.pop()
            for target in re.findall(r'\]\(([^)]+\.md)\)',p.read_text()):
                if '://' in target: continue
                q=(p.parent/target).resolve()
                if q not in reached:
                    reached.add(q)
                    pending.append(q)
        self.assertTrue(set((SKILL/'references').glob('*.md')) <= reached)

    def test_demo_curve_reproduces_exactly(self):
        path=SKILL/'assets/typst-starter/generate_demo_curve.py'
        spec=importlib.util.spec_from_file_location('curve',path)
        module=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(module.svg(),path.with_name('demo-curve.svg').read_text())
        self.assertAlmostEqual(module.response(0),0)
        self.assertAlmostEqual(module.response(1),0.6321205588285577)
        self.assertLess(module.response(5),1)


@unittest.skipUnless(PDF_DEPS and shutil.which('pdftoppm'),'PDF dependencies or Poppler unavailable')
class PDFHelperTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='notes-package-')
        self.root=Path(self.tmp.name)
        self.fixture=self.root/'fixture'
        self.run_script(SKILL/'evals/make_fixtures.py','--out',self.fixture)
        self.source=self.fixture/'micro.pdf'

    def tearDown(self):
        self.tmp.cleanup()

    def run_script(self,path,*args,ok=True):
        result=subprocess.run([sys.executable,str(path),*map(str,args)],capture_output=True,text=True)
        self.assertEqual(result.returncode==0,ok,result.stdout+result.stderr)
        return result

    def inventory(self):
        out=self.root/'inventory'
        self.run_script(SKILL/'scripts/source_assets.py','inventory','--out',out,self.source)
        return out

    def test_inventory_and_hash_verification(self):
        out=self.inventory()
        data=json.loads((out/'inventory.json').read_text())
        record=data['sources'][0]
        self.assertEqual(record['page_count'],7)
        text=(out/record['numbered_text']).read_text()
        self.assertIn('PDF PAGE 7',text)
        self.assertIn('lock ordering',text)
        self.run_script(SKILL/'scripts/source_assets.py','verify',out/'inventory.json')
        self.source.write_bytes(self.source.read_bytes()+b'\n% altered\n')
        result=self.run_script(SKILL/'scripts/source_assets.py','verify',out/'inventory.json',ok=False)
        self.assertIn(str(self.source),result.stdout)

    def test_inventory_does_not_replace_baseline(self):
        out=self.inventory()
        before=(out/'inventory.json').read_bytes()
        self.run_script(SKILL/'scripts/source_assets.py','inventory','--out',out,self.source,ok=False)
        self.assertEqual(before,(out/'inventory.json').read_bytes())

    def test_crop_provenance_and_bad_bounds(self):
        from PIL import Image
        out=self.root/'crop'
        before=hashlib.sha256(self.source.read_bytes()).hexdigest()
        args=['crop','--source',self.source,'--page','3','--bounds','0.02','0.25','0.9','0.95','--out',out,'--dpi','72']
        self.run_script(SKILL/'scripts/source_assets.py',*args)
        record=json.loads(next(out.glob('*.json')).read_text())
        self.assertEqual(record['source_sha256'],before)
        self.assertEqual(record['pdf_page'],3)
        self.assertIn('pending',record['visual_review'])
        with Image.open(record['png']) as image:
            self.assertAlmostEqual(image.width,720*.88,delta=2)
            self.assertAlmostEqual(image.height,600*.70,delta=2)
        self.run_script(SKILL/'scripts/source_assets.py','crop','--source',self.source,'--page','3',
            '--bounds','0.9','0','0.1','1','--out',out,ok=False)
        self.assertEqual(hashlib.sha256(self.source.read_bytes()).hexdigest(),before)

    def test_rotated_offset_crop_matches_render(self):
        from reportlab.pdfgen import canvas
        from pypdf import PdfReader,PdfWriter
        from pypdf.generic import RectangleObject
        from PIL import Image,ImageChops,ImageStat
        raw=self.root/'raw.pdf'
        c=canvas.Canvas(str(raw),pagesize=(400,300),invariant=1)
        c.setFillColorRGB(1,0,0); c.rect(0,0,200,300,fill=1,stroke=0)
        c.setFillColorRGB(0,0,1); c.rect(200,0,200,300,fill=1,stroke=0)
        c.save()
        page=PdfReader(raw).pages[0]
        page.cropbox=RectangleObject([50,40,350,260]); page.rotate(90)
        source=self.root/'rotated.pdf'
        writer=PdfWriter(); writer.add_page(page); writer.write(source)
        full=self.root/'full'
        subprocess.run(['pdftoppm','-cropbox','-r','72','-singlefile','-png',str(source),str(full)],check=True,capture_output=True)
        out=self.root/'rotated-crop'
        self.run_script(SKILL/'scripts/source_assets.py','crop','--source',source,'--page','1',
                        '--bounds','0.1','0.2','0.9','0.8','--dpi','72','--out',out)
        with Image.open(full.with_suffix('.png')) as im, Image.open(next(out.glob('*.png'))) as crop:
            expected=im.crop((22,60,198,240)).convert('RGB')
            actual=crop.convert('RGB').resize(expected.size)
            self.assertLess(sum(ImageStat.Stat(ImageChops.difference(expected,actual)).mean),8)

    def test_review_selected_pages_and_assets(self):
        out=self.root/'review'
        self.run_script(SKILL/'scripts/review_pdf.py',self.source,'--out',out,'--pages','1,3-4','--scale','500')
        report=json.loads((out/'review-report.json').read_text())
        self.assertEqual(report['rendered_pages'],[1,3,4])
        self.assertTrue(all(Path(x).exists() for x in report['contact_sheets']))
        self.assertIn('pending',report['visual_review'])
        self.run_script(SKILL/'scripts/review_pdf.py','--images',out/'page-0003.png','--out',self.root/'images')
        self.run_script(SKILL/'scripts/review_pdf.py',self.source,'--out',out,'--pages','8',ok=False)

    def test_resume_fixture_has_one_changed_source(self):
        root=self.fixture/'resume'
        state=json.loads((root/'state.json').read_text())
        changed=[x['id'] for x in state['concepts'] if hashlib.sha256((root/x['source']).read_bytes()).hexdigest()!=x['sha256']]
        self.assertEqual(changed,['module-03'])
        self.assertEqual(sum(len(x['inspected_pages']) for x in state['concepts']),144)
        self.assertEqual([x['id'] for x in state['concepts'] if x['status']=='analyzed'],['module-11','module-12'])
        self.assertEqual(state['concepts'][10]['prerequisites'],['module-03'])


if __name__=='__main__':
    unittest.main(verbosity=2)
