import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class GUI(QMainWindow):

    def __init__(self):
        super(GUI, self).__init__()        
        uic.loadUi('backup_app_design.ui', self)
        self.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = GUI()
    sys.exit(app.exec_())
