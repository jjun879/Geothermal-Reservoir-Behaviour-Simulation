import pandas as pd

from model import simulate_reservoir


def run_sensitivity_analysis(
    years,
    initial_pressure,
    initial_temperature,
    pressure_loss_coeff,
    pressure_recovery_coeff,
    temperature_loss_coeff,
    temperature_recovery_coeff,
    fixed_recharge,
    extraction_rates,
):
    sensitivity_results = []

    for extraction in extraction_rates:
        scenarios = {
            "Sensitivity scenario": {
                "extraction": extraction,
                "recharge": fixed_recharge,
            }
        }

        result = simulate_reservoir(
            years,
            initial_pressure,
            initial_temperature,
            pressure_loss_coeff,
            pressure_recovery_coeff,
            temperature_loss_coeff,
            temperature_recovery_coeff,
            scenarios,
        )

        final_row = result.iloc[-1]

        sensitivity_results.append({
            "extraction_rate": extraction,
            "final_pressure": final_row["pressure"],
            "final_temperature": final_row["temperature"],
        })

    return pd.DataFrame(sensitivity_results)


def print_summary(results_df, scenarios, months, initial_pressure, initial_temperature):
    final_results = results_df[results_df["month"] == months]

    print("\nSimulation Summary")
    print("------------------")

    for scenario in scenarios.keys():
        scenario_final = final_results[final_results["scenario"] == scenario].iloc[0]

        print(f"\n{scenario}")
        print(f"Extraction rate: {scenario_final['extraction']}")
        print(f"Recharge rate: {scenario_final['recharge']}")
        print(f"Final pressure: {scenario_final['pressure']:.2f}")
        print(f"Final temperature: {scenario_final['temperature']:.2f} °C")
        print(f"Pressure change: {scenario_final['pressure'] - initial_pressure:.2f}")
        print(f"Temperature change: {scenario_final['temperature'] - initial_temperature:.2f} °C")