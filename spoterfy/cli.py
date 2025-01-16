"""
Spoterfy CLI implementation
"""
import click
from .commands.auth import auth
from .commands.profile import profile
from .commands.devices import devices
from .commands.search import search

@click.group()
def cli():
    """Spoterfy - A Spotify CLI tool"""
    pass

cli.add_command(auth)
cli.add_command(profile) 
cli.add_command(devices)
cli.add_command(search)