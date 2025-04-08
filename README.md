# Auto-Leave Teams Meeting Bot

This is a small & handy Python bot that watches your Microsoft Teams meeting, counts participants, and automatically leaves (closes the window) if there are fewer than 5 people. Perfect for when you're done but too polite to leave first. 😅

## 🌱 Features
- 🧠 Uses OCR to read participant count from a screenshot
- 📸 Takes automatic screenshots of your screen
- 🪟 Detects the Teams window with `wmctrl` (Linux only)
- 💤 Monitors every 15 seconds and acts accordingly

## 🐧 Designed for Linux
This version is tailor-made for Linux distros using tools like:
- `wmctrl` to detect & close windows
- `mss` for fast screenshots
- `pytesseract` to extract text from the image

## 🛠️ Installation

1. **Install system dependencies**:
```bash
sudo apt install wmctrl tesseract-ocr
```

2. **Set up Python env**:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. **Create `requirements.txt`**:
```txt
mss
pytesseract
Pillow
```

## 🚀 Usage
```bash
python3 script.py
```
It will:
1. Find the Microsoft Teams window
2. Take a screenshot
3. Try to detect how many participants are there
4. If fewer than 5 → close the window 💨

## 📌 Notes
- OCR isn't always perfect! You might need to adjust lighting/font sizes or crop the screen.
- You can edit `screenshot_entire_screen()` to capture only part of the screen for better accuracy.

## 🧃 Future Ideas
- Crop only top-right corner where participant count shows
- Add support for Windows or macOS
- Tray icon or notification before closing

---

Made by Oxtornado. Enjoy!

