from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

DB_PARAMS = {
    "dbname": os.getenv("POSTGRES_DB", "rss_database"),
    "user": os.getenv("POSTGRES_USER", "rss_user"),
    "password": os.getenv("POSTGRES_PASSWORD", "rss_password"),
    "host": "db",
    "port": 5432,
}

def fetch_news():
    """Fetch news articles from the database."""
    conn = psycopg2.connect(**DB_PARAMS)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT title, publication_timestamp, link, image_url, summary 
        FROM news 
        WHERE publication_timestamp::date = CURRENT_DATE
        ORDER BY publication_timestamp DESC;
    """)
    news_items = cursor.fetchall()
    cursor.close()
    conn.close()
    return news_items

@app.route('/')
def home():
    news_items = fetch_news()
    return render_template("index.html", news=news_items)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)