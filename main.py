import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 30, brightness=1)

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

for color in colorList:
    pixels.fill(color) 
    pixels.show()
    time.sleep(2)
