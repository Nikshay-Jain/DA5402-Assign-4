#!/bin/bash
set -e

# Load environment variables
export PGPASSWORD=${POSTGRES_PASSWORD}

# Check if the database exists
CHECK_DB=$(psql -U "${POSTGRES_USER}" -d postgres -tAc "SELECT 1 FROM pg_database WHERE datname='${POSTGRES_DB}'")
if [ "$CHECK_DB" != "1" ]; then
    echo "Database does not exist. Creating..."
    psql -U "${POSTGRES_USER}" -d postgres -c "CREATE DATABASE ${POSTGRES_DB};"
fi

# Check if the news table exists
CHECK_TABLE=$(psql -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" -tAc "SELECT 1 FROM information_schema.tables WHERE table_name='news'")
if [ "$CHECK_TABLE" != "1" ]; then
    echo "Table does not exist. Creating..."
    psql -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" -f /docker-entrypoint-initdb.d/init-db.sql
else
    echo "Table exists. Skipping creation."
fi