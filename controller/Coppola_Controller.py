import requests
from WrapperConfiguration import WrapperConfiguration

class Coppola_Controller:
    def __init__(self, ttl):
        self.coppola_endpoint = None
        self.ttl = ttl
        self.url_list = None
        self.response_list = None
        self.shacl_shapes_path = [
            "./repository/shacl_shapes/facility-shapes.ttl",
            "./repository/shacl_shapes/process-shapes.ttl",
            "./repository/shacl_shapes/quality-shapes.ttl",
            "./repository/shacl_shapes/resource-shapes.ttl",
            "./repository/shacl_shapes/safety-shapes.ttl"]
    
    def set_coppola_config(self):
        wrapper_config = WrapperConfiguration()
        wrapper_config.get_configuration()
        self.coppola_endpoint = wrapper_config.coppola_endpoint
        self.url_list = [self.coppola_endpoint + '/api/process?format=turtle',
                         self.coppola_endpoint + '/api/facility?format=turtle',
                         self.coppola_endpoint + '/api/resource?format=turtle',
                         self.coppola_endpoint + '/api/quality?format=turtle',
                         self.coppola_endpoint + '/api/safety?format=turtle']
    
    def handle_error(self):
        pass
    
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
                print("Error validating")
                self.handle_error()
                pass
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
                self.handle_error()
                pass
            file.close()
    