# Proportionate technical verification

Read for technical university material, worked calculations, circuits, technical figures, or suspected source errors. Verification establishes what is supported and under which assumptions; a clean compile, polished diagram, or another agent's approval is not evidence of correctness.

## Choose the consequential checks

Prioritize results on which later explanations depend, multistep derivations, numerical examples, source corrections, supplemental technical claims, and diagrams encoding behavior. Check every worked example and every included technical diagram at the appropriate depth. Repeated routine identities can share a check; decorative layout does not require mathematical review. Scale effort to complexity and consequence, not page count.

For each important result, establish its source location, variables/units, conventions, and applicability. Identify whether it is a mathematical identity, an exact result within stated ideal assumptions, an approximate model, an empirical relationship, or an illustrative simplification. These distinctions need to appear where students use the result, not only in a review log.

Use a compact verification record alongside coverage/corrections, with separate worker files when delegated:

| Item and source/output location | Assumptions and claim type | Check and evidence | Outcome / remaining issue |
|---|---|---|---|

Record consequential checks and nontrivial evidence, such as a derivation, substitution, small script, truth table, trace, reference passage, or inspected schematic. Routine checks may be grouped. “Looks right” and “reviewer approved” do not count as evidence. A single combined chapter report is sufficient; avoid bookkeeping that merely repeats the textbook.

## Equations, derivations, and examples

1. Inspect the rendered source for missing minus signs, bars, indices, polarity, or implicit conventions before diagnosing a source error. State initial/boundary conditions, reference nodes/directions, operating region, and idealizations as relevant.
2. Reconstruct the important algebra or reasoning from the governing definitions/equations. Check intermediate equalities, substitutions, integrations, bounds, and numerical conversions, not only the final value. Identify where an approximation enters and retain the conditions it requires.
3. Check dimensional consistency at each significant step, including dimensionless arguments of logarithms/exponentials, normalized variables, angular versus cyclic frequency, and unit prefixes. Check signs and reference directions. Dimensionally correct equations can still be wrong.
4. Recompute nontrivial numerical examples with a calculator or a small reproducible script, retaining enough precision internally and rounding the presented result appropriately. Verify displayed intermediate values and the stated answer. Reusing the writer's final expression without checking its derivation only checks arithmetic.
5. Test relevant boundary/limiting cases, conservation or logical invariants, and physical plausibility. Substitute a derived solution into its original equation and initial conditions when useful. Check that a circuit/device solution satisfies the region assumptions used to derive it; treat a failed region check as a real error.
6. Compare the prose, equation, diagram, and worked result. A correct equation applied to a different circuit or timing convention is still incorrect teaching material. State the model's applicability and omitted effects where they affect the conclusion.

Use symbolic algebra, numerical evaluation, simulation, or enumeration when they materially improve confidence. These are optional methods, not mandatory dependencies: symbolic tools need domain assumptions, a simulator needs a valid model and netlist, and a plotted fit does not validate invented data. Keep any scripts, inputs, model versions, and outputs used as evidence. Direct derivation can establish familiar mathematics; use [authoring.md](authoring.md) for authoritative verification of unfamiliar or consequential additions.

## Subject-specific checks — select only those that apply

| Material | Check the failure modes that change the result |
|---|---|
| Mathematics / numerical methods | Definitions and domains, quantifiers, proof implications and converse, existence/uniqueness conditions, algebraic equivalence, convergence/stability assumptions, numerical conditioning and error bounds. |
| Probability / statistics | Conditioning events and denominators, normalization, independence assumptions, estimator/sample definitions, uncertainty, distribution support, and causal versus associational claims. |
| Mechanics / physical models | Coordinate/sign conventions, balances and conservation, constitutive assumptions, boundary/initial conditions, regimes, nondimensional groups, and physically meaningful limits. |
| Algorithms / computer science | Preconditions, loop/state invariants, termination, correctness argument, complexity model, counterexamples, and implementation versus abstract specification. |
| Digital logic / architecture | Truth table or Boolean equivalence; active-low signals and inversion bubbles; bit width, signedness and overflow; mux selection and state transitions; clock edge, reset and enable behavior; cycle counts and stated pipeline/hazard assumptions. |
| CMOS / VLSI | Device type, gate/drain/source/body connections and body ties; complementary network topology; reference voltages/current directions; threshold notation and operating region; capacitance/activity definitions, loading, delay and power units; scope of ideal switch or long-channel approximations. |
| Analog / semiconductor devices | KCL/KVL and reference polarities; bias point before small-signal analysis; dependent-source orientation; region consistency, gain signs, loading and frequency range; assumptions about temperature, device parameters and neglected effects. |
| Signals and systems | Continuous versus discrete variables; transform sign and normalization; frequency units, sampling assumptions and aliasing; convolution bounds; initial conditions, causality, stability and region of convergence where relevant. |
| Embedded systems | Hardware/ISA and register version; bit masks and widths; clock and timer assumptions, overflow and interrupt timing; memory ordering/atomicity claims and code behavior under the specified platform. |
| Operating systems | Scheduling/event traces; state transitions and invariants; synchronization interleavings and counterexamples; deadlock/progress assumptions; address translation units and page sizes; distinguish an abstract model from a specific implementation/version. |

These are review prompts, not a requirement to introduce unrelated topics. Use small representative cases, exhaustive checks for manageable finite logic, or a counterexample/trace when that provides stronger evidence than more prose.

## Technical visuals

Inspect topology and meaning independently of graphic polish. Trace electrical nodes and junctions, distinguish wire crossings from connections, and match component terminals, labels, polarity, current/signal arrows, buses, and reference nodes to the text or netlist. Check logic bubbles and clock edges against behavior. For timing diagrams verify time ordering, edge alignment, delays, sampling instants, and whether an idealized waveform omits physical effects. For plots check equations/data, scales, units, key points, trends, and parameter values against the calculation.

Inspect both source crops and generated figures at intended display size, then inspect their placement/caption in the compiled PDF. A crop can remove the qualifier that made a diagram correct. Keep unresolved topology or labels marked as unresolved instead of drawing a plausible replacement from guesswork. Tool choices and visual provenance are in [visuals-and-build.md](visuals-and-build.md).

## Independent review and stopping rule

Use a separate reviewer selectively for difficult derivations, consequential corrections, complex coupled systems, or unresolved disagreements. Follow [delegation.md](delegation.md) for capability selection and ownership. The reviewer gets the actual raw source, rendered diagram/output, assumptions, and relevant authoritative references and independently reconstructs the critical result. Request concrete errors, missing conditions, counterexamples, or confirmed checks with evidence, not a general approval. If no reviewer is available, perform a separate re-derivation or alternate-method check and disclose that it was self-review.

Close verification when:

- The concept specification accounts for all substantive source objectives, including late and graphical content; worked examples and self-test answers agree with the explanations. This is a coverage prerequisite, not proof of teaching adequacy.
- Important derivations, intermediate calculations, units, signs, assumptions, and relevant limit/plausibility checks have evidence; technical diagrams represent the stated system.
- Corrections and consequential supplemental claims have support, appropriate attribution, and stated model limits.
- No known consequential error remains presented as correct. Remaining source ambiguities or unavailable evidence are localized, explicitly conditional/unresolved, and disclosed as limitations; affected results are not labeled verified.
- Contradictions among prose, equations, tables, figures, notation, and dependent sections have been checked and resolved or localized explicitly.

Technical closure does not certify teaching adequacy or layout. Apply [pedagogical-review.md](pedagogical-review.md) separately, then final build/layout and input-preservation checks in [visuals-and-build.md](visuals-and-build.md).

Normally use one targeted review followed by correction and rechecking of affected results and their dependents. Repeat or broaden only when a substantive change, new finding, or failed check warrants it. Do not loop over unchanged chapters seeking consensus, add redundant examples to appear thorough, or replace evidence with a stronger model's confidence. If a missing source condition prevents completion, finish independent work and identify the precise unresolved requirement rather than inventing certainty.
