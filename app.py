import streamlit as st
import pandas as pd

# ------------------------------
# Page Configuration
# ------------------------------

st.set_page_config(
    page_title="Customer Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

# ------------------------------
# Load Data
# ------------------------------

rfm = pd.read_csv("data/customer_intelligence_final.csv")

# ------------------------------
# Title
# ------------------------------

st.title("📊 Customer Intelligence Platform")
st.markdown("Customer Segmentation | Churn Prediction | CLV Estimation")

st.divider()

# ------------------------------
# KPI Metrics
# ------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Customers",
        f"{rfm.shape[0]:,}"
    )

with col2:
    st.metric(
        "Average CLV",
        f"₹ {rfm['CLV'].mean():,.0f}"
    )

with col3:
    st.metric(
        "Churn Rate",
        f"{rfm['Churn'].mean()*100:.1f}%"
    )

st.divider()

# ------------------------------
# Charts Section
# ------------------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("Customer Segments")
    st.bar_chart(
        rfm["Segment"].value_counts()
    )

with col2:
    st.subheader("Customer Status")

    churn_df = (
        rfm["Churn"]
        .map({
            0: "Active",
            1: "Churned"
        })
        .value_counts()
    )

    st.bar_chart(churn_df)

st.divider()

# ------------------------------
# Customer Search
# ------------------------------

st.subheader("Customer Lookup")

customer_id = st.number_input(
    "Enter Customer ID",
    min_value=int(rfm["CustomerID"].min()),
    max_value=int(rfm["CustomerID"].max()),
    step=1
)

customer = rfm[rfm["CustomerID"] == customer_id]

if not customer.empty:
    st.write(customer)

st.divider()

# ------------------------------
# Top Customers
# ------------------------------

st.subheader("Top 10 Customers by CLV")

top_customers = (
    rfm
    .sort_values(
        by="CLV",
        ascending=False
    )
    .head(10)
)

st.dataframe(
    top_customers,
    use_container_width=True
)

st.divider()

# ------------------------------
# Model Performance
# ------------------------------

st.subheader("Model Performance")

performance_df = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "XGBoost Classifier"
    ],
    "Accuracy": [
        0.91,
        0.95
    ]
})

st.bar_chart(
    performance_df.set_index("Model")
)

# ------------------------------
# Footer
# ------------------------------

st.markdown("---")

st.caption(
    "Built using Python, Scikit-Learn, XGBoost and Streamlit"
)