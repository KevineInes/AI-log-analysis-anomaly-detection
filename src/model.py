import pandas as pd
from sklearn.ensemble import IsolationForest

#Charger les features
df=pd.read_csv("data/logs.csv")

#Recréer les features(comme avant)
df["failed"]=df["status"].apply(lambda x: 1 if x == "failed" else 0)
df["success"]=df["status"].apply(lambda x: 1 if x == "success" else 0)

features=df.groupby("ip").agg({
    "failed": "sum",
    "success": "sum",
    "port": "nunique",
})

features["total_events"]=features["failed"]+features["success"]

features["failed_ratio"]=features["failed"]/features["total_events"]
#Features ML
X=features[["failed", "success", "port", "failed_ratio", "total_events"]]

#Créer le modèle
model=IsolationForest(contamination=0.1)

#Entraîner le modèle
model.fit(X)
#prediction
features["anomaly"]=model.predict(X)


#Conversion en alerte
features["anomaly"]=features["anomaly"].apply(lambda x: "ANOMALIE" if x == -1 else "NORMAL")

#Afficher les résultats
print("\n=====RESULTATS DE DETECTION=====\n")
print(features)