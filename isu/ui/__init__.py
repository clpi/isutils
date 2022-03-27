"""

"""
from importlib import import_module
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
class UiLoad(QUiLoader):
    # ui_file: QFile
    # ui_dir: QDir = QDir(os.path.dirname(__file__))
    # parent: Any | None = QCoreApplication.instance()
    # uiload: QUiLoader = QUiLoader(parent=parent)
    # finished = Signal()
    # widget = QWidget()
    name: str
    parent: Any
    ui_file: QFile
    ui_widget: Any

    def __init__(self,
                 name: str,
                 dir: QDir,
                 parent: Any = QCoreApplication.instance()) -> None:
        """ NOTE: path is relative to <root>/ui """
        QUiLoader.__init__(self)
        # self.widget = self.createWidget()
        self.name = name
        self.parent = parent
        self.ui_file = QFile(dir.filePath(name))
        # self.ui_file.open(QFile.OpenModeFlag.ReadOnly)
        # self.finished.emit()

    def load_ui(self) -> Any:
        self.ldr: QUiLoader = QUiLoader(parent=self.parent)
        self.ui_widget = self.ldr.load(self.ui_file, parentWidget=self.parent)
        if self.ui_file.isOpen():
            self.ui_file.close()
        return self.ui_widget

    def show_ui(self) -> None:
        try:
            self.ui_widget.show()
        except Exception as e:
            print(f"ERROR: {self.errorString()} {e}")
            sys.exit(-1)

    def add_widget(self, classname: str, name: str) -> QWidget:
        new_wid: QWidget = self.createWidget(classname, name=name)
        return new_wid

    def find_child(self, type: type, name: str) -> object:
        return self.findChild(type=type,name=name)

    def add_action(self, name: str, parent: QObject) -> QAction:
        new_act: QAction = self.createAction(parent=parent,name=name)
        return new_act

    def open_widgets(self) -> List[str]:
        return self.availableWidgets()

    def open_layouts(self) -> List[str]:
        return self.availableLayouts()

    def children(self) -> List[QObject]:
        return self.children()

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
