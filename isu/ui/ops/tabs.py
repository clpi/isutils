from PyQt6.QtGui import ( QTextTable, )
from PyQt6.QtCore import ( 
    Qt, pyqtBoundSignal, pyqtSignal, pyqtSlot, pyqtEnum, pyqtClassInfo
)
from PyQt6.QtWidgets import (
    QWidget, QStackedWidget, QTabBar, QTabWidget, QTableView,
)
from typing import Optional

class OpTabs(QTabWidget):
    new_tab = pyqtSignal()
    ops_stack: QStackedWidget

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.setTabShape(QTabWidget.TabShape.Rounded)
        self.setElideMode(Qt.TextElideMode.ElideRight)
        self.ensurePolished()

    #     self.currentChanged.connect(self.on_current_changed)

    # @pyqtSlot(int)
    # def on_current_changed(idx: int):
    #     pass

    def current(self):
        return self.tabData(self.currentIndex())

    def stack_push(self, q: QWidget):
        self.ops_stack.addWidget(q)

    def __len__(self):
        return len(self.opsParamsStack)
    

    def stack_remove(self, idx: int) -> QWidget:
        w = self.ops_stack.widget(len(self)-1)
        self.ops_stack.removeWidget(w)
        return w

    def stack_pop(self) -> QWidget:
        w = self.stack_remove(len(self)-1)
        return w