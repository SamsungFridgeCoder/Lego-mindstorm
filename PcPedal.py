import serial
import xgamepad

# Connect to the LEGO hub over USB/Serial
ser = serial.Serial('COM3', 115200, timeout=1)  # Adjust the port as needed

# Initialize the virtual gamepad
gamepad = xgamepad.Gamepad()

def map_motor_position_to_trigger(motor_position):
    # Map the motor position (0-100) to trigger value (0-255)
    # XGamepad expects values in the range of 0-255 for triggers
    return int((motor_position / 100.0) * 255)

try:
    while True:
        # Read a line from the serial port
        line = ser.readline().decode('utf-8').strip()
        
        if line:
            # Convert the line to an integer (assuming motor position is sent as an integer)
            motor_position = int(line)
            
            # Map the motor position to the trigger value (0-255)
            trigger_value = map_motor_position_to_trigger(motor_position)
            
            # Set the right trigger value on the virtual gamepad
            gamepad.right_trigger(trigger_value)

except KeyboardInterrupt:
    # Close the serial connection on exit
    ser.close()