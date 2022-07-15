
from sqlalchemy import Column, Integer, String, BIGINT, TEXT, DATE
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import logging
from conexion import do_conection


Base = declarative_base()

class Informacion(Base):
    __tablename__ = 'informacion'

    id = Column(Integer, primary_key=True)
    index = Column(Integer)
    cod_localidad = Column(BIGINT)
    id_provincia = Column(BIGINT)
    id_departamento = Column(BIGINT)
    categoria = Column(TEXT)
    provincia = Column(TEXT)
    localidad = Column(TEXT)
    nombre = Column(TEXT)
    domicilio = Column(TEXT)
    codigo_postal = Column(TEXT)
    numero_de_telefono = Column(TEXT)
    mail = Column(TEXT)
    web = Column(TEXT)
    fecha_de_carga = Column(DATE)
    

class Conjuntos(Base):
    __tablename__ = 'conjuntos'

    id = Column(Integer, primary_key=True)
    index = Column(TEXT)
    cantidad = Column(BIGINT)
    fecha_de_carga = Column(DATE)

    

class InformacionCines(Base):
    __tablename__ = 'informacioncines'

    id = Column(Integer, primary_key=True)
    Provincia = Column(String)
    Pantallas = Column(Integer)
    Butacas = Column(Integer)
    espacio_INCAA = Column(Integer)
    fecha_de_carga = Column(DATE)

    
engine = do_conection()

class ManageSession:
    def manage_session(self):        
        Session = sessionmaker(engine)
        session = Session()
        return session
        

if __name__ == '__main__':
    logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style='{',
    filename='log.log',
    filemode='w'
    )
    Base.metadata.drop_all(engine)
    logging.info('drop DB')
    Base.metadata.create_all(engine)
    logging.info('create DB')
