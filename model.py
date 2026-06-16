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
    
    """
    Simulate geothermal reservoir pressure and temperature behaviour.

    Parameters
    ----------
    years : int
        Total simulation duration in years.

    initial_pressure : float
        Initial reservoir pressure (relative units).

    initial_temperature : float
        Initial reservoir temperature (°C).

    pressure_loss_coeff : float
        Pressure decline coefficient due to fluid extraction.

    pressure_recovery_coeff : float
        Pressure recovery coefficient due to recharge/injection.

    temperature_loss_coeff : float
        Temperature decline coefficient due to extraction.

    temperature_recovery_coeff : float
        Temperature recovery coefficient due to recharge.

    scenarios : dict
        Dictionary containing extraction and recharge rates for
        different operating scenarios.

    Returns
    -------
    pandas.DataFrame
        Time-series simulation results for all scenarios.
    """

    # Convert simulation length from years to months
    # Monthly timesteps = smoother trends than yearly
    months = years * 12
    time = np.arange(months + 1)

    all_results = []

    for scenario_name, values in scenarios.items():

        # Read extraction and recharge rates
        extraction_rate = values["extraction"]
        recharge_rate = values["recharge"]

        pressure = np.zeros(months + 1)
        temperature = np.zeros(months + 1)

        #initial conditions
        pressure[0] = initial_pressure
        temperature[0] = initial_temperature

        for t in range(months):
            # Pressure update:
            # Pressure decreases due to extraction
            # Pressure partially recovers due to recharg
            pressure[t + 1] = (
                pressure[t]
                - pressure_loss_coeff * extraction_rate
                + pressure_recovery_coeff * recharge_rate
            )
            # Temperature update:
            # Temperature decreases due to energy extraction
            # Temperature partially recovers due to recharge
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