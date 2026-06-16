import numpy as np
import pandas as pd


def simulate_reservoir(
    years,
    initial_pressure,
    initial_temperature,
    pressure_loss_coeff,
    pressure_recovery_coeff,
    temperature_loss_coeff,
    temperature_recovery_coeff,
    scenarios,
):
    months = years * 12
    time = np.arange(months + 1)

    all_results = []

    for scenario_name, values in scenarios.items():
        extraction_rate = values["extraction"]
        recharge_rate = values["recharge"]

        pressure = np.zeros(months + 1)
        temperature = np.zeros(months + 1)

        pressure[0] = initial_pressure
        temperature[0] = initial_temperature

        for t in range(months):
            pressure[t + 1] = (
                pressure[t]
                - pressure_loss_coeff * extraction_rate
                + pressure_recovery_coeff * recharge_rate
            )
            temperature[t + 1] = (
                temperature[t]
                - temperature_loss_coeff * extraction_rate
                + temperature_recovery_coeff * recharge_rate
            )

        for i in range(len(time)):
            all_results.append({
                "month": time[i],
                "year": time[i] / 12,
                "scenario": scenario_name,
                "pressure": pressure[i],
                "temperature": temperature[i],
                "extraction": extraction_rate,
                "recharge": recharge_rate,
            })

    return pd.DataFrame(all_results)