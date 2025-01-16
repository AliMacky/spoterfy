import click
import inquirer
import sys
from ..spotify import search as spotify_search
from ..utils import handle_keyboard_interrupt, suppress_inquirer_stderr

SEARCH_TYPES = [
    ('Tracks 🎵', 'track'),
    ('Artists 👤', 'artist'),
    ('Albums 💿', 'album'),
    ('Playlists 📂', 'playlist')
]

@click.command()
@click.option('--type', '-t', type=click.Choice(['track', 'artist', 'album', 'playlist']), help='Type of search to perform')
@click.option('--limit', '-l', type=int, default=10, help='Number of results to show (max 50)')
@click.argument('query', required=False)
@handle_keyboard_interrupt
def search(type, query, limit):
    """Search Spotify for tracks, artists, albums, or playlists"""
    limit = min(max(1, limit), 50)
    
    if not type:
        questions = [
            inquirer.List('type',
                         message="What would you like to search for?",
                         choices=SEARCH_TYPES,
                         default='track')
        ]
        answers = suppress_inquirer_stderr(inquirer.prompt)(questions)
        if answers is None:
            sys.exit(1)
        type = answers['type']
    
    if not query:
        query = click.prompt("Enter your search query")
    
    results = spotify_search(query, type, limit)
    if not results:
        return
    
    items = results.get(f"{type}s", {}).get("items", [])
    if not items:
        click.echo(f"No {type}s found for query: {query}")
        return

    for item in items:
        if type == 'track':
            click.echo(f"🎵 {item['name']} - {', '.join(artist['name'] for artist in item['artists'])}")
        elif type == 'artist':
            click.echo(f"👤 {item['name']}")
        elif type == 'album':
            click.echo(f"💿 {item['name']} - {item['artists'][0]['name']}")
        elif type == 'playlist':
            click.echo(f"📂 {item['name']} - {item['owner']['display_name']}")