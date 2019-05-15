import os


DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(os.environ('DB_USERNAME'), os.environ('DB_PASSWORD'), os.environ('DB_HOST'), os.environ('DB_PORT'), os.environ('DB_NAME'))
DATABASE_CONNET_OPTIONS = {}

THREADS_PER_PAGE = 2

CSRF_ENABLED = True

CSRF_SESSION_KEY ='secret'

SECRET_KEY ='secret'