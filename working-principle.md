# Working Principle

## 1. Piezoelectric conversion

Piezoelectric materials generate electrical charge when mechanically deformed. In this prototype, typing provides the mechanical excitation.

## 2. Rectification

A piezoelectric disc behaves approximately like an AC/pulsed source. A bridge rectifier converts the alternating waveform into a unidirectional charging current.

Schottky diodes such as 1N5819 can reduce forward-voltage losses compared with ordinary silicon diodes, although the exact loss depends on current and operating conditions.

## 3. Energy storage

The rectified output charges a capacitor.

The energy stored in a capacitor is:

**E = 1/2 C V²**

where:

- `E` = stored energy in joules
- `C` = capacitance in farads
- `V` = capacitor voltage in volts

## 4. Measurement

The Arduino measures the storage-capacitor voltage through a resistor divider.

For:

- `R1 = 100 kΩ`
- `R2 = 20 kΩ`

the Arduino pin sees:

`Vpin = Vcap × R2 / (R1 + R2)`

or:

`Vcap = Vpin × (R1 + R2) / R2`

For a 5 V ADC input limit, this divider ratio gives a theoretical measurement ceiling around 30 V. Use a suitably rated resistor network and keep a generous safety margin.

## 5. Why the output is small

A typing event is short and the mechanical displacement is small. Rectifier and leakage losses can also consume a significant fraction of the harvested energy. Consequently, the useful output is expected to be small.

## 6. Practical interpretation

The purpose is to demonstrate energy harvesting and measurement, not to replace a battery or USB charger.
