import os
import json
import click
import webbrowser
import threading
import time
import secrets
from bottle import Bottle, request
import requests
from ..config import AUTH_URL, TOKEN_URL, REDIRECT_URI, SCOPE, CREDS_FILE

def get_stored_credentials():
    try:
        with open(CREDS_FILE) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def save_credentials(creds):
    with open(CREDS_FILE, 'w') as f:
        json.dump(creds, f)

def create_env_file():
    click.echo("Please enter your Spotify API credentials:")
    client_id = click.prompt("Client ID", type=str)
    client_secret = click.prompt("Client Secret", type=str, hide_input=True)
    
    env_content = f"""# Spotify API Credentials
SPOTIFY_CLIENT_ID='{client_id}'
SPOTIFY_CLIENT_SECRET='{client_secret}'
"""
    with open(".env.local", "w") as f:
        f.write(env_content)
    
    click.echo("\nCredentials saved to .env.local")
    from dotenv import load_dotenv
    load_dotenv(".env.local", override=True)

def authenticate():
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

    if not client_id or not client_secret:
        click.echo("No Spotify API credentials found.")
        if click.confirm("Would you like to set them up now?", default=True):
            create_env_file()
            client_id = os.getenv('SPOTIFY_CLIENT_ID')
            client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        else:
            click.echo("\nYou can set up your credentials later by:")
            click.echo("1. Creating a Spotify app at https://developer.spotify.com/dashboard")
            click.echo("2. Adding http://localhost:8080/callback as a Redirect URI")
            click.echo("3. Creating a .env.local file with your credentials")
            click.echo("\nSee .env.example for the format.")
            return False

    app = Bottle()
    state = secrets.token_urlsafe(16)
    auth_finished = False
    server = None

    def run_server():
        nonlocal server
        server = app.run(host='localhost', port=8080, quiet=True)

    @app.route('/callback')
    def callback():
        nonlocal auth_finished, server
        error = request.query.get('error')
        if error:
            return f"Error: {error}"

        if request.query.get('state') != state:
            return "State mismatch. Possible CSRF attack."

        code = request.query.get('code')
        token_data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI,
            'client_id': client_id,
            'client_secret': client_secret
        }

        token_response = requests.post(TOKEN_URL, data=token_data)
        if token_response.status_code != 200:
            return f"Failed to get access token: {token_response.text}"

        save_credentials(token_response.json())
        auth_finished = True
        
        def shutdown():
            time.sleep(1)
            server.stop()
        
        threading.Thread(target=shutdown).start()
        return "Authentication successful! You can close this window."

    click.echo("Starting authentication server...")
    
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
    time.sleep(0.5)
    
    params = {
        'client_id': client_id,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'state': state,
        'scope': SCOPE
    }
    auth_url = f"{AUTH_URL}?{requests.compat.urlencode(params)}"
    
    click.echo("Opening browser for Spotify login...")
    webbrowser.open(auth_url)

    while not auth_finished and server_thread.is_alive():
        time.sleep(0.5)

    if auth_finished:
        click.echo("✨ Authentication completed successfully!")
        return True
    else:
        click.echo("❌ Authentication failed or was interrupted.")
        return False

@click.command()
def auth():
    """Authenticate with Spotify"""
    authenticate() 