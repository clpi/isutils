from dataclasses import dataclass
from typing import Tuple, List
from PyQt5.QtWidgets import QListWidgetItem

class OpType:
    def __init__(self):
        print("")

class Operation:

    op_type: OpType
    current: bool
    index: int

    def __init__(self, op_type: OpType, steps: List[str]):
        print("DF")

OP_TYPES = {
    "shell": {
        "path": str,
    },
    "insert": {
        "path": str,
    },
    "crop": {
    },
    "resize": {
        
    },
    "section": {

    },
    "audio": {

    },
}

@dataclass
class Insert(OpType):
    img_path: str
    fg_coords: Tuple[int, int]
    fg_dims: Tuple[int, int]

@dataclass
class Shell(OpType):
    img_path: str
    fg_coords: Tuple[int, int]
    fg_dims: Tuple[int, int]

@dataclass
class Audio(OpType):
    img_path: str
    fg_coords: Tuple[int, int]
    fg_dims: Tuple[int, int]
