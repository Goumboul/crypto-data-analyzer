import streamlit as st
from src.api import fetch_crypto_data
from src.analysis import add_price_change_category
from src.visualizations import plot_price, plot_change

st.set_page_config(page_title="Crypto Data Analyzer", layout="wide")
st.title("Crypto Data Analyzer")

currency = st.selectbox("Devise :", ["usd", "eur", "btc"], index=0)

df = fetch_crypto_data(vs_currency=currency)

df = add_price_change_category(df)

st.subheader("Top 10 Cryptos")
st.dataframe(df)
st.plotly_chart(plot_price(df), use_container_width=True)
st.plotly_chart(plot_change(df), use_container_width=True)
