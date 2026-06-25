import pandas as pd

df=pd.read_csv("data/logs.csv")
df["failed"]=df["status"].apply(lambda x: 1 if x == "failed" else 0)
df["success"]=df["status"].apply(lambda x: 1 if x == "success" else 0)

features=df.groupby("ip").agg({
    "failed": "sum",
    "success": "sum",
    "port": "nunique",
})

features["total_events"]=features["failed"]+features["success"]

features["failed_ratio"]=features["failed"]/features["total_events"]

features["fail_without_success"]=features.apply(lambda row: 1 if row["failed"] >= 3 and row["success"] == 0 else 0, axis=1)
print(features)