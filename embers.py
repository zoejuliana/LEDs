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

numLEDs = 64
#str(numLEDs)
client = opc.Client('localhost:7890')

while True:
    colorset1 = [ red,black,black,black,orange,black,black,black ] * numLEDs
    client.put_pixels(colorset1)
    time.sleep(3)

    colorset2 = [ red,black,yellow,black,orange,black,yellow,black ] * numLEDs
    client.put_pixels(colorset2)
    time.sleep(3)

    colorset3 = [ orange, yellow,black,red,black,red,black,red ] * numLEDs
    client.put_pixels(colorset3)
    time.sleep(3)

    colorset4 = [ black,yellow,black,red,black,black,orange,orange ] * numLEDs
    client.put_pixels(colorset4)
    time.sleep(3)

    colorset5 = [ yellow,black,orange,black,black,red,orange,black ] * numLEDs
    client.put_pixels(colorset5)
    time.sleep(3)
