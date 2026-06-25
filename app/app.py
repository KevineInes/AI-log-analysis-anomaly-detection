from sklearn.ensemble import IsolationForest
import streamlit as st
import pandas as pd

#Titre
st.title(" AI Log Analysis:Anomaly Detection")

#Chargement des données
df=pd.read_csv("data/logs.csv")

#transformation en colonnes
df["failed"]=df["status"].apply(lambda x: 1 if x == "failed" else 0)
df["success"]=df["status"].apply(lambda x: 1 if x == "success" else 0)

#Création des features
features=df.groupby("ip").agg({
    "failed": "sum",
    "success": "sum",
    "port": "nunique",
})

#Ajout de total_events et failed_ratio
features["total_events"]=features["failed"]+features["success"]
features["failed_ratio"]=features["failed"]/features["total_events"]

#préparation de données
X=features[["failed", "success", "port", "failed_ratio", "total_events"]]
#Ajout de la détection
model=IsolationForest(contamination=0.1)
model.fit(X)
#prédiction
features["anomaly"]=model.predict(X)
#conversion lisible
features["alert"]=features["anomaly"].apply(lambda x: "ANOMALIE" if x == -1 else "NORMAL")

#Affichage complet
st.write("Resultats globaux")
st.dataframe(features[[
"failed", "success", "port", "failed_ratio", "total_events", "alert"
]])

#Affichage des anomalies uniquement
st.write("Anomalies détectées")
anomalies=features[features["alert"]=="ANOMALIE"]
st.dataframe(anomalies)