import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def show_kpis(superstore_data):
    col1, col2, col3 = st.columns(3)
    n_customers = superstore_data["Customer ID"].nunique()
    n_orders = superstore_data["Order ID"].nunique()
    avg_sales_per_customer = (
        superstore_data.groupby("Customer ID", observed=False)["Sales"].sum().mean()
    )
    repeat_customers = (
        superstore_data.groupby("Customer ID", observed=False)["Order ID"]
        .nunique()
        .gt(1)
        .sum()
    )

    col1.metric("Unique customers", f"{n_customers}")
    col2.metric("Unique orders", f"{n_orders}")
    col3.metric("Orders per customer", f"{n_orders / n_customers:.2f}")

    col1.metric("Average sales per customer", f"${avg_sales_per_customer:,.2f}")
    col2.metric("Repeat customers", f"{repeat_customers}")
    col3.metric("Repeat customer %", f"{(repeat_customers / n_customers) * 100:.1f}%")

    st.subheader("Unique customers per year")
    superstore_data["Order Date"] = pd.to_datetime(superstore_data["Order Date"])
    customers_year = (
        superstore_data.groupby(superstore_data["Order Date"].dt.year)["Customer ID"]
        .nunique()
        .reset_index()
    )
    customers_year.columns = ["Year", "Unique customers"]
    customers_year["Year"] = customers_year["Year"].astype(str)
    st.line_chart(customers_year.set_index("Year"), use_container_width=True)


def show_segments(superstore_data):
    st.subheader("Customer segments")
    segment_counts = (
        superstore_data.groupby("Segment", observed=False)["Customer ID"]
        .nunique()
        .reset_index()
    )
    segment_counts.columns = ["Segment", "Unique customers"]
    fig_segment = px.pie(
        segment_counts,
        names="Segment",
        values="Unique customers",
        title="Customer segment proportion",
    )
    st.plotly_chart(fig_segment, use_container_width=True)


def show_clustering(superstore_data):
    st.subheader("Clients types")
    customer_features = (
        superstore_data.groupby("Customer ID", observed=False)
        .agg(
            total_spent=("Sales", "sum"),
            num_orders=("Order ID", "nunique"),
            num_products=("Product ID", "nunique"),
            first_purchase=("Order Date", "min"),
            last_purchase=("Order Date", "max"),
        )
        .reset_index()
    )

    customer_features["avg_spent_per_order"] = (
        customer_features["total_spent"] / customer_features["num_orders"]
    )
    customer_features["recency"] = (
        pd.to_datetime("today") - pd.to_datetime(customer_features["last_purchase"])
    ).dt.days

    scaler = StandardScaler()
    features_for_clustering = ["total_spent", "num_orders", "num_products", "recency"]
    scaled_features = scaler.fit_transform(customer_features[features_for_clustering])
    kmeans = KMeans(n_clusters=3, random_state=42)
    customer_features["Cluster"] = kmeans.fit_predict(scaled_features)

    cluster_summary = (
        customer_features.groupby("Cluster")
        .agg(
            avg_total_spent=("total_spent", "mean"),
            avg_num_orders=("num_orders", "mean"),
            avg_num_products=("num_products", "mean"),
            avg_spent_per_order=("avg_spent_per_order", "mean"),
            avg_recency_days=("recency", "mean"),
            num_customers=("Customer ID", "count"),
        )
        .reset_index(names="Groups")
    )
    cluster_summary = cluster_summary.rename(
        columns={
            "avg_total_spent": "Avg. total spent",
            "avg_num_orders": "Avg. orders",
            "avg_num_products": "Avg. products",
            "avg_spent_per_order": "Avg. spent/order",
            "avg_recency_days": "Avg. recency (days)",
            "num_customers": "Customers in group",
        }
    )
    st.dataframe(
        cluster_summary.style.format(
            {
                "Avg. total spent": "${:,.2f}",
                "Avg. orders": "{:.2f}",
                "Avg. products": "{:.2f}",
                "Avg. spent/order": "${:,.2f}",
                "Avg. recency (days)": "{:.0f}",
                "Customers in group": "{:.0f}",
            }
        ),
        use_container_width=True,
        hide_index=True,
    )


def customers() -> None:
    superstore_data = st.session_state.get("superstore_data", pd.DataFrame())
    st.title("🧍‍♂️ Customers 🧍‍♀️")

    tab1, tab2, tab3 = st.tabs(["KPIs", "Segments", "Groups"])

    with tab1:
        show_kpis(superstore_data)
    with tab2:
        show_segments(superstore_data)
    with tab3:
        show_clustering(superstore_data)
