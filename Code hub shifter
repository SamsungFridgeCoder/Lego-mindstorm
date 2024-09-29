from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math
import hub
import json

motor = Motor('E')# Adjust to the correct motor port
usb = hub.USB_VCP()# Create the USB virtual COM port

# Main loop to send motor position over USB
while True:
    motor_position = motor.get_position()

    # Send specific motor position data
    if 20 <= motor_position <= 70:
        usb.write(b"-\n")# Send minus (-)
    elif 320 <= motor_position <= 350:
        usb.write(b"+\n")# Send plus (+)
    wait_for_seconds(0.15)
