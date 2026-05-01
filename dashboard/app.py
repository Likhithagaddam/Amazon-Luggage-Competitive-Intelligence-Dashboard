import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/cleaned_data.csv")

st.title("🧳 Luggage Competitive Intelligence Dashboard")

# Filters
brands = st.multiselect("Select Brands", df["brand"].unique(), default=df["brand"].unique())
df = df[df["brand"].isin(brands)]

# Overview
st.subheader("Overview Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Products", df["title"].nunique())
col2.metric("Total Reviews", len(df))
col3.metric("Avg Sentiment", round(df["sentiment"].mean(), 2))

# Price comparison
st.subheader("Average Price by Brand")

price_df = df.groupby("brand")["price"].mean().reset_index()
fig = px.bar(price_df, x="brand", y="price", color="brand")
st.plotly_chart(fig)

# Sentiment comparison
st.subheader("Sentiment by Brand")

sent_df = df.groupby("brand")["sentiment"].mean().reset_index()
fig2 = px.bar(sent_df, x="brand", y="sentiment", color="brand")
st.plotly_chart(fig2)

# Ratings
st.subheader("Ratings Distribution")
fig3 = px.box(df, x="brand", y="rating", color="brand")
st.plotly_chart(fig3)

# Reviews
st.subheader("Sample Reviews")
st.dataframe(df[["brand", "title", "review", "sentiment"]].head(20))
