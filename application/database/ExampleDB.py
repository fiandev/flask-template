from application.core.Connection import Connection
from application.utilities.env import env

class ExampleDB (Connection):
    def __init__ (self):
        username = env("DB_USERNAME")
        password = env("DB_PASSWORD")
        clauster = env("DB_CLUSTER")
        client = env("DB_CLIENT")
        
        super().__init__(username, password, clauster, client)