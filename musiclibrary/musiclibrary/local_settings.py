# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rueiq*y+if*h$jxy-6yyt1fpd7px(ty*qf6^itpxn-3mi5occ6'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'BeepBoop2332!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
