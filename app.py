from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from room import Room, RoomList, RoomCreate

app = Flask(__name__)
app.secret_key = 'secret'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Room, '/room/<int:_id>')
api.add_resource(RoomCreate, '/room/create')
api.add_resource(RoomList, '/rooms')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)