import pyautogui
import time
import random

def jiggle_mouse():
    try:
        while True:
            # Move the mouse right
            pyautogui.moveRel(100, 0, duration=0.1)

            # Move the mouse down
            pyautogui.moveRel(0, 100, duration=0.1)

            # Move the mouse left
            pyautogui.moveRel(-101, 0, duration=0.1)

            # Move the mouse up
            pyautogui.moveRel(0, -100, duration=0.5)

            # Generate random movement offsets
            #dx = random.randint(-10, 10)
            #dy = random.randint(-10, 10)

            # Jiggle the mouse
            #pyautogui.moveRel(dx, dy, duration=10)

            # Perform a right click
            pyautogui.click(button='right')

            # Sleep for 10 seconds before the next jiggle
            time.sleep(5)
    except pyautogui.FailSafeException:
        print("Mouse jiggling stopped because the mouse was touched.")

# Start the mouse jiggling
jiggle_mouse()
