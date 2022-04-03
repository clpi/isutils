from typing import Sequence
from isu.models.step import Step
from PySide6.QtCore import *
from PySide6.QtWidgets import *

class DemoTreeWidget(QTreeWidget):
    def __init__(self, parent = None):
        QTreeWidget(self).__init__(parent)
        self.sections: Sequence[Sequence[Step]] = []
        self.steps = []
        self.parent = parent

    def get_step(self, sect_idx: int, step_idx: int):
        return self.sections[sect_idx][step_idx]

        

class DemoTreeWidgetItem(QTreeWidgetItem):
    def __init__(self, parent = None):
        QTreeWidgetItem(self).__init__(parent)
        self.parent = parent
        self.section_idx: int = 0
        self.stepa_idx: int | None = None
        
    def set_step_idx(self, idx: int):
        self.step_idx = idx

    def set_sect_idx(self, idx: int):
        self.sect_idx = idx