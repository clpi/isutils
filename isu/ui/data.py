"""Get the main loaded data"""

from pathlib import Path
from abc import abstractmethod, abstractproperty, ABC, ABCMeta
from this import d
import traceback, sys, enum
from enum import Enum, auto
from typing import Literal, Tuple, Optional, List, Union, Type, Any, Dict, Sequence, MutableSequence, Iterable, overload
from dataclasses import dataclass,  field
from isu.models.demo import Demo, section as sect
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from isu import operation
import enum
import pathlib
from isu.models import Demo, Audio, Script
from isu.operation import Op
from PySide6.QtCore import *
from dataclasses import dataclass

class OpList(QAbstractListModel):
    pass

@dataclass()
class OpQueue(MutableSequence, QRunnable):
    ops: MutableSequence[Type[Op]] = field(default_factory=list)
    # TODO: these should all be on a step by step basis
    # apply_to: Optional[List[int]] = None
    # all_steps: bool = False
    # steps_with: bool = False
    # step_substr: Optional[str] = None
    # demo: Optional[Demo] = None

    def __len__(self):
        return len(self.ops)

    def append(self, op: Type[Op]) -> None:
        self.ops.append(op)

    def __getitem__(self, idx: int) -> Type[Op]:
        return self.ops[idx]

    def __setitem__(self, idx: int, op: Type[Op]) -> None:
        self.ops[idx] = op

    def pop(self) -> Type[Op]:
        return self.ops.pop()

    def get_op(self, idx: int) -> Type[Op]: # type: ignore[override]
        return self.ops[idx]

    def set_op(self, idx: int, op: Type[Op]) -> Any:
        self.ops[idx] = op

    def set_demo(self, demo: Demo):
        self.demo = demo

    def has_demo(self) -> bool:
        return self.demo is not None

        ## TODO: Note that data should be assed to ops on execution,
        #        so adding a certain type by function should need only
        #        specification on the order of the function uniqueness,
        #        not need for the type to be passed in as well.

    @Slot(operation.Shell)
    def add_shell(self):
        pass

    @Slot(operation.Insert)
    def add_insert(self):
        pass

    @Slot(operation.Crop)
    def add_crop(self):
        pass

    @Slot(operation.Pace)
    def add_pacing(self):
        pass

    @Slot(operation.Text)
    def add_text(self):
        pass

    @Slot(operation.Render)
    def add_render(self):
        pass

    @Slot(operation.Section)
    def add_sect(self):
        pass

    def run(self):
        print("Running ops:")
        if d := self.demo:
            d.add_audio()
        print("Finished ops:")

@dataclass
class Context(QObject):
    executing: bool = False

    class Ops(QRunnable):
        """
        Class containing globally necessary data to perfrom the core functionality of the app,
        the various available operations, on demos loaded into memory.
        Args:
            QRunnable (_type_): _description_
        """
        
    #     class Asset(QObject, enum.Enum):
    #         DemoPath: pathlib.Path 
    #         ScriptPath: pathlib.Path
    #         AudioPath: pathlib.Path

    # # op: Ops.Assets.DemoPath | Ops.Assets.ScriptPath| Ops.Assets.AudioPath
    # LoadType = Demo | Script | Audio

    @dataclass()
    class Load(QObject):
        script: List[Script] =field(default_factory=list)
        demo: List[Demo] = field(default_factory=list)
        audio: List[Audio] =field(default_factory=list)

        def get_demo_list_items(self) -> List[str]:
            out: List[str] = []
            for demo in self.demo:
                out.append(demo.title)
            return out

    load: Load = Load()
    ops: OpQueue = OpQueue()

    def pop_left(self) -> Type[Op]:
        return self.ops.ops.pop(0)

    def pop(self) -> Type[Op]:
        return self.ops.ops.pop()

    def rm_idx(self, index: int = 0):
        self.ops.ops.__delitem__(index)

    def demo_list_titles(self) -> List[str]:
        return [title.title for title in self.load.demo]

class DataTable(QAbstractTableModel):
    def __init__(self, data, parent=None):
        super(DataTable, self).__init__(parent)
        self.dataee = data

    def rowCount(self):
        return len(self.dataee)

    def columnCount(self):
        return len(self.dataee[0])

    # def data(self, index, role=Qt.DisplayRole):
    #     if index.isValid() and role == Qt.DisplayRole:
    #         return self.datae[index.row()][index.column()]
    #     return None

    # def headerData(self, section, orientation, role=Qt.DisplayRole):
    #     if role == Qt.DisplayRole:
    #         if orientation == Qt.Horizontal:
    #             return self.datae[0][section]
    #         else:
    #             return self.datae[section][0]
    #     return None
    
class DemoList(list, QAbstractListModel):
    def __init__(self, data, parent=None):
        super(DemoList, self).__init__(parent)
        self.datae = data

    def rowCount(self, parent=QModelIndex()):
        return len(self.datae)

    # def data(self, index, role=Qt.DisplayRole):
    #     if index.isValid() and role == Qt.DisplayRole:
    #         return self.datae[index.row()]
    #     return None

    # def headerData(self, section, orientation, role=Qt.DisplayRole):
    #     if role == Qt.DisplayRole:
    #         if orientation == Qt.Horizontal:
    #             return self.datae[0][section]
    #         else:
    #             return self.datae[section][0]
    #     return None

class ScriptList(list, QAbstractListModel):
    def __init__(self, data, parent=None):
        super(ScriptList, self).__init__(parent)
        self.datae = data

    def rowCount(self, parent=QModelIndex()):
        return len(self.datae)

    # def data(self, index, role=Qt.DisplayRole):
    #     if index.isValid() and role == Qt.DisplayRole:
    #         return self.datae[index.row()]
    #     return None

    # def headerData(self, section, orientation, role=Qt.DisplayRole):
    #     if role == Qt.DisplayRole:
    #         if orientation == Qt.Horizontal:
    #             return self.datae[0][section]
    #         else:
    #             return self.datae[section][0]
    #     return None
    

    

class OpData:

    def __init__(self):
        self.apply_to: Optional[List[int]] = None
        self.all_steps: Optional[bool] = None
        self.steps_with: Optional[bool] = None
        self.step_substr: Optional[str] = None

class Ops(Sequence[Op]):
    ops: Sequence[Op] = []
    idx: int = 0

    def __init__(self, idx: Optional[int] = None, ops: Sequence[Op] = []) -> None:
        super().__init__()
        self.ops = ops
        if idx: self.idx = idx 
        else: self.idx = 0



    @property
    def operations(self) -> Sequence[Op]:
        return self.ops

    def currrent(self) -> Op:
        return self.ops[self.idx]

    def __len__(self) -> int:
        return len(self.ops)
