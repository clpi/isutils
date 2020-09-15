"""

"""
from abc import abstractmethod, abstractproperty, ABC, ABCMeta
from enum import Enum, auto
from typing import Tuple, Optional, List, Union, Type, Any, Dict
from dataclasses import dataclass
from models.demo.demo import Demo, section
#from ui.comp.op import OpWidget

SECTION_RULES: list = []
AUDIO_RULES: list = []

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

    def get_params(self) -> Dict[str, Any]:
        pass

@dataclass
class ShellOp(Op):
    img_path: str = ""
    fg_coord: Tuple[int, int] = (0, 0)
    fg_dim: Tuple[int, int] = (0, 0) #TODO set to demo dims on init

    def __str__(self) -> str:
        return "shell"

    #def get_params(self, op_widget: OpWidget) -> Dict[str, Any]:
        #pass

    def run(self, demo: Demo): #TODO add sect discrim fxn
        demo.shell_assets(to_sect=[], bg_path=self.img_path, asset_new_coord=self.fg_coord, asset_new_size=self.fg_dim)


@dataclass
class InsertOp(Op):
    img_path: str = ""
    fg_coord: Tuple[int, int] = (0, 0)
    fg_dim: Tuple[int, int] = (0, 0) #TODO set to demo dims on init

    def __str__(self) -> str:
        return "insert"

    def run(self, demo: Demo): #TODO add sect discrim fxn
        demo.shell_assets(to_sect=[], bg_path=self.img_path, asset_new_coord=self.fg_coord, asset_new_size=self.fg_dim)

    #def from_widget(self, op_widget: OpWidget) -> InsertOp:
        #for i in range(op_widget.topLevelItemCount()):
            #print(i)
        #apply_to = [sect for i in op_widget.applyToTreeWidget.topLevelItemCount()]
        #self.apply_to = op

    def get_params(self) -> Dict[str, Any]:
        pass

@dataclass
class SectionOp(Op):
    section_rules: Optional[List[str]] = None

    def __str__(self) -> str:
        return "section"

    def get_params(self) -> Dict[str, Any]:
        pass

    def run(self, demo: Demo) -> None:
        section(demo, add_intro_outro=True)

@dataclass
class AudioOp(Op):
    audio_rules: Optional[List[str]] = None

    def __str__(self) -> str:
        return "audio"

    def get_params(self) -> Dict[str, Any]:
        pass

    def run(self, demo: Demo) -> None:
        demo.add_audio()

@dataclass
class CropOp(Op):
    dims: Tuple[int, int, int, int] = (0, 0, 0, 0) #TODO set to demo dims 

    def __str__(self) -> str:
        return "crop"

    def get_params(self) -> Dict[str, Any]:
        pass

    def run(self) -> None:
        pass

@dataclass
class ComposeOp(Op):
    other_path: Optional[str] = None

    def __str__(self) -> str:
        return "compose"

    def get_params(self) -> Dict[str, Any]:
        pass

    def run(self) -> None:
        pass

@dataclass
class ResizeOp(Op):
    new_dim: Tuple[int, int] = (0, 0)

    def __str__(self) -> str:
        return "resize"

    def get_params(self) -> Dict[str, Any]:
        pass

    def run(self) -> None:
        pass

@dataclass
class MoveOp(Op):
    r1_coord: Tuple[int, int] = (0, 0)
    r1_dims: Tuple[int, int] = (0, 0)
    r2_coord: Tuple[int, int] = (0, 0)
    r2_dims: Tuple[int, int] = (0, 0)

    def __str__(self) -> str:
        return "move"

    def get_params(self) -> Dict[str, Any]:
        pass

    def run(self) -> None:
        pass

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