from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from config import db
from flask import Flask

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    
   

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    playlists = db.relationship("Playlist", backref="user")
    

    # @validates('password')
    # def validate_password(self, key, password):
    #     if password == "":
    #         raise ValueError("Must provide a password")
    #     return password

    # @validates('email')
    # def validate_email(self, key, email):
    #     if (email == "") or ('@' not in email) or ('.' not in email):
    #         raise ValueError("Must provide a valid email")
    #     return email

    # @hybrid_property
    # def password_hash(self):
    #     return self._password_hash
    
    # @password_hash.setter
    # def password_hash(self, password):
        

class Song(db.Model, SerializerMixin):
    __tablename__ = 'songs'
    
   

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    album_id = db.Column(db.Integer, db.ForeignKey ("albums.id"))
    

    
    playlists = db.relationship( 'Playlist', backref = 'song' )
    users = association_proxy( 'playlists', 'users' )




class Artist(db.Model, SerializerMixin):
    __tablename__ = 'artists'
    
   

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genre = db.Column(db.String)
    bio = db.Column(db.String)

    albums = db.relationship( 'Album', backref = 'artist' )
    songs = association_proxy( 'albums', 'songs' )


 

class Playlist(db.Model, SerializerMixin):
    __tablename__ = 'playlists'
    
   

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))
    artist_id = db.Column(db.Integer, db.ForeignKey ("artists.id"))
    user_id = db.Column(db.Integer, db.ForeignKey ("users.id")) 


   

class Album(db.Model, SerializerMixin):
    __tablename__ = 'albums'
    
   

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
