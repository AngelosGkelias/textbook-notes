#import "theme.typ": *
#show: textbook.with(
  title: "Visual Study Notes",
  subtitle: "A replaceable demonstration chapter",
)

= A first-order charging model

This demonstration verifies the starter's typography, mathematics, figure handling,
and answered self-tests. Replace it with the actual course content and source map.

== Intuition and assumptions

A resistor limits the current charging a capacitor. As the capacitor voltage rises,
the voltage across the resistor falls, so charging slows. The following ideal model
assumes a fixed source voltage, an initially uncharged capacitor, and constant
positive resistance and capacitance.

== Notation and equation

#table(
  columns: (1fr, 3fr, 1fr),
  table.header([Symbol], [Meaning], [Units]),
  $R$, [Resistance], [Ω],
  $C$, [Capacitance], [F],
  $V_S$, [Constant source voltage], [V],
  $v_C (t)$, [Capacitor voltage], [V],
  $tau = R C$, [Time constant], [s],
)

The current law and capacitor relation give
$ C (d v_C)/(d t) = (V_S - v_C)/R. $
With $v_C (0)=0$, the solution is
$ v_C (t) = V_S (1 - e^(-t/tau)). $

This is exact within the stated ideal model; it does not describe leakage or
voltage-dependent capacitance. Differentiating gives
$ (d v_C)/(d t) = (V_S / tau) e^(-t/tau) $. Substitution into the current equation
recovers both sides because $tau = R C$. The solution starts at zero and tends
to $V_S$ as time increases, while the current tends to zero. The exponential's
argument is dimensionless, and $R C$ has units $"Ω" dot "F" = "s"$.

#teaching-figure(
  "demo-curve.svg",
  [Original illustrative analytical model: after one time constant the capacitor
   reaches about 63.2% of the final voltage. The axes are normalized by $tau$ and $V_S$.],
  alt: "Normalized exponential charging curve, with a marked point at one time constant and 63.2 percent of final voltage.",
) <fig:charging>

As @fig:charging shows, one time constant is a useful scale, not the time at which
charging becomes exactly complete. The ideal curve approaches its final value
asymptotically.

== Worked example

For $R=10 " kΩ"$, $C=100 " nF"$, and $V_S=5 " V"$,
$ tau=(10 times 10^3)(100 times 10^(-9)) " s"=1 " ms". $
At $t=tau$, the capacitor voltage is $5(1-e^(-1)) " V" approx 3.16 " V"$.
The result lies between the initial zero voltage and the final 5 V, as expected.

#teaching-note([Common mistake])[
The time constant has units of time. A normalized time such as $t/tau$ is
unitless; it must not be substituted for a duration without the conversion.
]

== Recap and self-test

+ What happens if $R$ is doubled with $C$ fixed? \
  *Answer:* The time constant doubles; the final voltage is unchanged.
+ What fraction of the final voltage is reached at one time constant? \
  *Answer:* $1-e^(-1) approx 0.632$.
