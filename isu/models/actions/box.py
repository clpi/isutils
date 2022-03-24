from dataclasses import dataclass
from typing import List, Optional, Tuple
from PyQt6.QtCore import QObject


@dataclass
class Box(QObject):
    def __init__(self, parent=None):
        super(Box, self).__init__(parent)
        self.__name = ''
        self.__description = ''
