from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QDir,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLayout, QSizePolicy, QVBoxLayout,
    QWidget)
from isu.ui.data.loaded import DataLoaded
from isu.ui.data.steps import StepData
import sys, os

class DataView(object):
    uifile = QDir(os.path.dirname(os.path.realpath(__file__)))

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(529, 777)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stepsLayout = QVBoxLayout()
        self.stepsLayout.setSpacing(10)
        self.stepsLayout.setObjectName(u"stepsLayout")
        self.stepsLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.stepsLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addLayout(self.stepsLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, form):
        form.setWindowTitle(QCoreApplication.translate(b"dataPane", b"dataPane", None))
    # retranslateUi

