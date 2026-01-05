import tkinter as tk
from tkinter import messagebox
import pyautogui
import os
from datetime import datetime

# Create screenshots folder
SAVE_DIR = "screenshots"
os.makedirs(SAVE_DIR, exist_ok=True)

def capture_screenshot():
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = os.path.join(SAVE_DIR, f"screenshot_{timestamp}.png")

        screenshot = pyautogui.screenshot()
        screenshot.save(file_path)

        messagebox.showinfo("Success", f"Screenshot saved:\n{file_path}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# UI setup
root = tk.Tk()
root.title("Screenshot Utility")
root.geometry("300x150")
root.resizable(False, False)

label = tk.Label(root, text="Desktop Screenshot Tool", font=("Arial", 12))
label.pack(pady=10)

btn = tk.Button(root, text="Capture Screenshot", command=capture_screenshot)
btn.pack(pady=20)

root.mainloop()
