# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backup_app_design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class StartingWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.restore = QtWidgets.QPushButton(self.centralwidget)
        self.restore.setGeometry(QtCore.QRect(620, 350, 100, 100))
        restoreIcon = QtGui.QIcon()
        restoreIcon.addPixmap(QtGui.QPixmap("../icons/restore_f.png"))
        self.restore.setIcon(restoreIcon)
        self.restore.setIconSize(QtCore.QSize(200, 200))
        self.restore.clicked.connect(self.restoreButtonHandle)
        self.backupP = BackupWindow()
        self.restore.setObjectName("restore")

        self.backup = QtWidgets.QPushButton(self.centralwidget)
        self.backup.setGeometry(QtCore.QRect(80, 350, 100, 100))
        backupIcon = QtGui.QIcon()
        backupIcon.addPixmap(QtGui.QPixmap("../icons/backup_f.png"))
        self.backup.setIcon(backupIcon)
        self.backup.setIconSize(QtCore.QSize(200, 200))
        self.backup.clicked.connect(self.backupButtonHandle)
        self.restoreP = RestoreWindow()
        self.backup.setObjectName("backup")

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(150, 20, 500, 362))
        logo = QtGui.QPixmap("../icons/logo.png")
        self.title.setPixmap(logo)
        self.title.setObjectName("title")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Teamwork Backup App"))

    def restoreButtonHandle(self):
        self.backupP.show()

    def backupButtonHandle(self):
        self.restoreP.show()

class BackupWindow(QtWidgets.QMainWindow):
    def setupUI(self, MainWindow):
        pass

class RestoreWindow(QtWidgets.QMainWindow):
    def setupUI(self, MainWindow):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setFixedSize(800, 600)
    ui = StartingWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())