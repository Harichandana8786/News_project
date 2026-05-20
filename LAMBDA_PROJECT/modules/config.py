import os

# =====================================
# NEWS API CONFIG
# =====================================

API_KEY = os.getenv("API_KEY")

NEWS_URL = (
    f"https://newsapi.org/v2/top-headlines?"
    f"country=us&apiKey={API_KEY}"
)

# =====================================
# S3 CONFIG
# =====================================

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

# =====================================
# DATABASE CONFIG
# =====================================

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT", "5432")