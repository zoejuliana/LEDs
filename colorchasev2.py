#!/usr/bin/env python
##red (255,0,0)
##orange (255,100,0)
##yellow (255,150,10)
##green (0,255,0)
##light blue (0,255,255)
##dark blue (0,0,255)
##purple (255,0,255)
##pink (255,0,10)
##white (255,255,255)
##black (0,0,0)

import opc, time
client = opc.Client('localhost:7890')

while True:
    redback = [ (255,0,0) ] * 64
    client.put_pixels(redback)
    time.sleep(3)
    numLEDs = 0

    while numLEDs<63:
        orange = [ (255,100,0) ] * numLEDs
        client.put_pixels(orange)
        time.sleep(3)
        numLEDs = numLEDs + 1
        client.put_pixels(orange)
        time.sleep(3)
        
    orangeback = [ (255,100,0) ] * 64
    client.put_pixels(orangeback)
    time.sleep(3)
    numLEDs=0

    while numLEDs<63:
        yellow = [ (255,150,10) ] * numLEDs
        client.put_pixels(yellow)
        time.sleep(3)
        numLEDs = numLEDs + 1
        client.put_pixels(yellow)
        time.sleep(3)

    yellowback = [ (255,150,10) ] * 64
    client.put_pixels(yellowback)
    time.sleep(3)
    numLEDs=0

    while numLEDs<63:
        green = [ (0,255,0) ] * numLEDs
        client.put_pixels(green)
        time.sleep(3)
        numLEDs = numLEDs + 1
        client.put_pixels(green)
        time.sleep(3)

    greenback = [ (0,255,0) ] * 64
    client.put_pixels(greenback)
    time.sleep(3)
    numLEDs=0

    while numLEDs<63:
        blue = [ (0,0,255) ] * numLEDs
        client.put_pixels(blue)
        time.sleep(3)
        numLEDs = numLEDs + 1
        client.put_pixels(blue)
        time.sleep(3)

    blueback = [ (0,0,255) ] * 64
    client.put_pixels(blueback)
    time.sleep(3)
    numLEDs=0

    while numLEDs<63:
        purple = [ (255,0,255) ] * numLEDs
        client.put_pixels(purple)
        time.sleep(3)
        numLEDs = numLEDs + 1
        client.put_pixels(purple)
        time.sleep(3)

    purpleback = [ (255,0,255) ] * 64
    client.put_pixels(purpleback)
    time.sleep(3)
    numLEDs=0

    while numLEDs<63:
        red = [ (255,0,0) ] * numLEDs
        client.put_pixels(red)
        time.sleep(3)
        numLEDs = numLEDs + 1
        client.put_pixels(red)
        time.sleep(3)

    client.put_pixels(redback)
    time.sleep(3)

