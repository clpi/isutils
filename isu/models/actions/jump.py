from dataclasses import dataclass
from PySide6.QtCore import QObject, pyqtSignal, pyqtEnum
from typing import List, Optional, Tuple


@dataclass
class Jumpbox(QObject):
    """
    Jumpbox model.
    """

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()
