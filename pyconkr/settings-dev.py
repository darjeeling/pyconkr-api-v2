import os

from pyconkr.settings import *
from pyconkr.storage import *

DEBUG = True

ALLOWED_HOSTS += [
    "api-dev.pycon.kr",
]

# RDS
DATABASES = {
    "default": {
        "ENGINE": "mysql.connector.django",
        "NAME": os.getenv("AWS_RDS_DATABASE"),
        "USER": os.getenv("AWS_RDS_USER_ID"),
        "PASSWORD": os.getenv("AWS_RDS_PW"),
        "HOST": os.getenv("AWS_RDS_HOST"),
        "PORT": os.getenv("AWS_RDS_PORT"),
    }
}

# django-storages: S3
del MEDIA_ROOT
# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
# STATICFILES_STORAGE = "storages.backends.s3boto3.S3StaticStorage"

DEFAULT_FILE_STORAGE = "pyconkr.storage.MediaStorage"
STATICFILES_STORAGE = "pyconkr.storage.StaticStorage"

AWS_S3_ACCESS_KEY_ID = os.getenv("AWS_S3_ACCESS_KEY_ID")
AWS_S3_SECRET_ACCESS_KEY = os.getenv("AWS_S3_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = "ap-northeast-2"
AWS_STORAGE_BUCKET_NAME = "pyconkr-api-v2-static-dev"
