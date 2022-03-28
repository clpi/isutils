import os, sys
from typing import Optional, Any, Tuple, List
from pathlib import Path
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

class CropOp(OpUi, QWidget):

    uifile = QDir(os.path.dirname(os.path.realpath(__file__)))

    def __init__(self, parent: QWidget | None) -> None:
        QWidget.__init__(self, parent)
        UiLoad().loadUi("crop.ui", self, parent)
        self.load_ui()
        self.load_widgets()

    def load_ui(self):
        pass

    def load_widgets(self):
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
