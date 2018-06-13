#!/usr/bin/env python

# Open Pixel Control client: All lights to solid white

import opc, time

numLEDs = 64
client = opc.Client('localhost:7890')

while True:
    for i in range(9):
        red = [ (0,0,0) ] * numLEDs
        #background color
        red[i] = (255, 0, 0)
        #moving color
        client.put_pixels(red)
        #execute
        time.sleep(.05)
        
    for i in range(10,19):
        orange = [ (0,0,0) ] * numLEDs
        #background color
        orange[i] = (255, 128, 0)
        #moving color
        client.put_pixels(orange)
        #execute
        time.sleep(.05)
        
    for i in range(20,29):
        yellow = [ (0,0,0) ] * numLEDs
        #background color
        yellow[i] = (200, 150, 10)
        #moving color
        client.put_pixels(yellow)
        #execute
        time.sleep(.05)

    for i in range(30,39):
        green = [ (0,0,0) ] * numLEDs
        #background color
        green[i] = (0, 255, 0)
        #moving color
        client.put_pixels(green)
        #execute
        time.sleep(.05)

    for i in range(40,49):
        blue = [ (0,0,0) ] * numLEDs
        #background color
        blue[i] = (0, 225, 255)
        #moving color
        client.put_pixels(blue)
        #execute
        time.sleep(.05)

    for i in range(50,59):
        purple = [ (0,0,0) ] * numLEDs
        #background color
        purple[i] = (225, 0, 255)
        #moving color
        client.put_pixels(purple)
        #execute
        time.sleep(.05)

    for i in range(60,numLEDs):
        pink = [ (0,0,0) ] * numLEDs
        #background color
        pink[i] = (255, 0, 128)
        #moving color
        client.put_pixels(pink)
        #execute
        time.sleep(.05)


