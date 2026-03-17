def check_alerts(data):
    alerts = []

    if data["hemoglobin"] < 9:
        alerts.append("⚠️ Severe anemia risk")

    if data["glucose"] > 180:
        alerts.append("⚠️ High diabetes risk")

    if data["cholesterol"] > 240:
        alerts.append("⚠️ High cholesterol")

    if data["platelets"] < 150:
        alerts.append("⚠️ Low platelets")

    return alerts
