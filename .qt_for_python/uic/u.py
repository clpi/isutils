# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'u.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import openshot_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(580, 501)
        icon = QIcon()
        icon.addFile(u":/openshot.svg", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.vbox_parent = QVBoxLayout()
        self.vbox_parent.setObjectName(u"vbox_parent")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.vboxTreeParent = QVBoxLayout()
        self.vboxTreeParent.setObjectName(u"vboxTreeParent")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btnMoveUp = QPushButton(Dialog)
        self.btnMoveUp.setObjectName(u"btnMoveUp")
        icon1 = QIcon()
        iconThemeName = u"go-up"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u"", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnMoveUp.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.btnMoveUp)

        self.btnMoveDown = QPushButton(Dialog)
        self.btnMoveDown.setObjectName(u"btnMoveDown")
        icon2 = QIcon()
        iconThemeName = u"go-down"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u"", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnMoveDown.setIcon(icon2)

        self.horizontalLayout_6.addWidget(self.btnMoveDown)

        self.btnShuffle = QPushButton(Dialog)
        self.btnShuffle.setObjectName(u"btnShuffle")
        icon3 = QIcon()
        iconThemeName = u"view-refresh"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u"", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnShuffle.setIcon(icon3)

        self.horizontalLayout_6.addWidget(self.btnShuffle)

        self.btnRemove = QPushButton(Dialog)
        self.btnRemove.setObjectName(u"btnRemove")
        icon4 = QIcon()
        iconThemeName = u"list-remove"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u"", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnRemove.setIcon(icon4)

        self.horizontalLayout_6.addWidget(self.btnRemove)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.vboxTreeParent.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_2.addLayout(self.vboxTreeParent)

        self.vbox_properties = QVBoxLayout()
        self.vbox_properties.setObjectName(u"vbox_properties")
        self.lblTimelineLocation = QLabel(Dialog)
        self.lblTimelineLocation.setObjectName(u"lblTimelineLocation")
        self.lblTimelineLocation.setStyleSheet(u"font-weight: bold")
        self.lblTimelineLocation.setMargin(0)

        self.vbox_properties.addWidget(self.lblTimelineLocation)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lblStartTime = QLabel(Dialog)
        self.lblStartTime.setObjectName(u"lblStartTime")
        self.lblStartTime.setMinimumSize(QSize(100, 0))
        self.lblStartTime.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.lblStartTime)

        self.txtStartTime = QDoubleSpinBox(Dialog)
        self.txtStartTime.setObjectName(u"txtStartTime")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtStartTime.sizePolicy().hasHeightForWidth())
        self.txtStartTime.setSizePolicy(sizePolicy)
        self.txtStartTime.setMinimumSize(QSize(150, 0))
        self.txtStartTime.setMaximum(999999999.000000000000000)

        self.horizontalLayout_4.addWidget(self.txtStartTime)


        self.vbox_properties.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblTrack = QLabel(Dialog)
        self.lblTrack.setObjectName(u"lblTrack")
        self.lblTrack.setMinimumSize(QSize(100, 0))
        self.lblTrack.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.lblTrack)

        self.cmbTrack = QComboBox(Dialog)
        self.cmbTrack.setObjectName(u"cmbTrack")
        self.cmbTrack.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_3.addWidget(self.cmbTrack)


        self.vbox_properties.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_11.addWidget(self.label_3)

        self.txtImageLength = QDoubleSpinBox(Dialog)
        self.txtImageLength.setObjectName(u"txtImageLength")
        sizePolicy.setHeightForWidth(self.txtImageLength.sizePolicy().hasHeightForWidth())
        self.txtImageLength.setSizePolicy(sizePolicy)
        self.txtImageLength.setMinimumSize(QSize(150, 0))
        self.txtImageLength.setMaximum(999999999.000000000000000)

        self.horizontalLayout_11.addWidget(self.txtImageLength)


        self.vbox_properties.addLayout(self.horizontalLayout_11)

        self.lblFade = QLabel(Dialog)
        self.lblFade.setObjectName(u"lblFade")
        self.lblFade.setStyleSheet(u"font-weight: bold; margin-top: 15px;")
        self.lblFade.setMargin(0)

        self.vbox_properties.addWidget(self.lblFade)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblFade1 = QLabel(Dialog)
        self.lblFade1.setObjectName(u"lblFade1")
        self.lblFade1.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.lblFade1)

        self.cmbFade = QComboBox(Dialog)
        self.cmbFade.setObjectName(u"cmbFade")
        self.cmbFade.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_5.addWidget(self.cmbFade)


        self.vbox_properties.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lblFadeLength = QLabel(Dialog)
        self.lblFadeLength.setObjectName(u"lblFadeLength")
        self.lblFadeLength.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.lblFadeLength)

        self.txtFadeLength = QDoubleSpinBox(Dialog)
        self.txtFadeLength.setObjectName(u"txtFadeLength")
        self.txtFadeLength.setMinimumSize(QSize(150, 0))
        self.txtFadeLength.setMaximum(999999999.000000000000000)
        self.txtFadeLength.setValue(2.000000000000000)

        self.horizontalLayout_8.addWidget(self.txtFadeLength)


        self.vbox_properties.addLayout(self.horizontalLayout_8)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-weight: bold; margin-top: 15px;")

        self.vbox_properties.addWidget(self.label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.cmbZoom = QComboBox(Dialog)
        self.cmbZoom.setObjectName(u"cmbZoom")
        self.cmbZoom.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_7.addWidget(self.cmbZoom)


        self.vbox_properties.addLayout(self.horizontalLayout_7)

        self.lblTransition = QLabel(Dialog)
        self.lblTransition.setObjectName(u"lblTransition")
        self.lblTransition.setStyleSheet(u"font-weight: bold; margin-top: 15px;")
        self.lblTransition.setMargin(0)

        self.vbox_properties.addWidget(self.lblTransition)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lblTransition1 = QLabel(Dialog)
        self.lblTransition1.setObjectName(u"lblTransition1")
        self.lblTransition1.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.lblTransition1)

        self.cmbTransition = QComboBox(Dialog)
        self.cmbTransition.setObjectName(u"cmbTransition")
        self.cmbTransition.setMinimumSize(QSize(150, 0))
        self.cmbTransition.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_9.addWidget(self.cmbTransition)


        self.vbox_properties.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lblTransitionLength = QLabel(Dialog)
        self.lblTransitionLength.setObjectName(u"lblTransitionLength")
        self.lblTransitionLength.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.lblTransitionLength)

        self.txtTransitionLength = QDoubleSpinBox(Dialog)
        self.txtTransitionLength.setObjectName(u"txtTransitionLength")
        self.txtTransitionLength.setMinimumSize(QSize(150, 0))
        self.txtTransitionLength.setMaximum(999999999.000000000000000)
        self.txtTransitionLength.setValue(2.000000000000000)

        self.horizontalLayout_10.addWidget(self.txtTransitionLength)


        self.vbox_properties.addLayout(self.horizontalLayout_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vbox_properties.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.vbox_properties)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.vbox_parent.addLayout(self.verticalLayout)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.lblTotalLength = QLabel(Dialog)
        self.lblTotalLength.setObjectName(u"lblTotalLength")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblTotalLength.sizePolicy().hasHeightForWidth())
        self.lblTotalLength.setSizePolicy(sizePolicy1)
        self.lblTotalLength.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.lblTotalLength)

        self.lblTotalLengthValue = QLabel(Dialog)
        self.lblTotalLengthValue.setObjectName(u"lblTotalLengthValue")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lblTotalLengthValue.sizePolicy().hasHeightForWidth())
        self.lblTotalLengthValue.setSizePolicy(sizePolicy2)
        self.lblTotalLengthValue.setMinimumSize(QSize(75, 0))
        self.lblTotalLengthValue.setStyleSheet(u"font-weight:bold;")
        self.lblTotalLengthValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.lblTotalLengthValue)


        self.vbox_parent.addLayout(self.horizontalLayout_12)

        self.btnBox = QDialogButtonBox(Dialog)
        self.btnBox.setObjectName(u"btnBox")
        self.btnBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.btnBox.setCenterButtons(False)

        self.vbox_parent.addWidget(self.btnBox)


        self.horizontalLayout.addLayout(self.vbox_parent)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Add To Timeline", None))
#if QT_CONFIG(tooltip)
        self.btnMoveUp.setToolTip(QCoreApplication.translate("Dialog", u"Move Up", None))
#endif // QT_CONFIG(tooltip)
        self.btnMoveUp.setText("")
#if QT_CONFIG(tooltip)
        self.btnMoveDown.setToolTip(QCoreApplication.translate("Dialog", u"Move Down", None))
#endif // QT_CONFIG(tooltip)
        self.btnMoveDown.setText("")
#if QT_CONFIG(tooltip)
        self.btnShuffle.setToolTip(QCoreApplication.translate("Dialog", u"Shuffle", None))
#endif // QT_CONFIG(tooltip)
        self.btnShuffle.setText("")
#if QT_CONFIG(tooltip)
        self.btnRemove.setToolTip(QCoreApplication.translate("Dialog", u"Remove", None))
#endif // QT_CONFIG(tooltip)
        self.btnRemove.setText("")
        self.lblTimelineLocation.setText(QCoreApplication.translate("Dialog", u"Timeline Location", None))
        self.lblStartTime.setText(QCoreApplication.translate("Dialog", u"Start Time (seconds):", None))
        self.lblTrack.setText(QCoreApplication.translate("Dialog", u"Track:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Image Length (seconds):", None))
        self.lblFade.setText(QCoreApplication.translate("Dialog", u"Fade", None))
        self.lblFade1.setText(QCoreApplication.translate("Dialog", u"Fade:", None))
        self.lblFadeLength.setText(QCoreApplication.translate("Dialog", u"Length (seconds):", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Zoom", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Zoom:", None))
        self.lblTransition.setText(QCoreApplication.translate("Dialog", u"Transition", None))
        self.lblTransition1.setText(QCoreApplication.translate("Dialog", u"Transition:", None))
        self.lblTransitionLength.setText(QCoreApplication.translate("Dialog", u"Length:", None))
        self.lblTotalLength.setText(QCoreApplication.translate("Dialog", u"Total Length (seconds):", None))
        self.lblTotalLengthValue.setText(QCoreApplication.translate("Dialog", u"0.0", None))
    # retranslateUi

