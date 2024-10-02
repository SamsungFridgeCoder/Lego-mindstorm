import serial
import vgamepad as vg
import re

# Connect to the LEGO hub over USB/Serial
ser = serial.Serial('COM3', 115200, timeout=1)  # Adjust the port as needed

# Initialize the virtual gamepad
gamepad = vg.VX360Gamepad()

def map_motor_position_to_trigger(motor_position):
    # Define the minimum and maximum motor positions
    min_motor_position = 0
    max_motor_position = 360
    
    # Normalize the motor position to a 0-1 range
    normalized_position = (motor_position - min_motor_position) / (max_motor_position - min_motor_position)
    
    # Ensure the normalized position is within the 0-1 range
    normalized_position = max(0.0, min(1.0, normalized_position))
    
    return normalized_position

try:
    while True:
        # Read a line from the serial port
        line = ser.readline().decode('utf-8').strip()
        if line:
            try:
                # Use regex to extract values between semicolons
                motor_position_str = re.search(r';(\d+);', line)
                
                if motor_position_str:
                    motor_position = int(motor_position_str.group(1))
                    print(f"Motor position: {motor_position}")
                    
                    # Map the motor position to a trigger value between 0.0 and 1.0
                    trigger_value = map_motor_position_to_trigger(motor_position)
                    print(f"Mapped trigger value: {trigger_value}")
                    
                    # Set the right trigger value on the virtual gamepad
                    gamepad.right_trigger_float(trigger_value)
                    
                    # Update the gamepad state
                    gamepad.update()
                else:
                    print(f"No motor position found in line: {line}")
            except Exception as e:
                print(f"Error processing line: {line}, Error: {e}")
                continue

except KeyboardInterrupt:
    # Close the serial connection on exit
    ser.close()