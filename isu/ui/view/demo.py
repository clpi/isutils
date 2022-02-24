from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import (
    QMenu
)
from PyQt6.QtGui import (QAction, QWindowStateChangeEvent, QContextMenuEvent)
from PyQt6.QtCore import (
    QAbstractItemModel, QXmlStreamEntityDeclaration, QXmlStreamEntityResolver, QXmlStreamAttribute,
    QDataStream,
)

class DemoView(QtWidgets.QTreeView):
    menu = QMenu

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.initActions()

    def initActions(self):
        self.selectStep = QAction("Select step", self)
        self.selectSect = QAction("Select section", self)
        self.selectAllSects = QAction("Select all", self)
        sep = QAction(self)
        sep.setSeparator(True)
        self.dupeStep = QAction("Duplicate step", self)
        self.dupeSect = QAction("Duplicate section", self)
        self.addActions([self.selectStep, self.selectSect, self.selectAllSects, self.dupeStep, self.dupeSect])
        pass
        

    def contextMenuEvent(self, e: QContextMenuEvent) -> None:
        menu = QMenu(self)
        if e.isInputEvent():
            menu.addActions(iter(self.actions()))
            return super().contextMenuEvent(e)
        menu.exec(e.globalPos())

    def delStep(self):
        pass

        
    def delSect(self):
        pass