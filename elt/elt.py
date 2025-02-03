import requests
import psycopg2
import os

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB","my_db"),
    user=os.getenv("POSTGRES_USER","user"),
    password=os.getenv("POSTGRES_PASSWORD","password"),
    host="db"
)
cursor=conn.cursor()


resp = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
data = resp.json()

cursor.execute("CREATE TABLE IF NOT EXISTS crypto_prices (id SERIAL PRIMARY KEY, currency VARCHAR(50), price FLOAT)")
cursor.execute("INSERT INTO crypto_prices (currency, price) VALUES ('Bitcoin',%s)",(data['bitcoin']['usd'],))

conn.commit()
cursor.close()
conn.close()