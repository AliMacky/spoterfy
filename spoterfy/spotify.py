import click
import requests
from .config import SPOTIFY_API_BASE
from .commands.auth import get_stored_credentials

def get_profile():
    creds = get_stored_credentials()
    if not creds:
        click.echo("No credentials found. Please run 'spoterfy auth' first.")
        return None

    headers = {'Authorization': f"Bearer {creds.get('access_token')}"}
    response = requests.get(f"{SPOTIFY_API_BASE}/me", headers=headers)

    if response.status_code == 401:
        click.echo("Token expired. Please run 'spoterfy auth' again.")
        return None
    elif response.status_code != 200:
        click.echo(f"Error: {response.status_code}")
        click.echo(response.text)
        return None

    return response.json() 

def get_available_devices():
    creds = get_stored_credentials()
    if not creds:
        click.echo("No credentials found. Please run 'spoterfy auth' first.")
        return None

    headers = {'Authorization': f"Bearer {creds.get('access_token')}"}
    response = requests.get(f"{SPOTIFY_API_BASE}/me/player/devices", headers=headers)

    if response.status_code == 401:
        click.echo("Token expired. Please run 'spoterfy auth' again.")
        return None
    elif response.status_code != 200:
        click.echo(f"Error: {response.status_code}")
        click.echo(response.text)
        return None

    return response.json() 

def search(query, searchType, limit=10):
    creds = get_stored_credentials()
    if not creds:
        click.echo("No credentials found. Please run 'spoterfy auth' first.")
        return None

    headers = {'Authorization': f"Bearer {creds.get('access_token')}"}
    params = {
        'q': query,
        'type': searchType,
        'limit': limit
    }
    response = requests.get(f"{SPOTIFY_API_BASE}/search", headers=headers, params=params)

    if response.status_code == 401:
        click.echo("Token expired. Please run 'spoterfy auth' again.")
        return None
    elif response.status_code != 200:
        click.echo(f"Error: {response.status_code}")
        click.echo(response.text)
        return None

    return response.json() 