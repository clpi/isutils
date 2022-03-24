from dataclasses import dataclass
from ..operation import Op
from isu.models.demo import Demo
from PIL import Image
import os, glob
from typing import Optional, List, Dict, Any, Tuple



@dataclass
class Crop(Op):
    x: int = 0
    y: int = 0
    height: int = 1920
    width: int = 1080

    def __str__(self) -> str:
        return "crop"

    def get_params(self) -> Dict[str, Any]:
        return { "": "" }

    def run(self, demo: Demo): #TODO add sect discrim fxn
        super(Crop, self).run(demo)
        # self.finish()
