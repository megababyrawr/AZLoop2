

def send_command(torque, speed, direction, inv_enable, inv_discharge, speed_mode, torque_limit, in_time):

    with open('fpga.txt', 'a') as pretend_fpga:
        pretend_fpga.write("Torque: " + str(torque)
                           + "\nSpeed: " + str(speed)
                           + "\nDirection: " + str(direction)
                           + "\ninv_enable: " + str(inv_enable)
                           + "\ninv_discharge: " + str(inv_discharge)
                           + "\nSpeed Mode: " + str(speed_mode)
                           + "\nTorque Limit: " + str(torque_limit)
                           + "\nIn Time: " + str(in_time)
                           )

    return()

def send_enable(enabled_state):

    with open('fpga.txt', 'a') as pretend_fpga:
        pretend_fpga.write('Send Enable\n')

    return()

def send_settings(command_mode_curve):

    with open('fpga.txt', 'a') as pretend_fpga:
        pretend_fpga.write('Send Settings\n')

    return()

    return()