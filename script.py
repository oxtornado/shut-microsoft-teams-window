import subprocess
import mss
import pytesseract
from PIL import Image
import time

# Set Tesseract path if needed:
# pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

def find_teams_window():
    result = subprocess.run(["wmctrl", "-l"], stdout=subprocess.PIPE, text=True)
    for line in result.stdout.splitlines():
        if "Teams" in line or "teams.microsoft.com" in line:
            print("Found window:", line)
            return line.split()[0]  # window ID
    return None

def screenshot_entire_screen(output_path="teams.png"):
    with mss.mss() as sct:
        sct.shot(output=output_path)
    return output_path

def get_participant_count_from_screenshot(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    print("OCR text:", text)

    for word in text.split():
        if word.isdigit():
            return int(word)
    return None

def close_window(window_id):
    subprocess.run(["wmctrl", "-ic", window_id])

def main():
    while True:
        window_id = find_teams_window()
        if window_id:
            print(f"Monitoring window: {window_id}")

            screenshot_path = screenshot_entire_screen()

            count = get_participant_count_from_screenshot(screenshot_path)
            if count is not None and count < 5:
                print(f"Only {count} participants. Closing Teams window.")
                close_window(window_id)
                break
            else:
                print(f"{count} participants. Staying in meeting.")
        else:
            print("No Teams window found.")

        time.sleep(15)

if __name__ == "__main__":
    main()
