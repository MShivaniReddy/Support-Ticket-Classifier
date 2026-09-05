import streamlit as st
from predict import predict_category, predict_urgency

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Support Ticket Classifier",
    page_icon="🎫",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0b1120, #111827);
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

/* Main title */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #9ca3af;
    font-size: 17px;
    margin-bottom: 35px;
}

/* Cards */
.card {
    background: #182233;
    border: 1px solid #2b374a;
    border-radius: 18px;
    padding: 25px;
    text-align: center;
}

/* Result */
.result {
    background: #182233;
    border: 1px solid #334155;
    border-radius: 18px;
    padding: 30px;
    text-align: center;
}

.result-title {
    color: #9ca3af;
    font-size: 14px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.result-value {
    font-size: 26px;
    font-weight: 700;
}

/* Button */
.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 50px;
    font-size: 17px;
    font-weight: 700;
}

/* Text area */
textarea {
    border-radius: 12px !important;
}

/* Footer */
.footer {
    text-align: center;
    color: #8b95a7;
    padding: 30px;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown(
    '<div class="title">Support Ticket Classifier</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Automatically classify customer support tickets and determine their urgency using Machine Learning.'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- DASHBOARD CARDS ----------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="📂 Ticket Categories",
        value="5"
    )

with col2:
    st.metric(
        label="🚨 Urgency Levels",
        value="3"
    )

with col3:
    st.metric(
        label="🤖 Classification",
        value="AI"
    )

with col4:
    st.metric(
        label="⚡ Prediction",
        value="Real-Time"
    )


st.write("")


# ---------------- INPUT SECTION ----------------

st.subheader("📝 Customer Support Ticket")

st.caption(
    "Describe the customer's problem and click Analyze Ticket."
)

ticket = st.text_area(
    "Customer Ticket",
    placeholder="Example: My software keeps crashing whenever I try to open it.",
    height=150,
    label_visibility="collapsed"
)


# ---------------- ANALYZE ----------------

if st.button("🔍 Analyze Ticket"):

    if not ticket.strip():

        st.warning("⚠️ Please enter a customer support ticket.")

    else:

        category = predict_category(ticket)
        urgency = predict_urgency(ticket)

        st.divider()

        st.subheader("📊 Analysis Result")

        col1, col2 = st.columns(2)

        # Category
        with col1:

            st.markdown(
                '<div class="result">'
                '<div style="font-size:40px;">📁</div>'
                '<div class="result-title">Predicted Category</div>'
                f'<div class="result-value">{category}</div>'
                '</div>',
                unsafe_allow_html=True
            )

        # Urgency
        with col2:

            st.markdown(
                '<div class="result">'
                '<div style="font-size:40px;">🚨</div>'
                '<div class="result-title">Predicted Urgency</div>'
                f'<div class="result-value">{urgency}</div>'
                '</div>',
                unsafe_allow_html=True
            )


# ---------------- FOOTER ----------------

st.markdown(
    '<div class="footer">'
    '🤖 Powered by TF-IDF + Logistic Regression + Streamlit'
    '<br><br>'
    'Customer Support Ticket Classification System'
    '</div>',
    unsafe_allow_html=True
)
