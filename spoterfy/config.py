"""
Configuration settings for the Spoterfy CLI
"""
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env files
load_dotenv()  # load from .env
load_dotenv(".env.local", override=True)  # override with .env.local if it exists

# Spotify API endpoints
SPOTIFY_API_BASE = "https://api.spotify.com/v1"
AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
REDIRECT_URI = "http://localhost:8080/callback"

# OAuth scopes
SCOPE = "user-read-private user-read-email user-read-playback-state"

# File paths
CONFIG_DIR = Path.home() / ".config" / "spoterfy"
CREDS_FILE = CONFIG_DIR / "credentials.json"

# Ensure config directory exists
CONFIG_DIR.mkdir(parents=True, exist_ok=True) 