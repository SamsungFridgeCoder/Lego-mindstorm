import serial
import keyboard
import json

# Connect to the LEGO hub over USB/Serial
ser = serial.Serial('COM3', 115200, timeout=1)  # Adjust the port as needed

# Main loop to read data from LEGO hub and simulate key presses
while True:
    if ser.in_waiting > 0:
        try:
            data = ser.readline().decode().strip()  # Read data from LEGO hub
            print(f"Received raw data: {data}")  # Print received data for debugging
        except Exception as e:
            print(f"An error occurred: {e}")
