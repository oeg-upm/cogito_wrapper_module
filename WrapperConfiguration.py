from configparser import ConfigParser


class WrapperConfiguration:
    def __init__(self):
        self.__class__.helio = None
        self.__class__.translation_element = None
        self.__class__.translation_preprocess = None # Boolean
        self.__class__.translation_type = None
        self.__class__.thing_manager = None
        self.__class__.sse_url = None

    def get_configuration(self):
        config = ConfigParser()
        if config.read('./config.ini'):

            if not config.has_section('helio'):
                print("Missing 'helio' mandatory section in 'config.ini'.")
                exit()
            else:
                if not config.has_option('helio', 'host'):
                    print("Missing 'host' option in 'helio' section in 'config.ini'.")
                    exit()
            if not config.has_section('translation'):
                print("Missing 'translation' mandatory section in 'config.ini'.")
                exit()
            else:
                if not config.has_option('translation', 'element'):
                    print("Missing 'element' option in 'translation' section in 'config.ini'.")
                if not config.has_option('translation', 'preprocess'):
                    print("Missing 'preprocess' option in 'translation' section in 'config.ini'.")
                if not config.has_option('translation', 'type'):
                    print("Missing 'type' option in 'translation' section in 'config.ini'.")
            if not config.has_section('thing_manager'):
                print("Missing 'thing_manager' mandatory section in 'config.ini'.")
                exit()
            else:
                if not config.has_option('thing_manager', 'host'):
                    print("Missing 'host' option in 'thing_manager' section in 'config.ini'.")
                    exit()
                if not config.has_option('thing_manager', 'sse'):
                    print("Missing 'sse' option in 'thing_manager' section in 'config.ini'.")
                    exit()

            self.helio = config.get('helio', 'host')
            self.translation_element = config.get('translation', 'element')
            self.translation_preprocess = config.getboolean('translation', 'preprocess')
            self.translation_type = config.get('translation', 'type')
            self.thing_manager = config.get('thing_manager', 'host')
            self.sse_url = config.get('thing_manager', 'sse')