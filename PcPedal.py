import serial
import vgamepad as vg

# Connect to the LEGO hub over USB/Serial
ser = serial.Serial('COM3', 115200, timeout=1)  # Adjust the port as needed

# Initialize the virtual gamepad
gamepad = vg.VX360Gamepad()

def map_motor_position_to_trigger(motor_position):
    # Map the motor position (0-100) to a trigger value (0.0 - 1.0)
    return motor_position / 100.0

try:
    while True:
        # Read a line from the serial port
        line = ser.readline().decode('utf-8').strip()
        
        if line:
            try:
                # Convert the line to an integer (assuming motor position is sent as an integer)
                motor_position = int(line)
                
                # Map the motor position to a trigger value between 0.0 and 1.0
                trigger_value = map_motor_position_to_trigger(motor_position)
                
                # Set the right trigger value on the virtual gamepad
                gamepad.right_trigger_float(trigger_value)
                print(f"Mapped motor position {motor_position} to trigger value {trigger_value}")
                # Update the gamepad state
                gamepad.update()
            except:
                pass

except KeyboardInterrupt:
    # Close the serial connection on exit
    ser.close()