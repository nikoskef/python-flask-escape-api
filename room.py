import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Room(Resource):
    def get(self, _id):
        room = self.find_by_id(_id)
        if room:
            return room
        return {'message': 'Room not Found'}, 404

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM rooms WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'room': {
                'id': row[0],
                'Company': row[1],
                'Location': row[2],
                'Name': row[3],
                'Description': row[4],
                'Rate of Escape': row[5],
                'img': row[6],
                'Duration': row[7],
                'Played On': row[8]
                }
            }


class RoomList(Resource):
    def get(self):
        rooms = self.get_all_rooms()
        if rooms:
            return rooms
        return {'message': 'No rooms to display'}, 404

    @classmethod
    def get_all_rooms(cls):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM rooms"
        result = cursor.execute(query)
        rooms = []
        for row in result:
            rooms.append({'id': row[0],
                          'Company': row[1],
                          'Location': row[2],
                          'Name': row[3],
                          'Description': row[4],
                          'Rate of Escape': row[5],
                          'img': row[6],
                          'Duration': row[7],
                          'Played On': row[8]})

        connection.close()
        return {'rooms': rooms}


class RoomCreate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('company',
                        type=str,
                        required=True,
                        help='You must enter company'
                        )
    parser.add_argument('location',
                        type=str,
                        required=True,
                        help='You must enter a location'
                        )
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='You must enter a name'
                        )
    parser.add_argument('description',
                        type=str,
                        required=True,
                        help='You must enter a description'
                        )
    parser.add_argument('rateofescape',
                        type=str,
                        required=True,
                        help='You must enter a Rate of Escape'
                        )
    parser.add_argument('image',
                        type=str,
                        required=True,
                        help='You must enter an Image'
                        )
    parser.add_argument('duration',
                        type=str,
                        required=True,
                        help='You must enter a Duration'
                        )
    parser.add_argument('playedon',
                        type=str,
                        required=True,
                        help='You must enter a playedon'
                        )

    def post(self):
        data = RoomCreate.parser.parse_args()
        rooms = RoomList.get_all_rooms()
        if rooms:
            for room in rooms['rooms']:
                if room['Name'].lower() == data['name'].lower() and room['Company'].lower() == data['company'].lower():
                    return {'message':"{} by {} already exists".format(room['Name'], room['Company'])}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO rooms VALUES (NULL,?, ?, ? ,? ,? ,? ,? ,?)"

        cursor.execute(query, (data['company'], data['location'], data['name'], data['description'], data['rateofescape'], data['image'], data['duration'], data['playedon']))

        connection.commit()
        connection.close()

        return {'message': 'Room Created'}, 201