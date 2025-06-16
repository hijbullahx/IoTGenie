import os
import dj_database_url

SECRET_KEY = os.environ.get("SECRET_KEY", "prDWK99ajI0JU7iy6QACCqR1nLGjyVneOs-i5mi71PFmteFDacejuRoX0pKQJUzCFxk")
DEBUG = os.environ.get("DEBUG", "False") == "True"
ALLOWED_HOSTS = [".onrender.com", "localhost"]

DATABASES = {
    "default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"