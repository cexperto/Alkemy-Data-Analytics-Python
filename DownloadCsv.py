import datetime

import os

class DownloadCsv:
    """
    Class for download csv:
    receive as params:
    data : is a dataframe
    name : is the file name
    """

    def __init__(self, data, name):
        self.data = data
        self.name = name

    def download_data(self):
        today = datetime.date.today()
        path = f'{self.name}/{today.year}/{today.month}'
        os.makedirs(path, exist_ok=True)
        name_file = f'{path}/{self.name}-{today.day}-{today.month}-{today.year}.csv'
        self.data.to_csv(name_file, index=False, encoding='utf-8')






