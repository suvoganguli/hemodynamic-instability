# Hemodynamic Instability Phenotyping

Exploratory analysis of ICU hemodynamic instability patterns using the PhysioNet 2019 Challenge dataset.

Rather than treating instability as a simple binary prediction problem, this project investigates whether distinct hemodynamic phenotypes emerge naturally from MAP (Mean Arterial Pressure) dynamics.

The analysis focuses on:
- sustained hypotension
- instability burden
- oscillatory behavior
- extreme excursion dynamics
- physiological heterogeneity across ICU patients

Using simple MAP-derived trajectory statistics, patients were grouped into interpretable instability phenotypes including:
- Stable Hemodynamics
- Oscillatory Instability
- Chronic Hypotensive Fragility
- Extreme Excursion Dynamics

The project combines:
- trajectory visualization
- instability quantification
- unsupervised clustering
- PCA-based visualization
- representative physiological trajectory analysis

## Dataset

This project uses the PhysioNet 2019 Sepsis Challenge dataset.

Each patient file contains hourly ICU physiological measurements including:
- Heart Rate (HR)
- Mean Arterial Pressure (MAP)
- Systolic Blood Pressure (SBP)
- Respiration Rate
- Oxygen Saturation (O2Sat)
- Temperature
- additional laboratory variables

## Key Instability Features

The exploratory phenotyping was based on several interpretable MAP-derived features:
- average MAP
- MAP variability
- low-MAP burden
- longest sustained low-MAP episode
- MAP excursion range

## Main Insight

The analysis suggests that ICU hemodynamic instability is not a single phenomenon.

Distinct physiological regimes emerge naturally, including:
- chronic hypotensive states
- oscillatory instability
- stable hemodynamics
- extreme excursion behavior

Interestingly, these MAP-derived phenotypes emerged despite relatively similar broader physiological measurements such as heart rate, respiration, temperature, and oxygen saturation.

## Notebook

The main exploratory analysis is contained in:

```text
notebooks/01_explore_hemodynamic_trajectories.ipynb
```
