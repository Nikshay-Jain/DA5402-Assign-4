import os
import time
import feedparser
import psycopg2
from datetime import datetime

# Load environment variables
RSS_FEED_URL = os.getenv("RSS_FEED_URL", "https://www.thehindu.com/news/national/?service=rss")
FETCH_INTERVAL = int(os.getenv("FETCH_INTERVAL", 600))  # Default: 10 minutes
DB_PARAMS = {
    "dbname": os.getenv("POSTGRES_DB", "rss_database"),
    "user": os.getenv("POSTGRES_USER", "rss_user"),
    "password": os.getenv("POSTGRES_PASSWORD", "rss_password"),
    "host": "db",
    "port": 5432,
}

def connect_db():
    """Establish database connection."""
    return psycopg2.connect(**DB_PARAMS)

def fetch_articles():
    """Fetch articles from the RSS feed."""
    feed = feedparser.parse(RSS_FEED_URL)
    articles = []
    for entry in feed.entries:
        title = entry.get("title", "").strip()
        link = entry.get("link", "").strip()
        pub_time = entry.get("published", "")
        pub_timestamp = datetime.strptime(pub_time, "%a, %d %b %Y %H:%M:%S %z") if pub_time else None
        image_url = entry.get("media_content", [{}])[0].get("url", "")
        tags = [tag["term"] for tag in entry.get("tags", [])]
        summary = entry.get("summary", "").strip()
        
        if title and link and pub_timestamp:
            articles.append((title, pub_timestamp, link, image_url, tags, summary))
    return articles

def insert_articles(articles):
    """Insert new articles into the database, avoiding duplicates."""
    conn = connect_db()
    cursor = conn.cursor()
    for article in articles:
        cursor.execute("""
            INSERT INTO news (title, publication_timestamp, link, image_url, tags, summary)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (link) DO NOTHING;
        """, article)
    conn.commit()
    cursor.close()
    conn.close()

def main():
    """Main loop to fetch and store RSS data periodically."""
    while True:
        print("Fetching articles...")
        articles = fetch_articles()
        if articles:
            insert_articles(articles)
            print(f"Inserted {len(articles)} new articles.")
        else:
            print("No new articles found.")
        time.sleep(FETCH_INTERVAL)

if __name__ == "__main__":
    main()
