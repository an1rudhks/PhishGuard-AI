import pickle
import streamlit as st

# Load model
with open("models/phishing_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Page config
st.set_page_config(
    page_title="AI-Powered Phishing Email Detector",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI-Powered Phishing Email Detector")

st.write(
    "Detect phishing emails using Machine Learning and phishing-pattern analysis."
)

st.divider()

email_text = st.text_area(
    "📧 Enter Email Content",
    height=250
)

if st.button("🔍 Analyze Email"):

    if email_text.strip():

        # -----------------------------
        # ML Prediction
        # -----------------------------
        email_vector = vectorizer.transform([email_text])

        ml_prediction = model.predict(email_vector)[0]

        # -----------------------------
        # Phishing Rules
        # -----------------------------
        phishing_keywords = [
            "verify",
            "password",
            "bank",
            "click",
            "reward",
            "winner",
            "urgent",
            "account",
            "login",
            "security",
            "suspended",
            "confirm",
            "limited",
            "update account",
            "reset password",
            "action required",
            "immediately",
            "within 24 hours",
            "unauthorized access",
            "secure link"
        ]

        found = []

        email_lower = email_text.lower()

        for keyword in phishing_keywords:
            if keyword in email_lower:
                found.append(keyword)

        keyword_count = len(found)

        # -----------------------------
        # Final Decision
        # -----------------------------
        if ml_prediction == "spam":
            final_prediction = "spam"

        elif keyword_count >= 3:
            final_prediction = "spam"

        else:
            final_prediction = "ham"

        # -----------------------------
        # UI
        # -----------------------------
        col1, col2 = st.columns([4, 1])

        with col1:

            if final_prediction == "spam":

                st.error(
                    "⚠️ Phishing / Spam Email Detected"
                )

                if keyword_count >= 5:
                    st.markdown("### Risk Level: 🔴 VERY HIGH")

                elif keyword_count >= 3:
                    st.markdown("### Risk Level: 🟠 HIGH")

                else:
                    st.markdown("### Risk Level: 🟡 MEDIUM")

            else:

                st.success(
                    "✅ Legitimate Email"
                )

                st.markdown("### Risk Level: 🟢 LOW")

        with col2:

            st.metric(
                "Words",
                len(email_text.split())
            )

            st.metric(
                "Characters",
                len(email_text)
            )

        st.divider()

        st.subheader("Detection Summary")

        st.write(
            f"Machine Learning Prediction: **{ml_prediction.upper()}**"
        )

        st.write(
            f"Suspicious Keywords Found: **{keyword_count}**"
        )

        if found:

            st.warning(
                "⚠️ Suspicious Keywords Detected"
            )

            for word in found:
                st.markdown(
                    f"🔹 **{word.upper()}**"
                )

        else:

            st.success(
                "No suspicious keywords detected."
            )

    else:

        st.warning(
            "Please enter email content."
        )