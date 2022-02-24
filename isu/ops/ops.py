import time, sys, traceback
import enum
from typing import Sequence
from PyQt6.QtCore import (
    QRunnable, pyqtSignal, pyqtSlot, pyqtEnum, QThread, QThreadPool, QObject, QTimer, QTime
)

class OpKind(enum.IntEnum):
    SHELL = 0,
    INSERT = 1,
    RENDER = 2,
    CROP = 3,
    AUDIO = 4,
    SECTION = 5,
    

class OpData(QObject):

    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(float)

class Op(QRunnable):
    kind: OpKind
    demo: str
    data: OpData

    def __init__(self, kind: OpKind, demo: str, *args, **kwargs):
        super(Op, self).__init__()
        self.demo = demo
        self.kind = kind
        self.args = args
        self.kwargs = kwargs
        self.data = OpData()

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
