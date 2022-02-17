from pynput.mouse import Button, Controller
import time
import random 
mouse = Controller()
starttime = time.time()

while True:
    print("Click")
    mouse.position = (100, 464)
    mouse.click(Button.left, 1)
    time.sleep(random.randint(240,510))
