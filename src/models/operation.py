"""

"""
from abc import abstractmethod, abstractproperty, ABC, ABCMeta
from enum import Enum, auto
from typing import Tuple, Optional, List, Union, Type
from dataclasses import dataclass

SECTION_RULES = []
AUDIO_RULES = []

class OpKind(Enum):
    Shell = auto()
    Insert = auto()
    Section = auto()
    Audio = auto()
    Crop = auto()


@dataclass
class Op:
    apply_to: Optional[List[int]] = None
    all_steps: bool = False
    steps_with: bool = False
    step_substr: Optional[str] = None

    def add_step(self):
        pass

    def add_sect(self):
        pass

@dataclass
class ShellOp(Op):
    img_path: str = ""
    fg_coord: Tuple[int, int] = (0, 0)
    fg_dim: Tuple[int, int] = (0, 0) #TODO set to demo dims on init

@dataclass
class InsertOp(Op):
    img_path: str = ""
    fg_coord: Tuple[int, int] = (0, 0)
    fg_dim: Tuple[int, int] = (0, 0) #TODO set to demo dims on init

@dataclass
class SectionOp(Op):
    section_rules: Optional[List[str]] = None

@dataclass
class AudioOp(Op):
    audio_rules: Optional[List[str]] = None

@dataclass
class CropOp(Op):
    dims: Tuple[int, int, int, int] = (0, 0, 0, 0) #TODO set to demo dims 

@dataclass
class ComposeOp(Op):
    other_path: Optional[str] = None

@dataclass
class ResizeOp(Op):
    new_dim: Tuple[int, int] = (0, 0)

@dataclass
class MoveOp(Op):
    r1_coord: Tuple[int, int] = (0, 0)
    r1_dims: Tuple[int, int] = (0, 0)
    r2_coord: Tuple[int, int] = (0, 0)
    r2_dims: Tuple[int, int] = (0, 0)

class OpData:

    def __init__(self):
        self.apply_to: Optional[List[int]] = None
        self.all_steps: bool = None
        self.steps_with: bool = None
        self.step_substr: Optional[str] = None

OP_TYPES = [
    ShellOp,
    InsertOp,
    SectionOp, 
    AudioOp,
    CropOp,
    ComposeOp,
    ResizeOp,
    MoveOp,
]

def get_op(op_idx: int) -> Type[Op]:
    return OP_TYPES[op_idx]

if __name__ == "__main__":
    pass