# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demodialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QSizePolicy, QWidget)

class Ui_DemoDialog(object):
    def setupUi(self, DemoDialog):
        if not DemoDialog.objectName():
            DemoDialog.setObjectName(u"DemoDialog")
        DemoDialog.resize(400, 300)
        self.buttonBox = QDialogButtonBox(DemoDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(DemoDialog)
        self.buttonBox.accepted.connect(DemoDialog.accept)
        self.buttonBox.rejected.connect(DemoDialog.reject)

        QMetaObject.connectSlotsByName(DemoDialog)
    # setupUi

    def retranslateUi(self, DemoDialog):
        DemoDialog.setWindowTitle(QCoreApplication.translate("DemoDialog", u"Dialog", None))
    # retranslateUi

