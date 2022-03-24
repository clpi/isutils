import os, sys
from pathlib import WindowsPath
from typing import Optional
from PIL import Image
from PyQt6.QtCore import (
    QFile, QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt
)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform
)
from PyQt6.QtWidgets import (
    QApplication, QSizePolicy, QWidget, QLabel, QFormLayout, QHBoxLayout,
    QVBoxLayout, QLineEdit, QLayout, QPushButton, QCheckBox, QComboBox, 
    QSpinBox, QStackedLayout, QStackedWidget, QFileDialog
    )
from PyQt6 import uic
from isu.operation import Audio
from isu.ui.ops.ops import OpUi
from PySide6.QtUiTools import QUiLoader

class AudioOp(OpUi, QWidget):

    def __init__(self, index: int = 4, parent: Optional[QWidget] = None):
        super().__init__(parent)
        path = os.path.join(os.path.dirname(__file__), "audio.ui")
        self.index = index
        uic.loadUi(path, self)
        self.loadUi()

    def op(self) -> Audio:
        return Audio()

    def load_ui(self, parent: QWidget | None = None):
        path = WindowsPath(os.path.dirname(__file__)) / "audio.ui"
        uif = QFile(str(path))
        uif.open(QFile.OpenModeFlag.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(uif, parentWidget=parent)
        self.ui.show()
        # self.opsParamsStack.addWidget(self)

        # self.shellBrowseImgBtn.clicked.connect(self.browse_shell)
        pass

    @staticmethod
    def cbidx() -> int:
        return 3

