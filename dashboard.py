import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI Sales Forecasting Dashboard", layout="wide")

# ----------------------------
# Styling
# ----------------------------
st.markdown("""
    <style>
    h1 {
        font-size: 40px !important;
    }
    h5 {
        font-size: 20px !important;
        color: #888;
    }
    .caption {
        font-size: 16px;
        color: #444;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Header
# ----------------------------
st.markdown("<h1 style='text-align: center;'>📊 Sales Forecasting Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Business Intelligence & Forecast Insights</h5>", unsafe_allow_html=True)
st.markdown("---")

# ----------------------------
# Monthly Sales Trend
# ----------------------------
st.subheader("📈 Monthly Sales Trend")
st.caption("Sales increased steadily from mid-2015 to late 2017, with noticeable peaks during holiday seasons. Performance dipped briefly in Q2 2017.")

# Resize image (medium size) using column layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("Images/monthly_sales_trend.png", use_container_width=True)

st.markdown("---")

# ----------------------------
# Forecasting Section
# ----------------------------
st.subheader("🔮 Forecast: Next 6 Months (Prophet Model)")

col1, col2 = st.columns(2)

with col1:
    st.image("Images/forecast_plot.png", caption="Projected Sales Trend", use_container_width=True)
    st.caption("Sales are expected to rise consistently, following a clear upward trend influenced by seasonal effects.")

with col2:
    st.image("Images/forecast_trend_seasonality.png", caption="Trend & Seasonality Breakdown", use_container_width=True)
    st.caption("Peaks typically occur around Nov–Dec, likely due to festive retail demand.")

st.markdown("---")

# ----------------------------
# Sales Insights Section
# ----------------------------
st.subheader("📊 Sales Breakdown & Category Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("Images/sales_by_category.png", caption="Sales by Product Category", use_container_width=True)
    st.caption("Office Supplies generate the most revenue, indicating high-volume, low-margin sales.")

with col2:
    st.image("Images/sales_by_segment.png", caption="Sales by Customer Segment", use_container_width=True)
    st.caption("Consumer segment drives 50%+ revenue, confirming strong B2C presence.")

with col3:
    st.image("Images/top_10_states.png", caption="Top 10 States by Sales", use_container_width=True)
    st.caption("California dominates sales. NY and TX also show strong performance.")

st.markdown("---")



