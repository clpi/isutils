from dataclasses import dataclass
from typing import List, Optional, Tuple
from PySide6.QtCore import (
    QObject, pyqtSignal, pyqtEnum, QPoint, QPointF, QSize, QSizeF,
    QRect, QRectF, QBuffer
)
from PySide6.QtGui import (
    QFont, QFontDatabase, QFontInfo, QColorConstants, QColor
)



@dataclass
class Textbox(QObject):
    """
    Textbox model.
    """
    super(QObject).__init__()
    pos: QPoint = QPoint(0, 0),
    size: QSize = QSize(0, 0)
    color: QColor = QColor(0, 0, 0, 255.0)
    font: QFont = QFont("Arial", pointSize=11, weight=1, italic=False)
    text: str = ""


class TextColor(QObject):
    """
    Text color class.
    """
    __slots__ = ('_color', '_name')

    def __init__(self, color: Tuple[int, int, int], name: str):
        super().__init__()
        self._color = color
        self._name = name

    @property
    def color(self) -> Tuple[int, int, int]:
        return self._color

    @property
    def name(self) -> str:
        """
        Get the name.
        """
        return self._name

    def __repr__(self) -> str:
        return f'<TextColor: {self._name}>'

