import serial
import keyboard  # Not used in the script but you may need it for keypress simulations
import json

# Connect to the LEGO hub over USB/Serial
ser = serial.Serial('COM3', 115200, timeout=1)  # Adjust the port as needed

# Main loop to read data from LEGO hub and simulate key presses
try:
    while True:
        if ser.in_waiting > 0:
            try:
                data = ser.readline().decode().strip()  # Read data from LEGO hub
                if '+' in data:
                    print("SHIFTING UP")
                    # You can simulate key presses using the keyboard module here if needed
                    # keyboard.press_and_release('shift+up')  # Example for keypress simulation
                else:
                    print("SHIFTING DOWN")
                    # Simulate a different key press if needed
                    # keyboard.press_and_release('shift+down')
            except Exception as e:
                print(f"An error occurred: {e}")
except KeyboardInterrupt:
    print("Exiting...")

# Close the serial connection when done
finally:
    ser.close()
