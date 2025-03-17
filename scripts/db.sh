#!/bin/bash

# Load environment variables from .env file
if [ -f ".env" ]; then
    set -a
    source .env
    set +a
else
    echo "Error: .env file not found." >&2
    exit 1
fi

# Check that required variables are set
REQUIRED_VARS=("POSTGRES_USER" "POSTGRES_PASSWORD" "POSTGRES_SERVER" "POSTGRES_DB" "POSTGRES_PORT")
for VAR in "${REQUIRED_VARS[@]}"; do
    if [ -z "${!VAR}" ]; then
        echo "Error: $VAR is not set in .env" >&2
        exit 1
    fi
done

# Construct the PostgreSQL connection string
DB_URL="postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_SERVER}:${POSTGRES_PORT}/${POSTGRES_DB}"

# Connect to the database
echo "Connecting to $POSTGRES_DB at $POSTGRES_SERVER:$POSTGRES_PORT as $POSTGRES_USER..."
psql "$DB_URL"
