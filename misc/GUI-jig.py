import pyautogui
import tkinter as tk
import threading
import time

class MouseJiggler:
    def __init__(self):
        self.jiggling = False

    def start_jiggling(self):
        self.jiggling = True
        threading.Thread(target=self.jiggle_mouse).start()

    def stop_jiggling(self):
        self.jiggling = False

    def jiggle_mouse(self):
        try:
            while self.jiggling:
                # Move in a square pattern
                pyautogui.moveRel(100, 0, duration=0.5)  # Move right
                pyautogui.moveRel(0, 100, duration=0.5)  # Move down
                pyautogui.moveRel(-100, 0, duration=0.5)  # Move left
                pyautogui.moveRel(0, -100, duration=0.5)  # Move up

                # Perform a left click
                pyautogui.click(button='right')

                # Pause for 10 seconds
                time.sleep(10)
        except pyautogui.FailSafeException:
            print("Mouse jiggling stopped because the mouse was touched.")

# Create the GUI window
window = tk.Tk()
window.title("Mouse Jiggler")

jiggler = MouseJiggler()

# Start Jiggling
jiggler.start_jiggling()

# Start Jiggling button
start_button = tk.Button(window, text="Start Jiggling", state="disabled")
start_button.pack()

# Stop Jiggling button
stop_button = tk.Button(window, text="Stop Jiggling", command=jiggler.stop_jiggling)
stop_button.pack()

# Start the GUI event loop
window.mainloop()
