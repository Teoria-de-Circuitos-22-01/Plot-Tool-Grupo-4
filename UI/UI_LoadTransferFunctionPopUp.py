# Form implementation generated from reading ui file 'UI_LoadTransferFunctionPopUp.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoadTransferFunctionPopUp(object):
    def setupUi(self, LoadTransferFunctionPopUp):
        LoadTransferFunctionPopUp.setObjectName("LoadTransferFunctionPopUp")
        LoadTransferFunctionPopUp.resize(425, 539)
        self.gridLayout = QtWidgets.QGridLayout(LoadTransferFunctionPopUp)
        self.gridLayout.setObjectName("gridLayout")
        self.MarkerLabel = QtWidgets.QLabel(LoadTransferFunctionPopUp)
        self.MarkerLabel.setObjectName("MarkerLabel")
        self.gridLayout.addWidget(self.MarkerLabel, 9, 0, 1, 1)
        self.StopDSB = QtWidgets.QDoubleSpinBox(LoadTransferFunctionPopUp)
        self.StopDSB.setMinimum(0.01)
        self.StopDSB.setMaximum(1e+29)
        self.StopDSB.setObjectName("StopDSB")
        self.gridLayout.addWidget(self.StopDSB, 4, 2, 1, 2)
        self.TransferFunctionButtonBox = QtWidgets.QDialogButtonBox(LoadTransferFunctionPopUp)
        self.TransferFunctionButtonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.TransferFunctionButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.TransferFunctionButtonBox.setObjectName("TransferFunctionButtonBox")
        self.gridLayout.addWidget(self.TransferFunctionButtonBox, 12, 2, 1, 2)
        self.StartFreqMultCB = QtWidgets.QComboBox(LoadTransferFunctionPopUp)
        self.StartFreqMultCB.setObjectName("StartFreqMultCB")
        self.gridLayout.addWidget(self.StartFreqMultCB, 3, 4, 1, 1)
        self.StartFreqLabel = QtWidgets.QLabel(LoadTransferFunctionPopUp)
        self.StartFreqLabel.setObjectName("StartFreqLabel")
        self.gridLayout.addWidget(self.StartFreqLabel, 3, 0, 1, 1)
        self.TexGroupBox = QtWidgets.QGroupBox(LoadTransferFunctionPopUp)
        self.TexGroupBox.setMinimumSize(QtCore.QSize(0, 175))
        self.TexGroupBox.setObjectName("TexGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.TexGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.addWidget(self.TexGroupBox, 1, 0, 1, 5)
        self.LineTypeLabel = QtWidgets.QLabel(LoadTransferFunctionPopUp)
        self.LineTypeLabel.setObjectName("LineTypeLabel")
        self.gridLayout.addWidget(self.LineTypeLabel, 7, 0, 1, 2)
        self.StopFreqMultCB = QtWidgets.QComboBox(LoadTransferFunctionPopUp)
        self.StopFreqMultCB.setObjectName("StopFreqMultCB")
        self.gridLayout.addWidget(self.StopFreqMultCB, 4, 4, 1, 1)
        self.LineTypeCB = QtWidgets.QComboBox(LoadTransferFunctionPopUp)
        self.LineTypeCB.setObjectName("LineTypeCB")
        self.gridLayout.addWidget(self.LineTypeCB, 7, 2, 1, 3)
        self.ColorLabel = QtWidgets.QLabel(LoadTransferFunctionPopUp)
        self.ColorLabel.setObjectName("ColorLabel")
        self.gridLayout.addWidget(self.ColorLabel, 8, 0, 1, 2)
        self.StopFreqLabel = QtWidgets.QLabel(LoadTransferFunctionPopUp)
        self.StopFreqLabel.setObjectName("StopFreqLabel")
        self.gridLayout.addWidget(self.StopFreqLabel, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ColorButton = QtWidgets.QPushButton(LoadTransferFunctionPopUp)
        self.ColorButton.setMinimumSize(QtCore.QSize(30, 30))
        self.ColorButton.setMaximumSize(QtCore.QSize(30, 30))
        self.ColorButton.setText("")
        self.ColorButton.setObjectName("ColorButton")
        self.horizontalLayout.addWidget(self.ColorButton)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 2, 1, 3)
        self.CheckButton = QtWidgets.QPushButton(LoadTransferFunctionPopUp)
        self.CheckButton.setObjectName("CheckButton")
        self.gridLayout.addWidget(self.CheckButton, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(LoadTransferFunctionPopUp)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.TransferFunctionLineEdit = QtWidgets.QLineEdit(LoadTransferFunctionPopUp)
        self.TransferFunctionLineEdit.setObjectName("TransferFunctionLineEdit")
        self.gridLayout.addWidget(self.TransferFunctionLineEdit, 0, 1, 1, 3)
        self.StartDSB = QtWidgets.QDoubleSpinBox(LoadTransferFunctionPopUp)
        self.StartDSB.setMinimum(0.01)
        self.StartDSB.setMaximum(1e+29)
        self.StartDSB.setObjectName("StartDSB")
        self.gridLayout.addWidget(self.StartDSB, 3, 2, 1, 2)
        self.TraceNameLabel = QtWidgets.QLabel(LoadTransferFunctionPopUp)
        self.TraceNameLabel.setObjectName("TraceNameLabel")
        self.gridLayout.addWidget(self.TraceNameLabel, 10, 0, 2, 1)
        self.MarkersCB = QtWidgets.QComboBox(LoadTransferFunctionPopUp)
        self.MarkersCB.setObjectName("MarkersCB")
        self.gridLayout.addWidget(self.MarkersCB, 9, 2, 1, 3)
        self.TraceNameLE = QtWidgets.QLineEdit(LoadTransferFunctionPopUp)
        self.TraceNameLE.setObjectName("TraceNameLE")
        self.gridLayout.addWidget(self.TraceNameLE, 10, 2, 2, 3)

        self.retranslateUi(LoadTransferFunctionPopUp)
        self.TransferFunctionButtonBox.rejected.connect(LoadTransferFunctionPopUp.reject) # type: ignore
        self.TransferFunctionButtonBox.accepted.connect(LoadTransferFunctionPopUp.accept) # type: ignore
        self.CheckButton.clicked.connect(LoadTransferFunctionPopUp.updateTransferFunction) # type: ignore
        self.TransferFunctionLineEdit.textEdited['QString'].connect(LoadTransferFunctionPopUp.textChange) # type: ignore
        self.ColorButton.clicked.connect(LoadTransferFunctionPopUp.ChooseColor) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(LoadTransferFunctionPopUp)

    def retranslateUi(self, LoadTransferFunctionPopUp):
        _translate = QtCore.QCoreApplication.translate
        LoadTransferFunctionPopUp.setWindowTitle(_translate("LoadTransferFunctionPopUp", "Agregar Transferencia"))
        self.MarkerLabel.setText(_translate("LoadTransferFunctionPopUp", "Marcadores"))
        self.StartFreqLabel.setText(_translate("LoadTransferFunctionPopUp", "Frec. inicial"))
        self.TexGroupBox.setTitle(_translate("LoadTransferFunctionPopUp", "Interpretado como"))
        self.LineTypeLabel.setText(_translate("LoadTransferFunctionPopUp", "Tipo de linea"))
        self.ColorLabel.setText(_translate("LoadTransferFunctionPopUp", "Color"))
        self.StopFreqLabel.setText(_translate("LoadTransferFunctionPopUp", "Frec. final"))
        self.CheckButton.setText(_translate("LoadTransferFunctionPopUp", "Check"))
        self.label.setText(_translate("LoadTransferFunctionPopUp", "H(s)"))
        self.TraceNameLabel.setText(_translate("LoadTransferFunctionPopUp", "Nombre de linea"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoadTransferFunctionPopUp = QtWidgets.QDialog()
    ui = Ui_LoadTransferFunctionPopUp()
    ui.setupUi(LoadTransferFunctionPopUp)
    LoadTransferFunctionPopUp.show()
    sys.exit(app.exec())
