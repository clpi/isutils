# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'insert.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QWidget)
class Ui_Form(object):
    def setupUi(self, insertTab):
        if not insertTab.objectName():
            insertTab.setObjectName(u"insertTab")
        self.formLayout_3 = QFormLayout(insertTab)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setVerticalSpacing(40)
        self.formLayout_3.setContentsMargins(-1, 40, -1, -1)
        self.label_32 = QLabel(insertTab)
        self.label_32.setObjectName(u"label_32")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_32)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.insertImgPath = QLineEdit(insertTab)
        self.insertImgPath.setObjectName(u"insertImgPath")

        self.horizontalLayout_20.addWidget(self.insertImgPath)

        self.insertBrowseImgBtn = QPushButton(insertTab)
        self.insertBrowseImgBtn.setObjectName(u"insertBrowseImgBtn")

        self.horizontalLayout_20.addWidget(self.insertBrowseImgBtn)


        self.formLayout_3.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_20)

        self.label_13 = QLabel(insertTab)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_26 = QLabel(insertTab)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_26)

        self.insertFgX = QSpinBox(insertTab)
        self.insertFgX.setObjectName(u"insertFgX")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.insertFgX.sizePolicy().hasHeightForWidth())
        self.insertFgX.setSizePolicy(sizePolicy)
        self.insertFgX.setMaximum(10000000)

        self.horizontalLayout_18.addWidget(self.insertFgX)

        self.label_29 = QLabel(insertTab)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_29)

        self.insertFgY = QSpinBox(insertTab)
        self.insertFgY.setObjectName(u"insertFgY")
        self.insertFgY.setMaximum(10000000)

        self.horizontalLayout_18.addWidget(self.insertFgY)


        self.formLayout_3.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_18)

        self.label_12 = QLabel(insertTab)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_12)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_33 = QLabel(insertTab)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_33)

        self.insertFgW = QSpinBox(insertTab)
        self.insertFgW.setObjectName(u"insertFgW")
        self.insertFgW.setBaseSize(QSize(1920, 0))
        self.insertFgW.setMaximum(1000000)
        self.insertFgW.setValue(1920)

        self.horizontalLayout_21.addWidget(self.insertFgW)

        self.label_34 = QLabel(insertTab)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_34)

        self.insertFgH = QSpinBox(insertTab)
        self.insertFgH.setObjectName(u"insertFgH")
        self.insertFgH.setMaximum(1000000000)
        self.insertFgH.setValue(1080)

        self.horizontalLayout_21.addWidget(self.insertFgH)


        self.formLayout_3.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_21)


        self.retranslateUi(insertTab)

        QMetaObject.connectSlotsByName(insertTab)
    # setupUi

    def retranslateUi(self, insertTab):
        self.label_32.setText(QCoreApplication.translate("Form", u"Image to paste", None))
        self.insertBrowseImgBtn.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Coords of image on assets", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"X", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"Y", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Dimensions of image on assets", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"Width", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"Height", None))
        pass
    # retranslateUi

