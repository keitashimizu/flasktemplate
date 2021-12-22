import os
from posix import environ
class SystemConfig:
  DEBUG = True
  JSON_AS_ASCII = False
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
      'user': os.environ.get('DB_USER'),
      'password': os.environ.get('DB_PASSWORD'),
      'host': os.environ.get('DB_HOST'),
      'db_name': os.environ.get('DB_NAME')
  })
Config = SystemConfig