import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainUI05 import Ui_MainWindow
import test_python_fpga
import logging
class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)
        self.setupUi(self)

        self.pushButtonOn.clicked.connect(self.on)

        self.pushButtonOff.clicked.connect(self.off)

        self.pushButtonPrepDataValues.clicked.connect(self.prepdatavalues)

        self.pushButtonSendCommand.clicked.connect(self.pushbuttonsendcommand)

        self.pushButtonHaltCommand.clicked.connect(self.pushbuttonhaltcommand)

        self.pushButtonLogName.clicked.connect(self.pushbuttonlogname)


    a_targetTorque = 0 #int
    a_targetSpeed = 0 #int
    a_direction = 0 #boolean 1 is forward, 0 is backward
    a_inv_enable = 0 #boolean 1 is on
    a_inv_discharge = 0 #boolean ignore
    a_targetMode = 0 #boolean 0=speed, 1=torque
    a_torqueLimit = 0 #int
    a_targetTime = 0 #int
    a_chosenCurve = 0 #int, 0 is instant, 1 is linear

    mirror_direction = "backward"
    mirror_inv_enable = "inv enable on"
    mirror_targetMode = "speed mode"
    mirror_chosenCure = "instant curve"

    logname = "LogsDefault.txt"
    lognameshiftregister = "LogsDefault.txt"
    consolelogname = "Console.txt"

    errorFormatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    # format settings for logging handlers
    infoFormatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

    errorLogger = logging.getLogger(__name__)  # errorLogger object
    errorLogger.setLevel(logging.ERROR)

    infoLogger = logging.getLogger(__name__)  # infoLogger object
    infoLogger.setLevel(logging.INFO)

    info_handler = logging.FileHandler('infoLog' + logname)  # infoHandler setup
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(infoFormatter)

    error_handler = logging.FileHandler('errorLog' + logname)  # errorHandler setup
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(errorFormatter)

    infoLogger.addHandler(info_handler)
    errorLogger.addHandler(error_handler)

    infoLogger.info("\nProgram initialized with values:\n"
                    "a_targetTorque = %i\n"
                    "a_targetSpeed = %i\n" 
                    "a_direction = %i\n" 
                    "a_inv_enable = %i \n"
                    "a_inv_discharge = %i\n"
                    "a_targetMode = %i\n"
                    "a_torqueLimit = %i\n"
                    "a_targetTime = %i\n"
                    "a_chosenCurve = %i" % (a_targetTorque, a_targetSpeed, a_direction, a_inv_enable, a_inv_discharge
                                            , a_targetMode, a_torqueLimit, a_targetTime, a_chosenCurve))


    def getnewcurve(self): #returns number of selected curve
        currentcurvetext = self.comboBoxCurveChoices.currentText()
        print(currentcurvetext)
        if currentcurvetext == "Instant Curve":
            self.infoLogger.info("f: getnewcurve r:0")
            return 0
        elif currentcurvetext == "Linear Curve":
            self.infoLogger("f:getnewcurve r:1")
            return 1

    def setcurrentcurve(self): #sets a_chosenCurve to new chosen curve
        self.a_chosenCurve = self.getnewcurve()
        if self.a_chosenCurve == 0:
            self.labelCurve.setText("Instant Curve")
            self.infoLogger.info("f:setcurrentcurve r:instant curve")
        elif self.a_chosenCurve == 1:
            self.labelCurve.setText("Linear Curve")
            self.infoLogger.info("f:setcurrentcurve r:linear curve")

    def resetcurrentcurve(self): #puts a_chosenCurve to 0
        self.a_chosenCurve = 0
        self.writetolog("f:resetcurrentcurve")

    def getmode(self): #returns number of chosen mode
        if self.radioButtonSpeed.isChecked():
            return 0
        elif self.radioButtonTorque.isChecked():
            return 1
        else:
            return 9

    def setmode(self): #sets a_targetMode to selected mode
        tempmode = self.getmode()
        if tempmode == 0:
            self.a_targetMode = 0
            self.labelMode.setText("Speed Mode")
        elif tempmode == 1:
            self.a_targetMode = 1
            self.labelMode.setText("Torque Mode")
        elif tempmode == 9:
            print("No mode is chosen")

    def resetmode(self): #sets a_targetMode to 0
        self.a_targetMode = 0
        print("Mode reset to 0")

    def getdirection(self): #returns chosen direction
        if self.radioButtonFoward.isChecked():
            return 1
        elif self.radioButtonBackward.isChecked():
            return 0
        else:
            return 9

    #def setdirection(self): #sets a_direction to chosen direction
    #    tempdirection = self.getdirection()
    #    if tempdirection == 1:
    #        self.a_direction = 1
    #        self.labelDirection.setText("Forward")
    #    elif tempdirection == 0:
    #        self.a_direction = 0
    #        self.labelDirection.setText("Backward")
    #    elif tempdirection == 9:
    #        print("No direction is chosen")

    def resetdirection(self): #sets a_direction to 0
        self.a_direction = 0
        print("Direction reset to 0")

    def inv_enableon(self): #sets inv_enable to 1
        self.a_inv_enable = 1
        print("Enableon set to 1")

    def inv_enableoff(self): #sets inv_enable to 0
        self.a_inv_enable = 0
        print("Enableon set to 0")

    def resetspeed(self): #sets a_targetSpeed to 0
        self.a_targetSpeed = 0

    def resetintime(self): #sets a_targeTime to 0
        self.a_targetTime = 0 #will need to change this?

    def resettorquelimit(self): #sets a_torqueLimit to 0
        self.a_torqueLimit = 0

    def writetoconsolelog(self, input):
        with open(self.consolelogname, 'w') as console_log_file:
            console_log_file.write("\n" + input)
        self.updateconsole()

    def updateconsole(self):
        with open(self.consolelogname, 'r') as display_console:
            consolelogstr = str(display_console.read())
        self.textBrowserDisplay.setText(consolelogstr)
        self.textBrowserDisplay.verticalScrollBar().setValue(self.textBrowserDisplay.verticalScrollBar().maximum())

    def on(self): #sets the settings and inv_enable to 1, then sends settings

        if (self.radioButtonSpeed.isChecked() or self.radioButtonTorque.isChecked()):

            error_handler1 = logging.FileHandler('errorLog' + self.logname)  # errorHandler setup
            error_handler1.setLevel(logging.ERROR)
            error_handler1.setFormatter(self.errorFormatter)

            info_handler1 = logging.FileHandler('infoLog' + self.logname)  # infoHandler setup
            info_handler1.setLevel(logging.INFO)
            info_handler1.setFormatter(self.infoFormatter)

            self.infoLogger.removeHandler(self.error_handler)
            self.errorLogger.removeHandler(self.info_handler)

            self.error_handler = error_handler1
            self.info_handler = info_handler1

            self.errorLogger.addHandler(self.error_handler)  # binds handler with the logger object
            self.infoLogger.addHandler(self.info_handler)

            self.infoLogger.info("On function start")

            self.writetoconsolelog("Turn on successful.\nCurve mode is: " + self.mirror_chosenCure + "\nMode is: " +
                                   self.mirror_targetMode)

            self.setcurrentcurve()
            self.setmode()
            self.inv_enableon()
            test_python_fpga.send_settings(self.a_chosenCurve)
            test_python_fpga.send_enable(self.a_inv_enable)

        else:
            self.writetoconsolelog("Check speed or torque mode")

    def off(self):
        return 0

    def pushbuttonlogname(self):
        temp = str(self.lineEditLogName.text())

        if (temp == ""):
            print("Warning: No specified log file chosen. A default name will be used if turned on.")
        else:
            addonstr = temp + '.txt'
            self.labelCurrentLog.setText(addonstr)
            self.logname = addonstr
            self.consolelogname = "Console" + addonstr

    def prepdatavalues(self): #retrieves user input and preps it into Prepped Data Values
        targetspeededit = self.lineEditTargetSpeed.text()
        intimeedit = self.lineEditInTime.text()
        torquelimitedit = self.lineEditTorqueLimit.text()

        try:
            if targetspeededit == "":
                self.labelPreppedTargetSpeed.setText("0")
            elif int(targetspeededit) >= 0:
                self.labelPreppedTargetSpeed.setText(targetspeededit)
            else:
                print("Target Speed Cannot be negative")
        except ValueError:
            print("Invalid Target Speed")

        try:
            if intimeedit == "":
                self.labelPreppedInTime.setText("0")
            elif int(intimeedit) >= 0:
                self.labelPreppedInTime.setText(intimeedit)
            else:
                print("In Time Cannot be negative")
        except ValueError:
            print("Invalid In Time")

        if (self.a_targetMode == 1):
            try:
                if torquelimitedit == "":
                    self.labelPreppedTorqueLimit.setText("0")
                elif int(torquelimitedit) >=0:
                    self.labelPreppedTorqueLimit.setText(torquelimitedit)
                else:
                    print("Torque Limit cannot be negative")
            except ValueError:
                print("Invalid Torque Limit")

        if (self.getdirection()!=9):
            if (self.getdirection() == 0):
                self.labelDirection.setText("Backward")
            elif (self.getdirection() == 1):
                self.labelDirection.setText("Forward")
        else:
            print("No direction chosen")

    # sends command and prints to textBrowser
    def pushbuttonsendcommand(self): #sends contents of Prepped Data Values
        try:
            preppedSpeed = int(self.labelPreppedTargetSpeed.text())
            preppedTime = int(self.labelPreppedInTime.text())
            preppedTorqueLimit = int(self.labelPreppedTorqueLimit.text())
            if (self.labelDirection.text() == "Foward"):
                preppedDirection = 1
            elif (self.labelDirection.text() == "Backward"):
                preppedDirection = 0
            else:
                raise AttributeError("Invalid Prepped Direction")

            if not self.checkBoxSendConfirm.isChecked():
                toBeSent = "Send Confirm is not checked."
                self.textBrowserDisplay.setText(toBeSent)
            elif self.checkBoxSendConfirm.isChecked():

                self.a_targetSpeed = preppedSpeed
                self.a_targetTime = preppedTime
                self.a_torqueLimit = preppedTorqueLimit

                test_python_fpga.send_command(self.a_targetTorque, self.a_targetSpeed, self.a_direction,
                                              self.a_inv_enable,
                                              self.a_inv_discharge, self.a_targetMode, self.a_torqueLimit,
                                              self.a_targetTime
                                              )

                toBeSent = "Target speed of " + str(preppedSpeed) + " in " + str(preppedTime) + \
                           " seconds with a torque limit of " + str(preppedTorqueLimit) + " command sent."

                self.textBrowserDisplay.setText(toBeSent)
                self.checkBoxSendConfirm.setChecked(False)

        except AttributeError:
            print("Invalid Prepped Data Values")

    def pushbuttonhaltcommand(self): #sends halt values to fpga and Prepped Data Values accordingly
        #sends halt command and prints to textBrowser
        self.textBrowserDisplay.setText("Halt Command Sent")

        self.resetspeed()
        self.resetintime()
        self.resettorquelimit()

        #actual halt code


if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    nextGui = mainProgram()
    nextGui.show()
    sys.exit(app.exec_())