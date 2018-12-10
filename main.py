# Import the WS2801 module.
import time
import RPi.GPIO as GPIO
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

PIXEL_COUNT = 30
colorCounter = 0
colorList = [
    [255,108,17], # FF6C11 Cool orange
    [255,56,100], # FF3864 Magenta
    [45,226,230], # 2DDFE6 Cool Cyan
    [38,20,71], # 261447 Dark Purple
    [2,55,136], # 023788 Dark Blue
    [101,13,137], # 650D89 Cool Purple
    [146,0,117], # 920075 Dark Magenta
    [246,1,157], # F6019D Strong pink
    [212,0,120], # D40078 Dark pink
    [36,23,52], # 241734 Very dark purple
    [46,33,87], # 2E2157 Very Dark Blue
    [253,55,119], # FD3777 Red pink
    [247,6,207], # F706CF Purple Pink
    [253,29,83], # FD1D53 Red orange
    [249,100,14], # F9640E Dark orange peel
    [255,67,101], # FF4365 Coral Pink
    [84,13,110], # 540D6E Deep purple
    [121,30,148], # 791E94 Purple
    [84,19,136], # 541388 Strong purple
    [47,249,35], # 2FF923 Lightsaber green
    [229,48,28], # E5301C Lightsaber red
    [99,235,230], # 63EBE6 Lightsaber cyan
    [32,35,254] # 2023FE Lightsaber blue

]

def button_callback(channel):
    global colorCounter

    # Fill the pixels with the color in the list
    for i in range(0,PIXEL_COUNT):
        color = colorList[i]
        pixels.set_pixel_rgb(i, color[0], color[1], color[2])

    pixels.show()
    
    # Once we reach the last item in the list start back at the first
    # if not go to the next
    if colorCounter == (len(colorList)-1):
        colorCounter = 0
    else:
        colorCounter = colorCounter + 1



#   ______              __                         
#  /      \            |  \                        
# |  $$$$$$\  ______  _| $$_    __    __   ______  
# | $$___\$$ /      \|   $$ \  |  \  |  \ /      \ 
#  \$$    \ |  $$$$$$\\$$$$$$  | $$  | $$|  $$$$$$\
#  _\$$$$$$\| $$    $$ | $$ __ | $$  | $$| $$  | $$
# |  \__| $$| $$$$$$$$ | $$|  \| $$__/ $$| $$__/ $$
#  \$$    $$ \$$     \  \$$  $$ \$$    $$| $$    $$
#   \$$$$$$   \$$$$$$$   \$$$$   \$$$$$$ | $$$$$$$ 
#                                        | $$      
#                                        | $$      
#                                         \$$      

# Use physical pin numbering for button
GPIO.setmode(GPIO.BOARD)

# Set button selector pin to be an input pin and set initial value to be pulled low (off)
COLOR_BUTTON = 18
GPIO.setup(COLOR_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

# Specify a software SPI connection for Raspberry Pi on the following pins:
PIXEL_CLOCK = 14
PIXEL_DOUT  = 15
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, clk=PIXEL_CLOCK, do=PIXEL_DOUT)
pixels.clear()
pixels.show()

# Setup event on pin 10 rising edge
GPIO.add_event_detect(COLOR_BUTTON, GPIO.RISING, callback=button_callback) 

# Run until someone presses enter
message = input("Press enter to quit...\n\n") 

# Clean up
GPIO.cleanup()
