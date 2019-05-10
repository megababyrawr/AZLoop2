import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Test import Ui_MainWindow

class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)
        self.setupUi(self)

        self.pushButtonPrepDataValues.clicked.connect(self.prepdatavalues)

        self.pushButtonPrepSettings.clicked.connect(self.pushbuttonprepsettings)

        self.pushButtonSendCommand.clicked.connect(self.pushbuttonsendcommand)

        self.pushButtonHaltCommand.clicked.connect(self.pushbuttonhaltcommand)

    def prepdatavalues(self):
        self.labelPreppedTargetSpeed.setText(self.lineEditTargetSpeed.text())
        self.labelPreppedInTime.setText(self.lineEditInTime.text())

    def pushbuttonprepsettings(self):
        self.labelPreppedCurveMode.setText(self.comboBoxCurveChoices.currentText())

    # sends command and prints to textBrowser
    def pushbuttonsendcommand(self):

        preppedSpeed = int(self.labelPreppedTargetSpeed.text()) #NEED to make all labels 0 initially
        preppedTime = int(self.labelPreppedInTime.text())
        preppedSetting = self.labelPreppedCurveMode.text()

        toBeSent = "Target speed of " + str(preppedSpeed) + " in " + str(preppedTime) + " seconds using a " + preppedSetting + " command sent."
        self.textBrowserDisplay.setText(toBeSent)

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