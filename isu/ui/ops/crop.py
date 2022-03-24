import os, sys
from typing import Optional, Any, Tuple, List
from PIL import Image
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QDir, QFile,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (
    QApplication, QSizePolicy, QWidget, QLabel, QFormLayout, QHBoxLayout,
    QVBoxLayout, QLineEdit, QLayout, QPushButton, QCheckBox, QComboBox, 
    QSpinBox, QStackedLayout, QStackedWidget, QFileDialog
    )
from isu.models.demo import Demo
from isu.operation import Crop, Op
from isu.ui.ops.ops import OpUi
from isu.ui import UiLoad

class CropOp(OpUi):

    @staticmethod
    def cbidx() -> int:
        return 2

    def __init__(self, index: int, parent: Any):
        super(CropOp, self).__init__(parent)
        self.index = index
        dir = QDir(os.path.dirname(__file__) / Path("crop.ui"))
        self.ui = UiLoad(name="crop.ui", dir=dir, parent=parent)
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
