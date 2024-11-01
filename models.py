# models.py

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    artists = relationship("Artist", back_populates="genre")
    songs = relationship("Music", back_populates="genre")

class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    stage_name = Column(String, nullable=False)
    genre_id = Column(Integer, ForeignKey('genres.id'))
    bio = Column(String)
    location = Column(String)
    genre = relationship("Genre", back_populates="artists")
    songs = relationship("Music", back_populates="artist")

class Producer(Base):
    __tablename__ = 'producers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    studio_name = Column(String)
    location = Column(String)
    genre_id = Column(Integer, ForeignKey('genres.id'))
    genre = relationship("Genre")
    songs = relationship("Music", back_populates="producer")

class Music(Base):
    __tablename__ = 'music'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_date = Column(Date)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    producer_id = Column(Integer, ForeignKey('producers.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))
    artist = relationship("Artist", back_populates="songs")
    producer = relationship("Producer", back_populates="songs")
    genre = relationship("Genre", back_populates="songs")
