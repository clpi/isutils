from dataclasses import dataclass
from ..operation import Op
from isu.models.demo import Demo
from PIL import Image
import os, glob
from typing import Optional, List, Dict, Any, Tuple



@dataclass
class ComposeOp(Op):
    other_path: Optional[str] = None

    def __str__(self) -> str:
        return "compose"

    def get_params(self) -> Dict[str, Any]:
        return { "": "" }

    def run(self, demo: Demo): #TODO add sect discrim fxn
        super().run(demo)
        pass