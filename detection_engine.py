import re
import json

class DetectionEngine:
    def __init__(self, parsed_logs):
        self.logs = parsed_logs
        self.alerts = []

    def detect_failed_logins(self):
        for entry in self.logs:
            if re.search(r'Failed login', entry['message']):
                self.alerts.append({
                    "timestamp": entry['timestamp'],
                    "ip": entry.get('ip', 'N/A'),
                    "alert": "Failed login detected"
                })

    def detect_suspicious_paths(self):
        for entry in self.logs:
            if re.search(r'/etc/passwd|/root', entry['message']):
                self.alerts.append({
                    "timestamp": entry['timestamp'],
                    "ip": entry.get('ip', 'N/A'),
                    "alert": "Suspicious file path accessed"
                })

    def save_alerts(self, filename="alerts.json"):
        with open(filename, "w") as f:
            json.dump(self.alerts, f, indent=2)
