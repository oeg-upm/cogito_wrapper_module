import requests
from WrapperConfiguration import WrapperConfiguration
from service.Error_service import Error_service
import json
from rdflib import Graph

class Coppola_Controller:
    def __init__(self, ttl, project_id, file_id=None):
        self.coppola_endpoint = None
        self.ttl = ttl
        self.url_list = None
        self.response_list = None
        self.thing_manager_endpoint = None
        self.project_id = project_id
        self.file_id = file_id
        self.shacl_shapes_path = [
            "./repository/shacl_shapes/facility-shapes.ttl",
            "./repository/shacl_shapes/process-shapes.ttl",
            "./repository/shacl_shapes/quality-shapes.ttl",
            "./repository/shacl_shapes/resource-shapes.ttl",
            "./repository/shacl_shapes/safety-shapes.ttl"]
    
    def set_coppola_config(self):
        wrapper_config = WrapperConfiguration()
        wrapper_config.get_configuration()
        self.thing_manager_endpoint = wrapper_config.thing_manager_endpoint
        self.coppola_endpoint = wrapper_config.thing_manager
        self.url_list = [self.coppola_endpoint + '/api/process?format=turtle',
                         self.coppola_endpoint + '/api/facility?format=turtle',
                         self.coppola_endpoint + '/api/resource?format=turtle',
                         self.coppola_endpoint + '/api/quality?format=turtle',
                         self.coppola_endpoint + '/api/safety?format=turtle']
    
    def validate(self):
        self.insert_shacl_shapes()

        payload = self.ttl
        headers = {
            'Content-Type': 'text/plain'
        }
        self.response_list = []
        for url in self.url_list:
            try:
                print("Sending ttl to validate it with process ontology")
                response = requests.request("POST", url, headers=headers, data=payload)
                print("Validation of " + url.split("/")[-1].split("?")[0] + " ontology was SUCCESSFULLY made")
                self.response_list.append(url.split("/")[-1].split("?")[0] + " : " + response.text)
            except:
                print("Error accessing to RDF validator")
                error_service = Error_service("Error accessing to RDF validator", self.thing_manager_endpoint, self.project_id, self.file_id)
                error_service.handle_error()
        print(self.response_list)

    def insert_shacl_shapes(self):
        for path in self.shacl_shapes_path:
            file = open(path, "r+")
            shacl = ' '.join(file.readlines())
            payload = shacl
            headers = {
                'Content-Type': 'text/plain'
            }
            try:
                shacl_id = path.split('/')[-1].replace("-shapes.ttl", "")
                print("Register Shacl Shape", shacl_id)
                response = requests.request("PUT", self.coppola_endpoint + "/api/" + shacl_id, headers=headers, data=payload)
                print("Shacl Shape " + shacl_id + " registered")
            except:
                print("Error registering Shacl Shape")
                error_service = Error_service("Error registering Shacl Shape", self.thing_manager_endpoint, self.project_id, self.file_id)
                error_service.handle_error()
            file.close()

    def handle_validation(self, response_list):
        for response in response_list:
            response = response.split(":")
            g = Graph()
            g.parse(data=response[1], format="turtle")
            for row in g.query("select ?o where { ?s <http://www.w3.org/ns/shacl#conforms> ?o . }"):
                if row.o == "false":
                    error_service = Error_service("Validation of " + response[0] + " ontology was UNSUCCESSFULLY made:\n" + response[1], self.thing_manager_endpoint, self.project_id, self.file_id)
                    error_service.handle_error()
        
    