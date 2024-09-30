from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math
import hub
import json

motor = Motor('E')  # Adjust to the correct motor port
usb = hub.USB_VCP()  # Create the USB virtual COM port

# Main loop to send motor position over USB
while True:
    motor_position = motor.get_position()

    # Convert motor position to byte string and send it
    motor_position_str = str(motor_position) + "\n"
    usb.write(motor_position_str.encode())

    wait_for_seconds(0.15)