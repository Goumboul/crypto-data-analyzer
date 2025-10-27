def add_price_change_category(df):
    """
    Ajoute une colonne 'change_category' pour savoir si la crypto est en hausse ou baisse.
    """
    df['change_category'] = df['price_change_percentage_24h'].apply(
        lambda x: 'up' if x >= 0 else 'down'
    )
    return df
