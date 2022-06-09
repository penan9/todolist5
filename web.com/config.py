DEV_DB = 'sqlite:///data.db'

pg_user = 'admin'
pg_pass = 'admin'
pg_db = 'market'
pg_host = 'localhost'
pg_port = 5432

PROD_DB = f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}'

SESSION_COOKIE_NAME = 'google-login-session'
SECRET_KEY = '4325bedae2c4e7e790c43a05bc14d1914a979f9e07d92236ac93ec9533899fad'
CLIENT_ID = '881072346550-btb1pupabk29t35tcbkejdgh4or62tk8.apps.googleusercontent.com'
CLIENT_SECRET = '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'
ACCESS_TOKEN_URL = 'https://accounts.google.com/o/oauth2/token'
AUTHORIZE_URL = 'https://accounts.google.com/o/oauth2/auth'
API_BASE_URL = 'https://www.googleapis.com/oauth2/v1/'
USERINFO_ENDPOINT = 'https://openidconnect.googleapis.com/v1/userinfo'
