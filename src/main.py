from window import IscApp

import sys
from PyQt5 import (uic, QApplication)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = IscApp()
    win.show()
    app.exec_()
