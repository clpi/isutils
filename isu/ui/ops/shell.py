import os, sys
from isu.operation import Shell
from isu.models import Demo
from typing import Tuple
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
from isu.ui.ops.ops import OpUi
from typing import Optional, Sequence, Dict
from PyQt6 import uic

class ShellOp(OpUi):

    def __init__(self, parent: Optional[QWidget] = None, index:int = 0):
        super().__init__(parent)
        self.index = index
        path = os.path.join(os.path.dirname(__file__), "shell.ui")
        uic.loadUi(path, self)
        self.loadUi()

    @staticmethod
    def cbidx() -> int:
        return 0

    def loadUi(self):
        self.setObjectName(u"shellTab")
        self.setAutoFillBackground(False)

        self.shellImgPath : QLineEdit
        self.shellBrowseImgBtn : QPushButton

        self.shellFgX : QSpinBox
        self.shellFgY : QSpinBox

        self.shellFgW : QSpinBox
        self.shellFgH : QSpinBox

        # self.opsParamsStack.addWidget(self)

        self.shellBrowseImgBtn.clicked.connect(self.browse_shell)

    def browse_shell(self):
        try:
            fileName, _ = QFileDialog.getOpenFileName(self,"Browse for image files", "","All Files (*);;PNG files (*.png)")
            self.shellImgPath.setText(fileName)
            img_tmp = Image.open(fileName)
            iwidth, iheight = img_tmp.size
            if self.demo is not None:
                if iwidth > self.demo.res[0] or iheight > self.demo.res[1]:
                    pass
            #set op img path, def dims
        except: pass

    def op(self) -> Shell:
        return Shell(
            img_path=self.shellImgPath.text(), 
            fg_coord=(self.shellFgX.value(), self.shellFgY.value()), 
            fg_dim=(self.shellFgW.value(), self.shellFgH.value())
        )
