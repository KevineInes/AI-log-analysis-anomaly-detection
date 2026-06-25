--Description--
This project implements an AI-based anomaly detection system applied to cybersecurity logs. It uses Isolation Forest, an unsupervised machine learning algorithm, to automatically detect abnormal behaviors such as brute force attacks and port scans. The goal is to simulate how a security analyst can identify activities without predefined rules.

Ce projet implémente un système de détection d'anomalies basé sur l'IA appliqué à des logs de cybersécurité. Il utilise Isolation Forest, un algorithme de machine learning non supervisé, pour détecter automatiquement des comportements anormaux comme les attaques brute force ou les scans de ports.

--Domains covered/Domaines abordés
*Cybersecurity(log analysis, intrusion detection)
*Machine Learning(anomaly dtection with Isolation Forest)
*Data Processing(feature engineering with pandas)
*Web development(interactive dashboard with Streamlit)

*Cybersécurité(analyse de logs, détection d'intrusion)
*Machine Learning(détection d'anomalies avec Isolation Forest)
*Traitements de données( feature engineering avec pandas)
*Développement web(dashboard avec streamlit)

--Features/Fonctionnalités
*Log data processing
*Feature extraction(failed attempts, ratios, ports usage)
*AI-based anomaly detection
*Interactive visualization with Streamlit dashboard

*Traitement des logs
*création de variables(tentatives échouées, ratios, ports)
*Détection d'anomalies via IA
*Visualisation interactive avec Streamlit

--IsolationForest--
The project uses Isolation Forest, an unsupervised learning algorithm which learns the normal behavior of network activity, identifies anomalies as isolated or unusual patterns and does not required labeled data

Le projet utilise Isolation Forest, un algorithme non supervisé qui apprend le comportement normal d'un réseau, détecte les anomalies comme des comportements atypiques et ne nécessite pas de données étiquetées.

****How to Run/Lancer le projet****
git clone <your-repo>
cd ai-log-anomaly-detection
pip install -r requirements.txt
python -m streamlit run app/app.py

--Améliorations possibles/Improvements
Add visual charts for anomaly insights
Improve model tuning and evaluation
real-time log processing
combined rule-based and ML approaches

Ajouter des graphiques pour l'analyse
Améliorer le tuning du modèle
Traiter les logs en temps réel
Combiner règles + machine learning

AUTHOR
Kevine Ines NZENTI

Thanks for reading!!!