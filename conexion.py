from sqlalchemy import create_engine
from sqlalchemy.exc import DisconnectionError


from src.app import host, database, user, port, password

class ConexionToPostgreSQL:
    def __init__(self, host, database, user, port, password):
        self.host = host
        self.database = database
        self.user = user
        self.port = port
        self.password = password


    def conexion(self):
        try:
            conexion_string = f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
            alchemyEngine = create_engine(conexion_string)            
            return alchemyEngine
        except:
            raise DisconnectionError

def do_conection():
    instance_conexion = ConexionToPostgreSQL(host, database, user, port, password)
    return instance_conexion.conexion()

