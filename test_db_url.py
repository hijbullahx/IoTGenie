import os
import dj_database_url

# Get DATABASE_URL
database_url = os.environ.get('DATABASE_URL')
print(f"DATABASE_URL: {database_url}")

# Parse with dj-database-url
db_config = dj_database_url.config(
    default=database_url,
    conn_max_age=600,
    ssl_require=True
)
print(f"Parsed DB Config: {db_config}")