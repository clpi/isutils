from ctypes import Union
from typing import List, Type
from isu.operation.audio import Audio
from isu.models.demo import Demo
from isu.ui.ops.ops import OpUi
from .audio import AudioOp

from .crop import CropOp
from .insert import InsertOp
from .pace import PaceOp
from .render import RenderOp
from .section import SectionOp
from .shell import ShellOp
from .text import TextOp
from isu.operation import Op

OpUiKind = ShellOp | InsertOp | CropOp | SectionOp | AudioOp | PaceOp | TextOp | RenderOp

OP_UI_TYPES: List[Type[OpUi]] = [
    ShellOp,
    InsertOp,
    CropOp,
    SectionOp,
    AudioOp,
    PaceOp,
    TextOp,
    RenderOp,
]
