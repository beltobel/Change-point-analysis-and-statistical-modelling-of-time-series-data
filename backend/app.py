from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Load data
prices_df = pd.read_csv('../data/brent_oil_prices.csv')
# Use format='mixed' to handle multiple date formats
prices_df['Date'] = pd.to_datetime(prices_df['Date'], format='mixed', dayfirst=True)
prices_df = prices_df[(prices_df['Date'] >= '2012-01-01') & (prices_df['Date'] <= '2022-09-30')]
prices_df['Log_Returns'] = np.log(prices_df['Price']).diff()

events_df = pd.read_csv('../data/events_impacting_brent_oil_prices.csv')
events_df['Date'] = pd.to_datetime(events_df['Date'])

# Mock change points (replace with Task 2 results)
change_points = [
    {'date': '2014-11-25', 'mean_before': 100.50, 'mean_after': 50.25, 'percent_change': -50.00},
    {'date': '2020-03-10', 'mean_before': 45.80, 'mean_after': 32.06, 'percent_change': -30.00}
]

@app.route('/api/prices', methods=['GET'])
def get_prices():
    data = prices_df[['Date', 'Price', 'Log_Returns']].to_dict(orient='records')
    return jsonify(data)

@app.route('/api/events', methods=['GET'])
def get_events():
    data = events_df[['Date', 'Event Description', 'Category']].to_dict(orient='records')
    return jsonify(data)

@app.route('/api/change_points', methods=['GET'])
def get_change_points():
    return jsonify(change_points)

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    volatility = prices_df['Log_Returns'].std() * np.sqrt(252)  # Annualized volatility
    avg_change = np.mean([cp['percent_change'] for cp in change_points])
    metrics = {'volatility': volatility, 'avg_price_change': avg_change}
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(debug=True, port=5000)