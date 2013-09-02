import logging
import random
import SocketServer


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


class SocketTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        logging.debug("client connected: " + str(self.request.getpeername()))
        while True:
            cmd = self.request.recv(1024)
            logging.debug("data received: " + cmd)
            if cmd == 'voltage':
                self.request.send("%d" % random.randint(0, 300))
            elif cmd == 'current':
                self.request.send("%d" % random.randint(0, 50))
            elif cmd == 'frequency':
                self.request.send("%d" % random.randint(50, 60))
            elif cmd == 'switch_on':
                self.request.send("on")
            elif cmd == 'switch_off':
                self.request.send("off")
            elif cmd == 'frequency':
                self.request.send("%d" % random.randint(50, 60))
            elif cmd == 'quit':
                logging.debug("client disconnected: " + str(self.request.getpeername()))
                break
            else:
                self.request.send(cmd)



class SocketTCPServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
    allow_reuse_address = True


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 8200
    server = SocketTCPServer((HOST, PORT), SocketTCPHandler)
    server.serve_forever()
