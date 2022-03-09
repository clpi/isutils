import os, sys
from typing import List, Optional, Tuple
from isu.ui.ops.ops import OpUi
from isu.models.demo import Demo
from isu.operation import Insert, Op
from PIL import Image
from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (
    QFileDialog, 
    QApplication, QSizePolicy, QWidget, QLabel, QFormLayout, QHBoxLayout,
    QVBoxLayout, QLineEdit, QLayout, QPushButton, QCheckBox, QComboBox, 
    QSpinBox, QStackedLayout, QStackedWidget
    )
from PyQt6 import uic

class InsertOp(OpUi):

    @staticmethod
    def cbidx() -> int:
        return 1

    def __init__(self, index: int = 1, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.index = index
        path = os.path.join(os.path.dirname(__file__), "insert.ui")
        uic.loadUi(path, self)
        self.loadUi()

    def loadUi(self):
        self.setObjectName(u"insertTab")
        self.setAutoFillBackground(False)

        self.insertImgPath : QLineEdit
        self.insertBrowseImgBtn : QPushButton

        self.insertFgX: QSpinBox
        self.insertFgY: QSpinBox
        self.insertFgW: QSpinBox
        self.insertFgH: QSpinBox

        self.insertBrowseImgBtn.clicked.connect(self.browse_insert)

    def op(self) -> Insert:
        return Insert(
            # apply_to=apply_to, 
            # all_steps=all_steps,
            img_path=self.insertImgPath.text(),
            x=self.insertFgX.value(),
            y=self.insertFgY.value(),
            w=self.insertFgW.value(),
            h=self.insertFgH.value()
        )

    def browse_insert(self):
        try:
            fileName, _ = QFileDialog.getOpenFileName(self,"Browse for image files", "","All Files (*);;PNG files (*.png)")
            self.insertImgPath.setText(fileName)
            img_tmp = Image.open(fileName)
            iwidth, iheight = img_tmp.size
            if self.demo is not None:
                if iwidth > self.demo.res[0] or iheight > self.demo.res[1]:
                    pass
            #set op img path, def dims
        except: pass