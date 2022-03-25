import os, sys
from typing import Optional, Sequence, Dict, Any
from PIL import Image
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
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
from isu.ui import UiLoad
from isu.models.demo import Demo
from isu.ui.ops.ops import OpUi
from isu.operation.section import Section

class SectionOp(QObject, OpUi):

    ui: QWidget | None = None
    parent: Any = QCoreApplication.instance()
    index: int
    path: str

    def __init__(self, index:int = 0, parent: Any = QCoreApplication.instance() ):
        super(SectionOp, self).__init__(parent)
        self.index = index
        self.path = os.path.join(os.path.dirname(__file__), "section.ui")
        self.loadUi(parent=parent)

    @staticmethod
    def cbidx() -> int:
        return 3

    def loadUi(self):
        pass

    def op(self) -> Section:
        return Section()

        # self.opsParamsStack.addWidget(self)

        # self.shellBrowseImgBtn.clicked.connect(self.browse_shell)
