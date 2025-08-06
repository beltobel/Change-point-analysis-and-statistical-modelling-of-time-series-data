# Brent Oil Price Analysis and Dashboard
## Overview
This repository consolidates  the Brent Oil Price Analysis project, focusing on analyzing historical Brent oil prices (January 1, 1987, to September 30, 2022) through exploratory data analysis (EDA), stationarity testing, Bayesian change point detection, and an interactive dashboard. The project aims to identify structural breaks in oil prices, associate them with key events (e.g., geopolitical, OPEC decisions, economic shocks), and provide stakeholders with an intuitive visualization platform.

## Objectives

Establish a comprehensive data analysis workflow for Brent oil price data. <br>
Compile a dataset of 10-15 significant events impacting oil prices. <br>
Perform EDA to identify trends, outliers, and correlations. <br>
Test for stationarity using ADF and KPSS tests, applying transformations as needed. <br>
Implement Bayesian change point detection to identify structural breaks using PyMC. <br>
Develop an interactive dashboard with Flask backend and planned React frontend for visualizing price trends, events, and metrics. <br>
Document findings and methodologies in detailed reports. <br>

## Repository Structure
brent-oil-analysis/ <br>
├── data/
│   ├── brent_oil_prices.csv                # Historical Brent oil prices (1987–2022) <br>
│   └── events_impacting_brent_oil_prices.csv # Key events with descriptions and categories <br>
├── notebooks/ <br>
│   ├── eda.ipynb                           # Visualizations and correlation analysis <br>
│   ├── stationarity_test.ipynb             # ADF and KPSS tests, transformations <br>
│   ├── bayesian_change_point.ipynb         # Bayesian change point model implementation <br>
│   └── interprete_change_points.ipynb      # Posterior distribution analysis and visualizations <br>
├── reports/ <br>
│   ├── Task_1_Report.tex                   # LaTeX report for Task 1 <br>
│   └── Task_2_Change_Point_Analysis_Report.md # Markdown report for Task 2 <br>
├── app.py                                  # Flask backend for dashboard <br>
├── index.html                              # Placeholder for React frontend <br>
├── requirements.txt                        # Python dependencies <br>
└── README.md                               # This file <br>

## Workflow

### Data Collection:
Source Brent oil price data (brent_oil_prices.csv) and event data (events_impacting_brent_oil_prices.csv).
Preprocess data, converting dates to datetime and interpolating missing values.


### Exploratory Data Analysis (EDA):
Analyze trends, outliers, and correlations using eda.ipynb.
Visualize price distributions and event impacts (e.g., 2022 Russia-Ukraine War).


### Stationarity Testing:
Perform ADF and KPSS tests in stationarity_test.ipynb.
Apply transformations (e.g., differencing) to achieve stationarity.


### Change Point Detection:
Implement Bayesian change point model using PyMC in bayesian_change_point.ipynb.
Analyze posterior distributions and visualize results in interprete_change_points.ipynb.


### Dashboard Development:
Run Flask backend (app.py) to serve API endpoints for prices, events, change points, and metrics.
Plan React frontend for interactive visualizations using Recharts and Tailwind CSS.


### Reporting:
Compile Task 1 findings in Task_1_Report.tex.
Summarize Task 2 results in Task_2_Change_Point_Analysis_Report.md.



## Key Findings

**EDA**: Price distribution is right-skewed, with trends linked to events like the 2022 Russia-Ukraine War and the 1973 OPEC embargo.
**Stationarity**: Original data is non-stationary; differencing achieves stationarity.
**Change Point Detection:**
Significant change point in March 2020 (COVID-19 pandemic, Saudi-Russia price war), with a 39.29% mean price decrease (from $75.23 to $45.67 per barrel, 98.7% probability).
Additional change point in late 2014 aligns with the 2014–2015 oil price crash due to U.S. shale oil production and OPEC decisions.


**Dashboard**: Provides historical price trends, event correlations, and mock change point data (to be updated with actual results).

### Installation
**Prerequisite**s

Python 3.8+
Node.js (for planned React frontend)
Git
LaTeX distribution (e.g., TeX Live) for compiling reports

**Setup**

Clone the Repository: link from github

**Backend Setup**:
Create and activate a virtual environment:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:pip install -r requirements.txt <br>

**Required packages: **
pandas>=0.24.0s <br>
numpy>=1.25.0s <br>
matplotlib>=3.8s <br>
seaborns <br>
statsmodelss <br>
pymc>=5.25.1s <br>
arviz>=0.13.0s <br>
scipy>=1.4.1s <br>
jupyters <br>
flasks <br>
flask-cors <br>

Ensure data/ contains brent_oil_prices.csv and events_impacting_brent_oil_prices.csv.

Run Flask Backend:python app.py

Access API endpoints at http://localhost:5000 (e.g., /api/prices, /api/events, /api/change_points, /api/metrics).
Frontend Setup (Planned):

Start React development server:npm start

Access at http://localhost:8000.



## Usage

### Data Analysis:
Run eda.ipynb for visualizations and correlation analysis.
Use stationarity_test.ipynb for stationarity tests and transformations.
Execute bayesian_change_point.ipynb to detect change points and interprete_change_points.ipynb for result analysis.


### Dashboard:
Start Flask backend (python app.py) and access API endpoints via Postman or browser.
Once implemented, interact with the React frontend at http://localhost:8000 for visualizations, event filters, and metrics.

### Planned Enhancements

Frontend Development: Implement React frontend with Recharts for charts, Tailwind CSS for styling, and interactive features (date range selectors, event filters).
Real-Time Data: Integrate external API for recent oil price data.
Advanced Visualizations: Use D3.js for interactive timelines or heatmaps.
Export Functionality: Enable chart/data export as CSV/PDF.
