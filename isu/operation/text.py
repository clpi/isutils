from isu.models.demo import Demo
from dataclasses import dataclass
from ..operation import Op
from isu.models.demo import Demo
from PIL import Image
import os, glob
from typing import Optional, List, Dict, Any, Tuple
import lxml.etree as ET

def sect_test(xml_path: str):
    pass

@dataclass
class Text(Op):
    # section_rules: Optional[List[str]] = None

    def __str__(self) -> str:
        return "section"

    def get_params(self) -> Dict[str, Any]:
        return { "": "" }

    def run(self, demo: Demo): #TODO add sect discrim fxn
        super().run(demo)
        self.start()
        self.finish()
        # section(demo, add_intro_outro=True)