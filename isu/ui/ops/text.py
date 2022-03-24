import os, sys
from typing import Optional
from PIL import Image
from PySide6.QtCore import (
    Signal, Slot, QEnum,
    QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (
    QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (
    QApplication, QSizePolicy, QWidget, QLabel, QFormLayout, QHBoxLayout,
    QVBoxLayout, QLineEdit, QLayout, QPushButton, QCheckBox, QComboBox, 
    QSpinBox, QStackedLayout, QStackedWidget, QFileDialog
    )
from PySide6 import QtUiTools
from isu.ui.ops import OpUi
from isu.models.demo import Demo
from isu.operation.text import Text
class TextOp(OpUi):

    def __init__(self, parent: Optional[QWidget] = None, index: int = 0):
        super().__init__(index=index, parent=parent)
        path = os.path.join(os.path.dirname(__file__), "text.ui")
        self.index = index
        uic.loadUi(path, self)
        self.loadUi()

    def loadUi(self):
        # self.opsParamsStack.addWidget(self)

        # self.shellBrowseImgBtn.clicked.connect(self.browse_shell)
        pass

    def op(self) -> Text:
        return Text()
