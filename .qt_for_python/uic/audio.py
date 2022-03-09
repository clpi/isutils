# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'audio.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QLabel,
    QSizePolicy, QWidget)
class Ui_Form(object):
    def setupUi(self, audioOp):
        if not audioOp.objectName():
            audioOp.setObjectName(u"audioOp")
        self.formLayout_8 = QFormLayout(audioOp)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.comboBox = QComboBox(audioOp)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.comboBox)

        self.label_8 = QLabel(audioOp)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_8)


        self.retranslateUi(audioOp)

        QMetaObject.connectSlotsByName(audioOp)
    # setupUi

    def retranslateUi(self, audioOp):
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Mixed section and step audio", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Section audio only", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Step audio only", None))

        self.label_8.setText(QCoreApplication.translate("Form", u"Audio attachment behavior", None))
        pass
    # retranslateUi

