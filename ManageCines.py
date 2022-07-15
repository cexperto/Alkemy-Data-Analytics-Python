import pandas as pd
from datetime import datetime

class ManageCines:
    def __init__(self, df):
        self.df = df        

    def manage_cines(self):        
        df_pantallas = self.df.groupby(['Provincia'])['Pantallas'].count()
        df_butacas = self.df.groupby(['Provincia'])['Butacas'].count()
        df_incaa = self.df.groupby(['Provincia'])['espacio_INCAA'].count()
        df_cines = pd.concat([df_pantallas, df_butacas, df_incaa], axis=1, join="inner")
        df_cines['fecha_de_carga'] = datetime.utcnow()
        return df_cines
