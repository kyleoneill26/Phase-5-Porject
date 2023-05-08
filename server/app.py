from flask import Flask, request, make_response, session
from flask_migrate import Migrate
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError

# Local imports
from config import app, db, api
from models import User,Song,Album,Artist,Playlist



app.secret_key = b"\x7f\x7f(\xe8\x0c('\xa8\xa5\x82pb\t\x1d>rZ\x8c^\x7f\xbb\xe2L|"


class CheckSession(Resource):

    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first()
        if user:
            return user.to_dict()
        else:
            return {'message': '401: Not Authorized'}, 401

api.add_resource(CheckSession, '/check_session')

class Login(Resource):

    def post(self):
        user = User.query.filter(
            User.email == request.get_json()['email']
        ).first()
        
        if (user.password == request.get_json()['password']):
            session['user_id'] = user.id
            return user.to_dict()
        else:
            return {'message': '401: Not Authorized'}, 401

api.add_resource(Login, '/login')

class Logout(Resource):

    def delete(self):
        session['user_id'] = None
        return {'message': '204: No Content'}, 204

api.add_resource(Logout, '/logout')






class Users(Resource):
    def get(self):
        users = Users.query.all()
        users_dict = [user.to_dict() for user in users]
        if users == None:
            return make_response( { 'error' : '404: User Not Found' } )
        return make_response( users_dict, 200 )


    def post(self):
        data = request.get_json()
        try:
            new_user = User(
                fname = data['fname'],
                lname = data['lname'],
                email = data['email'],
                password = data['password'],
            )
        except: 
            return make_response({'error': '400 validation error'} ,400)
        db.session.add(new_user)
        db.session.commit()
        return make_response( new_user.to_dict(), 201) 
    

api.add_resource(Users, '/users')

class UsersById(Resource):
    def get(self, id):
        user = User.query.filter_by(id = id).first()
        if not user: 
            return make_response({'error': '404 user not found'} ,404)
        else:
            return make_response(user.to_dict(), 200) 

 

    def delete(self, id):
        user = User.query.filter_by(id = id).first()
        if not user: 
            return make_response({'error': '404 user not found'} ,404)
        else:
            db.session.delete(user)
            db.session.commit()
        return make_response({}, 204)


api.add_resource(UsersById, '/users/<int:id>') 


class Songs( Resource ):
    def get( self ):
        songs_list = []
        for s in Song.query.all():
            s_dict = {
                'id': s.id,
                'title': s.title,
                'genre': s.genre
            }
            songs_list.append( s_dict )
        return make_response( songs_list, 200 )

   
api.add_resource( Songs, '/songs' )



class Artists( Resource ):
    def get( self ):
        artists_list = []
        for a in Artist.query.all():
            a_dict = {
                'id': a.id,
                'name': a.name,
                'bio': a.bio
            }
            artists_list.append( a_dict )
        return make_response( artists_list, 200 )

    
api.add_resource( Artists, '/artists' )








class Playlists( Resource ):
    def get( self ):
        playlists_list = []
        for p in Playlist.query.all():
            p_dict = {
                'id': p.id,
                'name': p.name,
                'description': p.age
            }
            playlists_list.append( p_dict )
        return make_response( playlists_list, 200 )

    def post( self ):
        data = request.get_json()
        new_playlist = Playlist( name = data['name'], description = data['description'] )
        try:
            db.session.add( new_playlist )
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return make_response( {'error': 'validation errors'}, 422 )
        return make_response( new_playlist.to_dict(), 201 )

api.add_resource( Playlists, '/playlists' )


class PlaylistsById( Resource ):

    def get( self, id ):
        p = Playlist.query.filter_by( id = id ).first()
        if p == None:
            return make_response( { 'msg': 'Playlist not found' }, 404 )
        return make_response( p.to_dict(), 200 )

    def patch( self, id ):
        p = Playlist.query.filter_by( id = id ).first()
        if p == None:
            return make_response( { 'msg': 'Playlist not found' }, 404 )
        data = request.get_json()
        for key in data.keys():
            setattr( p, key, data[key] )
        db.session.add( p )
        db.session.commit()
        return make_response( p.to_dict(), 200 )

    def delete( self, id ):
        p = Playlist.query.filter_by( id = id ).first()
        if p == None:
            return make_response( { 'msg': 'Playlist not found' }, 404 )
        db.session.delete( p )
        db.session.commit()
        return make_response( {'msg': 'success'}, 200 )

api.add_resource( PlaylistsById, '/playlists/<int:id>')


class Albums( Resource ):
    def get( self ):
        albums_list = []
        for a in Album.query.all():
            a_dict = {
                'id': a.id,
                'title': a.name,
                'description': a.age
            }
            albums_list.append( a_dict )
        return make_response( albums_list, 200 )

    
api.add_resource( Albums, '/albums' )



if __name__ == '__main__':
    app.run(port=5555, debug=True)
