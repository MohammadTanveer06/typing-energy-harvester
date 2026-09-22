import argparse
import csv
import random
import time
from pathlib import Path

import matplotlib.pyplot as plt


def demo_data(seconds: int = 30):
    rows = []
    voltage = 0.02
    for t in range(0, seconds * 1000, 250):
        # Small illustrative charge rise; this is simulated, not measured.
        if random.random() < 0.28:
            voltage += random.uniform(0.002, 0.012)
        voltage += 0.00002
        voltage = min(voltage, 2.5)
        energy = 0.5 * 0.001 * voltage * voltage
        rows.append((t, voltage, energy))
    return rows


def serial_data(port: str, baud: int, seconds: int):
    try:
        import serial
    except ImportError as exc:
        raise SystemExit("Install requirements first: pip install -r requirements.txt") from exc

    ser = serial.Serial(port, baud, timeout=1)
    start = time.time()
    rows = []

    try:
        while time.time() - start < seconds:
            line = ser.readline().decode("utf-8", errors="ignore").strip()
            if not line or line.startswith("time_ms"):
                continue
            parts = line.split(",")
            if len(parts) != 3:
                continue
            try:
                rows.append((int(parts[0]), float(parts[1]), float(parts[2])))
            except ValueError:
                continue
    finally:
        ser.close()

    return rows


def save_csv(rows, filename: Path):
    with filename.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["time_ms", "voltage_V", "energy_J"])
        writer.writerows(rows)


def plot(rows, title):
    if not rows:
        raise SystemExit("No valid measurements were received.")

    t = [r[0] / 1000 for r in rows]
    v = [r[1] for r in rows]
    e = [r[2] for r in rows]

    fig1 = plt.figure()
    plt.plot(t, v)
    plt.xlabel("Time (s)")
    plt.ylabel("Capacitor voltage (V)")
    plt.title(title + " — Voltage")
    plt.grid(True, alpha=0.25)
    plt.tight_layout()

    fig2 = plt.figure()
    plt.plot(t, e)
    plt.xlabel("Time (s)")
    plt.ylabel("Stored energy (J)")
    plt.title(title + " — Stored Energy")
    plt.grid(True, alpha=0.25)
    plt.tight_layout()

    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Typing Energy Harvester dashboard")
    parser.add_argument("--demo", action="store_true", help="Use simulated measurements")
    parser.add_argument("--port", help="Arduino serial port")
    parser.add_argument("--baud", type=int, default=115200)
    parser.add_argument("--seconds", type=int, default=30)
    parser.add_argument("--output", default="dashboard_measurements.csv")
    args = parser.parse_args()

    if args.demo:
        rows = demo_data(args.seconds)
        title = "Simulated Typing Energy"
    elif args.port:
        rows = serial_data(args.port, args.baud, args.seconds)
        title = f"Arduino Measurements ({args.port})"
    else:
        raise SystemExit("Use --demo or provide --port.")

    save_csv(rows, Path(args.output))
    plot(rows, title)


if __name__ == "__main__":
    main()
