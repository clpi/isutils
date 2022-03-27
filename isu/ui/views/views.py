# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewsxXqZCV.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(403, 803)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.viewTabs = QTabWidget(Form)
        self.viewTabs.setObjectName(u"viewTabs")
        self.viewTabs.setDocumentMode(False)
        self.viewTabs.setMovable(True)
        self.demoTab = QWidget()
        self.demoTab.setObjectName(u"demoTab")
        self.verticalLayout_9 = QVBoxLayout(self.demoTab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.viewTabs.addTab(self.demoTab, "")
        self.previewTab = QWidget()
        self.previewTab.setObjectName(u"previewTab")
        self.verticalLayout_3 = QVBoxLayout(self.previewTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.viewTabs.addTab(self.previewTab, "")

        self.verticalLayout.addWidget(self.viewTabs)


        self.retranslateUi(Form)

        self.viewTabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.viewTabs.setTabText(self.viewTabs.indexOf(self.demoTab), QCoreApplication.translate("Form", u"Info", None))
        self.viewTabs.setTabText(self.viewTabs.indexOf(self.previewTab), QCoreApplication.translate("Form", u"Preview", None))
    # retranslateUi

