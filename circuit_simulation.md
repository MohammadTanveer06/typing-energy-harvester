# Circuit Simulation / Analytical Model

A full SPICE model is not included because a real piezoelectric disc has frequency-dependent electrical and mechanical behavior that is strongly dependent on mounting.

## First-order storage model

Once a rectified pulse train is produced, the capacitor can be treated approximately as an energy store.

For a capacitor `C`:

`E = 1/2 C V²`

The energy increase during one experiment is:

`ΔE = 1/2 C (V_end² - V_start²)`

Example only:

- `C = 1000 µF = 0.001 F`
- `V_start = 0.10 V`
- `V_end = 0.50 V`

Then:

`ΔE = 0.5 × 0.001 × (0.50² - 0.10²)`
`ΔE = 0.00012 J`

This example is illustrative, not an experimental result.
