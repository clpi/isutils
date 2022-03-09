from typing import Optional
from PyQt6.QtWidgets import QWidget
from isu.models import Demo
from isu.operation import Op


class OpUi(QWidget):

    @staticmethod
    def cbidx() -> int:
        return -1

    def __init__(self, parent: Optional[QWidget] = None, index: int = 0):
        super().__init__(parent)
        self.index = index
        self.initUi()

    def initUi(self):
        pass

    def op(self) -> Op:
        pass

    def run(self, demo: Demo):
        pass
        
