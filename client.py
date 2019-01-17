#!/usr/bin/env python3
import socket

HOST = "www.google.com"
PORT = 80
BUFFER_SIZE = 1024

#payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"
payload = """GET / HTTP/1.0
Host: {HOST}

""".format(HOST=HOST)

def connect_socket(addr):
    (family, socketype, proto, cannoname, sockaddr) = addr
    try:
        s = socket.socket(family,socketype, proto)
        s.connect(sockaddr)
        print("CONNECTED")
        s.sendall(payload.encode())
        full_data = b""
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            full_data += data
        print(full_data)
    except:
        print("DID NOT CONNECTED")

def main():
    addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)
    # linux: [0] is ipv4
    # mac: [1] is ipv4
    addr = addr_info[0]
    connect_socket(addr)


'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n')
    data = s.recv(BUFFER_SIZE)
print('Received', repr(data))
'''

if __name__ == "__main__":
    main()
