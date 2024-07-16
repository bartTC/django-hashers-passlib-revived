SECRET_KEY = "django-insecure-*a1o%0%focwg&3@8m0fu!52-r22&xyf58)w@6j0+#pbd9j#@g)"
DEBUG = False
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "hashers_passlib",
]
ROOT_URLCONF = None
AUTH_PASSWORD_VALIDATORS = []
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': ':memory:',
  }
}