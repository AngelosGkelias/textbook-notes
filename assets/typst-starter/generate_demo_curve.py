#!/usr/bin/env python3
"""Regenerate demo-curve.svg from the ideal RC model using only the standard library.

Normalized coordinates: x = t/(RC), y = v_C/V_S = 1 - exp(-x), x >= 0.
This is an illustrative analytical model, not measured or simulated data.
"""
from math import exp
from pathlib import Path


def response(x):
    return 1 - exp(-x)


def svg():
    def point(x, y):
        return 76 + 100 * x, 248 - 200 * y

    points = ' '.join(f'{px:.3f},{py:.3f}' for px, py in
                      (point(i / 40, response(i / 40)) for i in range(201)))
    mx, my = point(1, response(1))
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="640" height="320" viewBox="0 0 640 320">',
        '<title>Normalized ideal RC charging response</title>',
        '<desc>Analytical curve y = 1 - exp(-x), with x = t / tau and y = v_C / V_S. At x = 1, y is approximately 0.632.</desc>',
        '<rect width="640" height="320" fill="white"/>',
        '<g font-family="sans-serif" font-size="16" fill="#203443">',
    ]
    for x in range(6):
        px, _ = point(x, 0)
        parts.append(f'<path d="M{px} 48V248" stroke="#dce4e7"/>')
        parts.append(f'<text x="{px}" y="272" text-anchor="middle">{x}</text>')
    for y in (0, .5, 1):
        _, py = point(0, y)
        parts.append(f'<path d="M76 {py}H576" stroke="#dce4e7"/>')
        parts.append(f'<text x="62" y="{py + 5}" text-anchor="end">{y:g}</text>')
    parts += [
        '<path d="M76 40V248H590" fill="none" stroke="#203443" stroke-width="2"/>',
        f'<polyline points="{points}" fill="none" stroke="#087f8c" stroke-width="3"/>',
        f'<path d="M{mx} 248V{my:.3f}H76" fill="none" stroke="#a56317" stroke-dasharray="5 4"/>',
        f'<circle cx="{mx}" cy="{my:.3f}" r="4" fill="#a56317"/>',
        f'<text x="{mx + 12}" y="{my + 24:.3f}" fill="#8b5210">63.2% at t = τ</text>',
        '<text x="326" y="306" text-anchor="middle">Time t / τ</text>',
        '<text transform="translate(22 148) rotate(-90)" text-anchor="middle">Voltage v<tspan baseline-shift="sub" font-size="11">C</tspan><tspan baseline-shift="baseline"> / V</tspan><tspan baseline-shift="sub" font-size="11">S</tspan></text>',
        '</g></svg>',
    ]
    return '\n'.join(parts) + '\n'


if __name__ == '__main__':
    Path(__file__).with_name('demo-curve.svg').write_text(svg(), encoding='utf-8')
