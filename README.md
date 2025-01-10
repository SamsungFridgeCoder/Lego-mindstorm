LEGO Mindstorms Robot Inventor: Code Overview and Usage

Welcome to the LEGO Mindstorms Robot Inventor repository! This project includes three Python scripts designed to enhance your LEGO Mindstorms hub by enabling it to act as game controllers and automation tools. Here's a detailed breakdown of the scripts and their applications.

🚀 Features at a Glance

Motor Position Sender: Streams motor position data over USB.

LEGO Shifter for Racing Games: Simulates keyboard inputs for gear shifts.

PC Pedals for Racing Games: Maps motor positions to virtual gamepad triggers for throttle and brake control.

1. Motor Position Sender

📂 File: motor_position_sender.py

🎯 Purpose

This script continuously reads the motor position from the LEGO hub and sends it via USB in a structured format.

🛠️ Key Features

Streams motor data for external processing.

Configurable motor port (Motor('E')).

Sends data every 0.15 seconds.

🕹️ Application

Forms the backbone for transmitting motor data, enabling real-time data utilization.

💻 Usage

Connect the LEGO hub via USB.

Upload and run the script on the Mindstorms hub.

Monitor the data using a serial communication tool.

2. Serial Data to Keyboard Simulation

📂 File: serial_to_keyboard.py

🎯 Purpose

Reads motor position data and simulates keyboard inputs for gaming applications.

🛠️ Key Features

Interprets serial data to determine motor actions.

Simulates key presses (z for upshift and q for downshift).

Robust error handling for continuous operation.

🕹️ Application

Transforms the LEGO hub into a shifter for racing games, enabling precise gear shifting.

💻 Usage

Ensure the LEGO hub is connected and the correct serial port (e.g., COM3) is configured.

Install the required library: pip install keyboard.

Run the script to simulate gear shifting in games.

3. Virtual Gamepad Control

📂 File: virtual_gamepad_control.py

🎯 Purpose

Maps motor position data to a virtual gamepad’s triggers for use in racing games.

🛠️ Key Features

Reads and maps motor and controller values to gamepad inputs.

Converts motor data to analog trigger values (0.0 - 1.0).

Uses the vgamepad library for seamless gamepad emulation.

🕹️ Application

Turns the LEGO hub into PC pedals for racing games, where motor positions represent throttle and brake.

💻 Usage

Connect the LEGO hub via USB and configure the correct serial port.

Install the required library: pip install vgamepad.

Run the script and test the gamepad functionality in your favorite racing game.

🔧 Prerequisites

Hardware: LEGO Mindstorms Robot Inventor hub and compatible motors.

Software: Python 3.x.

Libraries:

keyboard (for serial_to_keyboard.py).

vgamepad (for virtual_gamepad_control.py).

Configured virtual COM port for serial communication.

⚙️ General Setup

Connect the LEGO hub to your computer via USB.

Adjust the motor and serial port configurations as needed.

Install necessary Python libraries using pip.

🛠️ Troubleshooting

Common Issues:

No Serial Data Received: Verify the serial port connection and settings.

Missing Libraries: Install required libraries with pip.

Gamepad Mapping Errors: Adjust the motor-to-trigger mapping functions in the script.

For additional support, refer to the LEGO Mindstorms documentation or community forums.

🌟 Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

Thank you for exploring the possibilities of LEGO Mindstorms with us. Happy building and gaming!

