# ![raspberry-logo](https://cloud.githubusercontent.com/assets/22894897/24567005/2d7de462-1632-11e7-978e-0afaa0e707ae.png)

# Blink + Pushbutton example

First step:

![blink](https://cloud.githubusercontent.com/assets/22894897/24591015/3ce471b2-17ce-11e7-8086-0284d7a9dcc4.gif)

Wiring:

<img width="1047" alt="screenshot 2017-04-04 21 32 03" src="https://cloud.githubusercontent.com/assets/22894897/24684682/2db7b152-197e-11e7-8574-b607c2d0940f.png">

Pin Reference:

![header_pinout-2](https://cloud.githubusercontent.com/assets/22894897/24590712/70a0ade6-17c8-11e7-8bee-d1370a0c90c5.jpg)

Using VNC Viewer to control the program from your phone:

![whatsapp image 2017-04-02 at 17 41 49](https://cloud.githubusercontent.com/assets/22894897/24590902/09942084-17cc-11e7-8dc2-abdb8249af2c.jpeg)

Download VNC Viewer from here: https://www.realvnc.com/download/viewer/ and get creative!

Python Code:

![](http://i.imgur.com/ZXtBfKC.jpg)

Demo:

![ledpush](https://cloud.githubusercontent.com/assets/22894897/24684928/4078caa4-1980-11e7-88bc-0ea03ba793ac.gif)

# Write a simple web server

'''python
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
'''python
    
