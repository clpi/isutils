"""

"""
from pathlib import Path
from abc import abstractmethod, abstractproperty, ABC, ABCMeta
import traceback, sys, enum
from enum import Enum, auto
from typing import Literal, Tuple, Optional, List, Union, Type, Any, Dict, Sequence, MutableSequence, Iterable, overload
from dataclasses import dataclass
from isu.models.demo import Demo, section as sect
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from isu import operation

from isu.models.section import Section
#from ui.comp.op import OpWidget

SECTION_RULES: list = []
AUDIO_RULES: list = []

class Op(QObject):

    class Status(enum.Enum):
        Done = auto()
        Failed = auto()
        InProgress= auto()
        Queued = auto()
        Canceled = auto()

        def done(self) -> bool:
            return self in [Op.Status.Done, Op.Status.Failed, Op.Status.Canceled]

    def __del__(self):
        self.wait()

    class Type(enum.Enum):
        Shell, Insert,  Crop, Audio, Section, Pace, Text , Render, Test = range(9)

    status = pyqtSignal(Status)
    prog = pyqtSignal(int)
    qmsg = pyqtSignal(str)

    def __init__(self, p: QWidget) -> None:    
        super().__init__(p)
        # self.kind = kind
        self.qmsg.emit(f"Initializing {self}")
        self.progress: int = 0

    def started(self) -> None:
        # self.timer.singleShot(0, self.run)
        self.status.emit(Op.Status.InProgress)
        print("[.operation.Op.run] RUNNING " + str(self))

    def updated(self, i: int) -> None:
        if i < 100:
            self.prog.emit(i)
        else:
            self.prog.emit(100)
            self.finished()
            
    def canceled(self) -> None:
        self.status.emit(Op.Status.Canceled)
        self.prog.emit(100)

    def finished(self) -> None:
        self.status.emit(Op.Status.Done)
        self.prog.emit(100)

    @pyqtSlot()
    def run(self, demo: Demo) -> None:
        self.started()
        print("    DEMO: " + str(demo.title))

        

# class OpQueue(QRunnable):
#     ops: List[Tuple[Type[Op], int]]

#     def __init__(self, demos: List[int] = [], ops: Sequence[Type[Op]] = [])  -> None:
#         super(QRunnable, self).__init__()
#         self.ops: List[Tuple[Type[Op], int]] = []
#         for i, o in enumerate(ops):
#             self.ops.append((o, demos[i]))

#     @pyqtSlot()
#     def run(self):
#         for op, demo in self.ops:
#             op()

@pyqtSlot()
def run(self, demo: Demo):
    print("Op running:")
    # try:
    #     result = print("dok")
    # except:
    #     traceback.print_exc()
    #     exctype, val = sys.exc_info()[:2]
    #     self.data.error.emit((exctype, val, traceback.format_exc()))
    # else:
    #     self.data.result.emit(result)
    # finally:
    #     self.data.finished.emit()
        
    # print("Op finished")



# class Op(QObject):
#     qstatus = pyqtSignal(Op.Status)
#     qkind   = pyqtSignal(Op.Type)
#     qerror = pyqtSignal(tuple)
#     qresult = pyqtSignal(object)
#     qprog = pyqtSignal(float)
#     qmsg    = pyqtSignal(str)

#     class Type(enum.Enum):
#         Shell, Insert,  Crop, Audio, Section, Pace, Text , Render = range(8)

#     def __init__(self, 
#                  index: int = 0, 
#                  kind: Op.Type = Op.Type.Shell, 
#                  demo: Demo = Demo(), 
#                  parent: QObject = None) -> None:    
#         super().__init__(parent)
#         self.status = Op.Status.Queued
#         self.kind = kind
#         self.msg  = "queued"
#         self.index = index
#         self.timer = QTimer(self)
#         self.progress: int = 0

#     def get_params(self):
#         return {}
        

#     @pyqtSlot()
#     def start(self) -> None:
#         self.status = Op.Status.InProgress
#         self.progress.emit(0.0)
#         # self.timer.singleShot(0, self.run)
#         self.qstatus.emit(self.status) 

#     @pyqtSlot()
#     def progress(self) -> None:
#         self.qprog.emit(self.progress) 

#     @pyqtSlot()
#     def cancel(self) -> None:
#         self.status = Op.Status.Cancelled
#         self.qstatus.emit(self.status)

#     @pyqtSlot()
#     def finish(self) -> None:
#         self.status = Op.Status.Completed
#         self.qstatus.emit(self.status)

#     def run(self) -> None:
#         pass
        

# class Job(QRunnable):
#     demo_idx: int
#     kind: Op.Type

#     def __init__(self, kind: Op.Type, demo: str, *args, **kwargs):
#         super(Op, self).__init__()
#         self.demo = demo
#         self.kind = kind
#         self.args = args
#         self.kwargs = kwargs

#     @pyqtSlot()
#     def run(self):
#         print("Op running:")
#         try:
#             result = print("dok")
#         except:
#             traceback.print_exc()
#             exctype, val = sys.exc_info()[:2]
#             self.data.error.emit((exctype, val, traceback.format_exc()))
#         else:
#             self.data.result.emit(result)
#         finally:
#             self.data.finished.emit()
            
#         print("Op finished")

# class OpQueue(QRunnable):

#     ops: Sequence[Op]

#     apply_to: Optional[List[int]] = None
#     all_steps: bool = False
#     steps_with: bool = False
#     step_substr: Optional[str] = None
#     demo: Optional[Demo] = None

#     def __init__(self, demo: Demo, **kwargs):
#         self.demo = demo

#     def set_demo(self, demo: Demo):
#         self.demo = demo

#     def has_demo(self) -> bool:
#         return self.demo is not None

#     def add_step(self):
#         pass

#     def add_sect(self):
#         pass

#     def get_params(self) -> Dict[str, Any]:
#         return { "": "" }

#     def run(self):
#         print("Running ops:")
#         if d := self.demo:
#             d.add_audio()
#         print("Finished ops:")

# class OpData:

#     def __init__(self):
#         self.apply_to: Optional[List[int]] = None
#         self.all_steps: Optional[bool] = None
#         self.steps_with: Optional[bool] = None
#         self.step_substr: Optional[str] = None

# class Ops(Sequence[Op]):
#     ops: Sequence[Op] = []
#     idx: int = 0

#     def __init__(self, idx: Optional[int] = None, ops: Sequence[Op] = []) -> None:
#         super().__init__()
#         self.ops = ops
#         if idx: self.idx = idx 
#         else: self.idx = 0

#     def __getattribute__(self, __name: str) -> Any:
#         return super().__getattribute__(__name)

#     def __getitem__(self, idx: int) -> Op: # type: ignore[override]
#         self.idx = idx
#         return self.ops[idx]

#     @property
#     def operations(self) -> Sequence[Op]:
#         return self.ops

#     def currrent(self) -> Op:
#         return self.ops[self.idx]

#     def __len__(self) -> int:
#         return len(self.ops)

class Test(Op):
    def run(self) -> None:
        return super().run()
        print("RUNNING TEST")