import serial
import pyvjoy

# Connect to the LEGO hub over USB/Serial
ser = serial.Serial('COM3', 115200, timeout=1)  # Adjust the port as needed

# Initialize the virtual joystick
j = pyvjoy.VJoyDevice(1)  # Assuming the first virtual joystick

def map_motor_position_to_trigger(motor_position):
    # Map the motor position (0-100) to trigger value (0-32767)
    return int((motor_position / 100.0) * 32767)

try:
    while True:
        # Read a line from the serial port
        line = ser.readline().decode('utf-8').strip()
        
        if line:
            # Convert the line to an integer (assuming motor position is sent as an integer)
            motor_position = int(line)
            
            # Map the motor position to trigger value
            trigger_value = map_motor_position_to_trigger(motor_position)
            
            # Set the trigger value on the virtual joystick
            j.set_axis(pyvjoy.HID_USAGE_Z, trigger_value)  # Assuming Z axis for the trigger

except KeyboardInterrupt:
    # Close the serial connection on exit
    ser.close()