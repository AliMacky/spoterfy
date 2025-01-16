import click
from ..spotify import get_available_devices

@click.command()
def devices():
    """Get your Spotify available devices information"""
    devices_data = get_available_devices()
    click.echo(devices_data)