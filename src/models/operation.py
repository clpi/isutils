from abc import abstractmethod, abstractproperty, ABC, ABCMeta
from enum import Enum, auto
from typing import Tuple, Optional, List
from dataclasses import dataclass

class OpKind(Enum):
    Shell = auto()
    Insert = auto()
    Section = auto()
    Audio = auto()
    Crop = auto()

@dataclass
class Op:

    apply_to: Optional[List[int]]

    #@abstractmethod
    def add_step(self):
        pass

    #@abstractmethod
    def add_section(self):
        pass

@dataclass
class ShellOp(Op):
    img_path: str
    fg_coord: Tuple[int, int]
    fg_dim: Tuple[int, int]

@dataclass
class InsertOp(Op):
    img_path: str
    fg_coord: Tuple[int, int]
    fg_dim: Tuple[int, int]

@dataclass
class SectionOp(Op):
    dummy: Optional[str]

@dataclass
class AudioOp(Op):
    dummy: Optional[str]

@dataclass
class CropOp(Op):
    dims: Tuple[int, int, int, int]

if __name__ == "__main__":
    pass
