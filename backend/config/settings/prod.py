import requests

from config.settings.base import *

DEBUG = True

ALLOWED_HOSTS += ["*"]


try:
    EC2_PRIVATE_IP = requests.get("http://169.254.169.254/latest/meta-data/local-ipv4", timeout=0.1).text
    ALLOWED_HOSTS.append(EC2_PRIVATE_IP)
except requests.exceptions.RequestException as e:
    print("no ec2 instance")

CORS_ALLOWED_ORIGINS = [
    "https://frontend-domain.com",
    "https://www.frontend-domain.com",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "DB_NAME",
#         "USER": "DB_USER",
#         "PASSWORD": "PASSWORD",
#         "HOST": "DB_HOST",
#         "PORT": "5432",
#     }
# }
