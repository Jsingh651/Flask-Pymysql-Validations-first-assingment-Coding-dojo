from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all (cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for i in results:
            users.append(cls(i))
        return users

    @classmethod 
    def create_user(cls,data):
        query = 'INSERT INTO users(first_name, last_name, email) VALUES (%(first_name)s,%(last_name)s,%(email)s);'
        return connectToMySQL('users_schema').query_db(query,data)


    @staticmethod
    def validate_users(user):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        is_valid = True
        if len(user['first_name']) < 1:
            flash("First name must be at least 1 character.")
            is_valid = False
        if len(user['last_name']) < 1:
            flash("Last name must be at least 1 character.")
            is_valid = False
        if len(user['email']) <= 1: 
            flash("Invalid email address!")
            is_valid = False
        return is_valid
