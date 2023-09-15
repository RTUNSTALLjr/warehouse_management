from flask_app.config.mysqlconnection import connectToMySQL

db = "wms"

class Role:
    def __init__ (self, data):
        self.id = data["id"]
        self.type = data["type"]
    
    @classmethod
    def create_role (cls, data):
        query = """
            INSERT INTO roles (type)
            VALUES (%(type)s)
            ;"""
        connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def get_all_roles (cls):
        query = """
            SELECT *
            FROM roles
            ORDER BY type
            """
        results = connectToMySQL(db).query_db(query)
        role_list = []
        if results:
            for row in results:
                role_list.append(cls(row))
        return role_list