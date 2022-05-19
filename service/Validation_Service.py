from rdflib import Graph
from pyshacl.validate import Validator

class Validation_Service:
    def __init__(self, data_graph, mapping_path):
        self.__shacl_graph = None
        self.__data_graph = Graph().parse(data_graph, format='turtle')
        self.__shapes_path = mapping_path.replace("mappings/mappings.ftl", "shapes/shapes.ttl")
        self.validation_result = None
        self.validation_report = None

    def __set_shacl_graph(self):
        with open(self.__shapes_path, 'r') as f:
            self.__shacl_graph = Graph().parse(f.read(), format='turtle')
        f.close()

    def validation(self):
        self.__set_shacl_graph()
        self.__set_data_graph()
        validation = Validator(self.__data_graph,self.__shacl_graph,options={"inference": "rdfs"},abort_on_error = False, meta_shacl = False, debug = False, advanced = True)
        self.validation_result, report_graph, self.validation_report = validation.run()