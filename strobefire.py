#!/usr/bin/env python

# Open Pixel Control client: All lights to solid white

import opc, time

numLEDs = 60
lessLEDs = 10
client = opc.Client('localhost:7890')

red = [ (225,0,0) ] * numLEDs
yellow = [ (255,130,10) ] * lessLEDs
black = [ (0,0,0) ] * numLEDs

while True:
    client.put_pixels(red)
    time.sleep(3)
    client.put_pixels(black)
    time.sleep(1)
    client.put_pixels(yellow)
    time.sleep(3)
    client.put_pixels(black)
    time.sleep(3)
