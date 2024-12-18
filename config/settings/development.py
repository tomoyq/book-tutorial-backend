from .base import *

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "user",
        "USER": "user",
        "PASSWORD": "postgres",
        "HOST": "host.docker.internal",
        "PORT": "5433",
        "ATOMIC_REQUESTS": True
    }
}