from datetime import datetime
import pandas as pd


class ManageInformacion:
    """
    Class for manage data for information table
    organize data accord standar names in titles in df
    """

    def __init__(self, df):
        self.df = df        
        self.columns = {
            df.columns[0] : 'cod_localidad', 
            df.columns[1] : 'id_provincia',
            df.columns[2] : 'id_departamento', 
            df.columns[4] : 'categoria',
            df.columns[6] : 'provincia', 
            df.columns[7] : 'localidad', 
            df.columns[8] : 'nombre',
            df.columns[9] : 'domicilio',
            df.columns[11]: 'codigo_postal', 
            df.columns[13] : 'numero_de_telefono', 
            df.columns[14] : 'mail', 
            df.columns[15] : 'web'
        }

    def manage_informacion(self):        
        change_names = self.df.rename(columns=self.columns)
        df = change_names[['cod_localidad', 'id_provincia', 'id_departamento', 'categoria', 'provincia',
        'localidad', 'nombre', 'domicilio', 'codigo_postal', 'numero_de_telefono' , 'mail', 'web']]
        
        pd.options.mode.chained_assignment = None  # default='warn'
        df['fecha_de_carga'] = datetime.utcnow()
        return df        
