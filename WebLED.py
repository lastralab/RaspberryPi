#!/usr/bin/env python
#firs line= path for python

import web
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#output channels:
GPIO.setup(28, GPIO.OUT) #red
GPIO.setup(29, GPIO.OUT) #green
GPIO.setup(30, GPIO.OUT) #blue
GPIO.setup(31, GPIO.OUT) #yellow

global status

status = [0,0,0,0]
#templates are in 4templates folder
render = web.template.render('4templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

class index:
    def __init__(self):
        self.hello = "Vamos a jugar..."
    def GET(self):
        getInput = web.input(turn="")
        command = str(getInput.turn)
        #conditions:
        if command == "1":
            if status[0] == 0:
                #toggle RED
                status[0] = 1
                GPIO.output(28, GPIO.HIGH)
                print 'ROJO'
                return render.index(status)
            elif status[0] == 1:
                status[0] = 0
                GPIO.output(28, GPIO.LOW)
                return render.index(status)
            else:
                print 'error'
            return render.index(status)
        if command == "2":
            if status[1] == 0:
                #toggle GREEN
                status[1] = 1
                GPIO.output(29, GPIO.HIGH)
                print 'VERDE'
                return render.index(status)
            elif status[1] == 1:
                status[1] = 0
                GPIO.output(29, GPIO.LOW)
                return render.index(status)
            else:
                print 'error'
            return render.index(status)
        if command == "3":
            if status[2] == 0:
                #toggle BLUE
                status[2] = 1
                GPIO.output(30, GPIO.HIGH)
                print 'AZUL'
                return render.index(status)
            elif status[2] == 1:
                status[2] = 0
                GPIO.output(30, GPIO.LOW)
                return render.index(status)
            else:
                print 'error'
            return render.index(status)
        if command == "4":
            if status[3] == 0:
                #toggle YELLOW
                status[3] = 1
                GPIO.output(31, GPIO.HIGH)
                print 'AMARILLO'
                return render.index(status)
            elif status[3] == 1:
                status[3] = 0
                GPIO.output(31, GPIO.LOW)
                return render.index(status)
            else:
                print 'error'
            return render.index(status)
        #default
        else:
            #has to start by visitin /?turn=on
            return render.index(status)
if __name__ == "__main__":
    app.run()
