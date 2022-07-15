import pandas as pd
from datetime import datetime


class ManageConjuntos:
    
    def __init__(self, table_query, field, operator, condition, engine):
        self.table_query = table_query        
        self.field = field
        self.condition = condition
        self.operator = operator
        self.engine = engine

    def manage_conjuntos(self):
        df = pd.read_sql(f'SELECT count({self.field}) as cantidad FROM \"public\".{self.table_query} where {self.field} {self.operator} \'{self.condition}\'', self.engine)
        df.rename(index={0: self.condition}, inplace=True)
        df['fecha_de_carga'] = datetime.utcnow()
        return df
        
