# Configuration file for jupyterhub.
import os
import sys
from dotenv import load_dotenv

load_dotenv()

c = get_config()  #noqa
'''
# Oauthenticator settings
c.JupyterHub.authenticator_class = "cilogon"
c.OAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']
c.OAuthenticator.client_id = os.environ['OAUTH_CLIENT_ID']
c.OAuthenticator.client_secret = os.environ['OAUTH_CLIENT_SECRET']
'''
# Dummy Authenticator for testing
c.JupyterHub.authenticator_class = 'dummy'
c.Authenticator.allowed_users = {'songzl8'}
c.Authenticator.admin_users = {'songzl8'}
c.DummyAuthenticator.password = "12345678"

# spawner settings
c.Spawner.notebook_dir="cybertraining/assignments"