import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainUI02 import Ui_MainWindow
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

    def getnewcurve(self):
        currentcurvetext = self.comboBoxCurveChoices.currentText()
        print(currentcurvetext)
        if currentcurvetext == "Instant Curve":
            return 0
        elif currentcurvetext == "Linear Curve":
            return 1
    def setcurrentcurve(self):
        self.a_chosenCurve = self.getnewcurve()
        if self.a_chosenCurve == 0:
            self.labelCurve.setText("Instant Curve")
        elif self.a_chosenCurve == 1:
            self.labelCurve.setText("Linear Curve")
        else:
            self.labelCurve.setText("Nothing")

    def resetcurrentcurve(self):
        self.a_chosenCurve = 0
        print("Chosen Curve reset to 0")

    def getmode(self):
        if self.radioButtonSpeed.isChecked():
            return 0
        elif self.radioButtonTorque.isChecked():
            return 1
        else:
            return 9
    def setmode(self):
        tempmode = self.getmode
        if tempmode == 0:
            self.a_targetMode = 0
            self.labelMode.setText("Speed Mode")
        elif tempmode == 1:
            self.a_targetMode = 1
            self.labelMode.setText("Torque Mode")
        elif tempmode == 9:
            print("No mode is chosen")
    def resetmode(self):
        self.a_targetMode = 0
        print("Mode reset to 0")
    def getdirection(self):
        if self.radioButtonFoward.isChecked():
            return 0
        elif self.radioButtonBackward.isChecked():
            return 1
        else:
            return 9
    def setdirection(self):
        tempdirection = self.getdirection()
        if tempdirection == 1:
            self.a_direction = 1
            self.labelDirection.setText("Forward")
        elif tempdirection == 0:
            self.a_direction = 0
            self.labelDirection.setText("Backward")
        elif tempdirection == 9:
            print("No direction is chosen")
    def resetdirection(self):
        self.a_direction = 0
        print("Direction reset to 0")
    def inv_enableon(self):
        self.a_inv_enable = 1
        print("Enableon set to 1")
    def inv_enableoff(self):
        self.a_inv_enable = 0
        print("Enableon set to 0")
    def on(self):
        self.setcurrentcurve()
        self.setdirection()
        self.setmode()
        self.inv_enableon()

        test_python_fpga.send_settings(self.a_chosenCurve)
        test_python_fpga.send_enable(self.a_inv_enable)

        #print to console

    def off(self):
        return 0


    def prepdatavalues(self):
        targetspeededit = self.lineEditTargetSpeed.text()
        intimeedit = self.lineEditInTime.text()
        torquelimitedit = self.lineEditTorqueLimit.text()

        if targetspeededit == "":
            self.labelPreppedTargetSpeed.setText("0")
        elif int(targetspeededit) >= 0:
            self.labelPreppedTargetSpeed.setText(targetspeededit)
        else:
            print("Invalid Target Speed")

        if intimeedit == "":
            self.labelPreppedInTime.setText("0")
        elif int(intimeedit) >= 0:
            self.labelPreppedInTime.setText(intimeedit)
        else:
            print("Invalid In Time")

        if torquelimitedit == "":
            self.labelTorqueLimit.setText("0")
        elif int(torquelimitedit) >=0:
            self.labelTorqueLimit.setText(targetspeededit)
        else:
            print("Invalid Torque Limit")


    def pushbuttonprepsettings(self):
        self.labelPreppedCurveMode.setText(self.comboBoxCurveChoices.currentText())

    # sends command and prints to textBrowser
    def pushbuttonsendcommand(self):
        preppedSpeed = int(self.labelPreppedTargetSpeed.text())  # NEED to make all labels 0 initially
        preppedTime = int(self.labelPreppedInTime.text())
        preppedSetting = int(self.labelPreppedCurveMode.text())
        if not self.checkBoxSendConfirm.isChecked():
            toBeSent = "Send Confirm is not checked."
            self.textBrowserDisplay.setText(toBeSent)
        if self.checkBoxSendConfirm.isChecked():

            self.setdirection()
            self.setmode()
            self.inv_enableon()

            test_python_fpga.send_settings(self.targetTorque, self.targetSpeed, self.direction, self.inv_enable, self.inv_discharge, self.targetMode, self.torqueLimit, self.targetTime)

            toBeSent = "Target speed of " + str(preppedSpeed) + " in " + str(preppedTime) + " seconds using a " + preppedSetting + " command sent."
            self.textBrowserDisplay.setText(toBeSent)
            self.checkBoxSendConfirm.setChecked(False)





            #need actual send code here
    def pushbuttonhaltcommand(self):
        #sends halt command and prints to textBrowser
        self.textBrowserDisplay.setText("Halt Command Sent")

        #actual halt code


if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    nextGui = mainProgram()
    nextGui.show()
    sys.exit(app.exec_())