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

    targetTorque = 0 #int
    targetSpeed = 0 #int
    direction = 0 #boolean
    inv_enable = 0 #boolean
    inv_discharge = 0 #boolean
    targetMode = 0 #boolean
    torqueLimit = 0 #int
    targetTime = 0 #int
    chosenCurve = 0 #int

    def on(self):

    def off(self):

    def prepdatavalues(self):
        self.labelPreppedTargetSpeed.setText(self.lineEditTargetSpeed.text())
        self.labelPreppedInTime.setText(self.lineEditInTime.text())

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