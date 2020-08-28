import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic


class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        path = os.path.join(os.path.dirname(__file__), "main.ui")
        uic.loadUi(path, self)
        

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()