import os, sys
from typing import Optional
# from tkinter import W
from typing import List, Tuple
from PIL import Image
from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (
    QApplication, QSizePolicy, QWidget, QLabel, QFormLayout, QHBoxLayout,
    QVBoxLayout, QLineEdit, QLayout, QPushButton, QCheckBox, QComboBox, 
    QSpinBox, QStackedLayout, QStackedWidget, QFileDialog
    )
from PyQt6 import uic
from isu.models.demo import Demo
from isu.operation import Crop, Op
from isu.ui.ops.ops import OpUi

class CropOp(OpUi):

    @staticmethod
    def cbidx() -> int:
        return 2

    def __init__(self, index: int, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.index = index
        path = os.path.join(os.path.dirname(__file__), "crop.ui")
        uic.loadUi(path, self)
        self.loadUi()

    def loadUi(self):
        self.cropSpinX: QSpinBox
        self.cropSpinY: QSpinBox
        self.cropSpinW: QSpinBox
        self.cropSpinH: QSpinBox

    def op(self) -> Crop:
        return Crop(
            # apply_to=apply_to, 
            # all_steps=all_steps,
            # demo=demo,
            x=self.cropSpinX.value(),
            y=self.cropSpinY.value(),
            width=self.cropSpinW.value(),
            height=self.cropSpinH.value()
        )
