import os
import sys
from typing import Any, List, Optional, Tuple

from isu.models.demo import Demo
from isu.operation import Insert, Op
from isu.ui import UiLoad
from isu.ui.ops.ops import OpUi
from PIL import Image
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QDir,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt, QFile,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFileDialog,
                               QFormLayout, QHBoxLayout, QLabel, QLayout,
                               QLineEdit, QPushButton, QSizePolicy, QSpinBox,
                               QStackedLayout, QStackedWidget, QVBoxLayout,
                               QWidget)


class InsertOp(OpUi):
    parent: Any
    index: int
    ui: QWidget

    def __init__(self, index: int = 1, parent: Any = QCoreApplication.instance()):
        super(OpUi, self).__init__(parent)
        self.parent = parent
        self.index = index
        self.load_ui()
        self.load_widgets()
        

    def load_ui(self):
        dir = QDir(os.path.join(os.path.dirname(__file__), "insert.ui"))
        loader: UiLoad = UiLoad(name="insert.ui", dir=dir, parent=self)
        self.ui: QWidget = loader.load_ui()
        
    def load_widgets(self):
        pass

    def load_data(self):
        self.setObjectName(u"insertTab")
        self.setAutoFillBackground(False)

        self.insertImgPath : QLineEdit
        self.insertBrowseImgBtn : QPushButton

        self.insertFgX: QSpinBox
        self.insertFgY: QSpinBox
        self.insertFgW: QSpinBox
        self.insertFgH: QSpinBox

        self.insertBrowseImgBtn.toggle.connect(self.browse_insert)

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
        except: pass
