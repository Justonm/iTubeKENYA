# controllers.py

import click
from models import Artist, Genre, Music
from database import SessionLocal
from sqlalchemy.orm import joinedload

def add_artist(name, stage_name, genre_name, location):
    """Add a new artist to the database with a specified genre."""
    session = SessionLocal()
    
    # Check if the genre exists; if not, create it
    genre = session.query(Genre).filter_by(name=genre_name).first()
    if not genre:
        genre = Genre(name=genre_name)
        session.add(genre)
        session.commit()
    
    # Create and add the artist
    artist = Artist(name=name, stage_name=stage_name, genre_id=genre.id, location=location)
    session.add(artist)
    session.commit()
    session.close()

def list_artists():
    """Return a list of all artists with their genres eagerly loaded."""
    session = SessionLocal()
    artists = session.query(Artist).options(joinedload(Artist.genre)).all()
    session.close()
    return artists

def list_songs_by_genre(genre_name):
    """Return a list of songs by a specific genre."""
    session = SessionLocal()
    genre = session.query(Genre).filter_by(name=genre_name).first()
    if not genre:
        session.close()
        click.echo(f"Genre '{genre_name}' not found.")
        return []

    songs = session.query(Music).filter(Music.genre_id == genre.id).options(joinedload(Music.artist)).all()
    session.close()
    if not songs:
        click.echo(f"No songs found for genre '{genre_name}'.")
        return []
    
    return songs

def delete_artist(artist_id):
    """Delete an artist by ID from the database."""
    session = SessionLocal()
    artist = session.query(Artist).filter_by(id=artist_id).first()
    if artist:
        session.delete(artist)
        session.commit()
        session.close()
        return f"Artist with ID {artist_id} deleted successfully."
    else:
        session.close()
        return f"Artist with ID {artist_id} not found."
