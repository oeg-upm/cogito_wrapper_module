


class File:

    def __init__(self):
        self.__project_id = ""
        self.__file_id = ""
        self.__file_url = ""

    def get_project_id(self):
        return self.__project_id

    def set_project_id(self, project_id):
        self.__project_id = project_id

    def get_file_id(self):
        return self.__file_id

    def set_file_id(self, file_id):
        self.__file_id = file_id

    def get_file_url(self):
        return self.__file_url
    
    def set_file_url(self, file_url):
        self.__file_url = file_url