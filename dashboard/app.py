# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import requests

# -------------------------------
# PAGE CONFIG
# -------------------------------


# -------------------------------
# HEADER SECTION
# -------------------------------
st.markdown(
    """
    <style>
        .big-font {
            font-size:28px !important;
            font-weight:700;
        }
        .metric-card {
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }
        .section-title {
            font-weight:600;
            font-size:18px;
            margin-top:20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<p class='big-font'>📊 Dashboard</p>", unsafe_allow_html=True)

API_BASE_URL = "http://127.0.0.1:8000/api"
st.set_page_config(page_title="Flipkart Data Intelligence", page_icon="📊", layout="wide")

try:
    response = requests.get(API_BASE_URL+"/total_city")
    if response.status_code == 200:
        data = pd.DataFrame(response.json()).iloc[0]
        total_city = data.get("total_cities", 0)
        total_revenue = data.get("total_revenue", 0)
        payment_option = data.get("total_payment_options", 0)
    else:
        st.error("⚠️ Failed to fetch metrics from API")
        total_city, total_revenue, payment_option = 0, 0, 0
except Exception as e:
    st.error(f"Error connecting to API: {e}")
    total_city, total_revenue, payment_option = 0, 0, 0

# -------------------------------
# KPI METRICS SECTION
# -------------------------------
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"<div class='metric-card'><h3>Total City</h3><h2>{total_city:.0f}</h2></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='metric-card'><h3>Total Revenue</h3><h2>₹{total_revenue:,.2f}</h2></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='metric-card'><h3>Payment Option</h3><h2>{payment_option:.0f}</h2></div>", unsafe_allow_html=True)

st.markdown("---")

# -------------------------------
# CHARTS SECTION
# -------------------------------
left_col, right_col = st.columns((2, 1))

with left_col:
    st.subheader("🏙 Top 10 Cities by Revenue")
    top_cities = requests.get(f"{API_BASE_URL}/top_cities?limit=10").json()
    df_cities = pd.DataFrame(top_cities)

    col1, col2 = st.columns(2)
    # col1.metric("Total Cities", len(df_cities))
    col1.metric("Top City", df_cities.iloc[0]['city'])
    col2.metric("Total Revenue", f"₹{df_cities['total_revenue'].sum():,.0f}")

    fig_bar = px.bar(
        df_cities,
        title="Top 10 Cities by Total Revenue",
        color="city",
        text_auto=".2s"
    )
    fig_bar.update_xaxes(title="City")
    fig_bar.update_yaxes(title="Total Revenue (₹)", tickprefix="₹")
    fig_bar.update_layout(showlegend=False)
    st.plotly_chart(fig_bar, use_container_width=True)

with right_col:
    st.subheader("🏙 Payment Option")
    payment_summary = requests.get(f"{API_BASE_URL}/payment_summary").json()
    payment = pd.DataFrame(payment_summary)
    col1, col2 = st.columns(2)
    col1.metric("Total Option", len(payment))
    col2.metric("Top Choice", payment.iloc[0]['payment_method'])
    fig_pie = px.pie(payment, names="payment_method", values="total_amount", hole=0.5)
    fig_pie.update_traces(textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)
    # st.markdown("---")

# -------------------------------
# TABLE SECTION
# -------------------------------
# st.markdown("<p class='section-title'>My Orders</p>", unsafe_allow_html=True)
# st.dataframe(
#     df[["order_id", "customer_id", "city", "amount", "status"]],
#     use_container_width=True,
#     hide_index=True
# )

# -------------------------------
# RIGHT SIDE ANALYTICS
# -------------------------------
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.markdown("<p class='section-title'>Contract by Type</p>", unsafe_allow_html=True)
    type_data = pd.DataFrame({
        "Type": ["NDA", "Insurance", "Lease", "Maintenance", "Purchase Agreement", "Sale"],
        "Value": [70, 25, 50, 65, 12, 10]
    })
    fig_type = px.bar(type_data, x="Value", y="Type", orientation="h", text="Value")
    fig_type.update_layout(height=300, showlegend=False)
    st.plotly_chart(fig_type, use_container_width=True)

with col2:
    st.markdown("<p class='section-title'>Average Cycle Time</p>", unsafe_allow_html=True)
    st.write("📄 NDA – **25 days**")
    st.write("🛡️ Insurance – **45 days**")
    st.write("🏠 Lease – **18 days**")
    st.write("🛍️ Purchase – **12 days**")
