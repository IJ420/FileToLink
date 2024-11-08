import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '23929647'))
API_HASH = environ.get('API_HASH', 'b9afa697042d998a758e407b84c86daf')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Bot settings
PORT = environ.get("PORT", "8080")

# Online Stream and Download
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002363768606'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '2016390875').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://krishnegi9211:krishnegi9211@cluster0.soq6v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")

# Shortlink Info
SHORTLINK = bool(environ.get('SHORTLINK', True)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'runurl.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '3a316a64da231058d60e832717d6c32da304d12d')
