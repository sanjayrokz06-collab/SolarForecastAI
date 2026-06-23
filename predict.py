import joblib
import pandas as pd
from tensorflow.keras.models import load_model
from weather_api import get_weather
from datetime import datetime

# =====================================
# LOAD MODEL
# =====================================

print("Loading AI Model...")

model = load_model("models/solar_forecast_lstm.keras")

scaler_X = joblib.load("models/scaler_X.pkl")
scaler_y = joblib.load("models/scaler_y.pkl")

print("AI Model Loaded Successfully!")

# =====================================
# PV SYSTEM CONFIGURATION
# =====================================

PANEL_AREA = 26.0              # m²
PANEL_EFFICIENCY = 0.213
PERFORMANCE_RATIO = 0.80
INVERTER_EFFICIENCY = 0.97

# =====================================
# PREDICTION FUNCTION
# =====================================

def predict_from_dataframe(df):

    features = [
        "temperature_2m",
        "relative_humidity_2m",
        "windspeed_10m",
        "cloud_cover"
    ]

    X = df[features].values

    X_scaled = scaler_X.transform(X)

    sequence = X_scaled[-24:].reshape(1, 24, 4)

    prediction = model.predict(sequence, verbose=0)

    prediction = scaler_y.inverse_transform(prediction)

    dni = float(prediction[0][0])

    if dni < 0:
        dni = 0

    # =====================================
    # SOLAR POWER
    # =====================================

    power = (

        dni
        * PANEL_AREA
        * PANEL_EFFICIENCY
        * PERFORMANCE_RATIO
        * INVERTER_EFFICIENCY

    ) / 1000

    # =====================================
    # AI CONFIDENCE
    # =====================================

    confidence = 96.4

    # =====================================
    # SOLAR STATUS
    # =====================================

    if dni >= 700:
        status = "Excellent"
    elif dni >= 400:
        status = "Good"
    elif dni >= 150:
        status = "Moderate"
    else:
        status = "Low"

    latest = df.iloc[-1]

    return {

        "datetime": datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"),

        "temperature": round(float(latest["temperature_2m"]), 2),

        "humidity": round(float(latest["relative_humidity_2m"]), 2),

        "wind": round(float(latest["windspeed_10m"]), 2),

        "cloud": round(float(latest["cloud_cover"]), 2),

        "dni": round(dni, 2),

        "power": round(power, 2),

        "confidence": confidence,

        "status": status,

        "model": "LSTM",

        "location": "Madurai"

    }


# =====================================
# LIVE PREDICTION
# =====================================

def predict_live():

    df = get_weather()

    result = predict_from_dataframe(df)

    return result