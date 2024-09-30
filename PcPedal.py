import serial
import vgamepad as vg
import json

# Connect to the LEGO hub over USB/Serial
ser = serial.Serial('COM3', 115200, timeout=1)  # Adjust the port as needed

# Initialize the virtual gamepad
gamepad = vg.VX360Gamepad()

def map_motor_position_to_trigger(motor_position):
    # Define the minimum and maximum motor positions
    min_motor_position = 17
    max_motor_position = 331
    
    # Normalize the motor position to a 0-1 range
    normalized_position = (motor_position - min_motor_position) / (max_motor_position - min_motor_position)
    
    # Ensure the normalized position is within the 0-1 range
    normalized_position = max(0.0, min(1.0, normalized_position))
    
    return normalized_position

try:
    while True:
        # Read a line from the serial port
        line = ser.readline().decode('utf-8').strip()
        print(f"Raw value: {line}")
        if line:
            try:
                # Split the line to separate the integer value from the JSON object
                parts = line.split(' ', 1)
                motor_position = int(parts[0])
                
                # Map the motor position to a trigger value between 0.0 and 1.0
                trigger_value = map_motor_position_to_trigger(motor_position)
                
                # Set the right trigger value on the virtual gamepad
                gamepad.right_trigger_float(trigger_value)
                print(f"Mapped motor position {motor_position} to trigger value {trigger_value}")
                # Update the gamepad state
                gamepad.update()
            except:
                continue

except KeyboardInterrupt:
    # Close the serial connection on exit
    ser.close()