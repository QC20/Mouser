import pyautogui
import random
import time

def jiggle_mouse():
    try:
        while True:
            # Generate random movement offsets
            dx = random.randint(-100, 105)
            dy = random.randint(-100, 100)

            # Jiggle the mouse
            pyautogui.moveRel(dx, dy, duration=0.1)

            # Perform a right click
            pyautogui.click(button='right')

            # Sleep for 10 seconds before the next jiggle
            time.sleep(1)
    except pyautogui.FailSafeException:
        print("Mouse jiggling stopped because the mouse was touched.")

# Start the mouse jiggling
jiggle_mouse()
