class AlertSystem:
    def __init__(self):
        self.thresholds = {'temperature': 35}
        self.alerts_triggered = []

    def check_thresholds(self, weather_data):
        for entry in weather_data:
            if entry['max_temp'] > self.thresholds['temperature']:
                alert_message = entry['city']+" exceeds 35°C"
                self.alerts_triggered.append(alert_message)
                print(alert_message)
