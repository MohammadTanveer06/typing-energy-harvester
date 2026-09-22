import csv
from pathlib import Path

C_F = 0.001  # 1000 uF


def energy(voltage_v: float) -> float:
    return 0.5 * C_F * voltage_v ** 2


def main():
    source = Path(__file__).with_name("raw_data.csv")

    with source.open(newline="") as f:
        rows = list(csv.DictReader(f))

    print("Typing Energy Harvester — Energy Analysis")
    print("=" * 52)

    for row in rows:
        if not row["vstart_V"] or not row["vend_V"]:
            continue

        start = float(row["vstart_V"])
        end = float(row["vend_V"])
        delta = energy(end) - energy(start)

        row["delta_energy_J"] = f"{delta:.10f}"

        print(
            f"Trial {row['trial']:>2} | {row['condition']:<10} | "
            f"{start:.4f} V → {end:.4f} V | ΔE = {delta:.10f} J"
        )

    print("\nFormula used: ΔE = 0.5 × C × (Vend² - Vstart²)")
    print(f"Capacitance: {C_F} F")


if __name__ == "__main__":
    main()
