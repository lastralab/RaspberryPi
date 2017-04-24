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

![ps](https://cloud.githubusercontent.com/assets/22894897/25349763/4ed426ba-28f9-11e7-907f-ca81ef5404fb.jpeg)

Demo:

![ledpush](https://cloud.githubusercontent.com/assets/22894897/24684928/4078caa4-1980-11e7-88bc-0ea03ba793ac.gif)

# Write a simple web server
Print "Got a request" on Raspberry Pi screen when the server has received a request.

```python
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
```
You access the socket through a terminal window and send messages to the server.

![rpi](https://cloud.githubusercontent.com/assets/22894897/25349520/877bdd2e-28f8-11e7-9afb-ed8e3ee77dc6.png)

# Tweeting from Raspberry Pi

You need:

-A twitter account

-Go to www.apps.twitter.com

-Create your app

-Create your python program and run it from your raspberry pi

```python
from twython import Twython, TwythonError

#be sure to keep these keys safe or else, everybody could manage your twitter account

C_KEY = "your own API KEY"
C_SECRET= "your API SECRET"
A_TOKEN = "your ACCESS TOKEN"
A_SECRET = "your ACCESS TOKEN SECRET"

pipitan = Twython(C_KEY, C_SECRET, A_TOKEN, A_SECRET)
message= 'This is my Raspberry Pi tweeting. #myFirstTweet'
try:
    pipitan.update_status(status= message)
except TwythonError as e:
    print e

print(status +" ------tweeted")
```

Tweeting from Raspberry Pi:

![2017-04-24-200516_1280x720_scrot](https://cloud.githubusercontent.com/assets/22894897/25362493/872b42f6-292a-11e7-83b7-35ffa2cc3eb1.png)

#myFirstTweet:

<img width="1196" alt="screenshot 2017-04-24 20 07 03" src="https://cloud.githubusercontent.com/assets/22894897/25362499/8e263930-292a-11e7-912c-cd171d003f5e.png">

Please, do not follow me.
