# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_opsWidget(object):
    def setupUi(self, opsWidget):
        if not opsWidget.objectName():
            opsWidget.setObjectName(u"opsWidget")
        opsWidget.resize(484, 779)
        self.opLayout = QVBoxLayout(opsWidget)
        self.opLayout.setObjectName(u"opLayout")
        self.operationSelect = QGroupBox(opsWidget)
        self.operationSelect.setObjectName(u"operationSelect")
        self.operationSelect.setEnabled(True)
        self.operationSelect.setFlat(True)
        self.verticalLayout_3 = QVBoxLayout(self.operationSelect)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(5, 20, 5, 20)
        self.applyOpLabel = QLabel(self.operationSelect)
        self.applyOpLabel.setObjectName(u"applyOpLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.applyOpLabel)

        self.opCombo = QComboBox(self.operationSelect)
        self.opCombo.addItem("")
        self.opCombo.addItem("")
        self.opCombo.addItem("")
        self.opCombo.addItem("")
        self.opCombo.addItem("")
        self.opCombo.addItem("")
        self.opCombo.addItem("")
        self.opCombo.addItem("")
        self.opCombo.setObjectName(u"opCombo")
        self.opCombo.setEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.opCombo)

        self.applyToLabel = QLabel(self.operationSelect)
        self.applyToLabel.setObjectName(u"applyToLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.applyToLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.allDemoCheck = QCheckBox(self.operationSelect)
        self.allDemoCheck.setObjectName(u"allDemoCheck")
        self.allDemoCheck.setMaximumSize(QSize(10000, 16777215))

        self.horizontalLayout_2.addWidget(self.allDemoCheck)

        self.allStepsCheck = QCheckBox(self.operationSelect)
        self.allStepsCheck.setObjectName(u"allStepsCheck")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allStepsCheck.sizePolicy().hasHeightForWidth())
        self.allStepsCheck.setSizePolicy(sizePolicy)
        self.allStepsCheck.setMinimumSize(QSize(180, 0))
        self.allStepsCheck.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.allStepsCheck)


        self.verticalLayout_18.addLayout(self.horizontalLayout_2)

        self.matchSubstringCheck = QCheckBox(self.operationSelect)
        self.matchSubstringCheck.setObjectName(u"matchSubstringCheck")

        self.verticalLayout_18.addWidget(self.matchSubstringCheck)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_16 = QLabel(self.operationSelect)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setEnabled(False)

        self.horizontalLayout_13.addWidget(self.label_16)

        self.matchSubstringText = QLineEdit(self.operationSelect)
        self.matchSubstringText.setObjectName(u"matchSubstringText")
        self.matchSubstringText.setEnabled(False)

        self.horizontalLayout_13.addWidget(self.matchSubstringText)


        self.verticalLayout_18.addLayout(self.horizontalLayout_13)


        self.horizontalLayout.addLayout(self.verticalLayout_18)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout)

        self.applyDemoLabel = QLabel(self.operationSelect)
        self.applyDemoLabel.setObjectName(u"applyDemoLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.applyDemoLabel)

        self.demoTargetCombo = QComboBox(self.operationSelect)
        self.demoTargetCombo.setObjectName(u"demoTargetCombo")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.demoTargetCombo)


        self.verticalLayout_3.addLayout(self.formLayout)


        self.opLayout.addWidget(self.operationSelect)

        self.groupBox_6 = QGroupBox(opsWidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setEnabled(True)
        self.groupBox_6.setFlat(True)
        self.verticalLayout = QVBoxLayout(self.groupBox_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.opsParamsStack = QStackedWidget(self.groupBox_6)
        self.opsParamsStack.setObjectName(u"opsParamsStack")
        self.opsParamsStack.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.opsParamsStack)


        self.opLayout.addWidget(self.groupBox_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.resetStepParamsBtn = QPushButton(opsWidget)
        self.resetStepParamsBtn.setObjectName(u"resetStepParamsBtn")

        self.horizontalLayout_9.addWidget(self.resetStepParamsBtn)

        self.saveStepParamsBtn = QPushButton(opsWidget)
        self.saveStepParamsBtn.setObjectName(u"saveStepParamsBtn")

        self.horizontalLayout_9.addWidget(self.saveStepParamsBtn)


        self.opLayout.addLayout(self.horizontalLayout_9)


        self.retranslateUi(opsWidget)
        self.opCombo.currentIndexChanged.connect(self.opsParamsStack.setCurrentIndex)

        self.opsParamsStack.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(opsWidget)
    # setupUi

    def retranslateUi(self, opsWidget):
        self.operationSelect.setTitle(QCoreApplication.translate("opsWidget", u"Operation", None))
        self.applyOpLabel.setText(QCoreApplication.translate("opsWidget", u"Operation", None))
        self.opCombo.setItemText(0, QCoreApplication.translate("opsWidget", u"Shell", None))
        self.opCombo.setItemText(1, QCoreApplication.translate("opsWidget", u"Insert", None))
        self.opCombo.setItemText(2, QCoreApplication.translate("opsWidget", u"Crop", None))
        self.opCombo.setItemText(3, QCoreApplication.translate("opsWidget", u"Section", None))
        self.opCombo.setItemText(4, QCoreApplication.translate("opsWidget", u"Audio", None))
        self.opCombo.setItemText(5, QCoreApplication.translate("opsWidget", u"Add pacing", None))
        self.opCombo.setItemText(6, QCoreApplication.translate("opsWidget", u"Add text", None))
        self.opCombo.setItemText(7, QCoreApplication.translate("opsWidget", u"Render to video", None))

        self.applyToLabel.setText(QCoreApplication.translate("opsWidget", u"Apply to:", None))
        self.allDemoCheck.setText(QCoreApplication.translate("opsWidget", u"Apply to all demos", None))
        self.allStepsCheck.setText(QCoreApplication.translate("opsWidget", u"Apply to all steps", None))
        self.matchSubstringCheck.setText(QCoreApplication.translate("opsWidget", u"Apply to steps with matching substring:", None))
        self.label_16.setText(QCoreApplication.translate("opsWidget", u"Steps containing:", None))
        self.applyDemoLabel.setText(QCoreApplication.translate("opsWidget", u"Demo", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("opsWidget", u"Parameters", None))
        self.resetStepParamsBtn.setText(QCoreApplication.translate("opsWidget", u"Reset to default", None))
        self.saveStepParamsBtn.setText(QCoreApplication.translate("opsWidget", u"Save step parameters", None))
        pass
    # retranslateUi

