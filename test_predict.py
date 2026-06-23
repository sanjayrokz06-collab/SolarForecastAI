import pandas as pd
from predict import predict_from_dataframe

df = pd.read_csv("datasets/madurai_solar_hourly_2021_to_today (1).csv")

result = predict_from_dataframe(df)

print(result)