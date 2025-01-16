import click
from ..spotify import get_profile

@click.command()
def profile():
    """Get your Spotify profile information"""
    profile_data = get_profile()
    if profile_data:
        click.echo("\n🎵 Spotify Profile Information:")
        click.echo(f"Display Name: {profile_data.get('display_name', 'N/A')}")
        click.echo(f"Email: {profile_data.get('email', 'N/A')}")
        click.echo(f"Country: {profile_data.get('country', 'N/A')}")
        click.echo(f"Account Type: {profile_data.get('product', 'N/A').title()}")
        click.echo(f"Followers: {profile_data.get('followers', {}).get('total', 0)}")
        if profile_data.get('images'):
            click.echo(f"Profile Image: {profile_data['images'][0].get('url', 'N/A')}")
        click.echo(f"Spotify URI: {profile_data.get('uri', 'N/A')}") 