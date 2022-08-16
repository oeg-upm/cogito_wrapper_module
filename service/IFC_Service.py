import requests
requests.packages.urllib3.disable_warnings()
import os


class Generate_IFC_Graph:
    def __init__(self): # file = temp.name
        self.url = "https://kgg.openmetrics.eu/"
        self.url_post = "https://kgg.openmetrics.eu/upload"
        self.url_get = "https://kgg.openmetrics.eu/download"
        self.files = []
        self.payload = {}
        self.raw_graph = ""


    def generate_graph(self):
        
        s = requests.Session()
        s.get(self.url, verify=False)

        file_path = "./repository/ifc/files/file.ifc"

        try:
            self.files = [('file',(file_path,open(file_path, 'rb'),'application/octet-stream'))]
        finally:
            os.remove(file_path)

        headers_post = {
            'Cookie': 'JSESSIONID=' + s.cookies.get_dict()['JSESSIONID']
        }
        headers_get = {
            'Cookie': 'JSESSIONID=' + s.cookies.get_dict()['JSESSIONID']
        }
        
        response_post = requests.post(self.url_post, headers=headers_post, data=self.payload, files=self.files, verify=False)
        response_get = requests.get(self.url_get, headers=headers_get, data=self.payload, verify=False)

        self.raw_graph = response_get.text