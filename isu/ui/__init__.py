"""

"""
from typing import Any, List, NoReturn, TypeVar, Type
from isu.app import MainApp
from isu.ui import Context, OpQueue, DemoList, ScriptList
from isu.ui.ops import OpUi
from .window import MainWindow

import sys, os, pathlib
from dataclasses import dataclass
from pathlib import Path, WindowsPath
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QAction
from PySide6.QtCore import QFile, QDir, Signal, Slot, QCoreApplication, QObject
from PySide6.QtWidgets import QApplication, QFileDialog, QWidget, QMainWindow, QDialog, QLayout

# Widg
class UiLoad(QObject):
    ui_file: QFile
    ui_dir: QDir = QDir(os.path.dirname(__file__))
    parent: Any | None = QCoreApplication.instance()
    uiload: QUiLoader = QUiLoader(parent=parent)
    finished = Signal()
    widget = QWidget()

    def __init__(self,
                 name: str,
                 dir: QDir,
                 parent: Any = QCoreApplication.instance()) -> None:
        """ NOTE: path is relative to <root>/ui """
        super(QObject, self).__init__()
        self.name = name
        self.parent = parent
        self.ui_file = QFile(dir.filePath(name))
        # self.ui_file.open(QFile.OpenModeFlag.ReadOnly)
        self.finished.emit()

    def load_ui(self) -> QWidget:
        self.ldr: QUiLoader = QUiLoader(parent=self.parent)
        widget: QWidget = self.ldr.load(self.ui_file, parentWidget=self.parent)
        if self.ui_file.isOpen():
            self.ui_file.close()
        return widget

    def show_ui(self) -> None:
        try:
            self.widget.show()
        except Exception as e:
            print(f"ERROR: {self.uiload.errorString()} {e}")
            sys.exit(-1)

    def add_widget(self, classname: str, name: str) -> QWidget:
        new_wid: QWidget = self.uiload.createWidget(classname, name=name)
        return new_wid

    def find_child(self, type: type, name: str) -> object:
        return self.uiload.findChild(type=type,name=name)

    def add_action(self, name: str, parent: QObject) -> QAction:
        new_act: QAction = self.uiload.createAction(parent=parent,name=name)
        return new_act

    def open_widgets(self) -> List[str]:
        return self.uiload.availableWidgets()

    def open_layouts(self) -> List[str]:
        return self.uiload.availableLayouts()

    def children(self) -> List[QObject]:
        return self.uiload.children()

    def set_parent(self, parent: Any) -> None:
        self.parent = parent

    def add_layout(self, layout: QLayout, parent: Any):
        pass

    @Slot()
    def new(parent: Any):
        return


def load_ui(widget: QWidget, parent: Any):
    uifile = QFile(os.path.dirname(__file__) / Path("prefs.ui"))
    loader = QUiLoader(parent = parent)
    widget = loader.load(uifile, parentWidget=parent)
    if widget: uifile.close()
    else:
        print(f"ERROR LOADING UI FILE: {loader.errorString()}")
