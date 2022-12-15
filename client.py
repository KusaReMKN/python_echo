#! /usr/bin/env python3

import socket
import sys

def clientSocket(host, serv):
    res = socket.getaddrinfo(host, serv, type=socket.SOCK_STREAM);
    for r in res:
        try:
            sock = socket.socket(family=r[0], type=r[1], proto=r[2]);
            sock.connect(r[4]);
            return sock;
        except Exception:
            continue;
    return None;

def main():
    if len(sys.argv) < 4:
        print('usage: ./client.py host port message [...]', file=sys.stderr);
        sys.exit(1);
    host = sys.argv[1];
    port = sys.argv[2];
    sock = clientSocket(host, port);
    if sock == None:
        print('Cannot connect', file=sys.stderr);
        sys.exit(1);
    msg = '';
    for i in range(len(sys.argv) - 3):
        if len(msg) != 0:
            msg += ' ';
        msg += sys.argv[3+i];
    sock.send(msg.encode('utf-8'));
    sock.shutdown(socket.SHUT_WR)
    msg = b'';
    data = sock.recv(512);
    while len(data) != 0:
        msg += data;
        data = sock.recv(512);
    print('From server:', msg.decode('utf-8'));
    sock.close();

if __name__ == '__main__':
    main();
