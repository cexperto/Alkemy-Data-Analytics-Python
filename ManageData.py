import requests
import pandas as pd
import io

class ManageDataToDF:
    def __init__(self, url):
        self.url =url

    def get_data_from_url(self):
        try:
            r = requests.get(self.url)
            if r.status_code == 200:
                return r.content
        except:
            raise requests.exceptions.Timeout

    def data_to_df(self, byteData):
        data = io.StringIO(byteData.decode('UTF-8'))
        df = pd.read_csv(data, sep=",")
        return df
    
class Application:
    def extract_data(self, url):
        manage_data = ManageDataToDF(url)
        data_url = manage_data.get_data_from_url()
        df = manage_data.data_to_df(data_url)        
        return df
