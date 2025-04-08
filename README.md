
# 🧠 Auto-Leave Teams Meeting Bot (Linux)

This Python bot monitors your Microsoft Teams meeting and automatically closes the **tab** (not the entire browser!) if there are fewer than 5 participants. Ideal for when the meeting is winding down and you're too polite to dip first 😅.

---

## 🌟 Features
- 🧠 Uses OCR to read the participant count (even with slight spelling errors like "reunién")
- 📸 Takes automatic screenshots of the participant section
- 🪟 Detects and brings the Teams window into focus
- 🚪 Closes only the **active tab** (not the whole browser window)
- 🔄 Checks every 15 seconds

---

## 🐧 Designed for Linux

This bot is built specifically for Linux using tools like:
- `wmctrl` – to detect & focus browser windows
- `pyautogui` – to send a `Ctrl+W` keypress
- `mss` – for fast, reliable screenshots
- `pytesseract` – for text recognition from screenshots

---

## 🛠️ Installation

### 1. Install system dependencies
```bash
sudo apt install wmctrl tesseract-ocr
```

### 2. Set up Python environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 🚀 How to Use
```bash
python3 script.py
```

### What it does:
1. Detects the Teams window (based on the title containing “Teams” or “teams.microsoft.com”)
2. Takes a screenshot of the top-right section of the screen
3. Extracts the text and tries to find “En esta reunión (X)” or slight variations
4. If participant count `< 5`, it:
   - Focuses the browser window
   - Closes just the active **tab** using `Ctrl+W`

---

## 📌 Notes
- Make sure the Teams tab is the active one in that browser window!
- Don't move your mouse or switch windows during the check—it relies on focus for the tab close.
- If OCR isn't recognizing the text well, you may need to tweak the screenshot area or lighting.

---

## 🧃 Future Ideas
- Add fuzzy string matching to improve OCR recognition
- Notification popup before closing the tab
- Tray icon to toggle bot on/off
- GUI to define the region and threshold

---

Made with caffeine and good intentions by **Oxtornado** ☕🌀  
Enjoy and auto-leave responsibly 😎
