from dataclasses import dataclass
from typing import List, Optional, Tuple
from PySide6.QtCore import QObject, QPointF, QPoint


@dataclass
class Highlight(QObject):
    pos: QPoint = QPoint(0, 0),
    size: QPoint = QPoint(0, 0)

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()
