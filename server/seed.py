from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Song, Playlist

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        User.query.delete()
        Song.query.delete()
        Review.query.delete()
        db.session.commit()

        print("Starting seed...")
        # Seed code goes here!

        u1 = User(fname = 'Kyle', lname = 'Oneill', email= 'koneill@email.com', password = 'password')


        song_list = [
    Song(title="Shake It Off", genre="Pop", album_id="1989"),
    Song(title="Love Story", genre="Country", album_id="Fearless"),
    Song(title="Blank Space", genre="Pop", album_id="1989"),
    Song(title="You Belong With Me", genre="Country", album_id="Fearless"),
    Song(title="Delicate", genre="Pop", album_id="reputation"),
    Song(title="Bad Blood", genre="Pop", album_id="1989"),
    Song(title="We Are Never Ever Getting Back Together", genre="Pop", album_id="Red"),
    Song(title="I Knew You Were Trouble", genre="Pop", album_id="Red"),
    Song(title="Lover", genre="Pop", album_id="Lover"),
    Song(title="Cardigan", genre="Pop", album_id="Folklore"),
    Song(title="Willow", genre="Pop", album_id="Evermore"),
    Song(title="All Too Well", genre="Pop", album_id="Red"),
    Song(title="Mean", genre="Country", album_id="Speak Now"),
    Song(title="Style", genre="Pop", album_id="1989"),
    Song(title="The Man", genre="Pop", album_id="Lover"),
    Song(title="Out Of The Woods", genre="Pop", album_id="1989"),
    Song(title="Red", genre="Country", album_id="Red"),
    Song(title="22", genre="Pop", album_id="Red"),
    Song(title="The 1", genre="Pop", album_id="Folklore"),
    Song(title="Exile", genre="Pop", album_id="Folklore"),
    Song(title="Everlong", genre="Rock", album_id="The Colour and the Shape"),
    Song(title="Learn to Fly", genre="Rock", album_id="There Is Nothing Left to Lose"),
    Song(title="The Pretender", genre="Rock", album_id="Echoes, Silence, Patience & Grace"),
    Song(title="All My Life", genre="Rock", album_id="One by One"),
    Song(title="Times Like These", genre="Rock", album_id="One by One"),
    Song(title="Best of You", genre="Rock", album_id="In Your Honor"),
    Song(title="Monkey Wrench", genre="Rock", album_id="The Colour and the Shape"),
    Song(title="My Hero", genre="Rock", album_id="The Colour and the Shape"),
    Song(title="Run", genre="Rock", album_id="Concrete and Gold"),
    Song(title="No One Knows", genre="Rock", album_id="Songs for the Deaf"),
    Song(title="All the Small Things", genre="Pop Punk", album_id="Enema of the State"),
    Song(title="What's My Age Again?", genre="Pop Punk", album_id="Enema of the State"),
    Song(title="First Date", genre="Pop Punk", album_id="Take Off Your Pants and Jacket"),
    Song(title="Feeling This", genre="Pop Punk", album_id="Blink-182"),
    Song(title="I Miss You", genre="Pop Punk", album_id="Blink-182"),
    Song(title="She's Out of Her Mind", genre="Pop Punk", album_id="California"),
    Song(title="Clocks", genre="Alternative", album_id="A Rush of Blood to the Head"),
    Song(title="Viva la Vida", genre="Alternative", album_id="Viva la Vida or Death and All His Friends"),
    Song(title="Yellow", genre="Alternative", album_id="Parachutes"),
    Song(title="The Scientist", genre="Alternative", album_id="A Rush of Blood to the Head"),
    Song(title="Wasted on You", genre="Country", album_id="Dangerous: The Double Album"),
    Song(title="Sand in My Boots", genre="Country", album_id="Dangerous: The Double Album"),
    Song(title="Cover Me Up", genre="Country", album_id="If I Know Me"),
    Song(title="More Than My Hometown", genre="Country", album_id="Dangerous: The Double Album"),
    Song(title="7 Summers", genre="Country", album_id="Dangerous: The Double Album"),
]


# add the song objects to the database session
for song in song_list:
    db.session.add(song)

# commit the changes to the database
db.session.commit()
      
playlist_list = [
    Playlist(name="Rock Playlist", song_id=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], artist_id=None, user_id=None),
    Playlist(name="Pop Punk Playlist", song_id=[11, 12, 13, 14, 15, 16, 17], artist_id=None, user_id=None),
    Playlist(name="Alternative Playlist", song_id=[18, 19, 20, 21], artist_id=None, user_id=None),
    Playlist(name="Country Playlist", song_id=[22, 23, 24, 25, 26], artist_id=None, user_id=None),
]
        

