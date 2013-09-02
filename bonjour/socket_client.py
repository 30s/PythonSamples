import time

from socket import *


HOST = '127.0.0.1'
PORT = 8200


def main():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.send('voltage')
    print sock.recv(1024)
    sock.send('current')
    print sock.recv(1024)
    sock.send('frequency')
    print sock.recv(1024)
    sock.send('switch_on')
    print sock.recv(1024)
    sock.send('switch_off')
    print sock.recv(1024)
    sock.send('quit')
    print sock.recv(1024)
    sock.close()


if __name__ == '__main__':
    main()

