# Geothermal Reservoir Behaviour Simulation

A simplified Python-based geothermal reservoir simulation model developed to analyse reservoir pressure and thermal behaviour under varying extraction and recharge conditions.

This project explores how different operational strategies may affect long-term geothermal reservoir behaviour. It compares sustainable operation, moderate over-extraction, and aggressive extraction scenarios over a 10-year simulation period.

## Project Overview

The model tracks changes in reservoir pressure and temperature over time using a simplified numerical approach. It is designed as a conceptual simulation rather than a full physics-based geothermal reservoir simulator.

The project includes:

* Scenario-based reservoir simulation
* Pressure and temperature behaviour analysis
* Extraction and recharge comparison
* Sensitivity analysis on extraction rate

## Model Description

The simulation uses a simplified balance model where reservoir pressure and temperature are affected by extraction and recharge.

An improved version of the model includes:

* Nonlinear extraction effects
* Recharge-based recovery
* Seasonal operating variation

This allows the model to produce more realistic reservoir behaviour than a purely linear decline model, while still remaining easy to modify.

## Scenarios

The model compares three operational scenarios:

1. Sustainable operation
   Extraction and recharge are balanced.

2. Moderate over-extraction
   Extraction exceeds recharge at a moderate level.

3. Aggressive extraction
   Extraction is significantly higher than recharge, representing a less sustainable operating condition.

## Outputs

The simulation generates:

* Reservoir pressure behaviour plot
* Reservoir temperature behaviour plot
* Final reservoir condition comparison
* Interactive pressure simulation
* Sensitivity analysis plot
* CSV files containing simulation results

Generated outputs are saved in:

```text
data/
figures/
```

## Packages Used

* Python
* NumPy
* Pandas
* Matplotlib
* Plotly

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the main simulation:

```bash
python main.py
```

## Project Structure

```text
geothermal-reservoir-simulation/
│
├── main.py
├── model.py
├── analysis.py
├── plots.py
├── requirements.txt
├── README.md
│
├── data/
└── figures/
```

## Limitations

This model is intentionally simplified. It does not account for full subsurface reservoir physics, spatial flow behaviour, rock-fluid interactions, detailed permeability fields, or physical dynamics.

Instead, the project focuses on using mathematical modelling and visualisation to explore key reservoir sustainability concepts in a more accessible way.

## Future Improvements

Possible future extensions include:

* Adding spatial reservoir grid modelling
* Including permeability and porosity effects
* Modelling injection and production wells separately
* Adding heat extraction efficiency calculations
* Calibrating model parameters using real geothermal field data
* Comparing simulated behaviour with operational reservoir monitoring data

## Purpose

This project was developed as a self-directed modelling exercise to strengthen understanding of geothermal reservoir behaviour, operational sustainability, and Python-based engineering simulation workflows.
