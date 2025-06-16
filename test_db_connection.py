import psycopg2

conn = psycopg2.connect(
    "postgresql://iotgenie-db_owner:npg_8CHoU3mJkgVe@ep-curly-base-a8ns257x-pooler.eastus2.azure.neon.tech/iotgenie-db?sslmode=require"
)
print("Connected to Neon database!")
conn.close()