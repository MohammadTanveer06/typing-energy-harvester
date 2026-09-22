# Typing Energy Harvester ⚡⌨️

A beginner-friendly engineering prototype that demonstrates how the mechanical force produced while typing can be converted into a small amount of electrical energy using piezoelectric elements.

> **Important scientific note:** A keyboard cannot realistically generate enough harvested energy to power a laptop or charge a phone. This project is an educational proof-of-concept for measuring tiny harvested energy and demonstrating energy conversion.

## Project flow

```text
Typing force
    ↓
Piezoelectric elements
    ↓
Bridge rectifier
    ↓
Storage capacitor
    ↓
Voltage divider
    ↓
Arduino measurement
    ↓
Energy calculation + dashboard
```

## Objectives

1. Convert typing-induced mechanical vibration/pressure into electrical pulses.
2. Rectify the piezoelectric AC output.
3. Store the harvested charge in a capacitor.
4. Measure capacitor voltage with an Arduino.
5. Calculate stored energy using:

**E = 1/2 × C × V²**

6. Record experimental results and compare different typing conditions.

## Repository structure

```text
typing-energy-harvester/
├── README.md
├── LICENSE
├── .gitignore
├── docs/
│   ├── project-overview.md
│   ├── working-principle.md
│   ├── results.md
│   ├── circuit-diagram.svg
│   └── block-diagram.svg
├── hardware/
│   ├── components.md
│   └── wiring.md
├── firmware/
│   └── arduino/
│       └── energy_monitor/
│           └── energy_monitor.ino
├── software/
│   └── dashboard/
│       ├── README.md
│       ├── requirements.txt
│       └── dashboard.py
├── simulation/
│   └── circuit_simulation.md
├── measurements/
│   ├── raw_data.csv
│   └── energy_analysis.py
└── presentation/
    └── slide-outline.md
```

## Quick start

### Hardware
Read [`hardware/components.md`](hardware/components.md) and [`hardware/wiring.md`](hardware/wiring.md).

### Arduino
Open:

`firmware/arduino/energy_monitor/energy_monitor.ino`

Upload it to an Arduino Uno/Nano.

The sketch expects the **rectified storage-capacitor voltage** through a resistor divider. Do **not** connect an unrectified piezo element directly to an Arduino analog pin.

### Dashboard

```bash
cd software/dashboard
pip install -r requirements.txt
python dashboard.py
```

The dashboard supports:

- Serial mode: read measurements from Arduino.
- Demo mode: generate sample data without hardware.

Example:

```bash
python dashboard.py --demo
```

### Data analysis

```bash
python measurements/energy_analysis.py
```

## Suggested experiment

Compare these three cases:

| Test | Typing condition |
|---|---|
| A | Light typing |
| B | Normal typing |
| C | Fast/heavy typing |

For each test, record:

- typing duration
- number of piezo elements
- starting capacitor voltage
- ending capacitor voltage
- estimated stored energy

Repeat each test at least three times.

## Expected observations

The harvested voltage is usually pulse-like and depends strongly on mechanical coupling, piezo placement, typing force, keyboard construction, rectifier losses, and capacitor size.

The project should be reported as a **micro-energy harvesting demonstration**, not as a practical power source for a computer.

## Safety

- Never connect a piezo disc directly to an Arduino analog input.
- Use the rectifier and voltage divider shown in the wiring documentation.
- Verify the voltage-divider output is within the Arduino ADC input range.
- Keep the prototype isolated from mains electricity.
- Discharge the storage capacitor safely before modifying wiring.

## License

MIT License. See [`LICENSE`](LICENSE).
