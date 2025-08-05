# Change-point-analysis-and-statistical-modelling-of-time-series-data

## Overview
This repository supports Task 1 of the Brent Oil Price Analysis project, focusing on establishing a data analysis workflow and understanding Brent oil price data through exploratory data analysis (EDA), stationarity testing, and change point modeling.

## Objectives

Define a workflow for analyzing Brent oil price data.
Compile a dataset of 10-15 key events (geopolitical, OPEC, economic shocks).
Identify assumptions and limitations, especially correlation vs. causation.
Select communication channels for stakeholders.
Analyze time series properties (trend, stationarity).
Explain change point models for detecting structural breaks.

## Repository Structure

data/
brent_oil_prices.csv: Historical Brent oil prices.
oil_market_events.csv: Key events dataset.


notebooks/
eda.ipynb: Visualizations and correlation analysis.
stationarity_test.ipynb: ADF and KPSS tests, transformations.


docs/
Task_1_Report.tex: Detailed report.


README.md: This file.

## Workflow

Collect Brent oil price and event data.
Perform EDA (trends, outliers, correlations).
Test stationarity (ADF, KPSS) and apply transformations.
Integrate event data to align with price changes.
Detect structural breaks using change point models.
Prepare for modeling (e.g., ARIMA) and reporting.

## Key Findings

EDA: Right-skewed price distribution, trends tied to events (e.g., 2022 Russia-Ukraine War).
Stationarity: Non-stationary data; differencing achieved stationarity.
Change Point Models: Identify break dates (e.g., 1973 OPEC embargo) and parameter shifts.

## Setup

Clone: git clone https://github.com/your-username/brent-oil-price-analysis.git
Install: pip install -r requirements.txt (pandas, numpy, matplotlib, seaborn, statsmodels, jupyter).
Run notebooks: jupyter notebook.
Compile report: latexmk -pdf docs/Task_1_Report.tex.
