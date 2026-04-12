import streamlit as st

st.set_page_config(page_title="Fraud AI", layout="centered")

st.title("🏦💳 Fraud Detection - BASIC")

st.write("✅ Application fonctionnelle")

# ---------------- INPUT ----------------
amount = st.number_input("💰 Montant", 0, 10000, 100)
country = st.selectbox("🌍 Pays étranger ?", ["Non", "Oui"])
device = st.selectbox("📱 Device suspect ?", ["Non", "Oui"])
transactions = st.slider("🔁 Transactions récentes", 0, 10, 1)

# ---------------- SCORE SIMPLE ----------------
if st.button("Tester"):

    score = 0

    if amount > 1000:
        score += 40
    if country == "Oui":
        score += 30
    if device == "Oui":
        score += 30
    if transactions > 5:
        score += 20

    score = min(score, 100)

    st.subheader("📊 Résultat")
    st.write("Score:", score)

    st.progress(score / 100)

    if score > 70:
        st.error("🚨 FRAUDE PROBABLE")
    elif score > 30:
        st.warning("⚠️ RISQUE MOYEN")
    else:
        st.success("✅ TRANSACTION NORMALE")