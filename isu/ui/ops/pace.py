import os, sys
from typing import Optional
from PIL import Image
from isu.models.demo import Demo
from isu.operation import Pace
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
from isu.ui.ops.ops import OpUi
from PyQt6.QtWidgets import QWidget

class PaceOp(OpUi):

    @staticmethod
    def cbidx() -> int:
        return 6

    def __init__(self, parent: Optional[QWidget] = None, index:int = 0):
        super().__init__(parent)
        self.index = index
        path = os.path.join(os.path.dirname(__file__), "pace.ui")
        uic.loadUi(path, self)
        self.loadUi()

    def op(self) -> Pace:
        return Pace()

    def loadUi(self):
        # self.opsParamsStack.addWidget(self)

        # self.shellBrowseImgBtn.clicked.connect(self.browse_shell)
        pass
