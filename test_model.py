import pandas as pd
import numpy as np
import joblib

from tensorflow.keras.models import load_model

print("Loading Model...")

model = load_model("models/solar_forecast_lstm.keras")

print("Loading Scalers...")

scaler_X = joblib.load("models/scaler_X.pkl")
scaler_y = joblib.load("models/scaler_y.pkl")

print("Loading Dataset...")

df = pd.read_csv("datasets/madurai_solar_hourly_2021_to_today (1).csv")

# Select required columns
features = [
    "temperature_2m",
    "relative_humidity_2m",
    "windspeed_10m",
    "cloud_cover"
]

X = df[features].values

# Scale inputs
X_scaled = scaler_X.transform(X)

# Take the last 24 hours
# Example: use a daytime window
start_index = 1000

sequence = X_scaled[start_index:start_index + 24]

sequence = sequence.reshape(1, 24, 4)

actual_dni = df["direct_normal_irradiance"].iloc[start_index + 24]

print("Actual DNI:", actual_dni)

# Predict
prediction = model.predict(sequence, verbose=0)

print("\nScaled Prediction:")
print(prediction)

# Convert back to original units
prediction = scaler_y.inverse_transform(prediction)

print("\nPredicted DNI (W/m²):")
print(prediction)

# Expected solar power for research system
AREA = 26.0
EFFICIENCY = 0.213
PR = 0.80
INVERTER = 0.97

power = (
    prediction[0][0]
    * AREA
    * EFFICIENCY
    * PR
    * INVERTER
) / 1000

print("\nEstimated Solar Power (kW):")
print(round(power, 2))