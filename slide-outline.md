# Presentation Slide Outline

## Slide 1 — Title
**Typing Energy Harvester Using Piezoelectric Elements**

Name: Mohammad Tanveer

## Slide 2 — Problem
Mechanical energy is continuously produced by human interaction with devices. Most of it is dissipated rather than harvested.

## Slide 3 — Idea
Use piezoelectric elements beneath/near typing force points to convert mechanical deformation or vibration into electrical pulses.

## Slide 4 — Block Diagram
Typing → Piezo → Rectifier → Capacitor → Arduino → Dashboard

## Slide 5 — Hardware
Show:
- piezo discs
- bridge rectifier
- capacitor
- resistor divider
- Arduino
- keyboard prototype

## Slide 6 — Working Principle
Explain the piezoelectric effect and rectification.

## Slide 7 — Energy Equation
`E = 1/2 C V²`

Explain why voltage measurement matters.

## Slide 8 — Software
Arduino measures voltage and energy. Python dashboard plots measurements.

## Slide 9 — Experimental Procedure
Compare light, normal, and fast/heavy typing. Repeat each condition three times.

## Slide 10 — Results
Insert the real values from `measurements/raw_data.csv`.

## Slide 11 — Limitations
- Tiny harvested energy
- Mechanical losses
- Rectifier losses
- Variation between typing styles
- Keyboard-dependent mounting

## Slide 12 — Future Work
- Better mechanical coupling
- Low-leakage power management
- More piezo elements
- Force/pressure sensing
- Supercapacitor experiments

## Slide 13 — Conclusion
The prototype demonstrates conversion and measurement of small mechanical energy from typing while providing a platform for further energy-harvesting experiments.
