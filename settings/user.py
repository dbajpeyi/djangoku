from settings.common import *

DEBUG=True

DATABASES = {
        'default': {
            'ENGINE' : 'django.db.backends.postgresql_psycopg2',
            'NAME'   : 'mysitedb',
            'USER'   : 'admin',
            'PASSWORD': 'admin',
            'HOST'   : 'localhost',
            'PORT'   : '5432',
            'OPTIONS':{
                'autocommit' : True
                }

            }
        }


