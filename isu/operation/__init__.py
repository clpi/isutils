from ctypes import Union
from typing import Type
from .operation import Op
from .shell import Shell, shell_assets
from .insert import Insert
from .crop import Crop
from .section import Section
from .audio import Audio
from .pace import Pace
from .text import Text
from .render import Render
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import (
    QFile, QDir, QTemporaryDir, QTemporaryFile,
    QRunnable, QUrl,
    QTimer, QTime, QObject, pyqtBoundSignal, pyqtClassInfo, pyqtEnum, pyqtSignal, pyqtSlot)
from enum import Enum
import enum

OP_TYPES = [
    Shell, #0
    Insert, #1
    Section, #2
    Audio, #3
    Crop, #4
    Pace, #5
    Text, #6
    Render, #7
]

def get_op(op_idx: int) -> Type[Op]:
    return OP_TYPES[op_idx]

# def op(parent: QWidget, op_idx: int, demo_idx: int, index: int = 0, ) -> Op:
#     op: Type[Op] = OP_TYPES[op_idx]
#     op(index=index, kind=Op.Type, parent=parent)
#     op()
    

OpType = Shell | Insert | Crop | Section | Audio | Pace | Text | Render

if __name__ == "__main__":
    pass