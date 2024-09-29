import serial
import keyboard  # For simulating key presses

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
                    keyboard.press_and_release('e')  # Simulate pressing 'E' for upshift
                else:
                    print("SHIFTING DOWN")
                    keyboard.press_and_release('q')  # Simulate pressing 'Q' for downshift
            except Exception as e:
                print(f"An error occurred: {e}")
except KeyboardInterrupt:
    print("Exiting...")

# Close the serial connection when done
finally:
    ser.close()
