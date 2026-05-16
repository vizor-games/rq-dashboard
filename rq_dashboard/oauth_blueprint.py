import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, redirect, url_for, session, g, jsonify, request, Blueprint
from authlib.integrations.flask_client import OAuth

from .web import blueprint as rq_dashboard_blueprint

OIDC_CLIENT_ID = os.environ.get('OIDC_CLIENT_ID')
OIDC_CLIENT_SECRET = os.environ.get('OIDC_CLIENT_SECRET')
OIDC_SERVER_METADATA_URL = os.environ.get('OIDC_SERVER_METADATA_URL')

oauth_bp = Blueprint('oauth', __name__)

oauth = OAuth()

oauth.register(
    name='oidc_provider',
    client_id=OIDC_CLIENT_ID,
    client_secret=OIDC_CLIENT_SECRET,
    server_metadata_url=OIDC_SERVER_METADATA_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)


@oauth_bp.route('/login')
def login():
    redirect_uri = url_for('oauth.auth_callback', _external=True)
    return oauth.oidc_provider.authorize_redirect(redirect_uri)


@oauth_bp.route('/auth-callback')
def auth_callback():
    try:
        token = oauth.oidc_provider.authorize_access_token()
        logging.warning(token)
        session['user'] = token.get('userinfo')
        return redirect(url_for('rq_dashboard.queues_overview'))

    except Exception as e:
        return f"Oauth error: {e}", 400