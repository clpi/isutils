from typing import Optional, Type, Any
from dataclasses import dataclass
from isu.ui.ops.tab import TabOp
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Signal, QEnum
from isu.models import Demo
from isu.operation import Op
from isu.ui import UiLoad, UiState
from isu.ui.ops import OpType, OpUi, to_op_type, to_ui_type

@dataclass
class OpUi(QWidget):
    """
    """
    op_idx: int = 0   # NOTE: corresponds to index of this op in the list of available op types
    step_idx: int = 0 # NOTE: corresponds to index of this op in sequennce of ops pending exec.
    demo_idx: int = 0 # NOTE: corresponds to the demo index selected as the target for this op

    def load_ui(self, parent: Any):
        pass

    @Slot(int)
    def to_op(self) -> Op:
        opty: Type[Op] = to_op_type(self.op_idx)
        return opty(parent=self)

    @Slot(int)
    def get_demo(self, index: int) -> Demo:

        return Demo()

    

    # def __init__(self, *args: Any, **kwds: Any) -> Any:
    #     self.to_op(self.op_idx)
    #     return super(OpUi, self).__init__(*args, **kwds)

    @Slot(int)
    def set_op_idx(self, index: int):
        self.op_idx = index

    @Slot(int)
    def set_step_idx(self, index: int):
        self.step_idx = index

    @Slot(int)
    def set_demo_idx(self, index: int):
        self.demo_idx = index




    def __init__(self, parent: Any, index: int = 0):
        super(OpUi, self).__init__(parent=parent)
        self.index = index
        self.init_ui(parent)

    def init_ui(self, parent: Any):
        pass

    def op(self, index: int) -> Op:
        return to_op_type(index, parent=self.parent)()

    def run(self, demo: Demo):
        pass
        
