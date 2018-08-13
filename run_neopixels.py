import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)#rainbow chase
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)#press to change color
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)#color chase
GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_UP)#color changing
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_UP)#embers
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP)#strobe
GPIO.setup(12, GPIO.OUT)  #LED to GPIO
#you need to establish an output even if you are not using it

#rainbowchase
def buttons1 ():
    if GPIO.input(40)==False:
        return True
    if GPIO.input(22)==False:
        return True
    if GPIO.input(32)==False:
        return True
    if GPIO.input(36)==False:
        return True
    if GPIO.input(38)==False:
        return True   
    return False
#press to change color
def buttons2 ():
    if GPIO.input(16)==False:
        return True
    #if GPIO.input(40)==False:
        #return 
    if GPIO.input(22)==False:
        return True
    if GPIO.input(32)==False:
        return True
    if GPIO.input(36)==False:
        return True
    if GPIO.input(38)==False:
        return True   
    return False
#color chase
def buttons3 ():
    if GPIO.input(16)==False:
        return True
    if GPIO.input(40)==False:
        return True
    #if GPIO.input(22)==False:
        #return True
    if GPIO.input(32)==False:
        return True
    if GPIO.input(36)==False:
        return True
    if GPIO.input(38)==False:
        return True   
    return False
#color changing
def buttons4 ():
    if GPIO.input(16)==False:
        return True
    if GPIO.input(40)==False:
        return True
    if GPIO.input(22)==False:
        return True
    #if GPIO.input(32)==False:
        #return True
    if GPIO.input(36)==False:
        return True
    if GPIO.input(38)==False:
        return True   
    return False
#embers
def buttons5 ():
    if GPIO.input(16)==False:
        return True
    if GPIO.input(40)==False:
        return True
    if GPIO.input(22)==False:
        return True
    if GPIO.input(32)==False:
        return True
    #if GPIO.input(36)==False:
        #return True
    if GPIO.input(38)==False:
        return True   
    return False
#strobe
def buttons6 ():
    if GPIO.input(16)==False:
        return True
    if GPIO.input(40)==False:
        return True
    if GPIO.input(22)==False:
        return True
    if GPIO.input(32)==False:
        return True
    if GPIO.input(36)==False:
        return True
    #if GPIO.input(38)==False:
        #return True   
    return False
    
import subprocess
connectionp=['sudo','/home/pi/Desktop/fcserver-rpi']
subprocess.Popen(connectionp)

import webbrowser
webbrowser.open('http://localhost:7890/',new=1)

import opc, time
time.sleep(1)

numLEDs = 64
client = opc.Client('localhost:7890')
#button=0
black=(0,0,0)
off=[black]*numLEDs

loopcount=0
def rainbowchase():
    print("rainbow chase")
    while True:
        red =(255,0,0)
        orange =(255,100,0)
        yellow =(255,150,10)
        green =(0,255,0)
        lightblue =(0,255,255)
        darkblue =(0,0,255)
        purple =(255,0,255)
        pink =(255,0,70)
        white =(255,255,255)
        black =(0,0,0)

        rainbow1 = [ red,orange,yellow,green,lightblue,darkblue,purple,pink ] * numLEDs
        client.put_pixels(rainbow1)
        if buttons1():
            return
        time.sleep(0.05)
        if buttons1():
            return

        rainbow2 = [ orange,yellow,green,lightblue,darkblue,purple,pink,red ] * numLEDs
        client.put_pixels(rainbow2)
        if buttons1():
            return
        time.sleep(0.05)
        if buttons1():
            return

        rainbow3 = [ yellow,green,lightblue,darkblue,purple,pink,red,orange ] * numLEDs
        client.put_pixels(rainbow3)
        if buttons1():
            return
        time.sleep(0.05)
        if buttons1():
            return

        rainbow4 = [ green,lightblue,darkblue,purple,pink,red,orange,yellow ] * numLEDs
        client.put_pixels(rainbow4)
        if buttons1():
            return
        time.sleep(0.05)
        if buttons1():
            return

        rainbow5 = [ lightblue,darkblue,purple,pink,red,orange,yellow,green ] * numLEDs
        client.put_pixels(rainbow5)
        if buttons1():
            return
        time.sleep(0.05)
        if buttons1():
            return

        rainbow6 = [ darkblue,purple,pink,red,orange,yellow,green,lightblue] * numLEDs
        client.put_pixels(rainbow6)
        if buttons1():
            return
        time.sleep(0.05)
        if buttons1():
            return

        rainbow7 = [ purple,pink,red,orange,yellow,green,lightblue,darkblue ] * numLEDs
        client.put_pixels(rainbow7)
        if buttons1():
            return
        time.sleep(0.05)
        if buttons1():
            return

        rainbow8 = [ pink,red,orange,yellow,green,lightblue,darkblue,purple ] * numLEDs
        client.put_pixels(rainbow8)
        if buttons1():
            return
        time.sleep(0.05)
        if buttons1():
            return

        rainbow9 = [red,orange,yellow,green,lightblue,darkblue,purple,pink ] * numLEDs
        client.put_pixels(rainbow9)
        if buttons1():
            return

def singlecolorpick():
    print('singlecolorpick')
    while True:
        button=0
        while button<10:
            if buttons2():
                return
            if GPIO.input(40) == False:
                red =(255,0,0)
                orange =(255,100,0)
                yellow =(255,150,10)
                green =(0,255,0)
                lightblue =(0,255,255)
                darkblue =(0,0,255)
                purple =(255,0,255)
                pink =(255,0,70)
                white =(255,255,255)
                black =(0,0,0)
                button += 1
                
                if (button==1):
                    press1 = [ red ] * numLEDs
                    client.put_pixels(press1)
                    if buttons2():
                        return
                    time.sleep(0.5)
                    print(button)
                            
                if (button==2):
                    press2 = [ orange ] * numLEDs
                    client.put_pixels(press2)
                    if buttons2():
                        return
                    time.sleep(0.5)
                    print(button)
                if (button==3):
                    press3 = [ yellow ] * numLEDs
                    client.put_pixels(press3)
                    if buttons2():
                        return
                    time.sleep(0.5)
                    print(button)
                if (button==4):
                    press4 = [ green ] * numLEDs
                    client.put_pixels(press4)
                    if buttons2():
                        return
                    time.sleep(0.5)
                    print(button)
                if (button==5):
                    press5 = [ darkblue ] * numLEDs
                    client.put_pixels(press5)
                    if buttons2():
                        return
                    time.sleep(0.5)
                    print(button)
                if (button==6):
                    press6 = [ lightblue ] * numLEDs
                    client.put_pixels(press6)
                    if buttons2():
                        return
                    time.sleep(0.5)
                    print(button)
                if (button==7):
                    press7 = [ purple ] * numLEDs
                    client.put_pixels(press7)
                    if buttons2():
                        return
                    time.sleep(0.5)
                    print(button)
                if (button==8):
                    press8 = [ pink ] * numLEDs
                    client.put_pixels(press8)
                    if buttons2():
                        return
                    time.sleep(0.5)
                    print(button)
                if (button==9):
                    press9 = [ white ] * numLEDs
                    client.put_pixels(press9)
                    if buttons2():
                        return
                    time.sleep(0.5)
                    print(button)
        black=(0,0,0)
        allblack=[black]*numLEDs
        client.put_pixels(allblack)
        if buttons2():
            return
        time.sleep(0.5)
        
def colorchase():
    print('color chase')
    while True:
        redback = [ (255,0,0) ] * 64
        client.put_pixels(redback)
        if buttons3():
            return
        time.sleep(3)
        if buttons3():
            return
        numLEDs = 0

        while numLEDs<63:
            if buttons3():
                return
            orange = [ (255,100,0) ] * numLEDs
            client.put_pixels(orange)
            if buttons3():
                return
            time.sleep(3)
            if buttons3():
                return
            numLEDs = numLEDs + 1
            client.put_pixels(orange)
            if buttons3():
                return
            time.sleep(3)
            if buttons3():
                return
            
        orangeback = [ (255,100,0) ] * 64
        client.put_pixels(orangeback)
        if buttons3():
            return
        time.sleep(3)
        if buttons3():
            return
        numLEDs=0

        while numLEDs<63:
            yellow = [ (255,150,10) ] * numLEDs
            client.put_pixels(yellow)
            if buttons3():
                return
            time.sleep(3)
            if buttons3():
                return
            numLEDs = numLEDs + 1
            client.put_pixels(yellow)
            if buttons3():
                return
            time.sleep(3)
            if buttons3():
                return

        yellowback = [ (255,150,10) ] * 64
        client.put_pixels(yellowback)
        if buttons3():
            return
        time.sleep(3)
        if buttons3():
            return
        numLEDs=0

        while numLEDs<63:
            green = [ (0,255,0) ] * numLEDs
            client.put_pixels(green)
            if buttons3():
                return
            time.sleep(3)
            if buttons3():
                return
            numLEDs = numLEDs + 1
            client.put_pixels(green)
            if buttons3():
                return
            time.sleep(3)
            if buttons3():
                return

        greenback = [ (0,255,0) ] * 64
        client.put_pixels(greenback)
        if buttons3():
            return
        time.sleep(3)
        if buttons3():
            return
        numLEDs=0

        while numLEDs<63:
            blue = [ (0,0,255) ] * numLEDs
            client.put_pixels(blue)
            if buttons3():
                return
            time.sleep(3)
            if buttons3():
                return
            numLEDs = numLEDs + 1
            client.put_pixels(blue)
            if buttons3():
                return
            time.sleep(3)
            if buttons3():
                return

        blueback = [ (0,0,255) ] * 64
        client.put_pixels(blueback)
        if buttons3():
            return
        time.sleep(3)
        if buttons3():
            return
        numLEDs=0

        while numLEDs<63:
            purple = [ (255,0,255) ] * numLEDs
            client.put_pixels(purple)
            if buttons3():
                return
            time.sleep(3)
            if buttons3():
                return
            numLEDs = numLEDs + 1
            client.put_pixels(purple)
            if buttons3():
                return
            time.sleep(3)
            if buttons3():
                return

        purpleback = [ (255,0,255) ] * 64
        client.put_pixels(purpleback)
        if buttons3():
            return
        time.sleep(3)
        if buttons3():
            return
        numLEDs=0

        while numLEDs<63:
            red = [ (255,0,0) ] * numLEDs
            client.put_pixels(red)
            if buttons3():
                return
            time.sleep(3)
            if buttons3():
                return
            numLEDs = numLEDs + 1
            client.put_pixels(red)
            if buttons3():
                return
            time.sleep(3)
            if buttons3():
                return

        client.put_pixels(redback)
        if buttons3():
            return
        time.sleep(3)
        if buttons3():
            return
    
def colorchange():
    print('color change')
    while True:
        if buttons4():
            return
        red =(255,0,0)
        orange =(255,100,0)
        yellow =(255,150,10)
        green =(0,255,0)
        lightblue =(0,255,255)
        darkblue =(0,0,255)
        purple =(255,0,255)
        pink =(255,0,70)
        white =(255,255,255)
        black =(0,0,0)
        
        blackset = [ black ] * numLEDs
        client.put_pixels(blackset)
        if buttons4():
            return
        time.sleep(.5)
        if buttons4():
            return
        
        redset = [ red ] * numLEDs
        client.put_pixels(redset)
        if buttons4():
            return
        time.sleep(3)
        if buttons4():
            return
        
        orangeset = [ orange ] * numLEDs
        client.put_pixels(orangeset)
        if buttons4():
            return
        time.sleep(3)
        if buttons4():
            return
         
        yellowset = [ yellow ] * numLEDs
        client.put_pixels(yellowset)
        if buttons4():
            return
        time.sleep(3)
        if buttons4():
            return
        
        greenset = [ green ] * numLEDs
        client.put_pixels(greenset)
        if buttons4():
            return
        time.sleep(3)
        if buttons4():
            return
        
        blueset = [ darkblue ] * numLEDs
        client.put_pixels(blueset)
        if buttons4():
            return
        time.sleep(3)
        if buttons4():
            return
        
        purpleset = [ purple ] * numLEDs
        client.put_pixels(purpleset)
        if buttons4():
            return
        time.sleep(3)
        if buttons4():
            return
        
        pinkset = [ pink ] * numLEDs
        client.put_pixels(pinkset)
        if buttons4():
            return
        time.sleep(3)
        if buttons4():
            return
        
    
def embers():
    print('embers')
    while True:
        red=(255,0,0)
        orange =(255,100,0)
        yellow =(255,150,10)
        white =(255,255,255)
        black =(0,0,0)
        
        colorset1 = [ red,black,black,black,orange,black,black,black ] * numLEDs
        client.put_pixels(colorset1)
        if buttons5():
            return
        time.sleep(3)
        
        colorset2 = [ red,black,yellow,black,orange,black,yellow,black ] * numLEDs
        client.put_pixels(colorset2)
        if buttons5:
            return
        time.sleep(3)

        colorset3 = [ orange, yellow,black,red,black,red,black,red ] * numLEDs
        client.put_pixels(colorset3)
        if buttons5():
            return
        time.sleep(3)

        colorset4 = [ black,yellow,black,red,black,black,orange,orange ] * numLEDs
        client.put_pixels(colorset4)
        if buttons5():
            return
        time.sleep(3)
        
        colorset5 = [ yellow,black,orange,black,black,red,orange,black ] * numLEDs
        client.put_pixels(colorset5)
        if buttons5():
            return
        time.sleep(3)

def strobe():
    print('strobe')
    while True:
        white=(255,255,255)
        black=(0,0,0)
        allwhite=[white]*numLEDs
        client.put_pixels(allwhite)
        if buttons6():
            return
        time.sleep(0.05)
        if buttons6():
            return
        allblack=[black]*numLEDs
        client.put_pixels(allblack)
        if buttons6():
            return
        time.sleep(0.05)
        if buttons6():
            return

while True:
    while True: 
        while GPIO.input(16)==False:
            rainbowchase()
  
        while GPIO.input(40)==False:
            singlecolorpick()

        while GPIO.input(22)==False:
            colorchase()
   
        while GPIO.input(32)==False:
            colorchange()
            
        while GPIO.input(36)==False:
            embers()
    
        while GPIO.input(38)==False:
            strobe()

client.put_pixels(off)
time.sleep(0.5)

GPIO.cleanup()
    
