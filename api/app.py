from flask import Flask, jsonify
import json
import os
# Imports are relative to the log-analysis-api folder, not the current file
# We are now running the api folder as a module
from parser.log_parser import LogParser  # <-- CHANGE THIS
from detection.detection_engine import DetectionEngine # <-- CHANGE THIS

app = Flask(__name__)
# ... (rest of the file is the same)
# The log file is one directory up (../) and then into the logs folder
LOG_FILE = "../logs/auth.log"
ALERTS_FILE = "alerts.json" 

def run_analysis():
    """Reruns the log parsing and detection to ensure fresh data."""
    try:
        # 1. Parse Logs
        parser = LogParser(LOG_FILE)
        parsed_logs = parser.parse()
        
        # 2. Run Detection (This will save alerts.json)
        engine = DetectionEngine(parsed_logs)
        # Save alerts.json in the current 'api' directory for easy reading
        engine.save_alerts(filename=ALERTS_FILE) 
        
        return parsed_logs
    except Exception as e:
        print(f"Error during analysis: {e}")
        return []

@app.route('/api/logs', methods=['GET'])
def get_logs():
    """Endpoint to return all parsed logs."""
    parsed_logs = run_analysis()
    return jsonify(parsed_logs)

@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    """Endpoint to return all detected alerts."""
    # Ensure alerts.json is up-to-date
    run_analysis() 
    
    # Read the alerts file
    try:
        with open(ALERTS_FILE, 'r') as f:
            alerts = json.load(f)
        return jsonify(alerts)
    except FileNotFoundError:
        return jsonify({"error": "Alerts file not found."}), 404

@app.route('/')
def home():
    return "Log Analysis API is running. Try /api/logs or /api/alerts"

if __name__ == '__main__':
    # Activate the virtual environment first, then run this file
    app.run(debug=True)