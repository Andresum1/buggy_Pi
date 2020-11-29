from gpiozero import Robot
from time import sleep

#robin = Robot(left=(9,10), right=(7,8))
robin = Robot(left=(9,10), right=(8,7))
robin.forward()
sleep(1)

robin.right(0.8)
sleep(1)

robin.backward(0.9)
sleep(1)

robin.left(0.7)
sleep(1)

robin.stop()
