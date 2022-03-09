from dataclasses import dataclass
from isu.operation import Op

from isu.models.demo import Demo
from PIL import Image
import os, glob
from typing import Optional, List, Dict, Any, Tuple


@dataclass
class Insert(Op):
    img_path: str = ""
    x: int = 0
    y: int = 0
    w: int = 1920
    h: int = 1080

    def __str__(self) -> str:
        return "insert"

    def run(self, demo: Demo): #TODO add sect discrim fxn
        # super().run(demo)
        self.started()
        self.finished()

    #def from_widget(self, op_widget: OpWidget) -> InsertOp:
        #for i in range(op_widget.topLevelItemCount()):
            #print(i)
        #apply_to = [sect for i in op_widget.applyToTreeWidget.topLevelItemCount()]
        #self.apply_to = op

    def get_params(self) -> Dict[str, Any]:
        return { "": "" }
