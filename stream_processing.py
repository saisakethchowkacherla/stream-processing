import pandas as pd

FILE_PATH = "input_stream/sample_power.csv"

df = pd.read_csv(FILE_PATH, sep=";")

df["datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"], dayfirst=True)

df["zone_id"] = "ZONE_RES_01"
df["zone_type"] = "residential"

industrial_baseline = 3.0

alerts = df[df["Global_active_power"] > industrial_baseline][
    ["zone_id", "zone_type", "datetime", "Global_active_power"]
]

alerts["industrial_average"] = industrial_baseline
alerts["alert_message"] = "GRID ANOMALY: Residential consumption exceeded industrial average"

print(alerts.head(20))
print("Scenario D completed successfully.")