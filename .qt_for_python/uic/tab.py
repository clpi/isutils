# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QSizePolicy, QSpacerItem, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)

class Ui_opsWidget(object):
    def setupUi(self, opsWidget):
        if not opsWidget.objectName():
            opsWidget.setObjectName(u"opsWidget")
        opsWidget.resize(498, 576)
        self.verticalLayout_4 = QVBoxLayout(opsWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalGroupBox_3 = QGroupBox(opsWidget)
        self.verticalGroupBox_3.setObjectName(u"verticalGroupBox_3")
        self.verticalGroupBox_3.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.verticalLayout_6 = QVBoxLayout(self.verticalGroupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.verticalGroupBox_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(463, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.verticalGroupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.comboBox_2 = QComboBox(self.verticalGroupBox_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.toolButton = QToolButton(self.verticalGroupBox_3)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout.addWidget(self.toolButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.targetLayout = QHBoxLayout()
        self.targetLayout.setObjectName(u"targetLayout")
        self.label = QLabel(self.verticalGroupBox_3)
        self.label.setObjectName(u"label")

        self.targetLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.targetLayout.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(self.verticalGroupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.targetLayout.addWidget(self.label_5)

        self.comboBox = QComboBox(self.verticalGroupBox_3)
        self.comboBox.setObjectName(u"comboBox")

        self.targetLayout.addWidget(self.comboBox)

        self.toolButton_2 = QToolButton(self.verticalGroupBox_3)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.targetLayout.addWidget(self.toolButton_2)


        self.verticalLayout_6.addLayout(self.targetLayout)


        self.horizontalLayout_5.addWidget(self.verticalGroupBox_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.verticalGroupBox_2 = QGroupBox(opsWidget)
        self.verticalGroupBox_2.setObjectName(u"verticalGroupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.allDemoCheck = QCheckBox(self.verticalGroupBox_2)
        self.allDemoCheck.setObjectName(u"allDemoCheck")
        self.allDemoCheck.setMaximumSize(QSize(10000, 16777215))

        self.verticalLayout_5.addWidget(self.allDemoCheck)

        self.allStepsCheck = QCheckBox(self.verticalGroupBox_2)
        self.allStepsCheck.setObjectName(u"allStepsCheck")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.allStepsCheck.sizePolicy().hasHeightForWidth())
        self.allStepsCheck.setSizePolicy(sizePolicy1)
        self.allStepsCheck.setMinimumSize(QSize(180, 0))
        self.allStepsCheck.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_5.addWidget(self.allStepsCheck)

        self.checkBox_2 = QCheckBox(self.verticalGroupBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_5.addWidget(self.checkBox_2)

        self.checkBox = QCheckBox(self.verticalGroupBox_2)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_5.addWidget(self.checkBox)

        self.matchSubstringCheck = QCheckBox(self.verticalGroupBox_2)
        self.matchSubstringCheck.setObjectName(u"matchSubstringCheck")

        self.verticalLayout_5.addWidget(self.matchSubstringCheck)

        self.lineEdit = QLineEdit(self.verticalGroupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_5.addWidget(self.lineEdit)


        self.horizontalLayout_5.addWidget(self.verticalGroupBox_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.groupBox = QGroupBox(opsWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.groupBox)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.stackedWidget.addWidget(self.page)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.groupBox)


        self.retranslateUi(opsWidget)

        QMetaObject.connectSlotsByName(opsWidget)
    # setupUi

    def retranslateUi(self, opsWidget):
        self.verticalGroupBox_3.setTitle(QCoreApplication.translate("opsWidget", u"Task Info", None))
        self.label_2.setText(QCoreApplication.translate("opsWidget", u"Task", None))
        self.label_4.setText(QCoreApplication.translate("opsWidget", u"Current:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("opsWidget", u"Shell", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("opsWidget", u"Insert", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("opsWidget", u"Crop", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("opsWidget", u"Section", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("opsWidget", u"Add Audio", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("opsWidget", u"Pacing", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("opsWidget", u"Add Text", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("opsWidget", u"Render", None))

        self.toolButton.setText(QCoreApplication.translate("opsWidget", u"...", None))
        self.label.setText(QCoreApplication.translate("opsWidget", u"Target", None))
        self.label_5.setText(QCoreApplication.translate("opsWidget", u"Demo:", None))
        self.toolButton_2.setText(QCoreApplication.translate("opsWidget", u"...", None))
        self.verticalGroupBox_2.setTitle(QCoreApplication.translate("opsWidget", u"Step Targets", None))
        self.allDemoCheck.setText(QCoreApplication.translate("opsWidget", u"Apply to all demos", None))
        self.allStepsCheck.setText(QCoreApplication.translate("opsWidget", u"Apply to all steps", None))
        self.checkBox_2.setText(QCoreApplication.translate("opsWidget", u"Apply to all steps of marked sections", None))
        self.checkBox.setText(QCoreApplication.translate("opsWidget", u"Apply to marked steps", None))
        self.matchSubstringCheck.setText(QCoreApplication.translate("opsWidget", u"Apply to steps with title containing:", None))
        self.groupBox.setTitle(QCoreApplication.translate("opsWidget", u"Parameters", None))
        pass
    # retranslateUi

