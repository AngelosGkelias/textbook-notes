#!/usr/bin/env python3
"""Generate small synthetic teaching inputs and a hash-linked resume fixture.

Requires reportlab, already common in the document runtime; no model/API calls.
Outputs only beneath the explicitly selected directory.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
from reportlab.pdfgen import canvas


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def page(c, title, lines):
    c.setFont('Helvetica-Bold', 18)
    c.drawString(40, 550, title)
    c.setFont('Helvetica', 12)
    for i, line in enumerate(lines):
        c.drawString(40, 510 - 22*i, line)


def graph(c):
    x0, y0, w, h = 80, 100, 540, 270
    c.setLineWidth(1)
    c.setStrokeColorRGB(0, 0, 0)
    c.line(x0, y0, x0+w, y0)
    c.line(x0, y0, x0, y0+h)
    c.setFont('Helvetica', 11)
    for x in range(7):
        xx = x0+w*x/6
        c.drawString(xx-3, y0-16, str(x))
    for y in (0, .5, 1):
        yy = y0+h*y
        c.drawString(x0-30, yy-3, str(y))
    c.drawString(310, 55, 'Concentration c [mol / m^3]')
    c.saveState()
    c.translate(25, 150)
    c.rotate(90)
    c.drawString(0, 0, 'Normalized flux J / Jmax [dimensionless]')
    c.restoreState()
    for k, color in ((1, (0, .35, .7)), (2, (.7, .2, .1))):
        c.setStrokeColorRGB(*color)
        p = c.beginPath()
        p.moveTo(x0, y0)
        for i in range(1, 121):
            x = i/20
            p.lineTo(x0+w*x/6, y0+h*x/(k+x))
        c.drawPath(p)
        c.setFillColorRGB(*color)
        c.drawString(460, 400-20*k, f'K = {k} mol / m^3')
    c.setFillColorRGB(0, 0, 0)


def micro(out):
    target = out/'micro.pdf'
    c = canvas.Canvas(str(target), pagesize=(720, 600), invariant=1)
    page(c, 'Fixed-point iteration', [
        'Objective: assess convergence, not merely solve a fixed-point equation.',
        'x_(n+1) = g(x_n), g(r) = r; near r: e_(n+1) approximately g\'(r) e_n.',
        'Example map: g(x) = 0.5 x + 1.'])
    c.showPage()
    page(c, 'Least squares through the origin', [
        'Real observations (x_i, y_i), not all x_i zero. No intercept is fitted.',
        'Choose b to minimize S(b) = sum_i (y_i - b x_i)^2.',
        'Result: b = sum_i x_i y_i / sum_i x_i^2.'])
    c.showPage()
    page(c, 'Saturating flux relationship', [
        'Steady ideal model: J(c) = Jmax c / (K + c), c >= 0, K > 0.',
        'Jmax is positive flux; K and c have concentration units.',
        'Analytical curves from this model, not measured data.'])
    graph(c)
    c.showPage()
    page(c, 'Same relationship, repeated presentation', [
        'Repeated graph from the preceding page; no additional technical data.'])
    graph(c)
    c.setFont('ZapfDingbats', 25)
    c.drawString(665, 510, 'H')
    c.setFont('Helvetica', 10)
    c.drawString(525, 465, 'Presentation decoration')
    c.showPage()
    page(c, 'Inference from a flag', [
        'P(A | F) = P(F | A) P(A) / P(F).',
        'Item class A prevalence: 0.10.',
        'Flag rate for class A: P(F | A) = 0.80.',
        'Flag rate for other items: P(F | not A) = 0.20.'])
    c.showPage()
    page(c, 'Diffusion length', [
        'Ideal one-dimensional unbiased diffusion; initial position is zero.',
        'Root-mean-square displacement L = 2 D t.',
        'D = 3 m^2/s; t = 2 s; claimed L = 12 m.'])
    c.showPage()
    page(c, 'Appendix: lock ordering', [
        'Two threads can acquire exclusive non-preemptible locks A and B.',
        'Thread 1 acquires A then waits for B; thread 2 acquires B then waits for A.',
        'Requiring all paths to acquire A before B prevents this circular wait.'])
    c.save()
    return target


def resume(out):
    root=out/'resume'
    root.mkdir()
    records=[]
    for i in range(12):
        name=f'module-{i+1:02}'
        source=root/f'{name}.pdf'
        c=canvas.Canvas(str(source), pagesize=(720,600), invariant=1)
        a = .2 + .02*i
        for p in range(12):
            page(c, f'Affine iteration {i+1}', [
                f'Module map: x_(n+1) = {a:.2f} x_n + 1.',
                'Fixed point r = 1 / (1-a); e_(n+1) = a e_n.',
                f'Presentation build {p+1} of 12: same map and objective.'])
            c.showPage()
        c.save()
        artifact=root/f'{name}.md'
        complete=i<10
        artifact.write_text(f'# {name}\n\nFor a={a:.2f}, r=1/(1-a)={1/(1-a):.6f}. '
                            'Subtract the fixed-point relation from the iteration: '
                            'e_(n+1)=a e_n, so |a|<1 contracts errors.\n' if complete else '')
        records.append({'id':name,'source':source.name,'sha256':sha(source),
                        'inspected_pages':list(range(1,13)), 'objective':'Derive fixed point and error contraction',
                        'prerequisites':[], 'requirements':'Explain subtraction and |a|<1; show one error update',
                        'depth':'concise, shared derivation in module-01',
                        'visuals':'none needed: scalar error update suffices',
                        'criterion':'Predict convergence from a and derive e_(n+1)=a e_n',
                        'destination':artifact.name,'artifact_sha256':sha(artifact),
                        'status':'accepted' if complete else 'analyzed'})
    records[10]['prerequisites']=['module-03']
    (root/'state.json').write_text(json.dumps({'fixture_note':'Synthetic imported accepted state, not evidence of a real prior run.',
        'audience':'First-year students who know scalar algebra', 'concepts':records},indent=2)+'\n')
    changed=root/'module-03.pdf'
    c=canvas.Canvas(str(changed), pagesize=(720,600), invariant=1)
    for p in range(12):
        page(c,'Affine iteration 3',["Module map: x_(n+1) = 1.10 x_n + 1.",
             'Fixed point r = 1 / (1-a); e_(n+1) = a e_n.',
             f'Presentation build {p+1} of 12: same map and objective.'])
        c.showPage()
    c.save()
    (root/'request.txt').write_text('Resume this imported accepted project state. Sources may have changed. '
        'Compare hashes, preserve still-valid accepted artifacts, and complete pending or invalidated concepts '
        'and their dependencies. Use the supplied teaching requirements where valid. Produce only the affected '
        'Markdown sections and a concise source-to-output audit/update of state.json. Log actual source ranges '
        'read and artifact/check reuse in operations.json. No PDF output or outside research is needed for this '
        'bounded resumption evaluation. Do not delegate.\n')
    return root


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args=parser.parse_args()
    if args.out.exists():
        parser.error('Use a new output directory to preserve fixture baselines.')
    args.out.mkdir(parents=True)
    micro(args.out)
    resume(args.out)
    (args.out/'request.txt').write_text('Use $textbook-notes to turn all seven supplied educational excerpts '
        'in micro.pdf into small, self-contained notes for first-year university students with algebra and '
        'elementary differentiation, but no prior probability or concurrent programming. First save a compact '
        'concept teaching specification and page dispositions before writing. Then author the corresponding '
        'sections with necessary teaching visuals and a concise evidence-based review. This is a bounded '
        'teaching evaluation: Markdown plus included figure assets is the requested format, no Typst/PDF output '
        'or outside research is needed. Do not delegate. Save analysis.md before notes.md; do not revise the '
        'original analysis after writing (record justified changes separately). Record actual model/settings '
        'and checks; leave unknown usage unknown.\n')
    print(args.out.resolve())

if __name__=='__main__':
    main()
