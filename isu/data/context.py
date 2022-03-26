
"""Get the main loaded data"""

from pathlib import Path
from PySide6.QtStateMachine import QState, QAbstractState, QStateMachine, QFinalState, QKeyEventTransition
from abc import abstractmethod, abstractproperty, ABC, ABCMeta
import traceback, sys, enum
from isu.ui import UiLoad 
from enum import Enum, auto, unique, Flag
from typing import Literal, Tuple, Optional, List, TypeAlias, Union, Type, Any, Dict, Iterable, overload
from collections.abc import MutableSequence, Sequence, MutableMapping
from collections import ChainMap, deque
from dataclasses import dataclass,  field, asdict, astuple, Field 
from isu.models.demo import Demo, section as sect
from PySide6.QtCore import QAbstractItemModel, QObject, QMetaObject, QMetaMethod, Signal, Slot, QEnum, QAbstractTableModel
from PySide6.QtWidgets import *
from isu import operation
from isu.models import Demo, Audio, Script
from isu.operation import Op
from PySide6.QtCore import QAbstractListModel, QAbstractItemModel, QModelIndex, QItemSelection, QItemSelectionModel, QRunnable
from dataclasses import dataclass

class OpList(QAbstractListModel):
    pass

OpSeq: TypeAlias = MutableSequence[Type[Op]]

# @dataclass
class Context(OpSeq, QRunnable):

    idx: int = 0
    executing: bool = False
    demo_list: List[Demo] = []
    script_list: List[Script] = []
    ops: MutableSequence[Type[Op]] = field(default_factory=list)
    ui: QWidget | None = None

    def __init__(self, idx: Optional[int] = None, ops_rem: OpSeq = [], parent: Any = None) -> None:
        super(OpSeq, self).__init__()
        self.ops: OpSeq = ops_rem
        match idx: 
            case None: self.idx = 0
            case i: self.idx = i
        self.load_ui()

    def load_ui(self) -> None:
        pass
        # loader: UiLoad = UiLoad(name="parent=parent)
        # self.ui = UiLoad.load_ui(parent=self)

    @property
    def operations(self) -> OpSeq:
        return self.ops

    def curr_op(self) -> Type[Op]:
        return self.ops[self.idx]

    def __len__(self):
        return len(self.ops)

    def append(self, op: Type[Op]) -> None:
        self.ops.append(op)

    def __getitem__(self, idx: int) -> Type[Op]:
        return self.ops[idx]

    def __setitem__(self, idx: int, op: Type[Op]) -> None:
        self.ops[idx] = op

    def __popitem__(self) -> Type[Op]:
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
    # ops: OpData = OpData()

    def pop_left(self) -> Type[Op]:
        return self.ops.pop(0)

    def pop(self) -> Type[Op]:
        return self.ops.pop()

    def rm_idx(self, index: int = 0):
        self.ops.__delitem__(index)

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
    
class DemoList(List, QAbstractListModel):

    def __init__(self,  demos: List[Demo] = [], index = 0, parent=None):
        super(DemoList, self).__init__(parent)
        self.index: int = index
        self.demos: List[Demo] = demos

    def __len__(self):
        return len(self.demos)

class ScriptList(List, QAbstractListModel):

    def __init__(self, scripts: List[Script] = [], index = 0, parent=None):
        super(ScriptList, self).__init__(parent)
        self.scripts: List[Script] = []
        self.index: int = index

    def __len__(self):
        return len(self.scripts)
    

    



class OpsSeq(MutableSequence[Op]):
    ops: MutableSequence[Op] = []
    idx: int = 0