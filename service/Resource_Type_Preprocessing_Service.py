


class Resource_Type_Pre_Service:
    def __init__(self):
        self.file_path = "./repository/resources/files/file.csv"
        self.text = None
    
    def read_file(self):
        with open(self.file_path, "r") as file:
            plaintext = file.read()
            self.text = plaintext.replace(' ', '_')
        file.close()

    def write_file(self):
        with open(self.file_path, "w") as file:
            file.write(self.text)
        file.close()