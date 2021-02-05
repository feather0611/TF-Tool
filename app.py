# coding: utf-8
import sys
from PyQt5.QtWidgets import *
from ui import Ui_MainWindow
import checkPackage


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if(checkPackage.preCheck()!=0):
	print("Error in import package!")
	sys.exit(0)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())