# Screenshot Module – Desktop Utility Application

This is a lightweight desktop application built using Python that captures full-screen screenshots and saves them locally with timestamped filenames. The application is packaged as a standalone Windows executable (.exe).

---

## Project Overview

This project is developed as part of the Student Project SOW – Applied AI & System Utilities. The main goal is to build a system-level desktop utility that demonstrates GUI development, file handling, and application deployment.

---

## Features

- Desktop-based application  
- Capture full-screen screenshots  
- Automatic timestamp-based file naming  
- Saves screenshots locally in a predefined folder  
- Screenshots remain private (no cloud storage)  
- Packaged as a standalone executable (.exe)  

---

## Technology Stack

- Python  
- Tkinter for GUI  
- PyAutoGUI for screenshot capture  
- OS and Datetime modules for file handling  
- PyInstaller for packaging into an executable  

---

## Project Structure
Screenshot-Module/
│
├── screenshot_app.py # Main application code
├── requirements.txt # Dependencies
├── README.md # Project documentation
│
├── dist/
│ └── screenshot_app.exe # Standalone executable
│
└── screenshots/ # Auto-generated screenshot folder

---

## How It Works

1. The user opens the desktop application.  
2. Clicks the "Capture Screenshot" button.  
3. The application captures the full screen, generates a timestamp, and saves the screenshot in the local folder.  
4. A message confirms that the screenshot has been saved successfully.  

---

## Running the Application (EXE)

1. Go to the `dist` folder.  
2. Double-click `screenshot_app.exe`.  
3. Click the "Capture Screenshot" button.  
4. Screenshots are saved inside the `dist/screenshots/` folder.  

---

## Running from Source Code 

To run directly from Python:

```bash
pip install -r requirements.txt
python screenshot_app.py
