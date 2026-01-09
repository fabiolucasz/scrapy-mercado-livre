import streamlit as st
import pandas as pd
import os

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_dir = os.path.join(base_dir, 'data', 'data.csv')

if not os.path.exists(data_dir):
    raise FileNotFoundError("Could not find data.csv")
print(f'base_dir: {base_dir}')
print(f'data_dir: {data_dir}')

df = pd.read_csv(data_dir)

st.title("Mercado Livre")
st.dataframe(df)

st.title("Top 10 Quantidade de Produtos por Marca")
st.dataframe(df['brand'].value_counts().head(10))

#Top 10 mais vendidos
st.title("Top 10 Mais Vendidos")
df_top_sell = df[['title', 'brand','sell_amount']]
st.dataframe(df_top_sell.sort_values(by='sell_amount', ascending=False).head(10))

st.title("Top 10 Média de Rating por Marca")
df_brand_unique = df['brand'].dropna().unique()

rating_list = []

#get top 10 rating for each brand and show mean
for brand in df_brand_unique:
    new_df = pd.DataFrame({
        "brand": [brand], 
        "rating": [df[df['brand'] == brand]['reviews_rating_number'].mean()],
        "count": [df[df['brand'] == brand]['reviews_rating_number'].count()]
    })
    rating_list.append(new_df)

rating_df = pd.concat(rating_list).sort_values(by='rating', ascending=False)
st.dataframe(rating_df.head(10))



    

