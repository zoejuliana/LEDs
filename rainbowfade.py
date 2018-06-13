#!/usr/bin/env python

# Open Pixel Control client: All lights to solid white

import opc, time

numLEDs = 64
client = opc.Client('localhost:7890')

while True:
        #red
        red = [ (225,0,0) ] * numLEDs
        client.put_pixels(red)
        time.sleep(5)
        #orange
        orange = [ (255,30,0) ] * numLEDs
        client.put_pixels(orange)
        time.sleep(5)
        #yellow
        yellow = [ (255,100,0) ] * numLEDs
        client.put_pixels(yellow)
        time.sleep(5)
        #green
        green = [ (0,255,0) ] * numLEDs
        client.put_pixels(green)
        time.sleep(5)
        #blue
        blue = [ (0,0,255) ] * numLEDs
        client.put_pixels(blue)
        time.sleep(5)
        #purple
        purple = [ (255,0,255) ] * numLEDs
        client.put_pixels(purple)
        time.sleep(5)
        #pink
        pink = [ (255,0,10) ] * numLEDs
        client.put_pixels(pink)
        time.sleep(5)
        #rainbow??
