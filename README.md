# Auto Copy Latest File

A simple Python utility that automatically copies the **most recently modified file** from a source folder (e.g., Documents) to a target folder (e.g., a USB pen-drive).

---

## Features
- Detects the last modified file in a given folder  
- Copies it to a destination (keeping the same filename)  
- Preserves file metadata (timestamps, permissions)  

---

## Requirements
- Python 3.7+  
- Works on **Windows**, **Linux**, and **macOS**  

---

## Usage
1. Plug in your pen-drive (e.g., `E:/` on Windows or `/media/usb` on Linux).  
2. Run the script from terminal:

---

## Author
**Sander Soares**  
BSc (Hons) in Computing IT | Networking & Cloud Enthusiast  

---
```bash
python auto_copy_latest.py "C:/Users/YourName/Documents" "E:/"
