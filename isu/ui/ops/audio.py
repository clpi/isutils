import os, sys
from typing import Optional
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
from isu.operation import Audio
from isu.ui.ops.ops import OpUi

class AudioOp(OpUi):

    @staticmethod
    def cbidx() -> int:
        return 3

    def __init__(self, index: int = 4, parent: Optional[QWidget] = None):
        super().__init__(parent)
        path = os.path.join(os.path.dirname(__file__), "audio.ui")
        self.index = index
        uic.loadUi(path, self)
        self.loadUi()

    def op(self) -> Audio:
        return Audio()

    def loadUi(self):
        # self.opsParamsStack.addWidget(self)

        # self.shellBrowseImgBtn.clicked.connect(self.browse_shell)
        pass
