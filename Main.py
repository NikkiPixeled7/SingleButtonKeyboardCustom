import serial
import pyautogui

pyautogui.PAUSE = 0

# Arduino connection
arduino = serial.Serial("COM5", 115200, timeout=0.01)

print("Single-key keyboard is running!")

space_held = False 

try:
    while True:

        signal = arduino.readline().decode(errors="ignore").strip()

        if signal == "DOWN" and not space_held:
            pyautogui.keyDown("space")
            space_held = True

        elif signal == "UP" and space_held:
            pyautogui.keyUp("space")
            space_held = False

except KeyboardInterrupt:
    print("Keyboard stopped.")

finally:
    pyautogui.keyUp("space")
    arduino.close()
