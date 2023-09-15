from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

db = "wms"

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.role = data["role"]

    @classmethod
    def create_user(cls, data):
        data["password"] = bcrypt.generate_password_hash(data["password"])
        query = """
            INSERT INTO users (name, password, role)
            VALUES (%(name)s, %(password)s, %(role)s);
            """
        user_id = connectToMySQL(db).query_db(query, data)
        return user_id