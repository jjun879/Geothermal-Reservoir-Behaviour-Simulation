import os
import numpy as np

from model import simulate_reservoir
from analysis import run_sensitivity_analysis, print_summary
from plots import (
    plot_pressure,
    plot_temperature,
    plot_final_conditions,
    plot_interactive_pressure,
    plot_sensitivity_pressure,
)


# ----------------------------------------------------
# Adjustable settings
# ----------------------------------------------------

YEARS = 10
MONTHS = YEARS * 12

INITIAL_PRESSURE = 100.0
INITIAL_TEMPERATURE = 250.0

PRESSURE_LOSS_COEFF = 0.08
PRESSURE_RECOVERY_COEFF = 0.05

TEMPERATURE_LOSS_COEFF = 0.025
TEMPERATURE_RECOVERY_COEFF = 0.015

SCENARIOS = {
    "Sustainable operation": {
        "extraction": 10,
        "recharge": 10,
    },
    "Moderate over-extraction": {
        "extraction": 15,
        "recharge": 8,
    },
    "Aggressive extraction": {
        "extraction": 22,
        "recharge": 5,
    },
}

FIXED_RECHARGE_FOR_SENSITIVITY = 10
EXTRACTION_RATES = np.arange(5, 31, 1)

DATA_FOLDER = "data"
FIGURES_FOLDER = "figures"


# ----------------------------------------------------
# Main workflow
# ----------------------------------------------------

def main():
    os.makedirs(DATA_FOLDER, exist_ok=True)
    os.makedirs(FIGURES_FOLDER, exist_ok=True)

    results_df = simulate_reservoir(
        YEARS,
        INITIAL_PRESSURE,
        INITIAL_TEMPERATURE,
        PRESSURE_LOSS_COEFF,
        PRESSURE_RECOVERY_COEFF,
        TEMPERATURE_LOSS_COEFF,
        TEMPERATURE_RECOVERY_COEFF,
        SCENARIOS,
    )

    results_df.to_csv(f"{DATA_FOLDER}/geothermal_simulation_results.csv", index=False)

    sensitivity_df = run_sensitivity_analysis(
        YEARS,
        INITIAL_PRESSURE,
        INITIAL_TEMPERATURE,
        PRESSURE_LOSS_COEFF,
        PRESSURE_RECOVERY_COEFF,
        TEMPERATURE_LOSS_COEFF,
        TEMPERATURE_RECOVERY_COEFF,
        FIXED_RECHARGE_FOR_SENSITIVITY,
        EXTRACTION_RATES,
    )

    sensitivity_df.to_csv(f"{DATA_FOLDER}/sensitivity_analysis.csv", index=False)

    plot_pressure(results_df, SCENARIOS, FIGURES_FOLDER)
    plot_temperature(results_df, SCENARIOS, FIGURES_FOLDER)
    plot_final_conditions(results_df, MONTHS, FIGURES_FOLDER)
    plot_interactive_pressure(results_df, SCENARIOS, FIGURES_FOLDER)
    plot_sensitivity_pressure(sensitivity_df, FIGURES_FOLDER)

    print_summary(
        results_df,
        SCENARIOS,
        MONTHS,
        INITIAL_PRESSURE,
        INITIAL_TEMPERATURE,
    )

    print("\nFiles generated successfully.")


if __name__ == "__main__":
    main()