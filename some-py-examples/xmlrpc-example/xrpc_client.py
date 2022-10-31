from xmlrpc.client import ServerProxy

proxy = ServerProxy('http://localhost:3000')

if __name__ == '__main__':
    print(proxy.list_directory("/home/eugene/"))
    print(proxy.return_none())
    print(getattr(proxy, 'qq')("message"))