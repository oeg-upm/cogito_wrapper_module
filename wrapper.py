from time import sleep
from sseclient import SSEClient
from configparser import ConfigParser
from WrapperConfiguration import WrapperConfiguration
from service.Wrapper_Service import WrapperService
import sys
sys.stdout.flush()



def wrapper():
    messages = SSEClient(wrapper_config.sse_url)
    wrapper = WrapperService(messages)
    if wrapper_config.channel == "project":
        wrapper.project_wrapper()
    elif wrapper_config.channel == "file" or "file" in wrapper_config.channel:
        wrapper.file_wrapper()
    else:
        # Send Error to Thing Manager with error_service
        print("Not project event")
        pass


if __name__ == '__main__':
    wrapper_config = WrapperConfiguration()
    wrapper_config.get_configuration()
    while True:
        try:
            print("Wrapper Process Started")
            wrapper()
            print("Wrapper Process Ended")
        except:
            print("Restarting SSE Client")
            exit()