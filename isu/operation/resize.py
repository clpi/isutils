from dataclasses import dataclass
from ..operation import Op
from isu.models.demo import Demo
from PIL import Image
import os, glob
from typing import Optional, List, Dict, Any, Tuple

@dataclass
class Resize(Op):
    new_dim: Tuple[int, int] = (0, 0)

    def __str__(self) -> str:
        return "resize"

    def get_params(self) -> Dict[str, Any]:
        return { "": "" }

    def run(self, demo: Demo): #TODO add sect discrim fxn
        super().run(demo)
        # self.demo.add_pacing()
        self.finish()
