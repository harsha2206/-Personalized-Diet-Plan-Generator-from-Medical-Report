from src.predict import predict_condition
from src.alerts import check_alerts

# Example input (from your parser)
sample_data = {
    "hemoglobin": 8.5,
    "glucose": 190,
    "cholesterol": 250,
    "platelets": 140
}

# Prediction
prediction = predict_condition(list(sample_data.values()))

# Alerts
alerts = check_alerts(sample_data)

print("Predicted Condition:", prediction)
print("Alerts:")
for alert in alerts:
    print(alert)
