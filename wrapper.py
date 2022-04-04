from time import sleep
from sseclient import SSEClient
from configparser import ConfigParser
from WrapperConfiguration import WrapperConfiguration
import sys

sys.stdout.flush()



def wrapper():
    messages = SSEClient(wrapper_config.sse_url)
    for msg in messages:
        msg_list = msg.data.split(';')
        if wrapper_config.translation_element == 'file':
            if msg_list[0] == "file": # If not file in event pass
                print("Counter: " + msg_list[3])
                #sleep(5)

            else:
                print("Not file event")
                pass

        elif wrapper_config.translation_element == 'project':
            if msg_list[0] == "project": # If not project in event pass
                print("Counter: " + msg_list[3])
                sleep(5)
            else:
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
            #pass