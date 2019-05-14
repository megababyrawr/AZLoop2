import python_fpga

# Example of how to send commands to the python_fpga module

# Set these variables to the values commanded from the GUI. Example values shown below.
enabled_state = 0 # Bool as 1 or 0

command_mode_curve = 0 # 0 = instant, 1 = linear

torque = 300 # Int (-32768 to 32767)
speed = 300 # Int (-32768 to 32767)
direction = 1 # Bool as 1 or 0 (1 = fwd, 0 = rev)
inv_enable = 1 # Bool as 1 or 0 (1 = enable)
inv_discharge = 1 # Bool as 1 or 0
speed_mode = 1 # Bool as 1 or 0
torque_limit = 300 # Int (-32768 to 32767)
in_time = 10 # Int (-32768 to 32767)

# Send all values to function_fpga module to be written to the FPGA for LabVIEW to read and process
python_fpga.send_enable(enabled_state)

python_fpga.send_settings(command_mode_curve)

python_fpga.send_command(torque, speed, direction, inv_enable, inv_discharge, speed_mode, torque_limit, in_time)