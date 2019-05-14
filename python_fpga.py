from nifpga import Session

# This module can read and write values to the FPGA session that is initialized by LabVIEW
# The cRIO controller must be connected and the Labview bitfile must be in the same directory as this module

# Open a reference to the running FPGA session which is already initialized in LabVIEW
session = Session(bitfile="PythonMotorTest_FPGATarget_FPGA_EBn6Kf8AHrE.lvbitx", resource="RIO://172.22.11.2/RIO0") 
torque_to_CAN = session.registers['torqueToCAN']
speed_to_CAN = session.registers['speedToCAN']
direction_to_CAN = session.registers['directionToCAN']
inverter_enable_to_CAN = session.registers['inverter_EnableToCAN']
inverter_discharge_to_CAN = session.registers['inverter_DischargeToCAN']
speed_mode_enable_to_CAN = session.registers['speed_Mode_EnableToCAN']
commanded_torque_limit_to_CAN = session.registers['commanded_Torque_LimitToCAN']
in_time_to_CAN = session.registers['in_timeToCAN']

program_enable_to_CAN = session.registers['program_enable']

command_mode_curve_to_CAN = session.registers['command_mode_curve']


# Write function arguments to FPGA for LabVIEW to read and process
def send_command(torque, speed, direction, inv_enable, inv_discharge, speed_mode, torque_limit, in_time):
    torque_to_CAN.write(torque)
    speed_to_CAN.write(speed)
    direction_to_CAN.write(direction)
    inverter_enable_to_CAN.write(inv_enable)
    inverter_discharge_to_CAN.write(inv_discharge)
    speed_mode_enable_to_CAN.write(speed_mode)
    commanded_torque_limit_to_CAN.write(torque_limit)
    in_time_to_CAN.write(in_time)
    return()

def send_enable(enabled_state):
    program_enable_to_CAN.write(enabled_state)
    return()

def send_settings(command_mode_curve):
    command_mode_curve_to_CAN.write(command_mode_curve)
    return()