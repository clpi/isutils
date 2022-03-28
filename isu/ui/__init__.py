from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDir, Signal, Slot, QCoreApplication, QObject, QMetaObject
from PySide6.QtWidgets import QApplication, QFileDialog, QWidget, QMainWindow, QDialog, QLayout
from pathlib import Path

class UiLoad(QUiLoader):

    def loadUi(self, uifile: str, baseinstance=None, parent=None) -> QWidget:
        self._baseinstance = baseinstance
        widget = self.load(uifile, parentWidget=parent)
        QMetaObject.connectSlotsByName(widget)
        return widget

    def createWidget(self, classname: str, parent=None, name=''):
        if parent is None and self._baseinstance is not None:
            widget = self._baseinstance
        else:
            widget = super(UiLoad, self).createWidget(classname, parent, name)
            if self._baseinstance is not None:
                setattr(self._baseinstance, name, widget)
        return widget