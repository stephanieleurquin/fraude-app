# 🏦💳 Fraud Detection - BASIC AI

Application Streamlit simple de détection de fraude basée sur un système de scoring intelligent.

---

## 🚀 Démo

L’application permet d’analyser une transaction et de détecter un niveau de risque :

- montant élevé
- pays étranger
- appareil suspect
- activité récente

---

## 🧠 Fonctionnement

Le système calcule un **score de risque (0 à 100)** basé sur des règles simples :

- +40 si montant > 1000€
- +30 si pays étranger
- +30 si appareil suspect
- +20 si plusieurs transactions récentes

---

## 📊 Résultat

L’application affiche :

- score de risque
- barre de progression
- niveau de danger :

### 🔴 > 70 : FRAUDE PROBABLE  
### 🟠 30 - 70 : RISQUE MOYEN  
### 🟢 < 30 : TRANSACTION NORMALE  

---

## ⚙️ Technologies utilisées

- Python 🐍
- Streamlit 📊

---

## ▶️ Lancer l’application

### 1. Installer Streamlit

bash
pip install streamlit

Lancer l’app
streamlit run fraud.py

fraud-app/
│
├── fraud.py
└── README.md

##Objectif du projet

Ce projet est une simulation pédagogique d’un système de détection de fraude bancaire.

Il permet de comprendre :

les systèmes de scoring
la logique de détection de risque
les bases des systèmes anti-fraude
🚀 Améliorations possibles
Ajouter Machine Learning (XGBoost / Logistic Regression)
Utiliser un dataset réel (Kaggle fraud detection)
Ajouter une API bancaire simulée
Dashboard avancé avec graphiques
Historique des transactions
