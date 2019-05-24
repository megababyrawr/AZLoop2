import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainUI03 import Ui_MainWindow
import test_python_fpga
class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)
        self.setupUi(self)

        self.pushButtonOn.clicked.connect(self.on)

        self.pushButtonOff.clicked.connect(self.off)

        self.pushButtonPrepDataValues.clicked.connect(self.prepdatavalues)

        self.pushButtonSendCommand.clicked.connect(self.pushbuttonsendcommand)

        self.pushButtonHaltCommand.clicked.connect(self.pushbuttonhaltcommand)

    a_targetTorque = 0 #int
    a_targetSpeed = 0 #int
    a_direction = 0 #boolean 1 is forward, 0 is backward
    a_inv_enable = 0 #boolean 1 is on
    a_inv_discharge = 0 #boolean ignore
    a_targetMode = 0 #boolean 0=speed, 1=torque
    a_torqueLimit = 0 #int
    a_targetTime = 0 #int
    a_chosenCurve = 0 #int, 0 is instant, 1 is linear

    def getnewcurve(self): #returns number of selected curve
        currentcurvetext = self.comboBoxCurveChoices.currentText()
        print(currentcurvetext)
        if currentcurvetext == "Instant Curve":
            return 0
        elif currentcurvetext == "Linear Curve":
            return 1
    def setcurrentcurve(self): #sets a_chosenCurve to new chosen curve
        self.a_chosenCurve = self.getnewcurve()
        if self.a_chosenCurve == 0:
            self.labelCurve.setText("Instant Curve")
        elif self.a_chosenCurve == 1:
            self.labelCurve.setText("Linear Curve")

    def resetcurrentcurve(self): #puts a_chosenCurve to 0
        self.a_chosenCurve = 0
        print("Chosen Curve reset to 0")

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
    def setdirection(self): #sets a_direction to chosen direction
        tempdirection = self.getdirection()
        if tempdirection == 1:
            self.a_direction = 1
            self.labelDirection.setText("Forward")
        elif tempdirection == 0:
            self.a_direction = 0
            self.labelDirection.setText("Backward")
        elif tempdirection == 9:
            print("No direction is chosen")
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

    def on(self): #sets the settings and inv_enable to 1, then sends settings
        self.setcurrentcurve()
        self.setdirection()
        self.setmode()
        self.inv_enableon()

        test_python_fpga.send_settings(self.a_chosenCurve)
        test_python_fpga.send_enable(self.a_inv_enable)

        #print to console

    def off(self):
        return 0


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

        try:
            if torquelimitedit == "":
                self.labelPreppedTorqueLimit.setText("0")
            elif int(torquelimitedit) >=0:
                self.labelPreppedTorqueLimit.setText(torquelimitedit)
            else:
                print("Torque Limit cannot be negative")
        except ValueError:
            print("Invalid Torque Limit")

    # sends command and prints to textBrowser
    def pushbuttonsendcommand(self): #sends contents of Prepped Data Values
        try:
            preppedSpeed = int(self.labelPreppedTargetSpeed.text())
            preppedTime = int(self.labelPreppedInTime.text())
            preppedTorqueLimit = int(self.labelPreppedTorqueLimit.text())
        except AttributeError:
            print("Invalid Prepped Data Values")
        if not self.checkBoxSendConfirm.isChecked():
            toBeSent = "Send Confirm is not checked."
            self.textBrowserDisplay.setText(toBeSent)
        elif self.checkBoxSendConfirm.isChecked():

            self.a_targetSpeed = preppedSpeed
            self.a_targetTime = preppedTime
            self.a_torqueLimit = preppedTorqueLimit

            test_python_fpga.send_command(self.a_targetTorque, self.a_targetSpeed, self.a_direction, self.a_inv_enable,
                                          self.a_inv_discharge, self.a_targetMode, self.a_torqueLimit, self.a_targetTime
                                          )

            toBeSent = "Target speed of " + str(preppedSpeed) + " in " + str(preppedTime) +\
                       " seconds with a torque limit of " + str(preppedTorqueLimit) + " command sent."

            self.textBrowserDisplay.setText(toBeSent)
            self.checkBoxSendConfirm.setChecked(False)

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