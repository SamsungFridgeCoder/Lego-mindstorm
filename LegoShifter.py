from mindstorms import MSHub, Motor
from mindstorms.control import wait_for_seconds
import hub

motor = Motor('E')  # Adjust to the correct motor port
usb = hub.USB_VCP()  # Create the USB virtual COM port

# Main loop to continuously send motor position over USB
while True:
    motor_position = motor.get_position()

    # Convert motor position to a byte string and send it over USB
    motor_position_str = f"{motor_position}\n"
    usb.write(motor_position_str.encode())

    # Wait for 0.15 seconds before sending the next position
    wait_for_seconds(0.15)