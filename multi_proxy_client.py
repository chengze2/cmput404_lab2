#!/usr/bin/env python3
import socket
from multiprocessing import Pool


HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

payload = """GET / HTTP/1.0
Host: www.google.com

"""


def connect_socket(addr):
    (family, socketype, proto, cannoname, sockaddr) = addr
    try:
        s = socket.socket(family,socketype, proto)
        s.connect(sockaddr)
        s.sendall(payload.encode())

        s.shutdown(socket.SHUT_WR)

        full_data = b""
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
               break
            full_data += data
        print(full_data)

    except:
        print("DID NOT CONNECT")
        pass
    finally:
        s.close()


def main():
    addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)
    #ipv6 for [1]
    #print(addr_info)
    # linux: [0] is ipv4
    # mac: [1] is ipv4
    addr = addr_info[1]
    #connect_socket(addr)
    with Pool() as p:
        p.map(connect_socket, [addr for _ in range(1,50)])

if __name__ == "__main__":
    main()
