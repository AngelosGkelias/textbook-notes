#!/usr/bin/env python3
"""Generate synthetic teaching inputs, comparison review cases and resume state.

Requires reportlab, already common in the document runtime; no model/API calls.
Outputs only beneath the explicitly selected directory.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
import shutil
from textwrap import dedent
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


def comparison(out):
    """Two-page source plus isolated forward-authoring and seeded review inputs."""
    root=out/'comparison'
    author=root/'author'
    review=root/'review'
    author.mkdir(parents=True)
    review.mkdir()
    source=author/'source.pdf'
    c=canvas.Canvas(str(source), pagesize=(720,600), invariant=1)

    def plot(curves):
        x0,y0,w,h=80,100,540,270
        c.setStrokeColorRGB(0,0,0)
        c.line(x0,y0,x0+w,y0)
        c.line(x0,y0,x0,y0+h)
        c.setFont('Helvetica',11)
        for u in range(7):
            c.drawString(x0+w*u/6-3,y0-18,str(u))
        for v in (0,.5,1):
            c.drawString(x0-30,y0+h*v-3,str(v))
        c.drawCentredString(350,55,'Normalized time u = t / T [dimensionless]')
        c.saveState()
        c.translate(25,150)
        c.rotate(90)
        c.drawString(0,0,'Normalized response y [dimensionless]')
        c.restoreState()
        for i,(label,points,color,dash) in enumerate(curves):
            c.setStrokeColorRGB(*color)
            c.setDash(dash)
            path=c.beginPath()
            path.moveTo(x0+w*points[0][0]/6,y0+h*points[0][1])
            for u,v in points[1:]:
                path.lineTo(x0+w*u/6,y0+h*v)
            c.drawPath(path)
            c.line(425,414-20*i,450,414-20*i)
            c.setFillColorRGB(*color)
            c.drawString(460,410-20*i,label)
        c.setDash([])
        c.setFillColorRGB(0,0,0)

    page(c,'Comparing response predictions',[
        'Objective: compare early response, half-height timing, and late behavior.',
        'Model A and Model B predict the same normalized quantity after one event.',
        'Synthetic illustrative model outputs, not measurements or a universal ranking.',
        'Only this graph is supplied; model equations and calibration data are unavailable.'])
    plot([
        ('Model A',list(enumerate([1,.60,.30,.15,.08,.04,.02])),(0,0,0),[]),
        ('Model B',list(enumerate([1,.45,.32,.23,.16,.11,.08])),(0,.35,.7),[6,3]),
    ])
    c.showPage()
    page(c,'A single-model illustration and an extension',[
        'Illustrative exponential: y = exp(-u), u = t/T; T > 0 is a time scale.',
        'It shows one response, with half-height at u = ln(2). It is not a fit to A or B.',
        'Optional extension: derive integral_0^infinity exp(-m u) du = 1/m, m > 0,',
        'then differentiate with respect to m.'])
    points=[(i/20,math.exp(-i/20)) for i in range(121)]
    plot([('Illustrative exponential',points,(0,0,0),[])])
    c.save()
    shutil.copyfile(source,review/'source.pdf')
    svg_points=' '.join(f'{50+80*u:.3f},{250-200*v:.3f}' for u,v in points)
    (review/'single-model.svg').write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" width="600" height="310" viewBox="0 0 600 310">'
        '<rect width="600" height="310" fill="white"/>'
        '<path d="M50 50 V250 H530" stroke="black" fill="none"/>'
        f'<polyline points="{svg_points}" fill="none" stroke="black" stroke-width="2"/>'
        '<g font-family="sans-serif" font-size="14"><text x="28" y="55">1</text>'
        '<text x="30" y="254">0</text><text x="525" y="270">6</text>'
        '<text x="240" y="290">u = t/T [dimensionless]</text>'
        '<text x="10" y="35">y</text><text x="250" y="75">y = exp(-u)</text></g></svg>')
    (review/'teaching-spec.md').write_text(dedent(f'''\
        # Teaching specification

        Source: source.pdf; SHA-256: {sha(source)}. Audience: students with algebra,
        elementary calculus and basic graph reading. Status: reviewed.

        | ID / source | Objective and depth | Visual decision / criterion | Destination / state |
        |---|---|---|---|
        | R / pp.1-2 | Explain normalized response and derive exponential timing; developed | Comparison on p.1 is redundant with the single-model illustration in notes.md#response. No calibration data are available to redraw it. Deriving half-height and the integral establishes understanding of both pages. | notes.md#response; reviewed |

        Page dispositions: p.1 consolidated into R; p.2 R. No substantive omissions.
        '''))
    (review/'notes.md').write_text(dedent('''\
        # Response models

        ## Response

        Normalized time u=t/T and response y are dimensionless; T>0 has time units.
        In the supplied comparison, B reaches half-height before A. A is initially
        above B, the curves cross, and B remains above A in the late plotted response.
        This is an illustrative comparison, not a universal ranking of models.

        ![Illustrative single exponential](single-model.svg)

        The figure shows the response topic using y=exp(-u), not calibrated data.
        Half-height obeys exp(-u)=1/2, so u=ln(2) and t=T ln(2).
        The source comparison need not be repeated because both visuals concern decay.

        For m>0, an antiderivative of exp(-m u) is -exp(-m u)/m.
        Its upper limit is zero and lower limit is -1/m, so the integral from zero
        to infinity is 1/m. Differentiating this result gives -1/m^2.
        These derivations supply analytical detail beyond the graphical comparison.
        '''))
    (review/'review-record.md').write_text(
        '# Teaching review\n\nStatus: accepted. All source pages and objectives are fulfilled. '
        'The single-model figure implements the visual decision; half-height and integral '
        'derivations are correct. No material teaching gap remains.\n')
    (author/'request.txt').write_text(
        'Use the supplied textbook-notes skill to teach source.pdf to students with algebra, '
        'elementary calculus and basic graph reading. Save analysis.md before notes.md; '
        'preserve the initial analysis and record later changes separately. Produce concise '
        'self-contained Markdown notes with necessary figure assets and an evidence-based '
        'review.md. Cover the substantive source objectives and justify visual/depth choices. '
        'No Typst build, outside research, installation or delegation. Record actual exposed '
        'settings/usage, leaving unavailable telemetry unknown. Keep inputs unchanged.\n')
    (review/'request.txt').write_text(
        'Use the supplied textbook-notes skill to review source.pdf, teaching-spec.md, '
        'notes.md, its figure and review-record.md for the declared audience. Report concrete '
        'teaching failures or acceptance evidence with source/destination locations and local '
        'repair requirements in findings.md. Check the supplied records against the actual '
        'source and notes. Do not repair the inputs. No outside research, installation, '
        'delegation or full textbook/PDF build. Record actual exposed settings/usage; '
        'leave unavailable telemetry unknown.\n')
    return root


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--case', choices=('all','comparison'), default='all',
                        help='Generate all fixtures or only the two-page comparison cases.')
    args=parser.parse_args()
    if args.out.exists():
        parser.error('Use a new output directory to preserve fixture baselines.')
    args.out.mkdir(parents=True)
    comparison(args.out)
    if args.case=='comparison':
        print(args.out.resolve())
        return
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
