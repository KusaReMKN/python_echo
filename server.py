#! /usr/bin/env python3

import socket
import sys
import threading

def serverSocket(serv):
    res = (socket.getaddrinfo(None, serv,
                              type=socket.SOCK_STREAM,
                              flags=socket.AI_PASSIVE));
    for r in res:
        try:
            sock = socket.socket(family=r[0], type=r[1], proto=r[2]);
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
            sock.bind(r[4]);
            sock.listen(5);
            return sock;
        except Exception:
            continue;
    return None;


def echoMain(sock):
    try:
        while True:
            data = sock.recv(512);
            if len(data) == 0:
                sock.close();
                return;
            sock.send(data);
    except Exception as hoge:
        sock.close();

def main():
    if len(sys.argv) < 2:
        print('usage: ./server.py port', file=sys.stderr);
        sys.exit(1);
    port = sys.argv[1];
    sock = serverSocket(port);
    if sock == None:
        print('Cannot listen', file=sys.stderr);
        sys.exit(1);
    print('Listening on', port);
    while True:
        (wsock, addr) = sock.accept();
        print('Connection from', addr);
        worker = threading.Thread(target=echoMain, args=(wsock,));
        worker.daemon = True;
        worker.start();

if __name__ == '__main__':
    main();
