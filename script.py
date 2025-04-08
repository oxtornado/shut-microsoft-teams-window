import subprocess
import mss
import pytesseract
from PIL import Image
import time
import re

def find_teams_window():
    result = subprocess.run(["wmctrl", "-l"], stdout=subprocess.PIPE, text=True)
    for line in result.stdout.splitlines():
        if "Teams" in line or "teams.microsoft.com" in line:
            print("✅ Ventana encontrada:", line)
            return line.split()[0]  # window ID
    return None

def screenshot_participant_section(output_path="participants.png"):
    with mss.mss() as sct:
        region = {
            "left": 1130,  # lado derecho
            "top": 250,                     # debajo barra superior
            "width": 100,
            "height": 50                  # suficiente para capturar "En esta reunión"
        }

        img = sct.grab(region)
        mss.tools.to_png(img.rgb, img.size, output=output_path)
    return output_path

def get_participant_count_from_screenshot(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    print("\n📝 Texto detectado por OCR:\n", text)

    # Buscar texto con formato "En esta reunión (X)"
    match = re.search(r"reu(?:nión|nion|nien|ni[eé]n)\s*\((\d+)\)", text, re.IGNORECASE)
    if match:
        count = int(match.group(1))
        print(f"👥 Participantes detectados: {count}")
        return count
    else:
        print("❌ No se encontró el texto esperado.")
    return None

def close_tab_in_window(window_id):
    # Traer al frente la ventana
    subprocess.run(["wmctrl", "-ia", window_id])
    time.sleep(0.5)  # Espera a que la ventana esté enfocada
    # Enviar Ctrl+W para cerrar pestaña
    import pyautogui
    pyautogui.hotkey('ctrl', 'w')
    print("🚪 Pestaña cerrada.")

def main():
    while True:
        window_id = find_teams_window()
        if window_id:
            print(f"🎯 Monitoreando ventana: {window_id}")

            screenshot_path = screenshot_participant_section()
            count = get_participant_count_from_screenshot(screenshot_path)

            if count is not None and count < 5:
                print(f"🔻 Solo hay {count} personas. Cerrando Teams...")
                close_tab_in_window(window_id)
                break
            elif count is not None:
                print(f"🔸 Hay {count} personas. Permaneciendo en la reunión.")
        else:
            print("🔍 No se detectó ninguna ventana de Teams.")

        time.sleep(5)

if __name__ == "__main__":
    main()
