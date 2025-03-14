CREATE TABLE IF NOT EXISTS news (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    publication_timestamp TIMESTAMP NOT NULL,
    link TEXT UNIQUE NOT NULL,
    image_url TEXT,
    tags TEXT[],
    summary TEXT
);