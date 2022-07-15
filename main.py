"""
This file is the entry point for execute the program
"""
import logging
from ManageInformacion import ManageInformacion
from ManageData import Application
from ManageConjuntos import ManageConjuntos
from ManageCines import ManageCines
from InsertData import InsertData
from DownloadCsv import DownloadCsv
from conexion import do_conection

app_data = Application()
engine = do_conection()


def execute_informacion(urls, table_insert):
    for k in urls.values():
        df = app_data.extract_data(k)
        data_informacion = ManageInformacion(df).manage_informacion()
        InsertData(data_informacion, table_insert, engine).insert_data()
    

def execute_conjuntos(table_query: str, table_insert: str, fields: list, operator: list, conditions: list):
    for condition in conditions:
        insert_categories = ManageConjuntos(table_query, fields[0], operator[0], condition, engine).manage_conjuntos()
        InsertData(insert_categories, table_insert, engine).insert_data()
    
    insert_fuente = ManageConjuntos(table_query, fields[1], operator[1], 'fuente', engine).manage_conjuntos()    
    insert_provincia = ManageConjuntos(table_query, fields[2], operator[1], 'provincia', engine).manage_conjuntos()
    InsertData(insert_fuente, table_insert, engine).insert_data()
    InsertData(insert_provincia, table_insert, engine).insert_data()

    
def execute_cines(url, table_insert):
    df = app_data.extract_data(url)
    manage_cines = ManageCines(df).manage_cines()
    InsertData(manage_cines, table_insert, engine).insert_data()
    
def downloads_csv(urls):
    for i in urls:
        manage_data = Application().extract_data(urls[i])
        download_file = DownloadCsv(manage_data, i).download_data()

urls = {
    'museos' : 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv',
    'cine' : 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv',
    'bibliotecas' : 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'
}

if __name__ == '__main__':
    logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style='{',
    filename='log.log',
    filemode='w'
    )
    conditions = ['Espacios de Exhibición Patrimonial', 'Salas de cine', 'Bibliotecas Populares']
    fields = ['categoria', 'web', 'provincia']
    table_query = 'informacion'
    table_insert = 'conjuntos'
    operators = ['=','!=']
    logging.info('Start download files')
    downloads_csv(urls)
    logging.info('Files downloaded')
    execute_informacion(urls, 'informacion')
    logging.info('Inserted data in information table')
    execute_conjuntos(table_query, table_insert, fields, operators, conditions)
    logging.info('Inserted data in conjuntos table')
    execute_cines(urls['cine'], 'informacioncines')
    logging.info('Inserted data in cines table')
    logging.info('Exit executed')


