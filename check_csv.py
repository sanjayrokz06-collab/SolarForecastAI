import pandas as pd

df = pd.read_csv("datasets/madurai_solar_hourly_2021_to_today (1).csv")

print(df.columns.tolist())
print(df.head())