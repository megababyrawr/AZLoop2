import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainUI02 import Ui_MainWindow
import python_fpga
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
    a_direction = 0 #boolean 0 is forward, 1 is backward
    a_inv_enable = 0 #boolean 1 is on
    a_inv_discharge = 0 #boolean ignore
    a_targetMode = 0 #boolean 0=speed, 1=torque
    a_torqueLimit = 0 #int
    a_targetTime = 0 #int
    a_chosenCurve = 0 #int, 0 is instant, 1 is linear

    def getnewcurve(self):
        currentcurvetext = self.comboBoxCurveChoices.currentText
        if currentcurvetext == "Instant Curve":
            return 0
        if currentcurvetext == "Linear Curve":
            return 1
    def setcurrentcurve(self):
        self.a_chosenCurve = self.getnewcurve()
        if self.chosenCurve == 0:
            self.labelCurve.setText("Instant Curve")
        if self.chosenCurve == 1:
            self.labelCurve.setText("Linear Curve")

    def resetcurrentcurve(self):
        self.a_chosenCurve = 0

    def getmode(self):
        if self.radioButtonSpeed.isChecked():
            return 0
        if self.radioButtonTorque.isChecked():
            return 1
    def setmode(self):
        if self.getmode == 0:
            self.a_targetMode = 0
            self.labelMode.setText("Speed Mode")
        if self.getmode == 1:
            self.a_targetMode = 1
            self.labelMode.setText("Torque Mode")
    def resetmode(self):
        self.a_targetMode = 0
    def getdirection(self):
        if self.radioButtonFoward.isChecked():
            return 1
        if self.radioButtonBackward.isChecked():
            return 0
    def setdirection(self):
        if self.getdirection() == 0:
            self.a_direction = 0
            self.labelDirection.setText("Forward")
        if self.getdirection() == 1:
            self.a_direction = 1
            self.labelDirection.setText("Backward")
    def resetdirection(self):
        self.a_direction = 0
    def inv_enableon(self):
        self.a_inv_enable = 1
    def inv_enableoff(self):
        self.a_inv_enable = 0
    def on(self):
        self.setcurrentcurve()
        self.inv_enableon()

        python_fpga.send_settings(self.a_chosenCurve)
        python_fpga.send_enable(self.a_inv_enable)

    def off(self):



    def prepdatavalues(self):
        self.labelPreppedTargetSpeed.setText(self.lineEditTargetSpeed.text())
        self.labelPreppedInTime.setText(self.lineEditInTime.text())
        self.labelTorqueLimit.setText(self.lineEditTorqueLimit.text())
        self.
    def pushbuttonprepsettings(self):
        self.labelPreppedCurveMode.setText(self.comboBoxCurveChoices.currentText())

    # sends command and prints to textBrowser
    def pushbuttonsendcommand(self):
        preppedSpeed = int(self.labelPreppedTargetSpeed.text())  # NEED to make all labels 0 initially
        preppedTime = int(self.labelPreppedInTime.text())
        preppedSetting = self.labelPreppedCurveMode.text()
        if not self.checkBoxSendConfirm.isChecked():
            toBeSent = "Send Confirm is not checked."
            self.textBrowserDisplay.setText(toBeSent)
        if self.checkBoxSendConfirm.isChecked():

            self.setdirection()
            self.setmode()
            self.inv_enableon()

            python_fpga.send_settings(self.targetTorque, self.targetSpeed, self.direction, self.inv_enable, self.inv_discharge, self.targetMode, self.torqueLimit, self.targetTime)

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