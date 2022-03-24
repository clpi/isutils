from dataclasses import dataclass
from typing import List, Optional, Tuple
from PySide6.QtCore import QObject

@dataclass
class Textbox(QObject):
    """
    Textbox model.
    """
    super(QObject).__init__()
    pos: Tuple[int, int] = (0, 0)
    size: Tuple[int, int] = (0, 0)
