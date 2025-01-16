# Spoterfy 🎵

A powerful command-line interface for Spotify that lets you control your music playback and manage your Spotify account right from your terminal.

## Features

- 🔐 Secure OAuth2 authentication with Spotify
- 👤 View your Spotify profile information
- 🎮 List and manage your Spotify playback devices
- 🎧 More features coming soon...

## Prerequisites

- Python 3.8 or higher
- A Spotify account (Free or Premium)

## Setting Up Your Development Environment

### Creating a Virtual Environment

Always use a virtual environment to isolate project dependencies and avoid conflicts with other Python projects:

```bash
# Create a virtual environment in the project directory
python -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

Your terminal prompt should now show `(.venv)`, indicating the virtual environment is active. Always make sure your virtual environment is activated when working on this project.

To deactivate the virtual environment when you're done:
```bash
deactivate
```

## Installation

1. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install Spoterfy:
   ```bash
   pip install spoterfy
   ```

## Setting up your Spotify Application

Before using Spoterfy, you'll need to create a Spotify application. This is a one-time setup process:

1. Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)

2. Log in with your Spotify account

3. Click "Create App"
   - App name: Choose any name (e.g., "My Spoterfy CLI")
   - App description: Optional
   - Redirect URI: Add `http://localhost:8080/callback`
   - Click "Create"

4. On your app's page, you'll see your Client ID
   - Click "Settings" to view your Client Secret
   - Keep these values handy for the next step

5. Configure Spoterfy with your app credentials:
   ```bash
   spoterfy auth
   ```
   - When prompted, enter your Client ID and Client Secret
   - These will be saved securely in a `.env.local` file

## Usage

### First-time Authentication

1. Run the authentication command:
   ```bash
   spoterfy auth
   ```

2. Your browser will open automatically to log in to Spotify
   - Grant the requested permissions
   - The window will close automatically when done

### Available Commands

View your profile information:
```bash
spoterfy profile
```

List your available Spotify devices:
```bash
spoterfy devices
```

Search Spotify for tracks, artists, albums, or playlists:
```bash
# Interactive search (will prompt for type and query)
spoterfy search

# Search with specific type and query
spoterfy search --type track "your search query"

# Limit the number of results (max 50)
spoterfy search --type album --limit 20 "your search query"
```

Available search types:
- `track`: Search for songs
- `artist`: Search for artists
- `album`: Search for albums
- `playlist`: Search for playlists

## Troubleshooting

### Common Issues

1. **"No Spotify API credentials found"**
   - Run `spoterfy auth` to set up your credentials
   - Make sure you've created a Spotify app and added the correct redirect URI

2. **401 Unauthorized Error**
   - Your token might have expired. Run `spoterfy auth` again
   - Verify your Client ID and Secret are correct

3. **Callback URI Error**
   - Make sure you've added `http://localhost:8080/callback` to your Spotify app's Redirect URIs

### Still Having Issues?

- Check if your Spotify application settings are correct in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
- Ensure you have the latest version of Spoterfy installed
- Try removing the credentials file (`~/.config/spoterfy/credentials.json`) and authenticating again

## Development

Want to contribute to Spoterfy? Here's how to set up the development environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spoterfy.git
   cd spoterfy
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Run the CLI in development mode:
   ```bash
   poetry run spoterfy
   ```

## Security Notes

- Your Spotify API credentials are stored locally in `.env.local`
- Access tokens are stored in `~/.config/spoterfy/credentials.json`
- Never share your Client Secret or access tokens
- The application only requests the minimum required permissions (scopes) to function

## License

This project is licensed under the MIT License - see the LICENSE file for details. 