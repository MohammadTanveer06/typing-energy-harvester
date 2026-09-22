# Wiring Guide — Beginner Version

## A. Piezo array to bridge rectifier

Connect multiple piezo elements according to the experiment design. Piezo discs have two electrical leads and produce an AC/pulsed signal.

For a simple test, connect the piezo array to the AC terminals of a four-diode bridge rectifier.

The bridge `+` output goes to the storage capacitor positive terminal.

The bridge `-` output goes to common ground.

## B. Storage capacitor

Connect:

- bridge `+` → capacitor `+`
- bridge `-` → capacitor `-`
- capacitor `-` → Arduino GND

Observe capacitor polarity carefully.

## C. Voltage divider

Use:

- `R1 = 100 kΩ` from capacitor `+` to Arduino A0.
- `R2 = 20 kΩ` from Arduino A0 to GND.

Thus:

`V_A0 = V_cap × 20 / (100 + 20)`

and the sketch reconstructs the capacitor voltage.

## D. Arduino

- A0 → divider midpoint.
- GND → circuit common ground.
- USB → computer.

## Very important

1. Do not connect the raw piezo signal to A0.
2. Do not exceed the Arduino analog input rating.
3. Confirm the storage capacitor voltage before plugging into the Arduino.
4. The diagram is conceptual; verify your exact Arduino board and component ratings before powering the circuit.

## Mechanical mounting

Place the piezo elements where typing causes repeatable flexing or vibration. Avoid locations that can damage the keyboard. Tape/foam mounts can be used for first experiments.

## Recommended first test

Build the circuit with **one piezo element first**. Confirm that tapping/typing produces a measurable capacitor-voltage change. Then scale to 4 and 8 elements.
