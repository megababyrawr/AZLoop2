# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AZLoop2.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(758, 586)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxDataValues = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxDataValues.setGeometry(QtCore.QRect(380, 10, 361, 321))
        self.groupBoxDataValues.setObjectName("groupBoxDataValues")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBoxDataValues)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 331, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelTargetSpeed = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelTargetSpeed.setObjectName("labelTargetSpeed")
        self.gridLayout.addWidget(self.labelTargetSpeed, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.lineEditInTime = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEditInTime.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEditInTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditInTime.setObjectName("lineEditInTime")
        self.gridLayout.addWidget(self.lineEditInTime, 1, 4, 1, 1)
        self.lineEditTargetSpeed = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEditTargetSpeed.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEditTargetSpeed.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditTargetSpeed.setObjectName("lineEditTargetSpeed")
        self.gridLayout.addWidget(self.lineEditTargetSpeed, 0, 4, 1, 1)
        self.lineEditTorqueLimit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEditTorqueLimit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditTorqueLimit.setObjectName("lineEditTorqueLimit")
        self.gridLayout.addWidget(self.lineEditTorqueLimit, 2, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.labelInTime = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelInTime.setObjectName("labelInTime")
        self.gridLayout.addWidget(self.labelInTime, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 2)
        self.gridLayout.setColumnStretch(4, 2)
        self.pushButtonPrepDataValues = QtWidgets.QPushButton(self.groupBoxDataValues)
        self.pushButtonPrepDataValues.setGeometry(QtCore.QRect(230, 150, 121, 23))
        self.pushButtonPrepDataValues.setObjectName("pushButtonPrepDataValues")
        self.groupBoxPreppedDataValues = QtWidgets.QGroupBox(self.groupBoxDataValues)
        self.groupBoxPreppedDataValues.setGeometry(QtCore.QRect(10, 170, 341, 141))
        self.groupBoxPreppedDataValues.setObjectName("groupBoxPreppedDataValues")
        self.labelPreppedTargetSpeedLabel = QtWidgets.QLabel(self.groupBoxPreppedDataValues)
        self.labelPreppedTargetSpeedLabel.setGeometry(QtCore.QRect(10, 40, 101, 20))
        self.labelPreppedTargetSpeedLabel.setObjectName("labelPreppedTargetSpeedLabel")
        self.labelPreppedInTimeLabel = QtWidgets.QLabel(self.groupBoxPreppedDataValues)
        self.labelPreppedInTimeLabel.setGeometry(QtCore.QRect(10, 70, 121, 20))
        self.labelPreppedInTimeLabel.setObjectName("labelPreppedInTimeLabel")
        self.labelPreppedTargetSpeed = QtWidgets.QLabel(self.groupBoxPreppedDataValues)
        self.labelPreppedTargetSpeed.setGeometry(QtCore.QRect(250, 40, 81, 21))
        self.labelPreppedTargetSpeed.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPreppedTargetSpeed.setObjectName("labelPreppedTargetSpeed")
        self.labelPreppedInTime = QtWidgets.QLabel(self.groupBoxPreppedDataValues)
        self.labelPreppedInTime.setGeometry(QtCore.QRect(250, 70, 81, 21))
        self.labelPreppedInTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPreppedInTime.setObjectName("labelPreppedInTime")
        self.labelTorqueLimitLabel = QtWidgets.QLabel(self.groupBoxPreppedDataValues)
        self.labelTorqueLimitLabel.setGeometry(QtCore.QRect(10, 100, 121, 17))
        self.labelTorqueLimitLabel.setObjectName("labelTorqueLimitLabel")
        self.labelPreppedTorqueLimit = QtWidgets.QLabel(self.groupBoxPreppedDataValues)
        self.labelPreppedTorqueLimit.setGeometry(QtCore.QRect(250, 100, 81, 16))
        self.labelPreppedTorqueLimit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPreppedTorqueLimit.setObjectName("labelPreppedTorqueLimit")
        self.gridLayoutWidget.raise_()
        self.groupBoxPreppedDataValues.raise_()
        self.pushButtonPrepDataValues.raise_()
        self.pushButtonHaltCommand = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHaltCommand.setGeometry(QtCore.QRect(620, 460, 111, 51))
        self.pushButtonHaltCommand.setObjectName("pushButtonHaltCommand")
        self.groupBoxDisplay = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxDisplay.setGeometry(QtCore.QRect(20, 330, 591, 201))
        self.groupBoxDisplay.setTitle("")
        self.groupBoxDisplay.setObjectName("groupBoxDisplay")
        self.textBrowserDisplay = QtWidgets.QTextBrowser(self.groupBoxDisplay)
        self.textBrowserDisplay.setGeometry(QtCore.QRect(10, 30, 571, 161))
        self.textBrowserDisplay.setObjectName("textBrowserDisplay")
        self.pushButtonSendCommand = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSendCommand.setGeometry(QtCore.QRect(620, 360, 111, 51))
        self.pushButtonSendCommand.setObjectName("pushButtonSendCommand")
        self.checkBoxSendConfirm = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxSendConfirm.setGeometry(QtCore.QRect(620, 420, 111, 23))
        self.checkBoxSendConfirm.setObjectName("checkBoxSendConfirm")
        self.groupBoxSettings = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxSettings.setGeometry(QtCore.QRect(20, 10, 351, 321))
        self.groupBoxSettings.setObjectName("groupBoxSettings")
        self.comboBoxCurveChoices = QtWidgets.QComboBox(self.groupBoxSettings)
        self.comboBoxCurveChoices.setGeometry(QtCore.QRect(20, 40, 171, 21))
        self.comboBoxCurveChoices.setObjectName("comboBoxCurveChoices")
        self.comboBoxCurveChoices.addItem("")
        self.comboBoxCurveChoices.addItem("")
        self.radioButtonSpeed = QtWidgets.QRadioButton(self.groupBoxSettings)
        self.radioButtonSpeed.setGeometry(QtCore.QRect(30, 80, 71, 23))
        self.radioButtonSpeed.setObjectName("radioButtonSpeed")
        self.buttonGroupSpeedTorque = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroupSpeedTorque.setObjectName("buttonGroupSpeedTorque")
        self.buttonGroupSpeedTorque.addButton(self.radioButtonSpeed)
        self.radioButtonTorque = QtWidgets.QRadioButton(self.groupBoxSettings)
        self.radioButtonTorque.setGeometry(QtCore.QRect(120, 80, 71, 23))
        self.radioButtonTorque.setObjectName("radioButtonTorque")
        self.buttonGroupSpeedTorque.addButton(self.radioButtonTorque)
        self.radioButtonFoward = QtWidgets.QRadioButton(self.groupBoxSettings)
        self.radioButtonFoward.setGeometry(QtCore.QRect(30, 120, 112, 23))
        self.radioButtonFoward.setObjectName("radioButtonFoward")
        self.buttonGroupForwardBackward = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroupForwardBackward.setObjectName("buttonGroupForwardBackward")
        self.buttonGroupForwardBackward.addButton(self.radioButtonFoward)
        self.radioButtonBackward = QtWidgets.QRadioButton(self.groupBoxSettings)
        self.radioButtonBackward.setGeometry(QtCore.QRect(120, 120, 112, 23))
        self.radioButtonBackward.setObjectName("radioButtonBackward")
        self.buttonGroupForwardBackward.addButton(self.radioButtonBackward)
        self.pushButtonOn = QtWidgets.QPushButton(self.groupBoxSettings)
        self.pushButtonOn.setGeometry(QtCore.QRect(210, 180, 131, 51))
        self.pushButtonOn.setObjectName("pushButtonOn")
        self.pushButtonOff = QtWidgets.QPushButton(self.groupBoxSettings)
        self.pushButtonOff.setGeometry(QtCore.QRect(210, 250, 131, 51))
        self.pushButtonOff.setObjectName("pushButtonOff")
        self.groupBoxCurrentSettings = QtWidgets.QGroupBox(self.groupBoxSettings)
        self.groupBoxCurrentSettings.setGeometry(QtCore.QRect(10, 150, 191, 161))
        self.groupBoxCurrentSettings.setObjectName("groupBoxCurrentSettings")
        self.labelMode = QtWidgets.QLabel(self.groupBoxCurrentSettings)
        self.labelMode.setGeometry(QtCore.QRect(10, 80, 171, 17))
        self.labelMode.setObjectName("labelMode")
        self.labelDirection = QtWidgets.QLabel(self.groupBoxCurrentSettings)
        self.labelDirection.setGeometry(QtCore.QRect(10, 120, 171, 17))
        self.labelDirection.setObjectName("labelDirection")
        self.labelCurve = QtWidgets.QLabel(self.groupBoxCurrentSettings)
        self.labelCurve.setGeometry(QtCore.QRect(10, 40, 171, 17))
        self.labelCurve.setObjectName("labelCurve")
        self.groupBoxSettings.raise_()
        self.groupBoxDataValues.raise_()
        self.groupBoxDisplay.raise_()
        self.pushButtonSendCommand.raise_()
        self.pushButtonHaltCommand.raise_()
        self.checkBoxSendConfirm.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 758, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHi_D = QtWidgets.QAction(MainWindow)
        self.actionHi_D.setObjectName("actionHi_D")
        self.menuFile.addAction(self.actionHi_D)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AZLoop"))
        self.groupBoxDataValues.setTitle(_translate("MainWindow", "Data Values"))
        self.labelTargetSpeed.setText(_translate("MainWindow", "Target Speed"))
        self.labelInTime.setText(_translate("MainWindow", "In time (seconds)"))
        self.label.setText(_translate("MainWindow", "Torque Limit (optional)"))
        self.pushButtonPrepDataValues.setText(_translate("MainWindow", "Prep Data Values"))
        self.groupBoxPreppedDataValues.setTitle(_translate("MainWindow", "Prepped Data Values"))
        self.labelPreppedTargetSpeedLabel.setText(_translate("MainWindow", "Target Speed"))
        self.labelPreppedInTimeLabel.setText(_translate("MainWindow", "In time (seconds)"))
        self.labelPreppedTargetSpeed.setText(_translate("MainWindow", "0"))
        self.labelPreppedInTime.setText(_translate("MainWindow", "0"))
        self.labelTorqueLimitLabel.setText(_translate("MainWindow", "Torque Limit"))
        self.labelPreppedTorqueLimit.setText(_translate("MainWindow", "0"))
        self.pushButtonHaltCommand.setText(_translate("MainWindow", "Halt Command"))
        self.pushButtonSendCommand.setText(_translate("MainWindow", "Send Command"))
        self.checkBoxSendConfirm.setText(_translate("MainWindow", "Send Confirm"))
        self.groupBoxSettings.setTitle(_translate("MainWindow", "Settings"))
        self.comboBoxCurveChoices.setItemText(0, _translate("MainWindow", "Instant Curve"))
        self.comboBoxCurveChoices.setItemText(1, _translate("MainWindow", "Linear Curve"))
        self.radioButtonSpeed.setText(_translate("MainWindow", "Speed"))
        self.radioButtonTorque.setText(_translate("MainWindow", "Torque"))
        self.radioButtonFoward.setText(_translate("MainWindow", "Forward"))
        self.radioButtonBackward.setText(_translate("MainWindow", "Backward"))
        self.pushButtonOn.setText(_translate("MainWindow", "On"))
        self.pushButtonOff.setText(_translate("MainWindow", "Off"))
        self.groupBoxCurrentSettings.setTitle(_translate("MainWindow", "Current Settings"))
        self.labelMode.setText(_translate("MainWindow", "Mode"))
        self.labelDirection.setText(_translate("MainWindow", "Direction"))
        self.labelCurve.setText(_translate("MainWindow", "Curve"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionHi_D.setText(_translate("MainWindow", "Hi :D"))


