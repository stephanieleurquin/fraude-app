import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# -------------------------------
# 🔥 DATASET SIMULÉ FRAUDE
# -------------------------------
def generate_data(n=2000):
    np.random.seed(42)

    data = pd.DataFrame({
        "amount": np.random.gamma(2, 150, n),
        "country_risk": np.random.randint(0, 3, n),  # 0=low,1=medium,2=high
        "device_risk": np.random.randint(0, 2, n),
        "transactions_24h": np.random.randint(1, 20, n),
    })

    # règle simulée de fraude
    data["fraud"] = (
        (data["amount"] > 300) |
        (data["country_risk"] == 2) |
        (data["transactions_24h"] > 12)
    ).astype(int)

    return data

# -------------------------------
# 🚀 TRAIN MODEL
# -------------------------------
@st.cache_resource
def train_model(df):
    X = df.drop("fraud", axis=1)
    y = df["fraud"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    return model, acc

# -------------------------------
# 🌐 STREAMLIT APP
# -------------------------------

def main():
    st.title("🚨 Détection de Fraude IA")

    df = generate_data()
    model, acc = train_model(df)

    st.subheader("📊 Dataset")
    st.dataframe(df.head())

    st.subheader(f"🎯 Accuracy du modèle: {acc:.2f}")

    st.subheader("🧪 Test en temps réel")

    amount = st.slider("Montant", 0, 1000, 100)
    country = st.selectbox("Risque pays", [0, 1, 2])
    device = st.selectbox("Risque device", [0, 1])
    tx = st.slider("Transactions 24h", 1, 20, 3)

    input_data = np.array([[amount, country, device, tx]])

    prob = model.predict_proba(input_data)[0][1]
    prediction = model.predict(input_data)[0]

    st.subheader("📡 Score de risque")
    st.metric("Risque fraude (%)", f"{prob*100:.2f}%")

    if prediction == 1:
        st.error("🚨 FRAUDE SUSPECTÉE")
    else:
        st.success("✅ Transaction normale")

    st.subheader("📈 Statistiques")
    st.bar_chart(df["fraud"].value_counts())


if __name__ == "__main__":
       Auteur 

    Vanschoor S.
    main()
