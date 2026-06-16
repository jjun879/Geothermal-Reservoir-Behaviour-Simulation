import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go


def plot_pressure(results_df, scenarios, figures_folder):
    plt.figure(figsize=(10, 6))

    for scenario in scenarios.keys():
        scenario_data = results_df[results_df["scenario"] == scenario]
        plt.plot(
            scenario_data["year"],
            scenario_data["pressure"],
            linewidth=2,
            label=scenario,
        )

    plt.title("Reservoir Pressure Behaviour Over Time")
    plt.xlabel("Time (years)")
    plt.ylabel("Reservoir Pressure (relative units)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{figures_folder}/pressure_behaviour.png", dpi=300)
    plt.show()


def plot_temperature(results_df, scenarios, figures_folder):
    plt.figure(figsize=(10, 6))

    for scenario in scenarios.keys():
        scenario_data = results_df[results_df["scenario"] == scenario]
        plt.plot(
            scenario_data["year"],
            scenario_data["temperature"],
            linewidth=2,
            label=scenario,
        )

    plt.title("Reservoir Temperature Behaviour Over Time")
    plt.xlabel("Time (years)")
    plt.ylabel("Reservoir Temperature (°C)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{figures_folder}/temperature_behaviour.png", dpi=300)
    plt.show()


def plot_final_conditions(results_df, months, figures_folder):
    final_results = results_df[results_df["month"] == months]

    x = np.arange(len(final_results))
    width = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar(x - width / 2, final_results["pressure"], width, label="Final pressure")
    plt.bar(x + width / 2, final_results["temperature"], width, label="Final temperature")

    plt.xticks(x, final_results["scenario"], rotation=15, ha="right")
    plt.title("Final Reservoir Conditions After 10 Years")
    plt.ylabel("Value")
    plt.grid(True, axis="y", alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{figures_folder}/final_conditions.png", dpi=300)
    plt.show()


def plot_interactive_pressure(results_df, scenarios, figures_folder):
    fig = go.Figure()

    for scenario in scenarios.keys():
        scenario_data = results_df[results_df["scenario"] == scenario]

        fig.add_trace(go.Scatter(
            x=scenario_data["year"],
            y=scenario_data["pressure"],
            mode="lines",
            name=f"{scenario} - Pressure",
        ))

    fig.update_layout(
        title="Interactive Reservoir Pressure Simulation",
        xaxis_title="Time (years)",
        yaxis_title="Reservoir Pressure (relative units)",
        template="plotly_white",
        hovermode="x unified",
    )

    fig.write_html(f"{figures_folder}/interactive_pressure_simulation.html")


def plot_sensitivity_pressure(sensitivity_df, figures_folder):
    plt.figure(figsize=(10, 6))
    plt.plot(
        sensitivity_df["extraction_rate"],
        sensitivity_df["final_pressure"],
        marker="o",
        linewidth=2,
    )

    plt.title("Sensitivity Analysis: Extraction Rate vs Final Pressure")
    plt.xlabel("Extraction Rate")
    plt.ylabel("Final Pressure After 10 Years")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{figures_folder}/sensitivity_pressure.png", dpi=300)
    plt.show()