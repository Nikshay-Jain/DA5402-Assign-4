-- Ensure database exists (though handled by PostgreSQL on startup)
CREATE TABLE IF NOT EXISTS news (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    publication_timestamp TIMESTAMP NOT NULL,
    link TEXT NOT NULL UNIQUE, -- Ensures uniqueness
    image_url TEXT,
    tags TEXT[],
    summary TEXT
);