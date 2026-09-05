import streamlit as st
from predict import predict_category
from predict import predict_urgency

st.title("Support Ticket Classifier")

ticket = st.text_area(
    "Paste Customer Ticket"
)

if st.button("Analyze"):

    category = predict_category(ticket)
    urgency = predict_urgency(ticket)

    st.success(
        f"Category: {category}"
    )

    st.warning(
        f"Urgency: {urgency}"
    )