

#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Song, Playlist, Artist

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

s1 = Song(title="test",genre="testing",album_id="1")
db.session.add(s1)
db.session.commit


# from flask_sqlalchemy import SQLAlchemy


# # Remote library imports


# # Local imports
# from app import app
# from models import db, User, Song, Playlist, Artist

# if __name__ == '__main__':


u1 = User(fname = 'Kyle', lname = 'Oneill', email= 'koneill@email.com', password = 'password')






# # create a list of songs with artists
#     song_list = [
#         Song(title="Love Story", genre="Country Pop", album_id="Fearless", artist_id=1),
#         Song(title="You Belong with Me", genre="Country Pop", album_id="Fearless", artist_id=1),
#         Song(title="Teardrops on My Guitar", genre="Country Pop", album_id="Taylor Swift", artist_id=1),
#         Song(title="I Knew You Were Trouble", genre="Pop", album_id="Red", artist_id=1),
#         Song(title="We Are Never Ever Getting Back Together", genre="Pop", album_id="Red", artist_id=1),
#         Song(title="Blank Space", genre="Pop", album_id="1989", artist_id=1),
#         Song(title="Shake It Off", genre="Pop", album_id="1989", artist_id=1),
#         Song(title="Bad Blood", genre="Pop", album_id="1989", artist_id=1),
#         Song(title="Look What You Made Me Do", genre="Pop", album_id="Reputation", artist_id=1),
#         Song(title="Delicate", genre="Pop", album_id="Reputation", artist_id=1),
#         Song(title="End Game (feat. Ed Sheeran and Future)", genre="Pop", album_id="Reputation", artist_id=1),
#         Song(title="Me! (feat. Brendon Urie)", genre="Pop", album_id="Lover", artist_id=1),
#         Song(title="You Need to Calm Down", genre="Pop", album_id="Lover", artist_id=1),
#         Song(title="The Man", genre="Pop", album_id="Lover", artist_id=1),
#         Song(title="cardigan", genre="Alternative", album_id="folklore", artist_id=1),
#         Song(title="august", genre="Alternative", album_id="folklore", artist_id=1),
#         Song(title="willow", genre="Alternative", album_id="evermore", artist_id=1),
#         Song(title="no body, no crime (feat. HAIM)", genre="Alternative", album_id="evermore", artist_id=1),
#         Song(title="dorothea", genre="Alternative", album_id="evermore", artist_id=1),
#         Song(title="Everlong", genre="Rock", album_id="The Colour and the Shape", artist_id=2),
#         Song(title="Learn to Fly", genre="Rock", album_id="There Is Nothing Left to Lose", artist_id=2),
#         Song(title="Best of You", genre="Rock", album_id="In Your Honor", artist_id=2),
#         Song(title="The Pretender", genre="Rock", album_id="Echoes, Silence, Patience & Grace", artist_id=2),
#         Song(title="Rope", genre="Rock", album_id="Wasting Light", artist_id=2),
#         Song(title="All the Small Things", genre="Pop Punk", album_id="Enema of the State", artist_id=3),
#         Song(title="What's My Age Again?", genre="Pop Punk", album_id="Enema of the State", artist_id=3),
#         Song(title="Adam's Song", genre="Pop Punk", album_id="Enema of the State", artist_id=3),
#         Song(title="Feeling This", genre="Pop Punk", album_id="Blink-182", artist_id=3),
#         Song(title="I Miss You", genre="Pop Punk", album_id="Blink-182", artist_id=3),
#         Song(title="First Date", genre="Pop Punk", album_id="Take Off Your Pants and Jacket", artist_id=3),
#         Song(title="Always", genre="Pop Punk", album_id="Blink-182", artist_id=3),
#         Song(title="Violet Hill", genre="Alternative", album_id="Viva la Vida or Death and All His Friends", artist_id=4),
#         Song(title="Paradise", genre="Alternative", album_id="Mylo Xyloto", artist_id=4),
#         Song(title="Magic", genre="Alternative", album_id="Ghost Stories", artist_id=4),
#         Song(title="A Sky Full of Stars", genre="Alternative", album_id="Ghost Stories", artist_id=4),
#         Song(title="Adventure of a Lifetime", genre="Alternative", album_id="A Head Full of Dreams", artist_id=4),
#         Song(title="Higher Power", genre="Alternative", album_id="Music of the Spheres", artist_id=4),
#         Song(title="Whiskey Glasses", genre="Country", album_id="If I Know Me", artist_id=5),
#         Song(title="Up Down (feat. Florida Georgia Line)", genre="Country", album_id="If I Know Me", artist_id=5),
#         Song(title="Chasin' You", genre="Country", album_id="If I Know Me", artist_id=5),
#         Song(title="More Than My Hometown", genre="Country", album_id="Dangerous: The Double Album", artist_id=5),
#         Song(title="7 Summers", genre="Country", album_id="Dangerous: The Double Album", artist_id=5),
#         Song(title="Sand in My Boots", genre="Country", album_id="Dangerous: The Double Album", artist_id=5),
#         Song(title="Somebody's Problem", genre="Country", album_id="Dangerous: The Double Album", artist_id=5),
#         Song(title="Livin' the Dream", genre="Country", album_id="Dangerous: The Double Album", artist_id=5),
#         Song(title="Warning", genre="Country", album_id="Dangerous: The Double Album", artist_id=5),
#         Song(title="This Bar", genre="Country", album_id="Dangerous: The Double Album", artist_id=5),
#         Song(title="7 Summers - Remix (feat. Kid Cudi)", genre="Country", album_id="Dangerous: The Double Album (Dangerous Edition)", artist_id=5)
#     ]


# for song in song_list:
#     db.session.add(song)


# artist_list = [
#     Artist(name="Taylor Swift"),
#     Artist(name="Foo Fighters"),
#     Artist(name="Blink-182"),
#     Artist(name="Coldplay"),
#     Artist(name="Morgan Wallen")
# ]
# for artist in artist_list:
#     db.session.add(artist)


# playlist_list = [
#     Playlist(name="Rock Playlist", song_id=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], artist_id=None, user_id=None),
#     Playlist(name="Pop Punk Playlist", song_id=[11, 12, 13, 14, 15, 16, 17], artist_id=None, user_id=None),
#     Playlist(name="Alternative Playlist", song_id=[18, 19, 20, 21], artist_id=None, user_id=None),
#     Playlist(name="Country Playlist", song_id=[22, 23, 24, 25, 26], artist_id=None, user_id=None)
# ]
        

# for playlist in playlist_list:
#     db.session.add(playlist)