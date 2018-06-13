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


import subprocess
connectiono=['sudo','/home/pi/Desktop/processing-3.3.5/processing']
subprocess.Popen(connectiono)
#this executes the processing file as superuser

import subprocess
connectionp=['sudo','/home/pi/Desktop/fcserver-rpi']
subprocess.Popen(connectionp)
#this executes the fadecandy raspberry pi server as superuser

import webbrowser
webbrowser.open('http://localhost:7890/',new=1)
#imports the program called webbrowser (module import from github
##new=0 means open in existing window; new=1 means open in new window ;new=2 means open in new tab

import opc, time

numLEDs = 67
client = opc.Client('localhost:7890')

orange = [ (255,100,0) ] * numLEDs
client.put_pixels(orange)
time.sleep(1)
#this code turns all my leds orange which I added for testing purposes.
