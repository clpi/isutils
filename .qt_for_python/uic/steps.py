# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'steps.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(517, 412)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stepData = QTabWidget(Form)
        self.stepData.setObjectName(u"stepData")
        self.stepData.setEnabled(True)
        self.stepData.setMaximumSize(QSize(410, 16777215))
        self.stepsTab = QWidget()
        self.stepsTab.setObjectName(u"stepsTab")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepsTab.sizePolicy().hasHeightForWidth())
        self.stepsTab.setSizePolicy(sizePolicy)
        self.stepsTab.setMinimumSize(QSize(200, 278))
        self.stepsTab.setAutoFillBackground(False)
        self.verticalLayout_2 = QVBoxLayout(self.stepsTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 11, -1, -1)
        self.stepsTable = QTableWidget(self.stepsTab)
        self.stepsTable.setObjectName(u"stepsTable")

        self.verticalLayout_2.addWidget(self.stepsTable)

        self.stepButtons = QHBoxLayout()
        self.stepButtons.setObjectName(u"stepButtons")
        self.stepDownBtn = QPushButton(self.stepsTab)
        self.stepDownBtn.setObjectName(u"stepDownBtn")

        self.stepButtons.addWidget(self.stepDownBtn)

        self.stepUpBtn = QPushButton(self.stepsTab)
        self.stepUpBtn.setObjectName(u"stepUpBtn")

        self.stepButtons.addWidget(self.stepUpBtn)

        self.removeStepBtn = QPushButton(self.stepsTab)
        self.removeStepBtn.setObjectName(u"removeStepBtn")

        self.stepButtons.addWidget(self.removeStepBtn)

        self.addStepBtn = QPushButton(self.stepsTab)
        self.addStepBtn.setObjectName(u"addStepBtn")

        self.stepButtons.addWidget(self.addStepBtn)

        self.runBtn = QPushButton(self.stepsTab)
        self.runBtn.setObjectName(u"runBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.runBtn.sizePolicy().hasHeightForWidth())
        self.runBtn.setSizePolicy(sizePolicy1)
        self.runBtn.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setBold(False)
        self.runBtn.setFont(font)
        self.runBtn.setCheckable(False)
        self.runBtn.setFlat(False)

        self.stepButtons.addWidget(self.runBtn)


        self.verticalLayout_2.addLayout(self.stepButtons)

        self.stepData.addTab(self.stepsTab, "")
        self.templatesTab = QWidget()
        self.templatesTab.setObjectName(u"templatesTab")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.templatesTab.sizePolicy().hasHeightForWidth())
        self.templatesTab.setSizePolicy(sizePolicy2)
        self.verticalLayout_19 = QVBoxLayout(self.templatesTab)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.treeWidget = QTreeWidget(self.templatesTab)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy3)

        self.verticalLayout_19.addWidget(self.treeWidget)

        self.stepData.addTab(self.templatesTab, "")
        self.optionsTab = QWidget()
        self.optionsTab.setObjectName(u"optionsTab")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.optionsTab.sizePolicy().hasHeightForWidth())
        self.optionsTab.setSizePolicy(sizePolicy4)
        self.optionsTab.setAutoFillBackground(True)
        self.verticalLayout_17 = QVBoxLayout(self.optionsTab)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.stepOptionsTable = QTableWidget(self.optionsTab)
        self.stepOptionsTable.setObjectName(u"stepOptionsTable")

        self.verticalLayout_17.addWidget(self.stepOptionsTable)

        self.stepData.addTab(self.optionsTab, "")

        self.verticalLayout.addWidget(self.stepData)


        self.retranslateUi(Form)

        self.stepData.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.stepDownBtn.setText(QCoreApplication.translate("Form", u"<", None))
        self.stepUpBtn.setText(QCoreApplication.translate("Form", u">", None))
        self.removeStepBtn.setText(QCoreApplication.translate("Form", u"-", None))
        self.addStepBtn.setText(QCoreApplication.translate("Form", u"+", None))
        self.runBtn.setText(QCoreApplication.translate("Form", u"Run", None))
        self.stepData.setTabText(self.stepData.indexOf(self.stepsTab), QCoreApplication.translate("Form", u"Steps", None))
        self.stepData.setTabText(self.stepData.indexOf(self.templatesTab), QCoreApplication.translate("Form", u"Templates", None))
        self.stepData.setTabText(self.stepData.indexOf(self.optionsTab), QCoreApplication.translate("Form", u"Options", None))
    # retranslateUi

