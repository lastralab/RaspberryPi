#Author: Niam Moltta

import socket
import sys

ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
msinfo = socket.getaddrinfo(None, 1234)
print(msinfo[3][4])

try:
    ms.bind(msinfo[3][4])
except socket.error:
    print("Failed to bind")
    sys.exit()
ms.listen(5)

while True:
    conn, addr = ms.accept()
    data = conn.recv(1024)
    if not data:
        break
    print("Got a request!")

    print (data)

conn.close()
ms.close()

    
