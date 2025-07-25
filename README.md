# PV-Hosting-Capacity-Analysis

A comprehensive tool for evaluating photovoltaic (PV) integration impacts on distribution systems through stochastic and time-series analysis.

## Key Features

- **Stochastic Analysis**: Evaluates PV hosting capacity under randomized PV placements (correlated with load profiles) using Monte Carlo Simulation
- **Time-Series Analysis**: Hourly analysis of voltage profiles and reverse power flow
- **Electric Network**: Tested on standard IEEE 123-bus feeder with multiple deployment scenarios
- **Visual Reporting**: Generates PV penetration levels vs. bus voltage profiles

## Requirements

### Core Software
- [OpenDSS](https://www.epri.com/pages/sa/opendss) (Distribution System Simulator)
- [Python 3.7.9](https://www.python.org/downloads/release/python-379/)

### Python Packages
```bash
pip install py-dss-interface==1.0.9  # Python-OpenDSS interface
pip install numpy pandas matplotlib  # Data analysis and visualization
pip install seaborn scipy            # Additional utilities
