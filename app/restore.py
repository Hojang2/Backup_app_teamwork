# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os

class RestoreWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

    def setupUi(self):
        self.setObjectName("restore")
        self.setFixedSize(480, 240)

        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")

        self._cRestore = QtWidgets.QRadioButton(self.centralwidget)
        self._cRestore.setGeometry(QtCore.QRect(10, 10, 100, 20))
        self._cRestore.setObjectName("compress")

        self._pRestore = QtWidgets.QFileDialog(self.centralwidget)
        self._pRestoreButton = QtWidgets.QPushButton(self.centralwidget)
        self._pRestoreLabel = QtWidgets.QLabel(self.centralwidget)
        self._pRestoreButton.setGeometry(QtCore.QRect(10, 40, 50, 30))
        self._pRestoreLabel.setGeometry(QtCore.QRect(65, 40, 465, 30))
        self._pRestoreButton.setText("File:")
        self._pRestore.setObjectName("path")
        self._pRestoreButton.clicked.connect(self._pRestoreButtonHandle)

        self._oRestore = QtWidgets.QFileDialog(self.centralwidget)
        self._oRestoreButton = QtWidgets.QPushButton(self.centralwidget)
        self._oRestoreLabel = QtWidgets.QLabel(self.centralwidget)
        self._oRestoreButton.setGeometry(QtCore.QRect(10, 80, 50, 30))
        self._oRestoreLabel.setGeometry(QtCore.QRect(65, 80, 465, 30))
        self._oRestoreButton.setText("Output:")
        self._oRestore.setObjectName("output")
        self._oRestoreButton.clicked.connect(self._oRestoreButtonHandle)

        self.submitRestore = QtWidgets.QPushButton(self.centralwidget)
        self.submitRestore.setGeometry(QtCore.QRect(220, 160, 50, 40))
        self.submitRestore.setObjectName("submit")
        self.submitRestore.clicked.connect(self.RestoreSystemPrint)
         
        self.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Restore"))
        self._cRestore.setText(_translate("MainWindow", "Compression"))
        self.submitRestore.setText(_translate("MainWindow", "Submit!"))


    def _pRestoreButtonHandle(self):
        path = self._pRestore.getOpenFileName(self)
        self._pRestoreLabel.setText(path[0])

    def _oRestoreButtonHandle(self):
        output = self._oRestore.getExistingDirectory(self)
        self._oRestoreLabel.setText(output)

    def RestoreSystemPrint(self):
        if self._cRestore.isChecked():
            os.system("python main.py -r -c -p {} -o {}".format(self._pRestoreLabel.text(), self._oRestoreLabel.text()))
        else:
            os.system("python main.py -r -p {} -o {}".format(self._pRestoreLabel.text(), self._oRestoreLabel.text()))
        self.hide()
