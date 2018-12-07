import board
import neopixel
import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

colorButton = 10

colorCounter = 0

colorList = [
    (255,108,17),
    (255,56,100),
    (45,226,230),
    (38,20,71),
    (2,55,136),
    (101,13,137),
    (146,0,117),
    (246,1,157),
    (212,0,120),
    (36,23,52),
    (46,33,87),
    (253,55,119),
    (247,6,207),
    (253,29,83),
    (249,100,14),
    (255,67,101),
    (84,13,110),
    (121,30,148),
    (84,19,136)
]

def button_callback(channel):
    global colorCounter

    # Fill the pixels with the color in the list
    pixels.fill(colorList[colorCounter]) 
    pixels.show()
    
    # Once we reach the last item in the list start back at the first
    # if not go to the next
    if colorCounter == (len(colorList)-1):
        colorCounter = 0
    else:
        colorCounter = colorCounter + 1

 # Use physical pin numbering for button
GPIO.setmode(GPIO.BOARD)

# Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

# Setup pixel strip using neopixel library
pixels = neopixel.NeoPixel(board.D18, 30, brightness=1) 

# Setup event on pin 10 rising edge
GPIO.add_event_detect(colorButton,GPIO.RISING,callback=button_callback) 

# Run until someone presses enter
message = input("Press enter to quit...\n\n") 

# Clean up
GPIO.cleanup()
