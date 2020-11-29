from gpiozero import Robot
from tkinter import *
import board
import neopixel
from time import sleep
pixel_pin = board.D18
# The number of NeoPixels
num_pixels = 1


ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)

## Robot Config
bot = Robot(left=(9,10), right=(7,8))
main =Tk()
def leftKey(event):
    bot.left(0.4)
    sleep(0.04)
    bot.stop()
    print("left")
def rightKey(event):
    bot.right(0.4)
    sleep(0.04)
    bot.stop()
    print("righ")
def upKey(event):
    bot.forward(0.7)
    sleep(0.05)
    bot.stop()
    print("Forward")
def downKey(event):
    bot.backward(0.7)
    sleep(0.05)
    bot.stop()
    print("backward")
def ctrlKey(event):
    bot.stop()
    print("stop")
def lshiftkey(event):
    pixels.fill((255, 255, 255))
    pixels.show()
    print("ligh") 
def tabkey(event):
    pixels.fill((0, 0, 0))
    pixels.show()
    print("ligh_off")    
def escKey(event):
    import sys; sys.exit()
frame = Frame(main,width=100,height=100)
frame.bind('<Left>',leftKey)
frame.bind('<Right>',rightKey)
frame.bind('<Up>',upKey)
frame.bind('<Down>',downKey)
frame.bind('<Control_L>',ctrlKey)
frame.bind('<Shift_L>',lshiftkey)
frame.bind('<Tab>',tabkey)
frame.bind('<Escape>',escKey)
frame.focus_set()
frame.pack()
main.mainloop()

