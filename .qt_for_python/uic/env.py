# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'env.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QTabWidget, QWidget)

class Ui_ConfigCapture_UI(object):
    def setupUi(self, ConfigCapture_UI):
        if not ConfigCapture_UI.objectName():
            ConfigCapture_UI.setObjectName(u"ConfigCapture_UI")
        ConfigCapture_UI.resize(525, 520)
        self.gridLayout_8 = QGridLayout(ConfigCapture_UI)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, -1, -1)
        self.label = QLabel(ConfigCapture_UI)
        self.label.setObjectName(u"label")

        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)

        self.kcfg_defaultcapture = QComboBox(ConfigCapture_UI)
        self.kcfg_defaultcapture.addItem("")
        self.kcfg_defaultcapture.addItem("")
        self.kcfg_defaultcapture.setObjectName(u"kcfg_defaultcapture")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kcfg_defaultcapture.sizePolicy().hasHeightForWidth())
        self.kcfg_defaultcapture.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.kcfg_defaultcapture, 0, 1, 1, 1)

        self.tabWidget = QTabWidget(ConfigCapture_UI)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(401, 0))
        self.ffmpeg_tab = QWidget()
        self.ffmpeg_tab.setObjectName(u"ffmpeg_tab")
        self.gridLayout = QGridLayout(self.ffmpeg_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(self.ffmpeg_tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 10, 0, 4, 8)

        self.label_9 = QLabel(self.ffmpeg_tab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 2)

        self.kcfg_alsachannels = QSpinBox(self.ffmpeg_tab)
        self.kcfg_alsachannels.setObjectName(u"kcfg_alsachannels")

        self.gridLayout.addWidget(self.kcfg_alsachannels, 15, 6, 1, 2)

        self.label_24 = QLabel(self.ffmpeg_tab)
        self.label_24.setObjectName(u"label_24")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_24, 18, 0, 1, 2)

        self.label_4 = QLabel(self.ffmpeg_tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 2)

        self.kcfg_v4l_format = QComboBox(self.ffmpeg_tab)
        self.kcfg_v4l_format.setObjectName(u"kcfg_v4l_format")

        self.gridLayout.addWidget(self.kcfg_v4l_format, 3, 3, 1, 5)

        self.label_11 = QLabel(self.ffmpeg_tab)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 15, 5, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(127, 21, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 9, 3, 1, 2)

        self.config_v4l = QPushButton(self.ffmpeg_tab)
        self.config_v4l.setObjectName(u"config_v4l")

        self.gridLayout.addWidget(self.config_v4l, 9, 5, 1, 3)

        self.kcfg_v4l_alsadevice = QComboBox(self.ffmpeg_tab)
        self.kcfg_v4l_alsadevice.setObjectName(u"kcfg_v4l_alsadevice")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.kcfg_v4l_alsadevice.sizePolicy().hasHeightForWidth())
        self.kcfg_v4l_alsadevice.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.kcfg_v4l_alsadevice, 15, 0, 1, 5)

        self.label_31 = QLabel(self.ffmpeg_tab)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout.addWidget(self.label_31, 7, 0, 1, 3)

        self.p_progressive = QLabel(self.ffmpeg_tab)
        self.p_progressive.setObjectName(u"p_progressive")

        self.gridLayout.addWidget(self.p_progressive, 9, 0, 1, 2)

        self.label_30 = QLabel(self.ffmpeg_tab)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout.addWidget(self.label_30, 1, 0, 1, 2)

        self.label_14 = QLabel(self.ffmpeg_tab)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 2, 0, 1, 2)

        self.v4l_profile_box = QHBoxLayout()
        self.v4l_profile_box.setObjectName(u"v4l_profile_box")

        self.gridLayout.addLayout(self.v4l_profile_box, 18, 3, 1, 5)

        self.kcfg_detectedv4ldevices = QComboBox(self.ffmpeg_tab)
        self.kcfg_detectedv4ldevices.setObjectName(u"kcfg_detectedv4ldevices")

        self.gridLayout.addWidget(self.kcfg_detectedv4ldevices, 1, 3, 1, 5)

        self.p_aspect = QLabel(self.ffmpeg_tab)
        self.p_aspect.setObjectName(u"p_aspect")

        self.gridLayout.addWidget(self.p_aspect, 6, 3, 1, 5)

        self.label_23 = QLabel(self.ffmpeg_tab)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 6, 0, 1, 2)

        self.kcfg_v4l_captureaudio = QCheckBox(self.ffmpeg_tab)
        self.kcfg_v4l_captureaudio.setObjectName(u"kcfg_v4l_captureaudio")

        self.gridLayout.addWidget(self.kcfg_v4l_captureaudio, 14, 0, 1, 8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 20, 1, 1, 3)

        self.kcfg_v4l_capturevideo = QCheckBox(self.ffmpeg_tab)
        self.kcfg_v4l_capturevideo.setObjectName(u"kcfg_v4l_capturevideo")

        self.gridLayout.addWidget(self.kcfg_v4l_capturevideo, 0, 0, 1, 8)

        self.label_6 = QLabel(self.ffmpeg_tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.line_2 = QFrame(self.ffmpeg_tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 17, 0, 1, 8)

        self.label_32 = QLabel(self.ffmpeg_tab)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout.addWidget(self.label_32, 8, 0, 1, 2)

        self.p_size = QLabel(self.ffmpeg_tab)
        self.p_size.setObjectName(u"p_size")

        self.gridLayout.addWidget(self.p_size, 4, 3, 1, 5)

        self.p_display = QLabel(self.ffmpeg_tab)
        self.p_display.setObjectName(u"p_display")

        self.gridLayout.addWidget(self.p_display, 7, 3, 1, 5)

        self.kcfg_video4vdevice = QLineEdit(self.ffmpeg_tab)
        self.kcfg_video4vdevice.setObjectName(u"kcfg_video4vdevice")

        self.gridLayout.addWidget(self.kcfg_video4vdevice, 2, 3, 1, 5)

        self.p_colorspace = QLabel(self.ffmpeg_tab)
        self.p_colorspace.setObjectName(u"p_colorspace")

        self.gridLayout.addWidget(self.p_colorspace, 8, 3, 1, 5)

        self.p_fps = QLabel(self.ffmpeg_tab)
        self.p_fps.setObjectName(u"p_fps")

        self.gridLayout.addWidget(self.p_fps, 5, 3, 1, 5)

        self.tabWidget.addTab(self.ffmpeg_tab, "")
        self.screen_grab_tab = QWidget()
        self.screen_grab_tab.setObjectName(u"screen_grab_tab")
        self.gridLayout_5 = QGridLayout(self.screen_grab_tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.kcfg_grab_hide_mouse = QCheckBox(self.screen_grab_tab)
        self.kcfg_grab_hide_mouse.setObjectName(u"kcfg_grab_hide_mouse")

        self.gridLayout_5.addWidget(self.kcfg_grab_hide_mouse, 3, 0, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(237, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(383, 160, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 8, 0, 1, 3)

        self.label_screengrab = QLabel(self.screen_grab_tab)
        self.label_screengrab.setObjectName(u"label_screengrab")
        sizePolicy1.setHeightForWidth(self.label_screengrab.sizePolicy().hasHeightForWidth())
        self.label_screengrab.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.label_screengrab, 5, 0, 1, 1)

        self.kcfg_grab_capture_type = QComboBox(self.screen_grab_tab)
        self.kcfg_grab_capture_type.addItem("")
        self.kcfg_grab_capture_type.addItem("")
        self.kcfg_grab_capture_type.setObjectName(u"kcfg_grab_capture_type")

        self.gridLayout_5.addWidget(self.kcfg_grab_capture_type, 0, 0, 1, 3)

        self.screen_grab_profile_box = QHBoxLayout()
        self.screen_grab_profile_box.setObjectName(u"screen_grab_profile_box")

        self.gridLayout_5.addLayout(self.screen_grab_profile_box, 5, 1, 1, 2)

        self.label_18 = QLabel(self.screen_grab_tab)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_5.addWidget(self.label_18, 2, 0, 1, 1)

        self.region_group = QFrame(self.screen_grab_tab)
        self.region_group.setObjectName(u"region_group")
        self.region_group.setFrameShape(QFrame.StyledPanel)
        self.region_group.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.region_group)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.kcfg_grab_follow_mouse = QCheckBox(self.region_group)
        self.kcfg_grab_follow_mouse.setObjectName(u"kcfg_grab_follow_mouse")

        self.horizontalLayout.addWidget(self.kcfg_grab_follow_mouse)

        self.kcfg_grab_hide_frame = QCheckBox(self.region_group)
        self.kcfg_grab_hide_frame.setObjectName(u"kcfg_grab_hide_frame")

        self.horizontalLayout.addWidget(self.kcfg_grab_hide_frame)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 3)

        self.label_19 = QLabel(self.region_group)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 1, 0, 1, 1)

        self.kcfg_grab_offsetx = QSpinBox(self.region_group)
        self.kcfg_grab_offsetx.setObjectName(u"kcfg_grab_offsetx")
        sizePolicy.setHeightForWidth(self.kcfg_grab_offsetx.sizePolicy().hasHeightForWidth())
        self.kcfg_grab_offsetx.setSizePolicy(sizePolicy)
        self.kcfg_grab_offsetx.setMaximum(5000)
        self.kcfg_grab_offsetx.setValue(0)

        self.gridLayout_3.addWidget(self.kcfg_grab_offsetx, 1, 1, 1, 1)

        self.kcfg_grab_offsety = QSpinBox(self.region_group)
        self.kcfg_grab_offsety.setObjectName(u"kcfg_grab_offsety")
        sizePolicy.setHeightForWidth(self.kcfg_grab_offsety.sizePolicy().hasHeightForWidth())
        self.kcfg_grab_offsety.setSizePolicy(sizePolicy)
        self.kcfg_grab_offsety.setMaximum(5000)
        self.kcfg_grab_offsety.setValue(0)

        self.gridLayout_3.addWidget(self.kcfg_grab_offsety, 1, 2, 1, 1)

        self.label_20 = QLabel(self.region_group)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_3.addWidget(self.label_20, 2, 0, 1, 1)

        self.kcfg_grab_width = QSpinBox(self.region_group)
        self.kcfg_grab_width.setObjectName(u"kcfg_grab_width")
        self.kcfg_grab_width.setMinimum(1)
        self.kcfg_grab_width.setMaximum(5000)
        self.kcfg_grab_width.setValue(1280)

        self.gridLayout_3.addWidget(self.kcfg_grab_width, 2, 1, 1, 1)

        self.kcfg_grab_height = QSpinBox(self.region_group)
        self.kcfg_grab_height.setObjectName(u"kcfg_grab_height")
        self.kcfg_grab_height.setMinimum(1)
        self.kcfg_grab_height.setMaximum(5000)
        self.kcfg_grab_height.setValue(720)

        self.gridLayout_3.addWidget(self.kcfg_grab_height, 2, 2, 1, 1)


        self.gridLayout_5.addWidget(self.region_group, 1, 0, 1, 3)

        self.kcfg_grab_fps = QDoubleSpinBox(self.screen_grab_tab)
        self.kcfg_grab_fps.setObjectName(u"kcfg_grab_fps")
        self.kcfg_grab_fps.setMinimum(1.000000000000000)
        self.kcfg_grab_fps.setMaximum(1000.000000000000000)

        self.gridLayout_5.addWidget(self.kcfg_grab_fps, 2, 1, 1, 1)

        self.tabWidget.addTab(self.screen_grab_tab, "")
        self.decklink_tab = QWidget()
        self.decklink_tab.setObjectName(u"decklink_tab")
        self.gridLayout_6 = QGridLayout(self.decklink_tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.kcfg_decklink_capturedevice = QComboBox(self.decklink_tab)
        self.kcfg_decklink_capturedevice.setObjectName(u"kcfg_decklink_capturedevice")
        sizePolicy.setHeightForWidth(self.kcfg_decklink_capturedevice.sizePolicy().hasHeightForWidth())
        self.kcfg_decklink_capturedevice.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.kcfg_decklink_capturedevice, 0, 1, 1, 1)

        self.kcfg_decklink_filename = QLineEdit(self.decklink_tab)
        self.kcfg_decklink_filename.setObjectName(u"kcfg_decklink_filename")

        self.gridLayout_6.addWidget(self.kcfg_decklink_filename, 5, 1, 1, 1)

        self.label_16 = QLabel(self.decklink_tab)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.label_16, 2, 0, 1, 1)

        self.label_29 = QLabel(self.decklink_tab)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_6.addWidget(self.label_29, 5, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 327, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_4, 6, 1, 1, 1)

        self.label_27 = QLabel(self.decklink_tab)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_6.addWidget(self.label_27, 0, 0, 1, 1)

        self.decklink_profile_box = QHBoxLayout()
        self.decklink_profile_box.setSpacing(0)
        self.decklink_profile_box.setObjectName(u"decklink_profile_box")

        self.gridLayout_6.addLayout(self.decklink_profile_box, 2, 1, 1, 1)

        self.tabWidget.addTab(self.decklink_tab, "")
        self.audio_tab = QWidget()
        self.audio_tab.setObjectName(u"audio_tab")
        self.gridLayout_2 = QGridLayout(self.audio_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.audio_tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_2 = QLabel(self.audio_tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 661, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 6, 1, 1, 1)

        self.label_3 = QLabel(self.audio_tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)

        self.audiocapturesamplerate = QComboBox(self.audio_tab)
        self.audiocapturesamplerate.setObjectName(u"audiocapturesamplerate")

        self.gridLayout_2.addWidget(self.audiocapturesamplerate, 5, 1, 1, 1)

        self.kcfg_audiocapturevolume = QSlider(self.audio_tab)
        self.kcfg_audiocapturevolume.setObjectName(u"kcfg_audiocapturevolume")
        self.kcfg_audiocapturevolume.setMaximum(100)
        self.kcfg_audiocapturevolume.setSliderPosition(100)
        self.kcfg_audiocapturevolume.setTracking(True)
        self.kcfg_audiocapturevolume.setOrientation(Qt.Horizontal)
        self.kcfg_audiocapturevolume.setInvertedAppearance(False)
        self.kcfg_audiocapturevolume.setInvertedControls(False)
        self.kcfg_audiocapturevolume.setTickPosition(QSlider.TicksAbove)

        self.gridLayout_2.addWidget(self.kcfg_audiocapturevolume, 3, 1, 1, 1)

        self.audiocapturechannels = QComboBox(self.audio_tab)
        self.audiocapturechannels.setObjectName(u"audiocapturechannels")

        self.gridLayout_2.addWidget(self.audiocapturechannels, 4, 1, 1, 1)

        self.kcfg_defaultaudiocapture = QComboBox(self.audio_tab)
        self.kcfg_defaultaudiocapture.setObjectName(u"kcfg_defaultaudiocapture")

        self.gridLayout_2.addWidget(self.kcfg_defaultaudiocapture, 1, 1, 1, 1)

        self.label_33 = QLabel(self.audio_tab)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_2.addWidget(self.label_33, 1, 0, 1, 1)

        self.labelNoAudioDevices = QLabel(self.audio_tab)
        self.labelNoAudioDevices.setObjectName(u"labelNoAudioDevices")
        font = QFont()
        font.setPointSize(10)
        self.labelNoAudioDevices.setFont(font)

        self.gridLayout_2.addWidget(self.labelNoAudioDevices, 2, 0, 1, 2)

        self.tabWidget.addTab(self.audio_tab, "")

        self.gridLayout_8.addWidget(self.tabWidget, 1, 0, 1, 2)

        QWidget.setTabOrder(self.kcfg_defaultcapture, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.kcfg_grab_capture_type)
        QWidget.setTabOrder(self.kcfg_grab_capture_type, self.kcfg_grab_follow_mouse)
        QWidget.setTabOrder(self.kcfg_grab_follow_mouse, self.kcfg_grab_hide_frame)
        QWidget.setTabOrder(self.kcfg_grab_hide_frame, self.kcfg_grab_offsetx)
        QWidget.setTabOrder(self.kcfg_grab_offsetx, self.kcfg_grab_offsety)
        QWidget.setTabOrder(self.kcfg_grab_offsety, self.kcfg_grab_width)
        QWidget.setTabOrder(self.kcfg_grab_width, self.kcfg_grab_height)

        self.retranslateUi(ConfigCapture_UI)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ConfigCapture_UI)
    # setupUi

    def retranslateUi(self, ConfigCapture_UI):
        self.label.setText(QCoreApplication.translate("ConfigCapture_UI", u"Default capture device", None))
        self.kcfg_defaultcapture.setItemText(0, QCoreApplication.translate("ConfigCapture_UI", u"FFmpeg", None))
        self.kcfg_defaultcapture.setItemText(1, QCoreApplication.translate("ConfigCapture_UI", u"Screen grab", None))

        self.label_9.setText(QCoreApplication.translate("ConfigCapture_UI", u"Capture format", None))
        self.label_24.setText(QCoreApplication.translate("ConfigCapture_UI", u"Encoding profile", None))
        self.label_4.setText(QCoreApplication.translate("ConfigCapture_UI", u"Frame rate:", None))
        self.label_11.setText(QCoreApplication.translate("ConfigCapture_UI", u"Channels", None))
        self.config_v4l.setText(QCoreApplication.translate("ConfigCapture_UI", u"Edit", None))
        self.label_31.setText(QCoreApplication.translate("ConfigCapture_UI", u"Display aspect ratio:", None))
        self.p_progressive.setText(QCoreApplication.translate("ConfigCapture_UI", u"Interlaced", None))
        self.label_30.setText(QCoreApplication.translate("ConfigCapture_UI", u"Detected devices", None))
        self.label_14.setText(QCoreApplication.translate("ConfigCapture_UI", u"Video device", None))
        self.p_aspect.setText(QCoreApplication.translate("ConfigCapture_UI", u"59/54", None))
        self.label_23.setText(QCoreApplication.translate("ConfigCapture_UI", u"Pixel aspect ratio:", None))
        self.kcfg_v4l_captureaudio.setText(QCoreApplication.translate("ConfigCapture_UI", u"Capture audio (ALSA)", None))
        self.kcfg_v4l_capturevideo.setText(QCoreApplication.translate("ConfigCapture_UI", u"Capture video (Video4Linux2)", None))
        self.label_6.setText(QCoreApplication.translate("ConfigCapture_UI", u"Size:", None))
        self.label_32.setText(QCoreApplication.translate("ConfigCapture_UI", u"Colorspace", None))
        self.p_size.setText(QCoreApplication.translate("ConfigCapture_UI", u"720x576", None))
        self.p_display.setText(QCoreApplication.translate("ConfigCapture_UI", u"4/3", None))
        self.kcfg_video4vdevice.setText("")
        self.p_colorspace.setText("")
        self.p_fps.setText(QCoreApplication.translate("ConfigCapture_UI", u"25/1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ffmpeg_tab), QCoreApplication.translate("ConfigCapture_UI", u"FFmpeg", None))
        self.kcfg_grab_hide_mouse.setText(QCoreApplication.translate("ConfigCapture_UI", u"Hide cursor", None))
        self.label_screengrab.setText(QCoreApplication.translate("ConfigCapture_UI", u"Encoding profile", None))
        self.kcfg_grab_capture_type.setItemText(0, QCoreApplication.translate("ConfigCapture_UI", u"Full Screen Capture", None))
        self.kcfg_grab_capture_type.setItemText(1, QCoreApplication.translate("ConfigCapture_UI", u"Region Capture", None))

        self.label_18.setText(QCoreApplication.translate("ConfigCapture_UI", u"Frame rate", None))
        self.kcfg_grab_follow_mouse.setText(QCoreApplication.translate("ConfigCapture_UI", u"Follow mouse", None))
        self.kcfg_grab_hide_frame.setText(QCoreApplication.translate("ConfigCapture_UI", u"Hide frame", None))
        self.label_19.setText(QCoreApplication.translate("ConfigCapture_UI", u"Offset", None))
        self.label_20.setText(QCoreApplication.translate("ConfigCapture_UI", u"Size", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.screen_grab_tab), QCoreApplication.translate("ConfigCapture_UI", u"Screen Grab", None))
        self.label_16.setText(QCoreApplication.translate("ConfigCapture_UI", u"Encoding profile", None))
        self.label_29.setText(QCoreApplication.translate("ConfigCapture_UI", u"Capture file name:", None))
        self.label_27.setText(QCoreApplication.translate("ConfigCapture_UI", u"Detected devices", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.decklink_tab), QCoreApplication.translate("ConfigCapture_UI", u"Blackmagic", None))
        self.label_5.setText(QCoreApplication.translate("ConfigCapture_UI", u"Sample rate:", None))
        self.label_2.setText(QCoreApplication.translate("ConfigCapture_UI", u"Capture volume:", None))
        self.label_3.setText(QCoreApplication.translate("ConfigCapture_UI", u"Channels:", None))
        self.label_33.setText(QCoreApplication.translate("ConfigCapture_UI", u"Device:", None))
        self.labelNoAudioDevices.setText(QCoreApplication.translate("ConfigCapture_UI", u"Make sure you have audio plugins installed on your system", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.audio_tab), QCoreApplication.translate("ConfigCapture_UI", u"Audio", None))
        pass
    # retranslateUi

