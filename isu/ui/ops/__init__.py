from PySide6.QtCore import QEnum, QFlag, QMetaEnum, Signal, Slot
from ctypes import Union
from enum import Enum
from typing import List, Type, TypedDict, TypeAlias, NewType
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
OpKind = shell.Shell | insert.Insert | crop.Crop | section.Section | audio.Audio| pace.Pace | text.Text | render.Render

@QEnum
class OpType(Enum, QMetaEnum):
    ShellOp = shell.Shell,
    InsertOp = insert.Insert,
    CropOp = crop.Crop,
    SectionOp = section.Section,
    AudioOp = audio.Audio,
    PaceOp = pace.Pace,
    TextOp = text.Text,
    RenderOp = render.Render,

@staticmethod
def to_ui_type(idx: int = 0) -> Type[OpUi]:
    match idx:
        case 0: return ShellOp
        case 1: return InsertOp
        case 2: return CropOp
        case 3: return SectionOp
        case 4: return AudioOp
        case 5: return PaceOp
        case 6: return TextOp
        case 7: return RenderOp
        case _: return ShellOp

@staticmethod
def to_op_type(idx: int = 0) -> Type[Op]:
    match idx:
        case 0: return shell.Shell
        case 1: return insert.Insert
        case 2: return crop.Crop
        case 3: return section.Section
        case 4: return audio.Audio
        case 5: return pace.Pace
        case 6: return text.Text
        case 7: return render.Render
        case _: return shell.Shell


