# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from backup import BackupWindow
from restore import RestoreWindow

class StartingWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        
    def setupUi(self):
        """
        Prepares 
        """

        self.setObjectName("StartingWindow")
        self.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")

        self.restore = QtWidgets.QPushButton(self.centralwidget)
        self.restore.setGeometry(QtCore.QRect(620, 350, 100, 100))
        restoreIcon = QtGui.QIcon()
        restoreIcon.addPixmap(QtGui.QPixmap("icons/restore_f.png"))
        self.restore.setIcon(restoreIcon)
        self.restore.setIconSize(QtCore.QSize(200, 200))
        self.restore.clicked.connect(self.restoreButtonHandle)
        self.restore.setObjectName("restore")

        self.backup = QtWidgets.QPushButton(self.centralwidget)
        self.backup.setGeometry(QtCore.QRect(80, 350, 100, 100))
        backupIcon = QtGui.QIcon()
        backupIcon.addPixmap(QtGui.QPixmap("icons/backup_f.png"))
        self.backup.setIcon(backupIcon)
        self.backup.setIconSize(QtCore.QSize(200, 200))
        self.backup.clicked.connect(self.backupButtonHandle)
        self.backup.setObjectName("backup")

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(150, 20, 500, 362))
        logo = QtGui.QPixmap("icons/logo.png")
        self.title.setPixmap(logo)
        self.title.setObjectName("title")

        self.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Teamwork Backup App"))

    def backupButtonHandle(self):
        self.backupW = BackupWindow()
        self.backupW.setupUi()
        self.backupW.show()

    def restoreButtonHandle(self):
        self.restoreW = RestoreWindow()
        self.restoreW.setupUi()
        self.restoreW.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = StartingWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
