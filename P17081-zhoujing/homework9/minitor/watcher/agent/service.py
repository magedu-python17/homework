from zerorpc import Server

class Myrpc:

    def handle(self, **kwargs):
        return 'ack {}'.format(kwargs)

server = Server(Myrpc)
server.bind('tcp://192.168.11.101:9000')
server.run()


