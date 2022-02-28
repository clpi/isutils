"""

"""
from pathlib import Path
from abc import abstractmethod, abstractproperty, ABC, ABCMeta
from enum import Enum, auto
from typing import Tuple, Optional, List, Union, Type, Any, Dict, Sequence, MutableSequence, Iterable
from dataclasses import dataclass
from isu.models.demo import Demo, section
#from ui.comp.op import OpWidget

SECTION_RULES: list = []
AUDIO_RULES: list = []

class OpKind(Enum):
    Shell = auto()
    Insert = auto()
    Section = auto()
    Audio = auto()
    Crop = auto()
    Render = auto()


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
        return { "": "" }

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
        demo.insert_img(to_sect=[], fg_img_path=self.img_path, fg_img_coord=self.fg_coord, fg_img_size=self.fg_dim)

    #def from_widget(self, op_widget: OpWidget) -> InsertOp:
        #for i in range(op_widget.topLevelItemCount()):
            #print(i)
        #apply_to = [sect for i in op_widget.applyToTreeWidget.topLevelItemCount()]
        #self.apply_to = op

    def get_params(self) -> Dict[str, Any]:
        return { "": "" }

@dataclass
class SectionOp(Op):
    section_rules: Optional[List[str]] = None

    def __str__(self) -> str:
        return "section"

    def get_params(self) -> Dict[str, Any]:
        return { "": "" }

    def run(self, demo: Demo) -> None:
        section(demo, add_intro_outro=True)

@dataclass
class AudioOp(Op):
    audio_rules: Optional[List[str]] = None

    def __str__(self) -> str:
        return "audio"

    def get_params(self) -> Dict[str, Any]:
        return { "": "" }

    def run(self, demo: Demo) -> None:
        demo.add_audio()

@dataclass
class CropOp(Op):
    dims: Tuple[int, int, int, int] = (0, 0, 0, 0) #TODO set to demo dims

    def __str__(self) -> str:
        return "crop"

    def get_params(self) -> Dict[str, Any]:
        return { "": "" }

    def run(self) -> None:
        pass

@dataclass
class ComposeOp(Op):
    other_path: Optional[str] = None

    def __str__(self) -> str:
        return "compose"

    def get_params(self) -> Dict[str, Any]:
        return { "": "" }

    def run(self) -> None:
        pass

@dataclass
class ResizeOp(Op):
    new_dim: Tuple[int, int] = (0, 0)

    def __str__(self) -> str:
        return "resize"

    def get_params(self) -> Dict[str, Any]:
        return { "": "" }

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
        return { "": "" }

    def run(self) -> None:
        pass

@dataclass
class AnimateOp(Op):

    def __str__(self) -> str:
        return "rename"

    def get_params(self) -> Dict[str, Any]:
        return { "": "" }

    def run(self) -> None:
        pass

@dataclass
class PacingOp(Op):

    def __str__(self) -> str:
        return "pacing"

    def get_params(self) -> Dict[str, Any]:
        return { "": "" }

    def run(self) -> None:
        pass

@dataclass
class RenderOp(Op):

    out_path: Path = Path("C:\\Users\\chris\\Documents\\out.avi")

    def __str__(self) -> str:
        return "render"

    def get_params(self) -> Dict[str, Any]:
        return { "": "" }

    def run(self, demo: Demo) -> None:
        print("[RenderOp.run] RUNNING RENDER OP on " + demo.title)
        demo.render_video(out_path=self.out_path)

class OpData:

    def __init__(self):
        self.apply_to: Optional[List[int]] = None
        self.all_steps: Optional[bool] = None
        self.steps_with: Optional[bool] = None
        self.step_substr: Optional[str] = None

OP_TYPES = [
    ShellOp, #0
    InsertOp, #1
    SectionOp, #2
    AudioOp, #3
    CropOp, #4
    ComposeOp, #5
    ResizeOp, #6
    PacingOp, #7
    AnimateOp, #8
    RenderOp, #9
]

def get_op(op_idx: int) -> Type[Op]:
    return OP_TYPES[op_idx]

if __name__ == "__main__":
    pass
