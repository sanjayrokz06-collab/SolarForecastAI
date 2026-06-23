import pandas as pd
import numpy as np
import joblib

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# ======================================
# LOAD DATASET
# ======================================

print("Loading Dataset...")

df = pd.read_csv("datasets/madurai_solar_hourly_2021_to_today (1).csv")

print("Dataset Loaded Successfully!")

# ======================================
# KEEP REQUIRED COLUMNS
# ======================================

df = df[[
    "temperature_2m",
    "relative_humidity_2m",
    "windspeed_10m",
    "cloud_cover",
    "direct_normal_irradiance"
]]

print("\nSelected Columns:")
print(df.columns)

# ======================================
# REMOVE MISSING VALUES
# ======================================

df.dropna(inplace=True)

print("\nMissing Values Removed.")

# ======================================
# INPUT AND OUTPUT
# ======================================

X = df[[
    "temperature_2m",
    "relative_humidity_2m",
    "windspeed_10m",
    "cloud_cover"
]].values

y = df[["direct_normal_irradiance"]].values

print("\nInput Shape :", X.shape)
print("Target Shape:", y.shape)

# ======================================
# SCALE DATA
# ======================================

print("\nScaling Data...")

scaler_X = MinMaxScaler()

scaler_y = MinMaxScaler()

X_scaled = scaler_X.fit_transform(X)

y_scaled = scaler_y.fit_transform(y)

print("Scaling Completed.")

# Save Scalers

joblib.dump(scaler_X, "models/scaler_X.pkl")

joblib.dump(scaler_y, "models/scaler_y.pkl")

print("Scalers Saved.")

# ======================================
# CREATE SEQUENCES
# ======================================

SEQ_LEN = 24

X_seq = []

y_seq = []

for i in range(len(X_scaled) - SEQ_LEN):

    X_seq.append(X_scaled[i:i + SEQ_LEN])

    y_seq.append(y_scaled[i + SEQ_LEN])

X_seq = np.array(X_seq)

y_seq = np.array(y_seq)

print("\nSequence Shape :", X_seq.shape)

print("Target Shape   :", y_seq.shape)

# ======================================
# TRAIN TEST SPLIT
# ======================================

X_train, X_test, y_train, y_test = train_test_split(

    X_seq,

    y_seq,

    test_size=0.2,

    random_state=42,

    shuffle=False

)

print("\nTraining Shape")

print(X_train.shape)

print(y_train.shape)

print("\nTesting Shape")

print(X_test.shape)

print(y_test.shape)

print("\nData Preprocessing Completed Successfully!")

# ======================================
# IMPORT DEEP LEARNING LIBRARIES
# ======================================

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

print("\nBuilding LSTM Model...")

# ======================================
# BUILD MODEL
# ======================================

model = Sequential()

model.add(
    LSTM(
        64,
        return_sequences=True,
        input_shape=(24, 4)
    )
)

model.add(Dropout(0.2))

model.add(
    LSTM(32)
)

model.add(Dropout(0.2))

model.add(Dense(1))

# ======================================
# COMPILE MODEL
# ======================================

model.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mae"]
)

print("\nModel Summary")

model.summary()

# ======================================
# EARLY STOPPING
# ======================================

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)

# ======================================
# TRAIN MODEL
# ======================================

print("\nTraining Started...\n")

history = model.fit(

    X_train,

    y_train,

    epochs=30,

    batch_size=32,

    validation_data=(X_test, y_test),

    callbacks=[early_stop],

    verbose=1

)

print("\nTraining Completed!")

# ======================================
# SAVE MODEL
# ======================================

model.save("models/solar_forecast_lstm.keras")

print("\nModel Saved Successfully!")

print("\nLocation:")

print("models/solar_forecast_lstm.keras")