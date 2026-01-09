import pandas as pd
from datetime import datetime
import sqlite3
import os

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
data_dir = os.path.join(base_dir, 'data')

print(data_dir)


df = pd.read_json(os.path.join(data_dir, 'data.jsonl'), lines=True)


df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)
df['old_price_amount'] = df['old_price_amount'].fillna(0).astype(float)
df['old_price_cents'] = df['old_price_cents'].fillna(0).astype(float)
df['price_amount'] = df['price_amount'].fillna(0).astype(float)
df['price_cents'] = df['price_cents'].fillna(0).astype(float)
df['sell_amount'] = df['sell_amount'].str.replace('| +', '',).str.replace(r'mil', '000', regex=True).str.replace(r'vendidos', '', regex=True)

df['price_F'] = df['price_amount'] + df['price_cents'] / 100
df['old_price_F'] = df['old_price_amount']+ df['old_price_cents'] /100
df['_source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"
df['_collected_at'] = datetime.now()


conn = sqlite3.connect(os.path.join(data_dir, 'quotes.db'))

df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)
df.to_csv(os.path.join(data_dir, 'data.csv'), index=False, encoding='utf-8')

conn.close()

print(df['sell_amount'])