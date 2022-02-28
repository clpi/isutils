import time, sys, traceback
from contextlib import AbstractContextManager
from enum import Enum, Flag, IntFlag
from dataclasses import dataclass, field
from typing import Sequence
from typing_extensions import Self
from PyQt6.QtCore import (
    QRunnable, pyqtSignal, pyqtSlot, pyqtEnum, QThread, QThreadPool, QObject, QTimer, QTime,
    QObject,
)

class Op(QObject):
    pass

class Data(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(float)


# @pyqtEnum
class Kind(Enum):
    Shell, Insert, Render, Crop, Audio, Section = range(6)
    
# @pyqtEnum
class Status(Flag):
    Completed, Progress, Failed = range(3)

class Job(QRunnable):
    kind: Kind
    demo: str
    data: Data

def __init__(self, kind: Kind, demo: str, *args, **kwargs):
    super(Op, self).__init__()
    self.demo = demo
    self.kind = kind
    self.args = args
    self.kwargs = kwargs
    self.data = Data()

@pyqtSlot()
def run(self):
    print("Op running:")
    try:
        result = print("dok")
    except:
        traceback.print_exc()
        exctype, val = sys.exc_info()[:2]
        self.data.error.emit((exctype, val, traceback.format_exc()))
    else:
        self.data.result.emit(result)
    finally:
        self.data.finished.emit()
        
    print("Op finished")

class OpQueue(QRunnable):

    ops: Sequence[Op]

    def run(self):
        print("Running ops:")
        print("Finished ops:")

