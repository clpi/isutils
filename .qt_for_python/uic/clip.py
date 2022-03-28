# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clip.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QRadioButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QStackedWidget, QWidget)

from kcombobox import KComboBox
from kurlrequester import KUrlRequester

class Ui_SlideshowClip_UI(object):
    def setupUi(self, SlideshowClip_UI):
        if not SlideshowClip_UI.objectName():
            SlideshowClip_UI.setObjectName(u"SlideshowClip_UI")
        SlideshowClip_UI.resize(354, 631)
        self.gridLayout_4 = QGridLayout(SlideshowClip_UI)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(6)
        self.icon_list = QListWidget(SlideshowClip_UI)
        self.icon_list.setObjectName(u"icon_list")

        self.gridLayout_4.addWidget(self.icon_list, 12, 0, 1, 4)

        self.animation = KComboBox(SlideshowClip_UI)
        self.animation.setObjectName(u"animation")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.animation.sizePolicy().hasHeightForWidth())
        self.animation.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.animation, 10, 2, 1, 2)

        self.slide_crop = QCheckBox(SlideshowClip_UI)
        self.slide_crop.setObjectName(u"slide_crop")

        self.gridLayout_4.addWidget(self.slide_crop, 4, 0, 1, 2)

        self.label_3 = QLabel(SlideshowClip_UI)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_2 = QLabel(SlideshowClip_UI)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.clip_duration = QLineEdit(SlideshowClip_UI)
        self.clip_duration.setObjectName(u"clip_duration")

        self.horizontalLayout_2.addWidget(self.clip_duration)

        self.clip_duration_frames = QSpinBox(SlideshowClip_UI)
        self.clip_duration_frames.setObjectName(u"clip_duration_frames")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.clip_duration_frames.sizePolicy().hasHeightForWidth())
        self.clip_duration_frames.setSizePolicy(sizePolicy1)
        self.clip_duration_frames.setMinimum(1)
        self.clip_duration_frames.setMaximum(256000)

        self.horizontalLayout_2.addWidget(self.clip_duration_frames)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 2, 1, 1)

        self.luma_softness = QSlider(SlideshowClip_UI)
        self.luma_softness.setObjectName(u"luma_softness")
        self.luma_softness.setEnabled(False)
        self.luma_softness.setMaximum(100)
        self.luma_softness.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.luma_softness, 8, 2, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.luma_duration = QLineEdit(SlideshowClip_UI)
        self.luma_duration.setObjectName(u"luma_duration")

        self.horizontalLayout.addWidget(self.luma_duration)

        self.luma_duration_frames = QSpinBox(SlideshowClip_UI)
        self.luma_duration_frames.setObjectName(u"luma_duration_frames")
        self.luma_duration_frames.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.luma_duration_frames.sizePolicy().hasHeightForWidth())
        self.luma_duration_frames.setSizePolicy(sizePolicy1)
        self.luma_duration_frames.setMinimum(1)
        self.luma_duration_frames.setMaximum(256000)

        self.horizontalLayout.addWidget(self.luma_duration_frames)


        self.gridLayout_4.addLayout(self.horizontalLayout, 5, 2, 1, 2)

        self.luma_fade = QCheckBox(SlideshowClip_UI)
        self.luma_fade.setObjectName(u"luma_fade")
        self.luma_fade.setEnabled(False)

        self.gridLayout_4.addWidget(self.luma_fade, 7, 0, 1, 1)

        self.slide_fade = QCheckBox(SlideshowClip_UI)
        self.slide_fade.setObjectName(u"slide_fade")

        self.gridLayout_4.addWidget(self.slide_fade, 5, 0, 1, 1)

        self.luma_file = KComboBox(SlideshowClip_UI)
        self.luma_file.setObjectName(u"luma_file")
        self.luma_file.setEnabled(False)

        self.gridLayout_4.addWidget(self.luma_file, 7, 2, 1, 2)

        self.label_softness = QLabel(SlideshowClip_UI)
        self.label_softness.setObjectName(u"label_softness")
        self.label_softness.setEnabled(False)

        self.gridLayout_4.addWidget(self.label_softness, 8, 0, 1, 1)

        self.groupBox = QGroupBox(SlideshowClip_UI)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.method_mime = QRadioButton(self.groupBox)
        self.method_mime.setObjectName(u"method_mime")
        self.method_mime.setChecked(True)

        self.gridLayout.addWidget(self.method_mime, 0, 0, 1, 1)

        self.method_pattern = QRadioButton(self.groupBox)
        self.method_pattern.setObjectName(u"method_pattern")

        self.gridLayout.addWidget(self.method_pattern, 0, 1, 1, 1)

        self.stackedWidget = QStackedWidget(self.groupBox)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 2, 1, 1)

        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.folder_url = KUrlRequester(self.page)
        self.folder_url.setObjectName(u"folder_url")

        self.gridLayout_2.addWidget(self.folder_url, 0, 1, 1, 2)

        self.image_type = KComboBox(self.page)
        self.image_type.setObjectName(u"image_type")

        self.gridLayout_2.addWidget(self.image_type, 1, 1, 1, 2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 2, 1, 1)

        self.pattern_url = KUrlRequester(self.page_2)
        self.pattern_url.setObjectName(u"pattern_url")

        self.gridLayout_3.addWidget(self.pattern_url, 0, 1, 1, 2)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 2)


        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 4)

        self.buttonBox = QDialogButtonBox(SlideshowClip_UI)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_4.addWidget(self.buttonBox, 14, 2, 1, 2)

        self.slide_loop = QCheckBox(SlideshowClip_UI)
        self.slide_loop.setObjectName(u"slide_loop")

        self.gridLayout_4.addWidget(self.slide_loop, 3, 0, 1, 1)

        self.clip_name = QLineEdit(SlideshowClip_UI)
        self.clip_name.setObjectName(u"clip_name")

        self.gridLayout_4.addWidget(self.clip_name, 0, 1, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.show_thumbs = QCheckBox(SlideshowClip_UI)
        self.show_thumbs.setObjectName(u"show_thumbs")

        self.horizontalLayout_3.addWidget(self.show_thumbs)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_info = QLabel(SlideshowClip_UI)
        self.label_info.setObjectName(u"label_info")

        self.horizontalLayout_3.addWidget(self.label_info)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 13, 0, 1, 4)

        self.clip_duration_format = KComboBox(SlideshowClip_UI)
        self.clip_duration_format.setObjectName(u"clip_duration_format")

        self.gridLayout_4.addWidget(self.clip_duration_format, 2, 3, 1, 1)

        self.label_6 = QLabel(SlideshowClip_UI)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 10, 0, 1, 1)

        self.low_pass = QCheckBox(SlideshowClip_UI)
        self.low_pass.setObjectName(u"low_pass")
        self.low_pass.setEnabled(False)

        self.gridLayout_4.addWidget(self.low_pass, 11, 0, 1, 4)


        self.retranslateUi(SlideshowClip_UI)
        self.buttonBox.accepted.connect(SlideshowClip_UI.accept)
        self.buttonBox.rejected.connect(SlideshowClip_UI.reject)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SlideshowClip_UI)
    # setupUi

    def retranslateUi(self, SlideshowClip_UI):
        SlideshowClip_UI.setWindowTitle(QCoreApplication.translate("SlideshowClip_UI", u"Slideshow Clip", None))
        self.slide_crop.setText(QCoreApplication.translate("SlideshowClip_UI", u"Center crop", None))
        self.label_3.setText(QCoreApplication.translate("SlideshowClip_UI", u"Name:", None))
        self.label_2.setText(QCoreApplication.translate("SlideshowClip_UI", u"Frame duration:", None))
        self.luma_fade.setText(QCoreApplication.translate("SlideshowClip_UI", u"Wipe:", None))
        self.slide_fade.setText(QCoreApplication.translate("SlideshowClip_UI", u"Dissolve:", None))
        self.label_softness.setText(QCoreApplication.translate("SlideshowClip_UI", u"Softness:", None))
        self.groupBox.setTitle(QCoreApplication.translate("SlideshowClip_UI", u"Image Selection Method", None))
        self.method_mime.setText(QCoreApplication.translate("SlideshowClip_UI", u"&MIME type", None))
        self.method_pattern.setText(QCoreApplication.translate("SlideshowClip_UI", u"Fi&lename pattern", None))
        self.label.setText(QCoreApplication.translate("SlideshowClip_UI", u"Folder:", None))
        self.label_4.setText(QCoreApplication.translate("SlideshowClip_UI", u"Image type:", None))
        self.label_5.setText(QCoreApplication.translate("SlideshowClip_UI", u"First frame", None))
        self.slide_loop.setText(QCoreApplication.translate("SlideshowClip_UI", u"Loop", None))
        self.show_thumbs.setText(QCoreApplication.translate("SlideshowClip_UI", u"Show thumbnails", None))
        self.label_info.setText(QCoreApplication.translate("SlideshowClip_UI", u"No image found", None))
        self.label_6.setText(QCoreApplication.translate("SlideshowClip_UI", u"Animation:", None))
        self.low_pass.setText(QCoreApplication.translate("SlideshowClip_UI", u"Low pass", None))
    # retranslateUi

