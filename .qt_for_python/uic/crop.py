# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crop.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QSizePolicy, QSpinBox, QWidget)
class Ui_Form(object):
    def setupUi(self, cropOp):
        if not cropOp.objectName():
            cropOp.setObjectName(u"cropOp")
        self.formLayout_4 = QFormLayout(cropOp)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setVerticalSpacing(40)
        self.formLayout_4.setContentsMargins(-1, 40, -1, -1)
        self.label_14 = QLabel(cropOp)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_30 = QLabel(cropOp)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_30)

        self.spinBox_21 = QSpinBox(cropOp)
        self.spinBox_21.setObjectName(u"spinBox_21")

        self.horizontalLayout_19.addWidget(self.spinBox_21)

        self.label_31 = QLabel(cropOp)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_31)

        self.spinBox_22 = QSpinBox(cropOp)
        self.spinBox_22.setObjectName(u"spinBox_22")

        self.horizontalLayout_19.addWidget(self.spinBox_22)


        self.formLayout_4.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_19)

        self.label_15 = QLabel(cropOp)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_35 = QLabel(cropOp)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_35)

        self.spinBox_25 = QSpinBox(cropOp)
        self.spinBox_25.setObjectName(u"spinBox_25")

        self.horizontalLayout_22.addWidget(self.spinBox_25)

        self.label_36 = QLabel(cropOp)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_36)

        self.spinBox_26 = QSpinBox(cropOp)
        self.spinBox_26.setObjectName(u"spinBox_26")

        self.horizontalLayout_22.addWidget(self.spinBox_26)


        self.formLayout_4.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_22)


        self.retranslateUi(cropOp)

        QMetaObject.connectSlotsByName(cropOp)
    # setupUi

    def retranslateUi(self, cropOp):
        self.label_14.setText(QCoreApplication.translate("Form", u"Crop start coordinates", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"X", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"Y", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Crop dimensions", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"Width", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"Height", None))
        pass
    # retranslateUi

