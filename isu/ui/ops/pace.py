import os, sys
from isu.ui import UiLoad
from typing import Optional, Any
from PIL import Image
from isu.models.demo import Demo
from isu.operation import Pace
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QDir,
    QMetaObject, QObject, QPoint, QRect,
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
from isu.ui.ops.ops import OpUi
from PySide6.QtWidgets import QWidget

class PaceOp(OpUi, QWidget):

    def __init__(self, parent: QWidget | None) -> None:
        QWidget.__init__(self, parent)
        UiLoad().loadUi("pace.ui", self, parent)
        self.load_widgets()

    def load_widgets(self):
        pass

    @staticmethod
    def cbidx() -> int:
        return 6

    def op(self) -> Pace:
        return Pace()

    def loadUi(self):
        # self.opsParamsStack.addWidget(self)

        # self.shellBrowseImgBtn.clicked.connect(self.browse_shell)
        pass
