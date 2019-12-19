from xmlrpc.server import SimpleXMLRPCServer
import os

# define server and create it
server = SimpleXMLRPCServer(('localhost', 3000), logRequests=True, allow_none=True)


# define any functions we want available
def list_directory(d):
    return os.listdir(d)


def return_none():
    return None


def qkrq(msg):
    return msg + " qkrq!"


# Register these functions with the instance
server.register_function(list_directory)
server.register_function(return_none)
server.register_function(qkrq, 'qq')


# go into serve_forever mode
if __name__ == '__main__':
    try:
        print("Serving...")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting...")
