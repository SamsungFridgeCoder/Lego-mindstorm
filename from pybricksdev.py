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
            
            # Attempt to decode JSON data
            if data.startswith('{') and data.endswith('}'):  # Check if it's a JSON object
                json_data = json.loads(data)
                print(f"Decoded JSON: {json_data}")  # Print decoded JSON
                
                # Extract motor position or other relevant data from JSON
                # Assuming json_data contains a key that represents motor position
                # Adjust the key based on the actual structure of the JSON data
                if 'motor_position' in json_data:
                    motor_position = json_data['motor_position']

                    # Define thresholds for key presses
                    if 20 <= motor_position <= 70:
                        keyboard.press_and_release('-')  # Simulate '-' key press
                        print("Pressed -")
                    elif 320 <= motor_position <= 350:
                        keyboard.press_and_release('shift+=')  # Simulate '+' key press
                        print("Pressed +")
            else:
                print("Received non-JSON data")

        except json.JSONDecodeError:
            print("Failed to decode JSON")
        except Exception as e:
            print(f"An error occurred: {e}")
