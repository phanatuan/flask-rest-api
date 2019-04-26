import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource): 

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required = True, help='Please enter username')
    parser.add_argument('password', type=str, required = True, help='Please enter password')

    @classmethod
    def post(cls): 

        data = cls.parser.parse_args()

        username = data['username']
        password = data['password']

        if UserModel.find_by_username(username): 
            return {'error': f'this username {username} already exists, fuck you'}, 400
        
        user = UserModel(**data)
        user.save_to_db()

        return {'user': { 
            'username': username, 
            'password': password
        }
        }, 201

