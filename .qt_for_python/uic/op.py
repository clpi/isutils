# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'op.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QScrollArea, QSizePolicy, QSpinBox, QStackedWidget,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_opsWidget(object):
    def setupUi(self, opsWidget):
        if not opsWidget.objectName():
            opsWidget.setObjectName(u"opsWidget")
        opsWidget.resize(484, 788)
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
        self.shellTab = QWidget()
        self.shellTab.setObjectName(u"shellTab")
        self.shellTab.setAutoFillBackground(False)
        self.formLayout_2 = QFormLayout(self.shellTab)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_2.setVerticalSpacing(40)
        self.formLayout_2.setContentsMargins(-1, 11, -1, -1)
        self.label = QLabel(self.shellTab)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.shellImgPath = QLineEdit(self.shellTab)
        self.shellImgPath.setObjectName(u"shellImgPath")

        self.horizontalLayout_4.addWidget(self.shellImgPath)

        self.shellBrowseImgBtn = QPushButton(self.shellTab)
        self.shellBrowseImgBtn.setObjectName(u"shellBrowseImgBtn")

        self.horizontalLayout_4.addWidget(self.shellBrowseImgBtn)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.label_2 = QLabel(self.shellTab)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.shellTab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.shellFgX = QSpinBox(self.shellTab)
        self.shellFgX.setObjectName(u"shellFgX")
        self.shellFgX.setMaximum(100000000)

        self.horizontalLayout_7.addWidget(self.shellFgX)

        self.label_4 = QLabel(self.shellTab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.shellFgY = QSpinBox(self.shellTab)
        self.shellFgY.setObjectName(u"shellFgY")
        self.shellFgY.setMaximum(100000000)

        self.horizontalLayout_7.addWidget(self.shellFgY)


        self.formLayout_2.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_7)

        self.label_5 = QLabel(self.shellTab)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.shellTab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.shellFgW = QSpinBox(self.shellTab)
        self.shellFgW.setObjectName(u"shellFgW")
        self.shellFgW.setMaximum(100000000)

        self.horizontalLayout_8.addWidget(self.shellFgW)

        self.label_6 = QLabel(self.shellTab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.shellFgH = QSpinBox(self.shellTab)
        self.shellFgH.setObjectName(u"shellFgH")
        self.shellFgH.setMaximum(10000000)

        self.horizontalLayout_8.addWidget(self.shellFgH)


        self.formLayout_2.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_8)

        self.opsParamsStack.addWidget(self.shellTab)
        self.insertTab = QWidget()
        self.insertTab.setObjectName(u"insertTab")
        self.formLayout_3 = QFormLayout(self.insertTab)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setVerticalSpacing(40)
        self.formLayout_3.setContentsMargins(-1, 40, -1, -1)
        self.label_32 = QLabel(self.insertTab)
        self.label_32.setObjectName(u"label_32")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_32)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.insertImgPath = QLineEdit(self.insertTab)
        self.insertImgPath.setObjectName(u"insertImgPath")

        self.horizontalLayout_20.addWidget(self.insertImgPath)

        self.insertBrowseImgBtn = QPushButton(self.insertTab)
        self.insertBrowseImgBtn.setObjectName(u"insertBrowseImgBtn")

        self.horizontalLayout_20.addWidget(self.insertBrowseImgBtn)


        self.formLayout_3.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_20)

        self.label_13 = QLabel(self.insertTab)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_26 = QLabel(self.insertTab)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_26)

        self.insertFgX = QSpinBox(self.insertTab)
        self.insertFgX.setObjectName(u"insertFgX")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.insertFgX.sizePolicy().hasHeightForWidth())
        self.insertFgX.setSizePolicy(sizePolicy1)
        self.insertFgX.setMaximum(10000000)

        self.horizontalLayout_18.addWidget(self.insertFgX)

        self.label_29 = QLabel(self.insertTab)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_29)

        self.insertFgY = QSpinBox(self.insertTab)
        self.insertFgY.setObjectName(u"insertFgY")
        self.insertFgY.setMaximum(10000000)

        self.horizontalLayout_18.addWidget(self.insertFgY)


        self.formLayout_3.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_18)

        self.label_12 = QLabel(self.insertTab)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_12)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_33 = QLabel(self.insertTab)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_33)

        self.insertFgW = QSpinBox(self.insertTab)
        self.insertFgW.setObjectName(u"insertFgW")
        self.insertFgW.setBaseSize(QSize(1920, 0))
        self.insertFgW.setMaximum(1000000)
        self.insertFgW.setValue(1920)

        self.horizontalLayout_21.addWidget(self.insertFgW)

        self.label_34 = QLabel(self.insertTab)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_34)

        self.insertFgH = QSpinBox(self.insertTab)
        self.insertFgH.setObjectName(u"insertFgH")
        self.insertFgH.setMaximum(1000000000)
        self.insertFgH.setValue(1080)

        self.horizontalLayout_21.addWidget(self.insertFgH)


        self.formLayout_3.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_21)

        self.opsParamsStack.addWidget(self.insertTab)
        self.sectionTab = QWidget()
        self.sectionTab.setObjectName(u"sectionTab")
        self.formLayout_6 = QFormLayout(self.sectionTab)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.sectionRulesListWidget = QListWidget(self.sectionTab)
        QListWidgetItem(self.sectionRulesListWidget)
        QListWidgetItem(self.sectionRulesListWidget)
        QListWidgetItem(self.sectionRulesListWidget)
        QListWidgetItem(self.sectionRulesListWidget)
        QListWidgetItem(self.sectionRulesListWidget)
        QListWidgetItem(self.sectionRulesListWidget)
        QListWidgetItem(self.sectionRulesListWidget)
        self.sectionRulesListWidget.setObjectName(u"sectionRulesListWidget")
        self.sectionRulesListWidget.setMaximumSize(QSize(16777215, 100))

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.sectionRulesListWidget)

        self.label_10 = QLabel(self.sectionTab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 20))

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.label_10)

        self.sectionCoverageLabel = QLabel(self.sectionTab)
        self.sectionCoverageLabel.setObjectName(u"sectionCoverageLabel")
        self.sectionCoverageLabel.setMaximumSize(QSize(16777215, 20))

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.sectionCoverageLabel)

        self.label_11 = QLabel(self.sectionTab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 20))

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.label_11)

        self.opsParamsStack.addWidget(self.sectionTab)
        self.audioTab = QWidget()
        self.audioTab.setObjectName(u"audioTab")
        self.formLayout_8 = QFormLayout(self.audioTab)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.comboBox = QComboBox(self.audioTab)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.comboBox)

        self.label_8 = QLabel(self.audioTab)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.opsParamsStack.addWidget(self.audioTab)
        self.cropTab = QWidget()
        self.cropTab.setObjectName(u"cropTab")
        self.formLayout_4 = QFormLayout(self.cropTab)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setVerticalSpacing(40)
        self.formLayout_4.setContentsMargins(-1, 40, -1, -1)
        self.label_14 = QLabel(self.cropTab)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_30 = QLabel(self.cropTab)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_30)

        self.spinBox_21 = QSpinBox(self.cropTab)
        self.spinBox_21.setObjectName(u"spinBox_21")

        self.horizontalLayout_19.addWidget(self.spinBox_21)

        self.label_31 = QLabel(self.cropTab)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_31)

        self.spinBox_22 = QSpinBox(self.cropTab)
        self.spinBox_22.setObjectName(u"spinBox_22")

        self.horizontalLayout_19.addWidget(self.spinBox_22)


        self.formLayout_4.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_19)

        self.label_15 = QLabel(self.cropTab)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_35 = QLabel(self.cropTab)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_35)

        self.spinBox_25 = QSpinBox(self.cropTab)
        self.spinBox_25.setObjectName(u"spinBox_25")

        self.horizontalLayout_22.addWidget(self.spinBox_25)

        self.label_36 = QLabel(self.cropTab)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_36)

        self.spinBox_26 = QSpinBox(self.cropTab)
        self.spinBox_26.setObjectName(u"spinBox_26")

        self.horizontalLayout_22.addWidget(self.spinBox_26)


        self.formLayout_4.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_22)

        self.opsParamsStack.addWidget(self.cropTab)
        self.composeTab = QWidget()
        self.composeTab.setObjectName(u"composeTab")
        self.verticalLayout_12 = QVBoxLayout(self.composeTab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")

        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.opsParamsStack.addWidget(self.composeTab)
        self.resizeTab = QWidget()
        self.resizeTab.setObjectName(u"resizeTab")
        self.verticalLayout_10 = QVBoxLayout(self.resizeTab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.opsParamsStack.addWidget(self.resizeTab)
        self.pacingTab = QWidget()
        self.pacingTab.setObjectName(u"pacingTab")
        self.verticalLayout_5 = QVBoxLayout(self.pacingTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.pacingTab)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        self.opsParamsStack.addWidget(self.pacingTab)
        self.animateTab = QWidget()
        self.animateTab.setObjectName(u"animateTab")
        self.verticalLayout_14 = QVBoxLayout(self.animateTab)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")

        self.verticalLayout_14.addLayout(self.verticalLayout_13)

        self.opsParamsStack.addWidget(self.animateTab)
        self.renderTab = QWidget()
        self.renderTab.setObjectName(u"renderTab")
        self.verticalLayout_4 = QVBoxLayout(self.renderTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.renderTabTabs = QTabWidget(self.renderTab)
        self.renderTabTabs.setObjectName(u"renderTabTabs")
        self.renderTabVideoTab = QWidget()
        self.renderTabVideoTab.setObjectName(u"renderTabVideoTab")
        self.verticalLayout_2 = QVBoxLayout(self.renderTabVideoTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.scrollArea = QScrollArea(self.renderTabVideoTab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Panel)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 438, 412))
        self.formLayout_10 = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.videoTitleLabel = QLabel(self.scrollAreaWidgetContents)
        self.videoTitleLabel.setObjectName(u"videoTitleLabel")

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.videoTitleLabel)

        self.renderOutputTitle = QLineEdit(self.scrollAreaWidgetContents)
        self.renderOutputTitle.setObjectName(u"renderOutputTitle")

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.renderOutputTitle)

        self.videoDirectoryLabel = QLabel(self.scrollAreaWidgetContents)
        self.videoDirectoryLabel.setObjectName(u"videoDirectoryLabel")

        self.formLayout_10.setWidget(1, QFormLayout.LabelRole, self.videoDirectoryLabel)

        self.renderOutputDir = QLineEdit(self.scrollAreaWidgetContents)
        self.renderOutputDir.setObjectName(u"renderOutputDir")

        self.formLayout_10.setWidget(1, QFormLayout.FieldRole, self.renderOutputDir)

        self.videoFormatLabel = QLabel(self.scrollAreaWidgetContents)
        self.videoFormatLabel.setObjectName(u"videoFormatLabel")

        self.formLayout_10.setWidget(2, QFormLayout.LabelRole, self.videoFormatLabel)

        self.renderOutputFormat = QComboBox(self.scrollAreaWidgetContents)
        self.renderOutputFormat.addItem("")
        self.renderOutputFormat.addItem("")
        self.renderOutputFormat.setObjectName(u"renderOutputFormat")

        self.formLayout_10.setWidget(2, QFormLayout.FieldRole, self.renderOutputFormat)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.renderTabTabs.addTab(self.renderTabVideoTab, "")
        self.renderTabAudioTab = QWidget()
        self.renderTabAudioTab.setObjectName(u"renderTabAudioTab")
        self.verticalLayout_6 = QVBoxLayout(self.renderTabAudioTab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollArea_2 = QScrollArea(self.renderTabAudioTab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 428, 402))
        self.formLayout_11 = QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_6.addWidget(self.scrollArea_2)

        self.renderTabTabs.addTab(self.renderTabAudioTab, "")
        self.renderTabPacingTab = QWidget()
        self.renderTabPacingTab.setObjectName(u"renderTabPacingTab")
        self.verticalLayout_8 = QVBoxLayout(self.renderTabPacingTab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea_3 = QScrollArea(self.renderTabPacingTab)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 428, 402))
        self.formLayout_12 = QFormLayout(self.scrollAreaWidgetContents_3)
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_8.addWidget(self.scrollArea_3)

        self.renderTabTabs.addTab(self.renderTabPacingTab, "")

        self.verticalLayout_4.addWidget(self.renderTabTabs)

        self.opsParamsStack.addWidget(self.renderTab)
        self.extraTab = QWidget()
        self.extraTab.setObjectName(u"extraTab")
        self.formLayout_7 = QFormLayout(self.extraTab)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.opsParamsStack.addWidget(self.extraTab)

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

        self.opsParamsStack.setCurrentIndex(9)
        self.renderTabTabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(opsWidget)
    # setupUi

    def retranslateUi(self, opsWidget):
        self.operationSelect.setTitle(QCoreApplication.translate("opsWidget", u"Operation", None))
        self.applyOpLabel.setText(QCoreApplication.translate("opsWidget", u"Operation", None))
        self.opCombo.setItemText(0, QCoreApplication.translate("opsWidget", u"Shell", None))
        self.opCombo.setItemText(1, QCoreApplication.translate("opsWidget", u"Insert", None))
        self.opCombo.setItemText(2, QCoreApplication.translate("opsWidget", u"Section", None))
        self.opCombo.setItemText(3, QCoreApplication.translate("opsWidget", u"Audio", None))
        self.opCombo.setItemText(4, QCoreApplication.translate("opsWidget", u"Crop", None))
        self.opCombo.setItemText(5, QCoreApplication.translate("opsWidget", u"Compose Demos", None))
        self.opCombo.setItemText(6, QCoreApplication.translate("opsWidget", u"Resize", None))
        self.opCombo.setItemText(7, QCoreApplication.translate("opsWidget", u"Add pacing", None))
        self.opCombo.setItemText(8, QCoreApplication.translate("opsWidget", u"Animate scroll steps", None))
        self.opCombo.setItemText(9, QCoreApplication.translate("opsWidget", u"Render to video", None))

        self.applyToLabel.setText(QCoreApplication.translate("opsWidget", u"Apply to:", None))
        self.allDemoCheck.setText(QCoreApplication.translate("opsWidget", u"Apply to all demos", None))
        self.allStepsCheck.setText(QCoreApplication.translate("opsWidget", u"Apply to all steps", None))
        self.matchSubstringCheck.setText(QCoreApplication.translate("opsWidget", u"Apply to steps with matching substring:", None))
        self.label_16.setText(QCoreApplication.translate("opsWidget", u"Steps containing:", None))
        self.applyDemoLabel.setText(QCoreApplication.translate("opsWidget", u"Demo", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("opsWidget", u"Parameters", None))
        self.label.setText(QCoreApplication.translate("opsWidget", u"Background", None))
#if QT_CONFIG(statustip)
        self.shellImgPath.setStatusTip(QCoreApplication.translate("opsWidget", u"Filepath of image to be used as shell for demo assets", None))
#endif // QT_CONFIG(statustip)
        self.shellBrowseImgBtn.setText(QCoreApplication.translate("opsWidget", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("opsWidget", u"Coordinates of assets on shell", None))
        self.label_3.setText(QCoreApplication.translate("opsWidget", u"X", None))
        self.label_4.setText(QCoreApplication.translate("opsWidget", u"Y", None))
        self.label_5.setText(QCoreApplication.translate("opsWidget", u"Dimensions of assets on shell", None))
        self.label_7.setText(QCoreApplication.translate("opsWidget", u"Width", None))
        self.label_6.setText(QCoreApplication.translate("opsWidget", u"Height", None))
        self.label_32.setText(QCoreApplication.translate("opsWidget", u"Image to paste", None))
        self.insertBrowseImgBtn.setText(QCoreApplication.translate("opsWidget", u"Browse", None))
        self.label_13.setText(QCoreApplication.translate("opsWidget", u"Coords of image on assets", None))
        self.label_26.setText(QCoreApplication.translate("opsWidget", u"X", None))
        self.label_29.setText(QCoreApplication.translate("opsWidget", u"Y", None))
        self.label_12.setText(QCoreApplication.translate("opsWidget", u"Dimensions of image on assets", None))
        self.label_33.setText(QCoreApplication.translate("opsWidget", u"Width", None))
        self.label_34.setText(QCoreApplication.translate("opsWidget", u"Height", None))

        __sortingEnabled = self.sectionRulesListWidget.isSortingEnabled()
        self.sectionRulesListWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.sectionRulesListWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("opsWidget", u"Step has TP, next step without TP", None));
        ___qlistwidgetitem1 = self.sectionRulesListWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("opsWidget", u"Step has TP, next step with TP", None));
        ___qlistwidgetitem2 = self.sectionRulesListWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("opsWidget", u"Step has TP, previous step without TP", None));
        ___qlistwidgetitem3 = self.sectionRulesListWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("opsWidget", u"Step has TP, previous step with TP", None));
        ___qlistwidgetitem4 = self.sectionRulesListWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("opsWidget", u"Step has fade-in", None));
        ___qlistwidgetitem5 = self.sectionRulesListWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("opsWidget", u"Step has jump box", None));
        ___qlistwidgetitem6 = self.sectionRulesListWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("opsWidget", u"Step TP contains text pattern...", None));
        self.sectionRulesListWidget.setSortingEnabled(__sortingEnabled)

        self.label_10.setText(QCoreApplication.translate("opsWidget", u"Insert new section on...", None))
        self.sectionCoverageLabel.setText(QCoreApplication.translate("opsWidget", u"Covers 0 steps in selected sections/steps", None))
        self.label_11.setText(QCoreApplication.translate("opsWidget", u"May not match number of audio soundbites (audio not imported)", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("opsWidget", u"Mixed section and step audio", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("opsWidget", u"Section audio only", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("opsWidget", u"Step audio only", None))

        self.label_8.setText(QCoreApplication.translate("opsWidget", u"Audio attachment behavior", None))
        self.label_14.setText(QCoreApplication.translate("opsWidget", u"Crop start coordinates", None))
        self.label_30.setText(QCoreApplication.translate("opsWidget", u"X", None))
        self.label_31.setText(QCoreApplication.translate("opsWidget", u"Y", None))
        self.label_15.setText(QCoreApplication.translate("opsWidget", u"Crop dimensions", None))
        self.label_35.setText(QCoreApplication.translate("opsWidget", u"Width", None))
        self.label_36.setText(QCoreApplication.translate("opsWidget", u"Height", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("opsWidget", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("opsWidget", u"Tab 2", None))
        self.videoTitleLabel.setText(QCoreApplication.translate("opsWidget", u"Video Title", None))
        self.videoDirectoryLabel.setText(QCoreApplication.translate("opsWidget", u"Video Directory", None))
        self.videoFormatLabel.setText(QCoreApplication.translate("opsWidget", u"Video Format", None))
        self.renderOutputFormat.setItemText(0, QCoreApplication.translate("opsWidget", u"avi", None))
        self.renderOutputFormat.setItemText(1, QCoreApplication.translate("opsWidget", u"mp4", None))

        self.renderTabTabs.setTabText(self.renderTabTabs.indexOf(self.renderTabVideoTab), QCoreApplication.translate("opsWidget", u"Video", None))
        self.renderTabTabs.setTabText(self.renderTabTabs.indexOf(self.renderTabAudioTab), QCoreApplication.translate("opsWidget", u"Audio", None))
        self.renderTabTabs.setTabText(self.renderTabTabs.indexOf(self.renderTabPacingTab), QCoreApplication.translate("opsWidget", u"Pacing", None))
        self.resetStepParamsBtn.setText(QCoreApplication.translate("opsWidget", u"Reset to default", None))
        self.saveStepParamsBtn.setText(QCoreApplication.translate("opsWidget", u"Save step parameters", None))
        pass
    # retranslateUi

