import tkinter as tk
import threading
import pyautogui
import time


class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jonas' Mouser App")
        
        self.start_button = tk.Button(root, text="Start", command=self.start_autogui)
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_autogui, state=tk.DISABLED)
        self.stop_button.pack(pady=10)
        
        self.running = False
        self.autogui_thread = None
    
    def start_autogui(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.running = True
        self.autogui_thread = threading.Thread(target=self.run_autogui)
        self.autogui_thread.start()
    
    def stop_autogui(self):
        self.running = False
        self.autogui_thread.join()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
    
    def run_autogui(self):
        # Delay execution to give time to position the cursor
        time.sleep(1)
        
        while self.running:
            # Get the screen size
            screen_width, screen_height = pyautogui.size()
            
            # Set the initial mouse position
            x, y = 100, 100
            
            # Define the square movement coordinates
            move_right = [(100, 100), (500, 100)]
            move_down = [(500, 100), (500, 500)]
            move_left = [(500, 500), (100, 500)]
            move_up = [(100, 500), (100, 100)]
            
            # Define the square movement sequence
            movements = [move_right, move_down, move_left, move_up]
            
            # Move the mouse cursor in a square pattern
            for movement in movements:
                pyautogui.moveTo(*movement[0], duration=3)
                time.sleep(1)
                pyautogui.moveTo(*movement[1], duration=3)
                time.sleep(1)
            
            # Perform a right-click
            pyautogui.rightClick()
            
            # Wait for 55 seconds before starting the next loop iteration
            time.sleep(55)

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()
