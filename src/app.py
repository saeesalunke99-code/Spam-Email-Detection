import streamlit as st
import joblib

# Load the trained model
model = joblib.load("spam_model.pkl")

st.title("📧 Spam Email Detection")
st.write("Enter a message below to check if it is Spam or Not Spam.")

message = st.text_area("Enter your message:")

if st.button("Check"):
    prediction = model.predict([message])[0]

    if prediction == "spam":
        st.error("🚨 This message is SPAM!")
    else:
        st.success("✅ This message is NOT SPAM.")