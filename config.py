import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'BLOB_ACCOUNT'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'BLOB_STORAGE_KEY'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'image'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'SQL_SERVER.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'SQL_DATABASE'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'SQL_USER_NAME'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'SQL_PASSWORD'

    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    if not CLIENT_SECRET:
        raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = os.environ.get('AUTHORITY') or 'AUTHORITY'

    CLIENT_ID = os.environ.get('CLIENT_ID') or 'CLIENT_ID'

    REDIRECT_PATH = "/getAToken"

    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"
