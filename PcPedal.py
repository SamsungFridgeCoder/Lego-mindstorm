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

def map_left_controller_to_trigger(left_value):
    # Define the min/max left controller values
    min_left_value = 0
    max_left_value = 360

    # Normalize the left controller value to 0-1 range
    normalized_left_value = (left_value - min_left_value) / (max_left_value - min_left_value)
    
    # Ensure the normalized position is within the 0-1 range
    normalized_left_value = max(0.0, min(1.0, normalized_left_value))
    
    return normalized_left_value

try:
    while True:
        # Read a line from the serial port
        line = ser.readline().decode('utf-8').strip()
        if line:
            try:
                # Use regex to extract values between semicolons and between dollar signs
                motor_position_str = re.search(r';(\d+);', line)  # Motor position between semicolons
                left_value_str = re.search(r'\$(\d+)\$', line)    # Left controller value between dollar signs
                
                if motor_position_str:
                    motor_position = int(motor_position_str.group(1))
                    print(f"Motor position: {motor_position}")
                    
                    # Map the motor position to a right trigger value between 0.0 and 1.0
                    trigger_value = map_motor_position_to_trigger(motor_position)
                    print(f"Mapped right trigger value: {trigger_value}")
                    
                    # Set the right trigger value on the virtual gamepad
                    gamepad.right_trigger_float(trigger_value)
                
                if left_value_str:
                    left_value = int(left_value_str.group(1))
                    print(f"Left controller value: {left_value}")
                    
                    # Map the left controller value to the left trigger between 0.0 and 1.0
                    left_trigger_value = map_left_controller_to_trigger(left_value)
                    print(f"Mapped left trigger value: {left_trigger_value}")
                    
                    # Set the left trigger value on the virtual gamepad
                    gamepad.left_trigger_float(left_trigger_value)
                    
                # Update the gamepad state
                gamepad.update()
                
            except Exception as e:
                print(f"Error processing line: {line}, Error: {e}")
                continue

except KeyboardInterrupt:
    # Close the serial connection on exit
    ser.close()