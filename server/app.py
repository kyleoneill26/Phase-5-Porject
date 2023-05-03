from flask import Flask, make_response, request, session, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError

# Local imports
from config import app, db, api
from models import User,Song,Album,Artist,Playlist


app = Flask( __name__ )

migrate = Migrate( app, db )
db.init_app( app )
api = Api( app )

# Views go here!

class Signup(Resource):
    
    def post(self):

        user_attr = ["username", "password", "email"]
        user_obj = {}

        for attr in user_attr:
            try:
                user_obj[attr] = request.get_json()[attr]
            except ValueError as e:
                return make_response({"Value Error": f"{e}"}, 400)
            
        newUser = User( 
                    username = user_obj[f'{user_attr[0]}'],
                    password_hash = user_obj[f'{user_attr[1]}'],
                    email = user_obj[f'{user_attr[2]}'],
                    )
        
        try:
            db.session.add(newUser)
            db.session.commit()       
        except IntegrityError:
            db.session.rollback()
            return make_response({
                    "Integrity Error": "Invalid Username"
                }, 400)

        db_user = User.query.filter(User.username == user_obj[f'{user_attr[0]}']).one()
        session['user_id'] = db_user.id

        response = make_response(
            newUser.to_dict(
                only = ('username', 'email')
            ),
            201
            )

        return response    

class Login(Resource):

    def post(self):

        sub_user = request.get_json().get('username')
        sub_pass = request.get_json().get('password')

        sel_user = User.query.filter(User.username == sub_user).one_or_none()
        if sel_user == None or sel_user.authenticate(sub_pass) == False:
            return make_response({"error":"Invalid Entry"}, 401)
        else:
            session['user_id'] = sel_user.id
            response = make_response(
                sel_user.to_dict(
                   only = ('username','email') 
                ),
                201
                )
            return response

class Logout(Resource):
    
    def delete(self):
        session.pop('user_id', None)
        response = make_response({"message":"You have been logged out"})
        return response

class CurrentSession(Resource):
    
    def get(self):

        if session['user_id'] is not None:
            
            sel_user = User.query.filter(User.id == session['user_id']).one()
            return make_response(
                sel_user.to_dict(
                    only = ('username','email')
                ),
                200
                )

        else:
            return make_response(
                {"error":"User not found! Please Sign In!"},
                404
            )
   

class Home(Resource):

    def get(self):
        pass


api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CurrentSession, '/currentsession')

if __name__ == '__main__':
    app.run(port=5555, debug=True)







class Users(Resource):
    
    def post(self):
        data = request.get_json()
        try:
            new_user = User(
                name= data['name'],
                genre= data['genre'],
                
                image= data['image']
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
