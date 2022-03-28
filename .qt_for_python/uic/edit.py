# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QScrollArea, QSizePolicy, QSpinBox, QTabWidget,
    QTextEdit, QToolButton, QVBoxLayout, QWidget)

from kmessagewidget import KMessageWidget

class Ui_EditRenderPreset_UI(object):
    def setupUi(self, EditRenderPreset_UI):
        if not EditRenderPreset_UI.objectName():
            EditRenderPreset_UI.setObjectName(u"EditRenderPreset_UI")
        EditRenderPreset_UI.resize(463, 630)
        self.verticalLayout_2 = QVBoxLayout(EditRenderPreset_UI)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mainBox = QHBoxLayout()
        self.mainBox.setObjectName(u"mainBox")
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setContentsMargins(-1, 20, 10, -1)
        self.groupLabel = QLabel(EditRenderPreset_UI)
        self.groupLabel.setObjectName(u"groupLabel")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.groupLabel)

        self.presetNameLabel = QLabel(EditRenderPreset_UI)
        self.presetNameLabel.setObjectName(u"presetNameLabel")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.presetNameLabel)

        self.preset_name = QLineEdit(EditRenderPreset_UI)
        self.preset_name.setObjectName(u"preset_name")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.preset_name)

        self.label_2 = QLabel(EditRenderPreset_UI)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.formatCombo = QComboBox(EditRenderPreset_UI)
        self.formatCombo.setObjectName(u"formatCombo")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.formatCombo)

        self.tabWidget = QTabWidget(EditRenderPreset_UI)
        self.tabWidget.setObjectName(u"tabWidget")
        self.video_tab = QWidget()
        self.video_tab.setObjectName(u"video_tab")
        self.verticalLayout_3 = QVBoxLayout(self.video_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.video_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 428, 650))
        self.formLayout_3 = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(-1, -1, 40, -1)
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.resWidth = QSpinBox(self.scrollAreaWidgetContents)
        self.resWidth.setObjectName(u"resWidth")
        self.resWidth.setMinimum(1)
        self.resWidth.setMaximum(8192)
        self.resWidth.setSingleStep(2)
        self.resWidth.setValue(1)

        self.horizontalLayout_3.addWidget(self.resWidth)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(10, 0))
        self.label_9.setText(u"x")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.resHeight = QSpinBox(self.scrollAreaWidgetContents)
        self.resHeight.setObjectName(u"resHeight")
        self.resHeight.setMinimum(1)
        self.resHeight.setMaximum(8192)
        self.resHeight.setSingleStep(2)

        self.horizontalLayout_3.addWidget(self.resHeight)

        self.linkResoultion = QToolButton(self.scrollAreaWidgetContents)
        self.linkResoultion.setObjectName(u"linkResoultion")
        icon = QIcon()
        iconThemeName = u"link"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.linkResoultion.setIcon(icon)
        self.linkResoultion.setCheckable(True)
        self.linkResoultion.setAutoRaise(True)

        self.horizontalLayout_3.addWidget(self.linkResoultion)


        self.formLayout_3.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.parCombo = QComboBox(self.scrollAreaWidgetContents)
        self.parCombo.setObjectName(u"parCombo")
        self.parCombo.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.parCombo)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_16)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.displayAspectNum = QSpinBox(self.scrollAreaWidgetContents)
        self.displayAspectNum.setObjectName(u"displayAspectNum")
        self.displayAspectNum.setMinimum(1)
        self.displayAspectNum.setMaximum(8192)

        self.horizontalLayout_4.addWidget(self.displayAspectNum)

        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(10, 0))
        self.label_17.setText(u":")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_17)

        self.displayAspectDen = QSpinBox(self.scrollAreaWidgetContents)
        self.displayAspectDen.setObjectName(u"displayAspectDen")
        self.displayAspectDen.setMinimum(1)
        self.displayAspectDen.setMaximum(8192)

        self.horizontalLayout_4.addWidget(self.displayAspectDen)


        self.formLayout_3.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.framerateNum = QSpinBox(self.scrollAreaWidgetContents)
        self.framerateNum.setObjectName(u"framerateNum")
        self.framerateNum.setMinimum(1)
        self.framerateNum.setMaximum(1000000)

        self.horizontalLayout.addWidget(self.framerateNum)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMinimumSize(QSize(10, 0))
        self.label_8.setText(u"/")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_8)

        self.framerateDen = QSpinBox(self.scrollAreaWidgetContents)
        self.framerateDen.setObjectName(u"framerateDen")
        self.framerateDen.setMinimum(1)
        self.framerateDen.setMaximum(9999)

        self.horizontalLayout.addWidget(self.framerateDen)


        self.formLayout_3.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.label_22 = QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_22)

        self.frameRateDisplay = QLabel(self.scrollAreaWidgetContents)
        self.frameRateDisplay.setObjectName(u"frameRateDisplay")
        self.frameRateDisplay.setEnabled(True)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.frameRateDisplay)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.scanningCombo = QComboBox(self.scrollAreaWidgetContents)
        self.scanningCombo.addItem("")
        self.scanningCombo.addItem("")
        self.scanningCombo.setObjectName(u"scanningCombo")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.scanningCombo)

        self.fieldOrderLabel = QLabel(self.scrollAreaWidgetContents)
        self.fieldOrderLabel.setObjectName(u"fieldOrderLabel")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.fieldOrderLabel)

        self.fieldOrderCombo = QComboBox(self.scrollAreaWidgetContents)
        self.fieldOrderCombo.addItem("")
        self.fieldOrderCombo.addItem("")
        self.fieldOrderCombo.setObjectName(u"fieldOrderCombo")
        self.fieldOrderCombo.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.fieldOrderCombo)

        self.colorspaceLabel = QLabel(self.scrollAreaWidgetContents)
        self.colorspaceLabel.setObjectName(u"colorspaceLabel")
        self.colorspaceLabel.setEnabled(False)

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.colorspaceLabel)

        self.colorspaceCombo = QComboBox(self.scrollAreaWidgetContents)
        self.colorspaceCombo.setObjectName(u"colorspaceCombo")
        self.colorspaceCombo.setEnabled(False)

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.colorspaceCombo)

        self.vCodecCombo = QComboBox(self.scrollAreaWidgetContents)
        self.vCodecCombo.setObjectName(u"vCodecCombo")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.vCodecCombo.sizePolicy().hasHeightForWidth())
        self.vCodecCombo.setSizePolicy(sizePolicy2)

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.vCodecCombo)

        self.vRateControlCombo = QComboBox(self.scrollAreaWidgetContents)
        self.vRateControlCombo.setObjectName(u"vRateControlCombo")
        sizePolicy2.setHeightForWidth(self.vRateControlCombo.sizePolicy().hasHeightForWidth())
        self.vRateControlCombo.setSizePolicy(sizePolicy2)

        self.formLayout_3.setWidget(9, QFormLayout.FieldRole, self.vRateControlCombo)

        self.label_24 = QLabel(self.scrollAreaWidgetContents)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.label_24)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(9, QFormLayout.LabelRole, self.label_12)

        self.default_vbitrate_label = QLabel(self.scrollAreaWidgetContents)
        self.default_vbitrate_label.setObjectName(u"default_vbitrate_label")

        self.formLayout_3.setWidget(10, QFormLayout.LabelRole, self.default_vbitrate_label)

        self.default_vbitrate = QSpinBox(self.scrollAreaWidgetContents)
        self.default_vbitrate.setObjectName(u"default_vbitrate")
        self.default_vbitrate.setMaximum(500000)

        self.formLayout_3.setWidget(10, QFormLayout.FieldRole, self.default_vbitrate)

        self.vBuffer_label = QLabel(self.scrollAreaWidgetContents)
        self.vBuffer_label.setObjectName(u"vBuffer_label")

        self.formLayout_3.setWidget(11, QFormLayout.LabelRole, self.vBuffer_label)

        self.vBuffer = QSpinBox(self.scrollAreaWidgetContents)
        self.vBuffer.setObjectName(u"vBuffer")
        self.vBuffer.setMaximum(9999)

        self.formLayout_3.setWidget(11, QFormLayout.FieldRole, self.vBuffer)

        self.vquality_label = QLabel(self.scrollAreaWidgetContents)
        self.vquality_label.setObjectName(u"vquality_label")

        self.formLayout_3.setWidget(12, QFormLayout.LabelRole, self.vquality_label)

        self.default_vquality = QSpinBox(self.scrollAreaWidgetContents)
        self.default_vquality.setObjectName(u"default_vquality")
        self.default_vquality.setMaximum(500000)

        self.formLayout_3.setWidget(12, QFormLayout.FieldRole, self.default_vquality)

        self.label_26 = QLabel(self.scrollAreaWidgetContents)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_3.setWidget(13, QFormLayout.LabelRole, self.label_26)

        self.gopSpinner = QSpinBox(self.scrollAreaWidgetContents)
        self.gopSpinner.setObjectName(u"gopSpinner")
        self.gopSpinner.setMaximum(999)
        self.gopSpinner.setSingleStep(1)

        self.formLayout_3.setWidget(13, QFormLayout.FieldRole, self.gopSpinner)

        self.fixedGop = QCheckBox(self.scrollAreaWidgetContents)
        self.fixedGop.setObjectName(u"fixedGop")
        self.fixedGop.setEnabled(False)

        self.formLayout_3.setWidget(14, QFormLayout.FieldRole, self.fixedGop)

        self.bFramesSpinner = QSpinBox(self.scrollAreaWidgetContents)
        self.bFramesSpinner.setObjectName(u"bFramesSpinner")
        self.bFramesSpinner.setEnabled(False)
        self.bFramesSpinner.setMinimum(-1)
        self.bFramesSpinner.setMaximum(8)
        self.bFramesSpinner.setValue(-1)

        self.formLayout_3.setWidget(15, QFormLayout.FieldRole, self.bFramesSpinner)

        self.bFramesLabel = QLabel(self.scrollAreaWidgetContents)
        self.bFramesLabel.setObjectName(u"bFramesLabel")

        self.formLayout_3.setWidget(15, QFormLayout.LabelRole, self.bFramesLabel)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.video_tab, "")
        self.audio_tab = QWidget()
        self.audio_tab.setObjectName(u"audio_tab")
        self.formLayout_2 = QFormLayout(self.audio_tab)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_15 = QLabel(self.audio_tab)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_15)

        self.audioChannels = QComboBox(self.audio_tab)
        self.audioChannels.setObjectName(u"audioChannels")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.audioChannels)

        self.label_13 = QLabel(self.audio_tab)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.aCodecCombo = QComboBox(self.audio_tab)
        self.aCodecCombo.setObjectName(u"aCodecCombo")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.aCodecCombo)

        self.label_11 = QLabel(self.audio_tab)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.audioSampleRate = QComboBox(self.audio_tab)
        self.audioSampleRate.addItem("")
        self.audioSampleRate.addItem("")
        self.audioSampleRate.addItem("")
        self.audioSampleRate.addItem("")
        self.audioSampleRate.addItem("")
        self.audioSampleRate.addItem("")
        self.audioSampleRate.addItem("")
        self.audioSampleRate.addItem("")
        self.audioSampleRate.setObjectName(u"audioSampleRate")
        self.audioSampleRate.setEditable(True)

        self.horizontalLayout_5.addWidget(self.audioSampleRate)

        self.label_20 = QLabel(self.audio_tab)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_5.addWidget(self.label_20)


        self.formLayout_2.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.label_14 = QLabel(self.audio_tab)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_14)

        self.aRateControlCombo = QComboBox(self.audio_tab)
        self.aRateControlCombo.setObjectName(u"aRateControlCombo")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.aRateControlCombo)

        self.label_18 = QLabel(self.audio_tab)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_18)

        self.aBitrate = QSpinBox(self.audio_tab)
        self.aBitrate.setObjectName(u"aBitrate")
        self.aBitrate.setMaximum(500000)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.aBitrate)

        self.label_19 = QLabel(self.audio_tab)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_19)

        self.aQuality = QSpinBox(self.audio_tab)
        self.aQuality.setObjectName(u"aQuality")
        self.aQuality.setMaximum(500000)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.aQuality)

        self.tabWidget.addTab(self.audio_tab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.speedsLabel = QLabel(self.tab)
        self.speedsLabel.setObjectName(u"speedsLabel")

        self.verticalLayout.addWidget(self.speedsLabel)

        self.speeds_list = QTextEdit(self.tab)
        self.speeds_list.setObjectName(u"speeds_list")
        self.speeds_list.setAcceptRichText(False)

        self.verticalLayout.addWidget(self.speeds_list)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.overrideParamsWarning = KMessageWidget(self.tab)
        self.overrideParamsWarning.setObjectName(u"overrideParamsWarning")
        self.overrideParamsWarning.setProperty("wordWrap", True)
        self.overrideParamsWarning.setProperty("closeButtonVisible", False)

        self.verticalLayout.addWidget(self.overrideParamsWarning)

        self.additionalParams = QPlainTextEdit(self.tab)
        self.additionalParams.setObjectName(u"additionalParams")

        self.verticalLayout.addWidget(self.additionalParams)

        self.parametersLabel = QLabel(self.tab)
        self.parametersLabel.setObjectName(u"parametersLabel")
        self.parametersLabel.setTextFormat(Qt.RichText)
        self.parametersLabel.setWordWrap(True)
        self.parametersLabel.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.parametersLabel)

        self.tabWidget.addTab(self.tab, "")

        self.formLayout_6.setWidget(4, QFormLayout.SpanningRole, self.tabWidget)

        self.parameters = QTextEdit(EditRenderPreset_UI)
        self.parameters.setObjectName(u"parameters")
        self.parameters.setReadOnly(True)
        self.parameters.setAcceptRichText(False)

        self.formLayout_6.setWidget(5, QFormLayout.SpanningRole, self.parameters)

        self.groupName = QComboBox(EditRenderPreset_UI)
        self.groupName.setObjectName(u"groupName")
        sizePolicy2.setHeightForWidth(self.groupName.sizePolicy().hasHeightForWidth())
        self.groupName.setSizePolicy(sizePolicy2)
        self.groupName.setEditable(True)
        self.groupName.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.groupName)


        self.mainBox.addLayout(self.formLayout_6)


        self.verticalLayout_2.addLayout(self.mainBox)

        self.buttonBox = QDialogButtonBox(EditRenderPreset_UI)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(EditRenderPreset_UI)
        self.buttonBox.rejected.connect(EditRenderPreset_UI.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(EditRenderPreset_UI)
    # setupUi

    def retranslateUi(self, EditRenderPreset_UI):
        EditRenderPreset_UI.setWindowTitle(QCoreApplication.translate("EditRenderPreset_UI", u"Save Render Preset", None))
        self.groupLabel.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Group:", None))
        self.presetNameLabel.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Preset name:", None))
        self.label_2.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Container:", None))
        self.label_4.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Resolution:", None))
        self.linkResoultion.setText(QCoreApplication.translate("EditRenderPreset_UI", u"...", None))
        self.label_6.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Pixel Aspect Ratio:", None))
        self.label_16.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Display Aspect Ratio:", None))
        self.label_3.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Frame Rate:", None))
        self.label_22.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Fields per Second:", None))
        self.frameRateDisplay.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Placeholder", None))
        self.label_7.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Scanning:", None))
        self.scanningCombo.setItemText(0, QCoreApplication.translate("EditRenderPreset_UI", u"Interlaced", None))
        self.scanningCombo.setItemText(1, QCoreApplication.translate("EditRenderPreset_UI", u"Progressive", None))

        self.fieldOrderLabel.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Field Order:", None))
        self.fieldOrderCombo.setItemText(0, QCoreApplication.translate("EditRenderPreset_UI", u"Bottom Field First", None))
        self.fieldOrderCombo.setItemText(1, QCoreApplication.translate("EditRenderPreset_UI", u"Top Field First", None))

        self.colorspaceLabel.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Colorspace:", None))
        self.label_24.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Codec:", None))
        self.label_12.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Rate Control:", None))
        self.default_vbitrate_label.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Bitrate:", None))
        self.default_vbitrate.setSuffix(QCoreApplication.translate("EditRenderPreset_UI", u"k", None))
        self.vBuffer_label.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Buffer Size:", None))
        self.vBuffer.setSuffix(QCoreApplication.translate("EditRenderPreset_UI", u" KiB", None))
        self.vquality_label.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Quality:", None))
#if QT_CONFIG(tooltip)
        self.label_26.setToolTip(QCoreApplication.translate("EditRenderPreset_UI", u"GOP = Group of Pictures", None))
#endif // QT_CONFIG(tooltip)
        self.label_26.setText(QCoreApplication.translate("EditRenderPreset_UI", u"GOP:", None))
        self.gopSpinner.setSpecialValueText(QCoreApplication.translate("EditRenderPreset_UI", u"Auto", None))
        self.gopSpinner.setSuffix(QCoreApplication.translate("EditRenderPreset_UI", u" frame(s)", None))
#if QT_CONFIG(tooltip)
        self.fixedGop.setToolTip(QCoreApplication.translate("EditRenderPreset_UI", u"A fixed GOP means that keyframes will not be inserted at detected scene changes.", None))
#endif // QT_CONFIG(tooltip)
        self.fixedGop.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Fixed", None))
        self.bFramesSpinner.setSpecialValueText(QCoreApplication.translate("EditRenderPreset_UI", u"Auto", None))
        self.bFramesSpinner.setSuffix(QCoreApplication.translate("EditRenderPreset_UI", u" frame(s)", None))
        self.bFramesLabel.setText(QCoreApplication.translate("EditRenderPreset_UI", u"B Frames:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.video_tab), QCoreApplication.translate("EditRenderPreset_UI", u"Video", None))
        self.label_15.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Channels:", None))
        self.label_13.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Codec:", None))
        self.label_11.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Sample Rate:", None))
        self.audioSampleRate.setItemText(0, QCoreApplication.translate("EditRenderPreset_UI", u"8000", None))
        self.audioSampleRate.setItemText(1, QCoreApplication.translate("EditRenderPreset_UI", u"12000", None))
        self.audioSampleRate.setItemText(2, QCoreApplication.translate("EditRenderPreset_UI", u"16000", None))
        self.audioSampleRate.setItemText(3, QCoreApplication.translate("EditRenderPreset_UI", u"22050", None))
        self.audioSampleRate.setItemText(4, QCoreApplication.translate("EditRenderPreset_UI", u"32000", None))
        self.audioSampleRate.setItemText(5, QCoreApplication.translate("EditRenderPreset_UI", u"44100", None))
        self.audioSampleRate.setItemText(6, QCoreApplication.translate("EditRenderPreset_UI", u"48000", None))
        self.audioSampleRate.setItemText(7, QCoreApplication.translate("EditRenderPreset_UI", u"96000", None))

        self.label_20.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Hz", None))
        self.label_14.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Rate Control:", None))
        self.label_18.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Bitrate:", None))
        self.aBitrate.setSuffix(QCoreApplication.translate("EditRenderPreset_UI", u"k", None))
        self.label_19.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Quality:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.audio_tab), QCoreApplication.translate("EditRenderPreset_UI", u"Audio", None))
        self.speedsLabel.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Speed options:", None))
#if QT_CONFIG(tooltip)
        self.speeds_list.setToolTip(QCoreApplication.translate("EditRenderPreset_UI", u"One line of options per speedup step, from slowest to fastest", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("EditRenderPreset_UI", u"Additional Parameters:", None))
        self.parametersLabel.setText(QCoreApplication.translate("EditRenderPreset_UI", u"<html><head/><body><p>See <a href=\"https://www.mltframework.org/plugins/ConsumerAvformat/\"><span style=\" text-decoration: underline; color:#2980b9;\">MLT documentation</span></a> for reference.</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("EditRenderPreset_UI", u"Other", None))
    # retranslateUi

