

class Project:

    def __init__(self):
        self.__project_id = ""
        self.__project_name = ""
        self.__project_description = ""



    def get_project_id(self):
        return self.__project_id

    def set_project_id(self, project_id):
        self.__project_id = project_id

    def get_project_name(self):
        return self.__project_name

    def set_project_name(self, project_name):
        self.__project_name = project_name

    def get_project_description(self):
        return self.__project_description

    def set_project_description(self, project_description):
        self.__project_description = project_description
    
    def to_json(self):
        return {
            "project_id": self.get_project_id(),
            "project_name": self.get_project_name(),
            "project_description": self.get_project_description()
        }
