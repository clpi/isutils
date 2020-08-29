from typing import Tuple, Optional, List
from dataclasses import dataclass

@dataclass
class Op:
    apply_to: Optional[List[int]]

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