#!/usr/bin/env python

# Open Pixel Control client: All lights to solid white

import opc, time

client = opc.Client('localhost:7890')
numLEDs = 64
#establish colors
red=(255,0,0)
orange=(255,30,0)
yellow=(255,100,0)
green=(0,255,0)
blue=(0,0,255)
purple=(255,0,255)
pink=(255,0,10)

#run in loop
while True: 
    red_blue = ( red, blue )*numLEDs
    client.put_pixels(red_blue)
    time.sleep(3)
