# cli.py

import click
from controllers import add_artist, list_artists, list_songs_by_genre, delete_artist
from database import init_db

@click.group()
def cli():
    """Welcome to iTubeKENYA CLI - Manage Kenyan music distribution!"""
    pass

@cli.command()
def init():
    """Initialize the database."""
    init_db()
    click.echo("Database initialized!")

@cli.command()
@click.argument('name')
@click.argument('stage_name')
@click.argument('genre')
@click.argument('location')
def add_new_artist(name, stage_name, genre, location):
    """Add a new artist to the database."""
    add_artist(name, stage_name, genre, location)
    click.echo(f"Artist '{name}' added successfully!")

@cli.command()
def list_all_artists():
    """List all artists."""
    artists = list_artists()
    for artist in artists:
        click.echo(f"{artist.stage_name} ({artist.name}) - Genre: {artist.genre.name}, Location: {artist.location}")

@cli.command()
@click.argument('genre')
def list_songs(genre):
    """List all songs by genre."""
    songs = list_songs_by_genre(genre)
    for song in songs:
        click.echo(f"{song.title} by {song.artist.stage_name}")

@cli.command()
@click.argument('artist_id', type=int)
def delete_artist_command(artist_id):
    """Delete an artist by ID."""
    result = delete_artist(artist_id)
    click.echo(result)

# Ensure commands are registered
if __name__ == '__main__':
    cli()
