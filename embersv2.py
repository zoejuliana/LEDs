#!/usr/bin/env python

import opc, time

red =(255,0,0)
orange =(255,100,0)
yellow =(255,150,10)
green =(0,255,0)
lightblue =(0,255,255)
darkblue =(0,0,255)
purple =(255,0,255)
pink =(255,0,10)
white =(255,255,255)
black =(0,0,0)

numLEDs = 50
client = opc.Client('localhost:7890')

turnblack = [ black ] * numLEDs
turnred = [ red ] * numLEDs
turnorange = [ orange ] * numLEDs
turnyellow = [ yellow ] * numLEDs


def redflicker():
    client.put_pixels(turnred)
    time.sleep(.5)
    client.put_pixels(turnblack)
    time.sleep(.5)

def orangeflicker():
    client.put_pixels(turnorange)
    time.sleep(.5)
    client.put_pixels(turnblack)
    time.sleep(.5)

def yellowflicker():
    client.put_pixels(turnyellow)
    time.sleep(.5)
    client.put_pixels(turnblack)
    time.sleep(.5)

def redsolid():
    client.put_pixels(turnred)
    time.sleep(.5)

def orangesolid():
    client.put_pixels(turnorange)
    time.sleep(.5)

def yellowsolid():
    client.put_pixels(turnyellow)
    time.sleep(.5)

def blacksolid():
    client.put_pixels(turnblack)
    time.sleep(.5)

def redtoorange():
    client.put_pixels(turnred)
    time.sleep(.5)
    client.put_pixels(turnorange)
    time.sleep(.5)

def orangetoyellow():
    client.put_pixels(turnorange)
    time.sleep(.5)
    client.put_pixels(turnyellow)
    time.sleep(.5)

def yellowtoblack():
    client.put_pixels(turnyellow)
    time.sleep(.5)
    client.put_pixels(turnblack)
    time.sleep(.5)

while True:
 

    

