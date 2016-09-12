DEBUG = True
AUTH_REQUIRED = True
SECRET_TOKEN = 'super-secret'
# Request header used to send the token. Gitlab uses X-Gitlab-Token:
TOKEN_HEADER = 'X-Gitlab-Token'
URL_PREFIX = '/gitlab/v1'
LISTENER = 'http://10.112.0.113:5000/git/v1/saltenvs'
