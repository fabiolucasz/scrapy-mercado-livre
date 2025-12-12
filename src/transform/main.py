import pandas as pd
from datetime import datetime
import sqlite3

df = pd.read_json('../../data/data.jsonl', lines=True)


df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)
df['old_price_amount'] = df['old_price_amount'].fillna(0).astype(float)
df['old_price_cents'] = df['old_price_cents'].fillna(0).astype(float)
df['price_amount'] = df['price_amount'].fillna(0).astype(float)
df['price_cents'] = df['price_cents'].fillna(0).astype(float)


df['price_F'] = df['price_amount'] + df['price_cents'] / 100
df['old_price_F'] = df['old_price_amount']+ df['old_price_cents'] /100
df['_source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"
df['_collected_at'] = datetime.now()


conn = sqlite3.connect('../../data/quotes.db')

df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

conn.close()

print(df)