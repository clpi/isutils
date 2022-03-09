import lxml.etree as ET
from typing import Optional, List, Dict, Any, Tuple
from PyQt6.QtCore import *
from dataclasses import dataclass
from ..operation import Op
from isu.models.demo import Demo
from PIL import Image
import os, glob

def sect_test(xml_path: str):
    pass

@dataclass
class Section(Op):
    section_rules: Optional[List[str]] = None

    status = pyqtSignal(Op.Status)
    prog = pyqtSignal(int)
    qmsg = pyqtSignal(str)

    def __str__(self) -> str:
        return "section"

    def get_params(self) -> Dict[str, Any]:
        return { "": "" }

    def run(self, demo: Demo): #TODO add sect discrim fxn
        self.started()
        self.finished()
        # self.demo.section_demo()