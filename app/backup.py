# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os

class BackupWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

    def setupUi(self):
        self.setObjectName("backup")
        self.setFixedSize(480, 240)

        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")

        self._cBackup = QtWidgets.QRadioButton(self.centralwidget)
        self._cBackup.setGeometry(QtCore.QRect(10, 10, 100, 20))
        self._cBackup.setObjectName("compress")

        self._pBackup = QtWidgets.QFileDialog(self.centralwidget)
        self._pBackupMenu = QtWidgets.QMenu(self.centralwidget)
        self._pBackupButton = QtWidgets.QPushButton(self.centralwidget)
        self._pBackupFile = QtWidgets.QAction(self.centralwidget)
        self._pBackupFolder = QtWidgets.QAction(self.centralwidget)
        self._pBackupLabel = QtWidgets.QLabel(self.centralwidget)
        self._pBackupButton.setGeometry(QtCore.QRect(10, 40, 50, 30))
        self._pBackupLabel.setGeometry(QtCore.QRect(65, 40, 465, 30))
        self._pBackupFile.setText("File:")
        self._pBackupFolder.setText("Folder:")
        self._pBackupMenu.addAction(self._pBackupFile)
        self._pBackupMenu.addAction(self._pBackupFolder)
        self._pBackupButton.setMenu(self._pBackupMenu)
        self._pBackupFile.triggered.connect(self._pBackupFileHandle)
        self._pBackupFolder.triggered.connect(self._pBackupFolderHandle)
        self._pBackup.setObjectName("path")

        self._oBackup = QtWidgets.QFileDialog(self.centralwidget)
        self._oBackupButton = QtWidgets.QPushButton(self.centralwidget)
        self._oBackupLabel = QtWidgets.QLabel(self.centralwidget)
        self._oBackupButton.setGeometry(QtCore.QRect(10, 80, 50, 30))
        self._oBackupLabel.setGeometry(QtCore.QRect(65, 80, 465, 30))
        self._oBackupButton.setText("Output:")
        self._oBackup.setObjectName("output")
        self._oBackupButton.clicked.connect(self._oBackupButtonHandle)

        self.submitBackup = QtWidgets.QPushButton(self.centralwidget)
        self.submitBackup.setGeometry(QtCore.QRect(220, 160, 50, 40))
        self.submitBackup.setObjectName("submit")
        self.submitBackup.clicked.connect(self.BackupSystemPrint)

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
        self.setWindowTitle(_translate("MainWindow", "Backup"))
        self._cBackup.setText(_translate("MainWindow", "Compression"))
        self.submitBackup.setText(_translate("MainWindow", "Submit!"))

    def _pBackupFileHandle(self):
        path = self._pBackup.getOpenFileName(self)
        self._pBackupLabel.setText(path[0])
    
    def _pBackupFolderHandle(self):
        path = self._oBackup.getExistingDirectory(self)
        self._pBackupLabel.setText(path)

    def _oBackupButtonHandle(self):
        output = self._oBackup.getExistingDirectory(self)
        self._oBackupLabel.setText(output)

    def BackupSystemPrint(self):
        if self._cBackup.isChecked():
            os.system("python main.py -c -p {} -o {}".format(self._pBackupLabel.text(), self._oBackupLabel.text()))
        else:
            os.system("python main.py -p {} -o {}".format(self._pBackupLabel.text(), self._oBackupLabel.text()))
        self.hide()