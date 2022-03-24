from dataclasses import dataclass
from ..operation import Op
from isu.models.demo import Demo
from PIL import Image
import os, glob
from typing import Optional, List, Dict, Any, Tuple
from PyQt6.QtCore import *

@dataclass
class Audio(Op):
    audio_rules: Optional[List[str]] = None
    qprog = pyqtSignal(int)

    def __str__(self) -> str:
        return "audio"

    def get_params(self) -> Dict[str, Any]:
        return { "": "" }

    def run(self, demo: Demo): #TODO add sect discrim fxn
        super().run(demo)
        # self.demo.add_audio()
        # self.start()
        # self.finish()
            
