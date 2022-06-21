from cgitb import handler
from time import sleep
from sseclient import SSEClient
from configparser import ConfigParser
from WrapperConfiguration import WrapperConfiguration
from controller.Wrapper_Controller import WrapperController
from service.Error_service import Errors
from signal import signal, SIGINT
import sys
sys.stdout.flush()



def wrapper():
    messages = SSEClient(wrapper_config.sse_url)
    wrapper = WrapperController(messages)
    if wrapper_config.channel == "project":
        wrapper.project_wrapper()
    elif wrapper_config.channel == "file" or "file" in wrapper_config.channel:
        wrapper.file_wrapper(wrapper_config.translation_type, wrapper_config.translation_preprocess)
    else:
        # Send Error to Thing Manager with error_service
        print("Not project event")
        pass

def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

if __name__ == '__main__':
    wrapper_config = WrapperConfiguration()
    wrapper_config.get_configuration()
    while True:
        try:
            print("Wrapper Process Started")
            wrapper()
            print("Wrapper Process Ended")
        except:
            exit(0)
            signal(SIGINT, handler)
            print("Restarting SSE Client")
            pass

            
            