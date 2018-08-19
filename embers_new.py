import subprocess
connectionp=['sudo','/home/pi/Desktop/fcserver-rpi']
subprocess.Popen(connectionp)

import webbrowser
webbrowser.open('http://localhost:7890/',new=1)

import opc, time
time.sleep(1)

numLEDs = 64
client = opc.Client('localhost:7890')

from random import shuffle

red=(255,0,0)
darkred=(250,0,0)
orange =(255,100,0)
darkorange=(100,35,0)
yellow =(255,150,10)
darkyellow=(80,50,10)
black =(0,0,0)

embersetmodel=[ red,yellow,orange,darkred,darkyellow,darkorange,black,black,black,black,black ]*numLEDs
#this is the base line up for the led colors
embersetnew=embersetmodel[:]
#this simply copies the base and sets it under a new name

while True:
    shuffle(embersetnew)
    #this shuffles the colors
    client.put_pixels(embersetnew)
    #typical turning on of the leds
    time.sleep(4)
