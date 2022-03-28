# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prof.ui'
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
    QDialogButtonBox, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QToolButton, QWidget)

from kcombobox import KComboBox
from kmessagewidget import KMessageWidget

class Ui_ProfilesDialog_UI(object):
    def setupUi(self, ProfilesDialog_UI):
        if not ProfilesDialog_UI.objectName():
            ProfilesDialog_UI.setObjectName(u"ProfilesDialog_UI")
        ProfilesDialog_UI.resize(594, 639)
        self.gridLayout_2 = QGridLayout(ProfilesDialog_UI)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.button_create = QToolButton(ProfilesDialog_UI)
        self.button_create.setObjectName(u"button_create")
        icon = QIcon()
        iconThemeName = u"document-new"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.button_create.setIcon(icon)

        self.gridLayout_2.addWidget(self.button_create, 0, 4, 1, 1)

        self.label = QLabel(ProfilesDialog_UI)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.button_delete = QToolButton(ProfilesDialog_UI)
        self.button_delete.setObjectName(u"button_delete")
        self.button_delete.setEnabled(False)
        icon1 = QIcon()
        iconThemeName = u"delete"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.button_delete.setIcon(icon1)

        self.gridLayout_2.addWidget(self.button_delete, 0, 6, 1, 1)

        self.properties = QGroupBox(ProfilesDialog_UI)
        self.properties.setObjectName(u"properties")
        self.gridLayout = QGridLayout(self.properties)
        self.gridLayout.setObjectName(u"gridLayout")
        self.aspect_den = QSpinBox(self.properties)
        self.aspect_den.setObjectName(u"aspect_den")
        self.aspect_den.setMinimum(1)
        self.aspect_den.setMaximum(10000)

        self.gridLayout.addWidget(self.aspect_den, 4, 3, 1, 1)

        self.size_w = QSpinBox(self.properties)
        self.size_w.setObjectName(u"size_w")
        self.size_w.setMinimum(1)
        self.size_w.setMaximum(10000)

        self.gridLayout.addWidget(self.size_w, 1, 1, 1, 1)

        self.size_h = QSpinBox(self.properties)
        self.size_h.setObjectName(u"size_h")
        self.size_h.setMinimum(1)
        self.size_h.setMaximum(10000)

        self.gridLayout.addWidget(self.size_h, 1, 3, 1, 1)

        self.fields = QLabel(self.properties)
        self.fields.setObjectName(u"fields")
        self.fields.setText(u"interl: 2*fps")

        self.gridLayout.addWidget(self.fields, 3, 3, 1, 1)

        self.label_dar = QLabel(self.properties)
        self.label_dar.setObjectName(u"label_dar")
        self.label_dar.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_dar, 5, 0, 1, 1)

        self.label_3 = QLabel(self.properties)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.description = QLineEdit(self.properties)
        self.description.setObjectName(u"description")

        self.gridLayout.addWidget(self.description, 0, 1, 1, 3)

        self.colorspace = KComboBox(self.properties)
        self.colorspace.setObjectName(u"colorspace")

        self.gridLayout.addWidget(self.colorspace, 7, 1, 1, 3)

        self.label_8 = QLabel(self.properties)
        self.label_8.setObjectName(u"label_8")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_8, 5, 2, 1, 1)

        self.field_order = QComboBox(self.properties)
        self.field_order.addItem("")
        self.field_order.addItem("")
        self.field_order.setObjectName(u"field_order")

        self.gridLayout.addWidget(self.field_order, 9, 1, 1, 3)

        self.display_num = QSpinBox(self.properties)
        self.display_num.setObjectName(u"display_num")
        self.display_num.setMinimum(1)
        self.display_num.setMaximum(10000)

        self.gridLayout.addWidget(self.display_num, 5, 1, 1, 1)

        self.label_scanning = QLabel(self.properties)
        self.label_scanning.setObjectName(u"label_scanning")
        self.label_scanning.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_scanning, 8, 0, 1, 1)

        self.label_4 = QLabel(self.properties)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)

        self.aspect_num = QSpinBox(self.properties)
        self.aspect_num.setObjectName(u"aspect_num")
        self.aspect_num.setMinimum(1)
        self.aspect_num.setMaximum(10000)

        self.gridLayout.addWidget(self.aspect_num, 4, 1, 1, 1)

        self.label_6 = QLabel(self.properties)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)

        self.label_2 = QLabel(self.properties)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.scanning = QComboBox(self.properties)
        self.scanning.addItem("")
        self.scanning.addItem("")
        self.scanning.setObjectName(u"scanning")

        self.gridLayout.addWidget(self.scanning, 8, 1, 1, 3)

        self.frame_num = QSpinBox(self.properties)
        self.frame_num.setObjectName(u"frame_num")
        self.frame_num.setMinimum(1)
        self.frame_num.setMaximum(500000)

        self.gridLayout.addWidget(self.frame_num, 2, 1, 1, 1)

        self.display_den = QSpinBox(self.properties)
        self.display_den.setObjectName(u"display_den")
        self.display_den.setMinimum(1)
        self.display_den.setMaximum(10000)

        self.gridLayout.addWidget(self.display_den, 5, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(105, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 11, 0, 1, 2)

        self.label_9 = QLabel(self.properties)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_12 = QLabel(self.properties)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_12, 7, 0, 1, 1)

        self.label_5 = QLabel(self.properties)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_field_order = QLabel(self.properties)
        self.label_field_order.setObjectName(u"label_field_order")
        self.label_field_order.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_field_order, 9, 0, 1, 1)

        self.label_7 = QLabel(self.properties)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_7, 4, 2, 1, 1)

        self.frame_den = QSpinBox(self.properties)
        self.frame_den.setObjectName(u"frame_den")
        self.frame_den.setMinimum(1)
        self.frame_den.setMaximum(10000)

        self.gridLayout.addWidget(self.frame_den, 2, 3, 1, 1)

        self.label_11 = QLabel(self.properties)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)

        self.effect_warning = KMessageWidget(self.properties)
        self.effect_warning.setObjectName(u"effect_warning")
        self.effect_warning.setWordWrap(True)
        self.effect_warning.setCloseButtonVisible(False)
        self.effect_warning.setMessageType(KMessageWidget.Warning)

        self.gridLayout.addWidget(self.effect_warning, 10, 1, 1, 3)


        self.gridLayout_2.addWidget(self.properties, 1, 0, 1, 8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.button_save = QToolButton(ProfilesDialog_UI)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setEnabled(False)
        icon2 = QIcon()
        iconThemeName = u"document-save"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.button_save.setIcon(icon2)

        self.gridLayout_2.addWidget(self.button_save, 0, 5, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 3, 3, 1, 2)

        self.buttonBox = QDialogButtonBox(ProfilesDialog_UI)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.gridLayout_2.addWidget(self.buttonBox, 3, 5, 1, 3)

        self.profiles_list = QComboBox(ProfilesDialog_UI)
        self.profiles_list.setObjectName(u"profiles_list")

        self.gridLayout_2.addWidget(self.profiles_list, 0, 1, 1, 1)

        self.button_default = QPushButton(ProfilesDialog_UI)
        self.button_default.setObjectName(u"button_default")

        self.gridLayout_2.addWidget(self.button_default, 3, 0, 1, 3)

        self.info_message = KMessageWidget(ProfilesDialog_UI)
        self.info_message.setObjectName(u"info_message")
        self.info_message.setWordWrap(True)

        self.gridLayout_2.addWidget(self.info_message, 2, 0, 1, 8)


        self.retranslateUi(ProfilesDialog_UI)
        self.buttonBox.accepted.connect(ProfilesDialog_UI.accept)
        self.buttonBox.rejected.connect(ProfilesDialog_UI.reject)

        QMetaObject.connectSlotsByName(ProfilesDialog_UI)
    # setupUi

    def retranslateUi(self, ProfilesDialog_UI):
        ProfilesDialog_UI.setWindowTitle(QCoreApplication.translate("ProfilesDialog_UI", u"Profiles", None))
#if QT_CONFIG(tooltip)
        self.button_create.setToolTip(QCoreApplication.translate("ProfilesDialog_UI", u"Create  new profile", None))
#endif // QT_CONFIG(tooltip)
        self.button_create.setText(QCoreApplication.translate("ProfilesDialog_UI", u"C", None))
        self.label.setText(QCoreApplication.translate("ProfilesDialog_UI", u"Profile:", None))
#if QT_CONFIG(tooltip)
        self.button_delete.setToolTip(QCoreApplication.translate("ProfilesDialog_UI", u"Delete profile", None))
#endif // QT_CONFIG(tooltip)
        self.button_delete.setText(QCoreApplication.translate("ProfilesDialog_UI", u"D", None))
        self.properties.setTitle(QCoreApplication.translate("ProfilesDialog_UI", u"Properties", None))
        self.label_dar.setText(QCoreApplication.translate("ProfilesDialog_UI", u"Display aspect ratio:", None))
        self.label_3.setText(QCoreApplication.translate("ProfilesDialog_UI", u"Frame rate:", None))
        self.label_8.setText(QCoreApplication.translate("ProfilesDialog_UI", u"/", None))
        self.field_order.setItemText(0, QCoreApplication.translate("ProfilesDialog_UI", u"Top Field First", None))
        self.field_order.setItemText(1, QCoreApplication.translate("ProfilesDialog_UI", u"Bottom Field First", None))

        self.label_scanning.setText(QCoreApplication.translate("ProfilesDialog_UI", u"Scanning:", None))
        self.label_4.setText(QCoreApplication.translate("ProfilesDialog_UI", u"/", None))
        self.label_6.setText(QCoreApplication.translate("ProfilesDialog_UI", u"x", None))
        self.label_2.setText(QCoreApplication.translate("ProfilesDialog_UI", u"Description:", None))
        self.scanning.setItemText(0, QCoreApplication.translate("ProfilesDialog_UI", u"Interlaced", None))
        self.scanning.setItemText(1, QCoreApplication.translate("ProfilesDialog_UI", u"Progressive", None))

        self.label_9.setText(QCoreApplication.translate("ProfilesDialog_UI", u"Pixel aspect ratio:", None))
        self.label_12.setText(QCoreApplication.translate("ProfilesDialog_UI", u"Colorspace:", None))
        self.label_5.setText(QCoreApplication.translate("ProfilesDialog_UI", u"Size:", None))
        self.label_field_order.setText(QCoreApplication.translate("ProfilesDialog_UI", u"Field order:", None))
        self.label_7.setText(QCoreApplication.translate("ProfilesDialog_UI", u"/", None))
        self.label_11.setText(QCoreApplication.translate("ProfilesDialog_UI", u"Fields per second:", None))
        self.effect_warning.setText(QCoreApplication.translate("ProfilesDialog_UI", u"The \"avfilter.fieldorder\" effect is internally used to set the field order, but the effect was not found.\n"
"This feature will not work as expected.", None))
#if QT_CONFIG(tooltip)
        self.button_save.setToolTip(QCoreApplication.translate("ProfilesDialog_UI", u"Save profile", None))
#endif // QT_CONFIG(tooltip)
        self.button_save.setText(QCoreApplication.translate("ProfilesDialog_UI", u"S", None))
        self.button_default.setText(QCoreApplication.translate("ProfilesDialog_UI", u"Use as default", None))
    # retranslateUi

