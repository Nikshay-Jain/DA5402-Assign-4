from flask import Flask, render_template, request
import psycopg2
import os
from datetime import datetime

app = Flask(__name__)

DB_PARAMS = {
    "dbname": os.getenv("POSTGRES_DB", "rss_database"),
    "user": os.getenv("POSTGRES_USER", "rss_user"),
    "password": os.getenv("POSTGRES_PASSWORD", "rss_password"),
    "host": "db",
    "port": 5432,
}

def fetch_news(selected_date):
    """Fetch news articles from the database for the given date."""
    conn = psycopg2.connect(**DB_PARAMS)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT title, publication_timestamp, link, image_url, summary 
        FROM news 
        WHERE publication_timestamp::date = %s
        ORDER BY publication_timestamp DESC;
    """, (selected_date,))
    news_items = cursor.fetchall()
    cursor.close()
    conn.close()
    return news_items

@app.route('/', methods=['GET'])
def home():
    selected_date = request.args.get('date', datetime.today().strftime('%Y-%m-%d'))
    news_items = fetch_news(selected_date)
    return render_template("index.html", news=news_items, selected_date=selected_date)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)