import logging
import random
import SocketServer


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


class SocketTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        logging.debug("client connected: " + str(self.request.getpeername()))
        while True:
            cmd = self.request.recv(1024).strip()
            logging.debug("data received: " + cmd)
            if cmd == 'voltage':
                resp = "voltage %d\n" % random.randint(0, 300)
            elif cmd == 'current':
                resp = "current %d\n" % random.randint(0, 50)
            elif cmd == 'frequency':
                resp = "frequency %d\n" % random.randint(50, 60)
            elif cmd == 'switch_on':
                resp = "on\n"
            elif cmd == 'switch_off':
                resp = "off\n"
            elif cmd == 'quit' or len(cmd) == 0:
                logging.debug("client disconnected: " + str(self.request.getpeername()))
                break
            else:
                resp = cmd
            self.request.send(resp)
            logging.debug("data sent: " + resp)



class SocketTCPServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
    allow_reuse_address = True


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 8200
    server = SocketTCPServer((HOST, PORT), SocketTCPHandler)
    server.serve_forever()
