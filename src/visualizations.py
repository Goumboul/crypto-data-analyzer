import plotly.express as px

def plot_price(df):
    fig = px.bar(df, x="name", y="current_price",
                 hover_data=["symbol", "market_cap", "total_volume"],
                 title="Top 10 Cryptos - Prix actuel (USD)")
    return fig

def plot_change(df):
    fig = px.bar(df, x="name", y="price_change_percentage_24h",
                 color="price_change_percentage_24h",
                 color_continuous_scale="RdYlGn",
                 title="Variation sur 24h (%)")
    return fig
