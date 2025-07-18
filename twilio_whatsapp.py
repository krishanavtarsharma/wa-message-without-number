# whatsapp_sender_app.py

import streamlit as st
from twilio.rest import Client

st.set_page_config(page_title="WhatsApp Sender", page_icon="📤")

st.title("📲 Send WhatsApp Message using Twilio (No Personal Number)")

# Input Twilio credentials
st.sidebar.header("🔐 Twilio Credentials")
account_sid = st.sidebar.text_input("Account SID", type="password")
auth_token = st.sidebar.text_input("Auth Token", type="password")
twilio_number = st.sidebar.text_input("Twilio WhatsApp Number", value="whatsapp:+14155238886")

# Message input
st.subheader("📨 Message Details")
to_number = st.text_input("Recipient Number (with country code, e.g., +91XXXXXXXXXX)")
message_body = st.text_area("Message")

if st.button("🚀 Send WhatsApp Message"):
    if account_sid and auth_token and to_number and message_body:
        try:
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                from_=twilio_number,
                body=message_body,
                to=f"whatsapp:{to_number}"
            )
            st.success(f"✅ Message sent successfully! SID: {message.sid}")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please fill in all required fields.")
