from dataclasses import dataclass
from ..operation import Op
from isu.models.demo import Demo
from PIL import Image
import os, glob
from typing import Optional, List, Dict, Any, Tuple


@dataclass
class Pace(Op):
    # r1_coord: Tuple[int, int] = (0, 0)
    # r1_dims: Tuple[int, int] = (0, 0)
    # r2_coord: Tuple[int, int] = (0, 0)
    # r2_dims: Tuple[int, int] = (0, 0)

    def __str__(self) -> str:
        return "move"

    def get_params(self) -> Dict[str, Any]:
        return { "": "" }

    def run(self, demo: Demo) -> None:
        super().run(demo)
