# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'time.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)

from kmessagewidget import KMessageWidget

class Ui_TimeRemap_UI(object):
    def setupUi(self, TimeRemap_UI):
        if not TimeRemap_UI.objectName():
            TimeRemap_UI.setObjectName(u"TimeRemap_UI")
        TimeRemap_UI.resize(398, 379)
        self.gridLayout_2 = QGridLayout(TimeRemap_UI)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.warningMessage = KMessageWidget(TimeRemap_UI)
        self.warningMessage.setObjectName(u"warningMessage")
        self.warningMessage.setWordWrap(True)
        self.warningMessage.setCloseButtonVisible(False)
        self.warningMessage.setMessageType(KMessageWidget.Warning)

        self.gridLayout_2.addWidget(self.warningMessage, 0, 0, 1, 1)

        self.remap_box = QFrame(TimeRemap_UI)
        self.remap_box.setObjectName(u"remap_box")
        self.remap_box.setFrameShape(QFrame.NoFrame)
        self.remap_box.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.remap_box)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.remap_box)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.button_center_top = QToolButton(self.remap_box)
        self.button_center_top.setObjectName(u"button_center_top")
        icon = QIcon()
        iconThemeName = u"align-horizontal-center"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.button_center_top.setIcon(icon)
        self.button_center_top.setAutoRaise(True)

        self.horizontalLayout_6.addWidget(self.button_center_top)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.horizontalSpacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer1)


        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.remapLayout = QVBoxLayout()
        self.remapLayout.setObjectName(u"remapLayout")

        self.gridLayout.addLayout(self.remapLayout, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.remap_box)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.button_center = QToolButton(self.remap_box)
        self.button_center.setObjectName(u"button_center")
        self.button_center.setIcon(icon)
        self.button_center.setAutoRaise(True)

        self.horizontalLayout_7.addWidget(self.button_center)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.button_prev = QToolButton(self.remap_box)
        self.button_prev.setObjectName(u"button_prev")
        self.button_prev.setAutoRaise(True)

        self.horizontalLayout_8.addWidget(self.button_prev)

        self.button_add = QToolButton(self.remap_box)
        self.button_add.setObjectName(u"button_add")
        self.button_add.setAutoRaise(True)

        self.horizontalLayout_8.addWidget(self.button_add)

        self.button_next = QToolButton(self.remap_box)
        self.button_next.setObjectName(u"button_next")
        self.button_next.setAutoRaise(True)

        self.horizontalLayout_8.addWidget(self.button_next)

        self.horizontalSpacer_3 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)

        self.info_frame = QFrame(self.remap_box)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setFrameShape(QFrame.NoFrame)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.info_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.info_frame)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.inLayout = QHBoxLayout()
        self.inLayout.setObjectName(u"inLayout")

        self.horizontalLayout_9.addLayout(self.inLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.info_frame)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.outLayout = QHBoxLayout()
        self.outLayout.setObjectName(u"outLayout")

        self.horizontalLayout_10.addLayout(self.outLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_9 = QLabel(self.info_frame)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.speedBefore = QDoubleSpinBox(self.info_frame)
        self.speedBefore.setObjectName(u"speedBefore")
        self.speedBefore.setMinimum(-100000.000000000000000)
        self.speedBefore.setMaximum(100000.000000000000000)
        self.speedBefore.setValue(100.000000000000000)

        self.horizontalLayout_11.addWidget(self.speedBefore)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.info_frame)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.speedAfter = QDoubleSpinBox(self.info_frame)
        self.speedAfter.setObjectName(u"speedAfter")
        self.speedAfter.setMinimum(-100000.000000000000000)
        self.speedAfter.setMaximum(100000.000000000000000)
        self.speedAfter.setValue(100.000000000000000)

        self.horizontalLayout_12.addWidget(self.speedAfter)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)


        self.gridLayout.addWidget(self.info_frame, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pitch_compensate = QCheckBox(self.remap_box)
        self.pitch_compensate.setObjectName(u"pitch_compensate")
        self.pitch_compensate.setChecked(True)
        self.pitch_compensate.setTristate(False)

        self.horizontalLayout_13.addWidget(self.pitch_compensate)

        self.frame_blending = QCheckBox(self.remap_box)
        self.frame_blending.setObjectName(u"frame_blending")

        self.horizontalLayout_13.addWidget(self.frame_blending)


        self.gridLayout.addLayout(self.horizontalLayout_13, 6, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.move_next = QCheckBox(self.remap_box)
        self.move_next.setObjectName(u"move_next")
        self.move_next.setChecked(True)

        self.horizontalLayout_14.addWidget(self.move_next)

        self.button_del = QToolButton(self.remap_box)
        self.button_del.setObjectName(u"button_del")
        icon1 = QIcon()
        iconThemeName = u"edit-delete"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.button_del.setIcon(icon1)

        self.horizontalLayout_14.addWidget(self.button_del)


        self.gridLayout.addLayout(self.horizontalLayout_14, 7, 0, 1, 1)


        self.gridLayout_2.addWidget(self.remap_box, 1, 0, 1, 1)


        self.retranslateUi(TimeRemap_UI)

        QMetaObject.connectSlotsByName(TimeRemap_UI)
    # setupUi

    def retranslateUi(self, TimeRemap_UI):
        TimeRemap_UI.setWindowTitle(QCoreApplication.translate("TimeRemap_UI", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("TimeRemap_UI", u"Source clip", None))
        self.button_center_top.setText(QCoreApplication.translate("TimeRemap_UI", u"...", None))
        self.label_5.setText(QCoreApplication.translate("TimeRemap_UI", u"Output", None))
        self.button_center.setText(QCoreApplication.translate("TimeRemap_UI", u"...", None))
        self.button_prev.setText(QCoreApplication.translate("TimeRemap_UI", u"...", None))
        self.button_add.setText(QCoreApplication.translate("TimeRemap_UI", u"...", None))
        self.button_next.setText(QCoreApplication.translate("TimeRemap_UI", u"...", None))
        self.label_7.setText(QCoreApplication.translate("TimeRemap_UI", u"Source time", None))
        self.label_8.setText(QCoreApplication.translate("TimeRemap_UI", u"Output time", None))
        self.label_9.setText(QCoreApplication.translate("TimeRemap_UI", u"Speed before", None))
        self.label_10.setText(QCoreApplication.translate("TimeRemap_UI", u"After", None))
        self.pitch_compensate.setText(QCoreApplication.translate("TimeRemap_UI", u"Pitch compensation", None))
        self.frame_blending.setText(QCoreApplication.translate("TimeRemap_UI", u"Frame blending", None))
        self.move_next.setText(QCoreApplication.translate("TimeRemap_UI", u"Preserve speed of next keyframes", None))
        self.button_del.setText(QCoreApplication.translate("TimeRemap_UI", u"...", None))
    # retranslateUi

