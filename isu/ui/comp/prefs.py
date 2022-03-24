import sys, os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List, Dict, Any
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import (Qt, QObject, Slot, Signal, QFile)
from PySide6.QtWidgets import (QMainWindow, QWidget, QDialog, QListWidget, QComboBox, QListWidgetItem, QTreeWidget, QTreeWidgetItem, QApplication)


@dataclass
class Prefs(QDialog):

    def __init__(self, parent: Optional[QMainWindow] = None):
        super(Prefs, self).__init__(parent)
        self.load_ui(parent=parent)

    def load_ui(self, parent: Any):
        uifile = QFile(os.path.dirname(__file__) / Path("prefs.ui"))
        loader = QUiLoader(parent = parent)
        self.ui = loader.load(uifile, parentWidget=parent)
        uifile.close()
        if not self.ui:
            print(f"ERROR LOADING UI FILE: {loader.errorString()}")
            sys.exit(-1)
        else:
            self.ui.show()
        pass

    @Slot()
    def open(self, parent: QWidget|None=None) -> None:
        self.show()



if __name__ == "__main__":

    app = QApplication(sys.argv)
    prefs = Prefs()
    prefs.show()
    app.exec()
