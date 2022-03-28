# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prop.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QCheckBox,
    QDialog, QDialogButtonBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QTabWidget, QToolButton, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

from kcolorbutton import KColorButton
from kcombobox import KComboBox
from kseparator import KSeparator
from kurllabel import KUrlLabel

class Ui_ClipProperties_UI(object):
    def setupUi(self, ClipProperties_UI):
        if not ClipProperties_UI.objectName():
            ClipProperties_UI.setObjectName(u"ClipProperties_UI")
        ClipProperties_UI.resize(344, 720)
        self.gridLayout_2 = QGridLayout(ClipProperties_UI)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.clip_thumb = QLabel(ClipProperties_UI)
        self.clip_thumb.setObjectName(u"clip_thumb")
        self.clip_thumb.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.clip_thumb, 0, 0, 1, 5)

        self.label_path = QLabel(ClipProperties_UI)
        self.label_path.setObjectName(u"label_path")

        self.gridLayout_2.addWidget(self.label_path, 1, 0, 1, 5)

        self.clip_path = QLineEdit(ClipProperties_UI)
        self.clip_path.setObjectName(u"clip_path")
        self.clip_path.setReadOnly(True)

        self.gridLayout_2.addWidget(self.clip_path, 2, 0, 1, 5)

        self.label_description = QLabel(ClipProperties_UI)
        self.label_description.setObjectName(u"label_description")

        self.gridLayout_2.addWidget(self.label_description, 3, 0, 1, 5)

        self.clip_description = QLineEdit(ClipProperties_UI)
        self.clip_description.setObjectName(u"clip_description")

        self.gridLayout_2.addWidget(self.clip_description, 4, 0, 1, 5)

        self.label_size = QLabel(ClipProperties_UI)
        self.label_size.setObjectName(u"label_size")

        self.gridLayout_2.addWidget(self.label_size, 5, 3, 1, 1)

        self.label_duration = QLabel(ClipProperties_UI)
        self.label_duration.setObjectName(u"label_duration")

        self.gridLayout_2.addWidget(self.label_duration, 5, 0, 1, 1)

        self.clip_filesize = QLabel(ClipProperties_UI)
        self.clip_filesize.setObjectName(u"clip_filesize")

        self.gridLayout_2.addWidget(self.clip_filesize, 5, 4, 1, 1)

        self.clip_license = KUrlLabel(ClipProperties_UI)
        self.clip_license.setObjectName(u"clip_license")

        self.gridLayout_2.addWidget(self.clip_license, 6, 0, 1, 5)

        self.tabWidget = QTabWidget(ClipProperties_UI)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tab_video = QWidget()
        self.tab_video.setObjectName(u"tab_video")
        self.verticalLayout = QVBoxLayout(self.tab_video)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.clip_vproperties = QTreeWidget(self.tab_video)
        self.clip_vproperties.setObjectName(u"clip_vproperties")
        self.clip_vproperties.setFrameShape(QFrame.NoFrame)
        self.clip_vproperties.setAlternatingRowColors(True)
        self.clip_vproperties.setSelectionMode(QAbstractItemView.NoSelection)
        self.clip_vproperties.setRootIsDecorated(False)
        self.clip_vproperties.setItemsExpandable(False)
        self.clip_vproperties.setAllColumnsShowFocus(True)
        self.clip_vproperties.setHeaderHidden(True)
        self.clip_vproperties.setColumnCount(2)

        self.verticalLayout.addWidget(self.clip_vproperties)

        self.tabWidget.addTab(self.tab_video, "")
        self.tab_audio = QWidget()
        self.tab_audio.setObjectName(u"tab_audio")
        self.verticalLayout_2 = QVBoxLayout(self.tab_audio)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.clip_aproperties = QTreeWidget(self.tab_audio)
        self.clip_aproperties.setObjectName(u"clip_aproperties")
        self.clip_aproperties.setFrameShape(QFrame.NoFrame)
        self.clip_aproperties.setAlternatingRowColors(True)
        self.clip_aproperties.setSelectionMode(QAbstractItemView.NoSelection)
        self.clip_aproperties.setRootIsDecorated(False)
        self.clip_aproperties.setItemsExpandable(False)
        self.clip_aproperties.setAllColumnsShowFocus(True)
        self.clip_aproperties.setHeaderHidden(True)
        self.clip_aproperties.setColumnCount(2)

        self.verticalLayout_2.addWidget(self.clip_aproperties)

        self.tabWidget.addTab(self.tab_audio, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 0, 0, 1, 1)

        self.clip_color = KColorButton(self.tab)
        self.clip_color.setObjectName(u"clip_color")

        self.gridLayout_5.addWidget(self.clip_color, 0, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(122, 118, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_slideshow = QWidget()
        self.tab_slideshow.setObjectName(u"tab_slideshow")
        self.gridLayout_6 = QGridLayout(self.tab_slideshow)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.slide_type_label = QLabel(self.tab_slideshow)
        self.slide_type_label.setObjectName(u"slide_type_label")

        self.gridLayout_6.addWidget(self.slide_type_label, 0, 0, 1, 1)

        self.image_type = KComboBox(self.tab_slideshow)
        self.image_type.setObjectName(u"image_type")

        self.gridLayout_6.addWidget(self.image_type, 0, 1, 1, 2)

        self.clip_filesize_4 = QLabel(self.tab_slideshow)
        self.clip_filesize_4.setObjectName(u"clip_filesize_4")

        self.gridLayout_6.addWidget(self.clip_filesize_4, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slide_duration = QLineEdit(self.tab_slideshow)
        self.slide_duration.setObjectName(u"slide_duration")

        self.horizontalLayout_2.addWidget(self.slide_duration)

        self.slide_duration_frames = QSpinBox(self.tab_slideshow)
        self.slide_duration_frames.setObjectName(u"slide_duration_frames")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slide_duration_frames.sizePolicy().hasHeightForWidth())
        self.slide_duration_frames.setSizePolicy(sizePolicy)
        self.slide_duration_frames.setMinimum(1)
        self.slide_duration_frames.setMaximum(256000)

        self.horizontalLayout_2.addWidget(self.slide_duration_frames)


        self.gridLayout_6.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.slide_duration_format = KComboBox(self.tab_slideshow)
        self.slide_duration_format.setObjectName(u"slide_duration_format")

        self.gridLayout_6.addWidget(self.slide_duration_format, 1, 2, 1, 1)

        self.slide_loop = QCheckBox(self.tab_slideshow)
        self.slide_loop.setObjectName(u"slide_loop")

        self.gridLayout_6.addWidget(self.slide_loop, 3, 0, 1, 3)

        self.slide_fade = QCheckBox(self.tab_slideshow)
        self.slide_fade.setObjectName(u"slide_fade")

        self.gridLayout_6.addWidget(self.slide_fade, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.luma_duration = QLineEdit(self.tab_slideshow)
        self.luma_duration.setObjectName(u"luma_duration")

        self.horizontalLayout.addWidget(self.luma_duration)

        self.luma_duration_frames = QSpinBox(self.tab_slideshow)
        self.luma_duration_frames.setObjectName(u"luma_duration_frames")
        sizePolicy.setHeightForWidth(self.luma_duration_frames.sizePolicy().hasHeightForWidth())
        self.luma_duration_frames.setSizePolicy(sizePolicy)
        self.luma_duration_frames.setMinimum(1)
        self.luma_duration_frames.setMaximum(256000)

        self.horizontalLayout.addWidget(self.luma_duration_frames)


        self.gridLayout_6.addLayout(self.horizontalLayout, 5, 1, 1, 2)

        self.slide_luma = QCheckBox(self.tab_slideshow)
        self.slide_luma.setObjectName(u"slide_luma")

        self.gridLayout_6.addWidget(self.slide_luma, 6, 0, 1, 1)

        self.luma_file = KComboBox(self.tab_slideshow)
        self.luma_file.setObjectName(u"luma_file")

        self.gridLayout_6.addWidget(self.luma_file, 6, 1, 1, 2)

        self.label_softness = QLabel(self.tab_slideshow)
        self.label_softness.setObjectName(u"label_softness")

        self.gridLayout_6.addWidget(self.label_softness, 7, 0, 1, 1)

        self.luma_softness = QSlider(self.tab_slideshow)
        self.luma_softness.setObjectName(u"luma_softness")
        self.luma_softness.setMaximum(100)
        self.luma_softness.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.luma_softness, 7, 1, 1, 2)

        self.slide_info = QLabel(self.tab_slideshow)
        self.slide_info.setObjectName(u"slide_info")

        self.gridLayout_6.addWidget(self.slide_info, 9, 0, 1, 3)

        self.verticalSpacer_6 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_6, 10, 1, 1, 1)

        self.slide_crop = QCheckBox(self.tab_slideshow)
        self.slide_crop.setObjectName(u"slide_crop")

        self.gridLayout_6.addWidget(self.slide_crop, 4, 0, 1, 1)

        self.label_animation = QLabel(self.tab_slideshow)
        self.label_animation.setObjectName(u"label_animation")

        self.gridLayout_6.addWidget(self.label_animation, 8, 0, 1, 1)

        self.animation = KComboBox(self.tab_slideshow)
        self.animation.setObjectName(u"animation")

        self.gridLayout_6.addWidget(self.animation, 8, 1, 1, 2)

        self.tabWidget.addTab(self.tab_slideshow, "")
        self.tab_image = QWidget()
        self.tab_image.setObjectName(u"tab_image")
        self.verticalLayout_3 = QVBoxLayout(self.tab_image)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_16 = QLabel(self.tab_image)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_3.addWidget(self.label_16)

        self.image_size = QLineEdit(self.tab_image)
        self.image_size.setObjectName(u"image_size")
        self.image_size.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.image_size)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.image_transparency = QCheckBox(self.tab_image)
        self.image_transparency.setObjectName(u"image_transparency")

        self.verticalLayout_3.addWidget(self.image_transparency)

        self.verticalSpacer_7 = QSpacerItem(20, 151, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)

        self.tabWidget.addTab(self.tab_image, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_7 = QGridLayout(self.tab_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.markers_list = QTreeWidget(self.tab_3)
        self.markers_list.setObjectName(u"markers_list")
        self.markers_list.setAlternatingRowColors(True)
        self.markers_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.markers_list.setRootIsDecorated(False)
        self.markers_list.setItemsExpandable(False)
        self.markers_list.setAllColumnsShowFocus(True)
        self.markers_list.setHeaderHidden(True)

        self.gridLayout_7.addWidget(self.markers_list, 0, 0, 1, 7)

        self.marker_new = QToolButton(self.tab_3)
        self.marker_new.setObjectName(u"marker_new")
        self.marker_new.setAutoRaise(True)

        self.gridLayout_7.addWidget(self.marker_new, 1, 0, 1, 1)

        self.marker_edit = QToolButton(self.tab_3)
        self.marker_edit.setObjectName(u"marker_edit")
        self.marker_edit.setAutoRaise(True)

        self.gridLayout_7.addWidget(self.marker_edit, 1, 1, 1, 1)

        self.marker_delete = QToolButton(self.tab_3)
        self.marker_delete.setObjectName(u"marker_delete")
        self.marker_delete.setAutoRaise(True)

        self.gridLayout_7.addWidget(self.marker_delete, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(177, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer, 1, 6, 1, 1)

        self.kseparator = KSeparator(self.tab_3)
        self.kseparator.setObjectName(u"kseparator")
        self.kseparator.setProperty("orientation", 5)

        self.gridLayout_7.addWidget(self.kseparator, 1, 3, 1, 1)

        self.marker_save = QToolButton(self.tab_3)
        self.marker_save.setObjectName(u"marker_save")
        self.marker_save.setAutoRaise(True)

        self.gridLayout_7.addWidget(self.marker_save, 1, 4, 1, 1)

        self.marker_load = QToolButton(self.tab_3)
        self.marker_load.setObjectName(u"marker_load")
        self.marker_load.setAutoRaise(True)

        self.gridLayout_7.addWidget(self.marker_load, 1, 5, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_9 = QGridLayout(self.tab_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.metadata_list = QTreeWidget(self.tab_5)
        self.metadata_list.setObjectName(u"metadata_list")
        self.metadata_list.setAlternatingRowColors(True)
        self.metadata_list.setRootIsDecorated(True)
        self.metadata_list.setItemsExpandable(True)
        self.metadata_list.setSortingEnabled(False)
        self.metadata_list.setAllColumnsShowFocus(True)
        self.metadata_list.setWordWrap(True)
        self.metadata_list.setHeaderHidden(True)
        self.metadata_list.setColumnCount(2)

        self.gridLayout_9.addWidget(self.metadata_list, 0, 0, 1, 2)

        self.analysis_box = QFrame(self.tab_5)
        self.analysis_box.setObjectName(u"analysis_box")
        self.analysis_box.setFrameShape(QFrame.NoFrame)
        self.analysis_box.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.analysis_box)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.analysis_list = QTreeWidget(self.analysis_box)
        self.analysis_list.setObjectName(u"analysis_list")
        self.analysis_list.setRootIsDecorated(False)
        self.analysis_list.setAllColumnsShowFocus(True)
        self.analysis_list.header().setVisible(False)

        self.gridLayout_4.addWidget(self.analysis_list, 0, 0, 1, 4)

        self.analysis_delete = QToolButton(self.analysis_box)
        self.analysis_delete.setObjectName(u"analysis_delete")
        self.analysis_delete.setAutoRaise(True)

        self.gridLayout_4.addWidget(self.analysis_delete, 1, 0, 1, 1)

        self.analysis_save = QToolButton(self.analysis_box)
        self.analysis_save.setObjectName(u"analysis_save")
        self.analysis_save.setAutoRaise(True)

        self.gridLayout_4.addWidget(self.analysis_save, 1, 1, 1, 1)

        self.analysis_load = QToolButton(self.analysis_box)
        self.analysis_load.setObjectName(u"analysis_load")
        self.analysis_load.setAutoRaise(True)

        self.gridLayout_4.addWidget(self.analysis_load, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(186, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)


        self.gridLayout_9.addWidget(self.analysis_box, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_advanced = QWidget()
        self.tab_advanced.setObjectName(u"tab_advanced")
        self.gridLayout_3 = QGridLayout(self.tab_advanced)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer = QSpacerItem(20, 19, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 13, 3, 1, 1)

        self.clip_force_ar = QCheckBox(self.tab_advanced)
        self.clip_force_ar.setObjectName(u"clip_force_ar")

        self.gridLayout_3.addWidget(self.clip_force_ar, 1, 1, 1, 1)

        self.clip_vindex = QSpinBox(self.tab_advanced)
        self.clip_vindex.setObjectName(u"clip_vindex")
        self.clip_vindex.setEnabled(False)
        self.clip_vindex.setMinimum(-1)
        self.clip_vindex.setValue(0)

        self.gridLayout_3.addWidget(self.clip_vindex, 7, 3, 1, 1)

        self.clip_aindex = QSpinBox(self.tab_advanced)
        self.clip_aindex.setObjectName(u"clip_aindex")
        self.clip_aindex.setEnabled(False)
        self.clip_aindex.setMinimum(-1)
        self.clip_aindex.setValue(0)

        self.gridLayout_3.addWidget(self.clip_aindex, 8, 3, 1, 1)

        self.clip_force_threads = QCheckBox(self.tab_advanced)
        self.clip_force_threads.setObjectName(u"clip_force_threads")

        self.gridLayout_3.addWidget(self.clip_force_threads, 6, 1, 1, 1)

        self.clip_force_vindex = QCheckBox(self.tab_advanced)
        self.clip_force_vindex.setObjectName(u"clip_force_vindex")

        self.gridLayout_3.addWidget(self.clip_force_vindex, 7, 1, 1, 1)

        self.clip_force_progressive = QCheckBox(self.tab_advanced)
        self.clip_force_progressive.setObjectName(u"clip_force_progressive")

        self.gridLayout_3.addWidget(self.clip_force_progressive, 3, 1, 1, 1)

        self.clip_threads = QSpinBox(self.tab_advanced)
        self.clip_threads.setObjectName(u"clip_threads")
        self.clip_threads.setEnabled(False)
        self.clip_threads.setMaximum(4)
        self.clip_threads.setValue(1)

        self.gridLayout_3.addWidget(self.clip_threads, 6, 3, 1, 1)

        self.clip_force_aindex = QCheckBox(self.tab_advanced)
        self.clip_force_aindex.setObjectName(u"clip_force_aindex")

        self.gridLayout_3.addWidget(self.clip_force_aindex, 8, 1, 1, 1)

        self.clip_force_framerate = QCheckBox(self.tab_advanced)
        self.clip_force_framerate.setObjectName(u"clip_force_framerate")

        self.gridLayout_3.addWidget(self.clip_force_framerate, 2, 1, 1, 1)

        self.clip_force_out = QCheckBox(self.tab_advanced)
        self.clip_force_out.setObjectName(u"clip_force_out")

        self.gridLayout_3.addWidget(self.clip_force_out, 0, 1, 1, 1)

        self.clip_framerate = QDoubleSpinBox(self.tab_advanced)
        self.clip_framerate.setObjectName(u"clip_framerate")
        self.clip_framerate.setEnabled(False)
        self.clip_framerate.setMaximum(1000.000000000000000)

        self.gridLayout_3.addWidget(self.clip_framerate, 2, 3, 1, 1)

        self.clip_force_colorspace = QCheckBox(self.tab_advanced)
        self.clip_force_colorspace.setObjectName(u"clip_force_colorspace")

        self.gridLayout_3.addWidget(self.clip_force_colorspace, 9, 1, 1, 1)

        self.clip_colorspace = KComboBox(self.tab_advanced)
        self.clip_colorspace.setObjectName(u"clip_colorspace")
        self.clip_colorspace.setEnabled(False)

        self.gridLayout_3.addWidget(self.clip_colorspace, 9, 3, 1, 1)

        self.clip_force_fieldorder = QCheckBox(self.tab_advanced)
        self.clip_force_fieldorder.setObjectName(u"clip_force_fieldorder")

        self.gridLayout_3.addWidget(self.clip_force_fieldorder, 5, 1, 1, 1)

        self.clip_full_luma = QCheckBox(self.tab_advanced)
        self.clip_full_luma.setObjectName(u"clip_full_luma")

        self.gridLayout_3.addWidget(self.clip_full_luma, 10, 1, 1, 3)

        self.clip_fieldorder = KComboBox(self.tab_advanced)
        self.clip_fieldorder.setObjectName(u"clip_fieldorder")
        self.clip_fieldorder.setEnabled(False)

        self.gridLayout_3.addWidget(self.clip_fieldorder, 5, 3, 1, 1)

        self.horizontalLayout_aspect = QHBoxLayout()
        self.horizontalLayout_aspect.setObjectName(u"horizontalLayout_aspect")
        self.clip_ar_num = QSpinBox(self.tab_advanced)
        self.clip_ar_num.setObjectName(u"clip_ar_num")
        self.clip_ar_num.setEnabled(False)
        self.clip_ar_num.setMinimum(1)
        self.clip_ar_num.setMaximum(9999)
        self.clip_ar_num.setValue(16)

        self.horizontalLayout_aspect.addWidget(self.clip_ar_num)

        self.label = QLabel(self.tab_advanced)
        self.label.setObjectName(u"label")

        self.horizontalLayout_aspect.addWidget(self.label)

        self.clip_ar_den = QSpinBox(self.tab_advanced)
        self.clip_ar_den.setObjectName(u"clip_ar_den")
        self.clip_ar_den.setEnabled(False)
        self.clip_ar_den.setMinimum(1)
        self.clip_ar_den.setMaximum(9999)
        self.clip_ar_den.setValue(9)

        self.horizontalLayout_aspect.addWidget(self.clip_ar_den)


        self.gridLayout_3.addLayout(self.horizontalLayout_aspect, 1, 3, 1, 1)

        self.clip_force_transparency = QCheckBox(self.tab_advanced)
        self.clip_force_transparency.setObjectName(u"clip_force_transparency")

        self.gridLayout_3.addWidget(self.clip_force_transparency, 11, 1, 1, 1)

        self.clip_transparency = KComboBox(self.tab_advanced)
        self.clip_transparency.addItem("")
        self.clip_transparency.addItem("")
        self.clip_transparency.setObjectName(u"clip_transparency")

        self.gridLayout_3.addWidget(self.clip_transparency, 11, 3, 1, 1)

        self.clip_progressive = KComboBox(self.tab_advanced)
        self.clip_progressive.setObjectName(u"clip_progressive")
        self.clip_progressive.setEnabled(False)

        self.gridLayout_3.addWidget(self.clip_progressive, 3, 3, 1, 1)

        self.clip_out = QLineEdit(self.tab_advanced)
        self.clip_out.setObjectName(u"clip_out")

        self.gridLayout_3.addWidget(self.clip_out, 0, 3, 1, 1)

        self.tabWidget.addTab(self.tab_advanced, "")

        self.gridLayout_2.addWidget(self.tabWidget, 7, 0, 1, 5)

        self.verticalSpacer_4 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 8, 2, 1, 2)

        self.buttonBox = QDialogButtonBox(ClipProperties_UI)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Close|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 9, 0, 1, 5)

        self.clip_duration = QLineEdit(ClipProperties_UI)
        self.clip_duration.setObjectName(u"clip_duration")

        self.gridLayout_2.addWidget(self.clip_duration, 5, 1, 1, 1)


        self.retranslateUi(ClipProperties_UI)
        self.buttonBox.accepted.connect(ClipProperties_UI.accept)
        self.buttonBox.rejected.connect(ClipProperties_UI.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ClipProperties_UI)
    # setupUi

    def retranslateUi(self, ClipProperties_UI):
        ClipProperties_UI.setWindowTitle(QCoreApplication.translate("ClipProperties_UI", u"Clip Properties", None))
        self.label_path.setText(QCoreApplication.translate("ClipProperties_UI", u"Path", None))
        self.label_description.setText(QCoreApplication.translate("ClipProperties_UI", u"Description", None))
        self.label_size.setText(QCoreApplication.translate("ClipProperties_UI", u"Size:", None))
        self.label_duration.setText(QCoreApplication.translate("ClipProperties_UI", u"Duration", None))
        self.clip_filesize.setText(QCoreApplication.translate("ClipProperties_UI", u"File size", None))
        self.clip_license.setText("")
        ___qtreewidgetitem = self.clip_vproperties.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("ClipProperties_UI", u"2", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("ClipProperties_UI", u"1", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_video), QCoreApplication.translate("ClipProperties_UI", u"Video", None))
        ___qtreewidgetitem1 = self.clip_aproperties.headerItem()
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("ClipProperties_UI", u"2", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("ClipProperties_UI", u"1", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_audio), QCoreApplication.translate("ClipProperties_UI", u"Audio", None))
        self.label_13.setText(QCoreApplication.translate("ClipProperties_UI", u"Color", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("ClipProperties_UI", u"Color", None))
        self.slide_type_label.setText(QCoreApplication.translate("ClipProperties_UI", u"Image type", None))
        self.clip_filesize_4.setText(QCoreApplication.translate("ClipProperties_UI", u"Frame duration", None))
        self.slide_loop.setText(QCoreApplication.translate("ClipProperties_UI", u"Loop", None))
        self.slide_fade.setText(QCoreApplication.translate("ClipProperties_UI", u"Dissolve", None))
        self.slide_luma.setText(QCoreApplication.translate("ClipProperties_UI", u"Wipe", None))
        self.label_softness.setText(QCoreApplication.translate("ClipProperties_UI", u"Softness", None))
        self.slide_info.setText(QCoreApplication.translate("ClipProperties_UI", u"No image found", None))
        self.slide_crop.setText(QCoreApplication.translate("ClipProperties_UI", u"Center crop", None))
        self.label_animation.setText(QCoreApplication.translate("ClipProperties_UI", u"Animation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_slideshow), QCoreApplication.translate("ClipProperties_UI", u"Slideshow", None))
        self.label_16.setText(QCoreApplication.translate("ClipProperties_UI", u"Image size", None))
        self.image_transparency.setText(QCoreApplication.translate("ClipProperties_UI", u"Transparent background", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_image), QCoreApplication.translate("ClipProperties_UI", u"Image", None))
        ___qtreewidgetitem2 = self.markers_list.headerItem()
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("ClipProperties_UI", u"Comment", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("ClipProperties_UI", u"Time", None));
        self.marker_new.setText(QCoreApplication.translate("ClipProperties_UI", u"N", None))
        self.marker_edit.setText(QCoreApplication.translate("ClipProperties_UI", u"E", None))
        self.marker_delete.setText(QCoreApplication.translate("ClipProperties_UI", u"D", None))
        self.marker_save.setText(QCoreApplication.translate("ClipProperties_UI", u"...", None))
        self.marker_load.setText(QCoreApplication.translate("ClipProperties_UI", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("ClipProperties_UI", u"Markers", None))
        ___qtreewidgetitem3 = self.metadata_list.headerItem()
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("ClipProperties_UI", u"2", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("ClipProperties_UI", u"1", None));
        ___qtreewidgetitem4 = self.analysis_list.headerItem()
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("ClipProperties_UI", u"2", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("ClipProperties_UI", u"1", None));
        self.analysis_delete.setText(QCoreApplication.translate("ClipProperties_UI", u"...", None))
        self.analysis_save.setText(QCoreApplication.translate("ClipProperties_UI", u"...", None))
        self.analysis_load.setText(QCoreApplication.translate("ClipProperties_UI", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("ClipProperties_UI", u"Metadata", None))
        self.clip_force_ar.setText(QCoreApplication.translate("ClipProperties_UI", u"Force aspect ratio", None))
        self.clip_force_threads.setText(QCoreApplication.translate("ClipProperties_UI", u"Decoding threads", None))
        self.clip_force_vindex.setText(QCoreApplication.translate("ClipProperties_UI", u"Video index", None))
        self.clip_force_progressive.setText(QCoreApplication.translate("ClipProperties_UI", u"Force scanning", None))
        self.clip_force_aindex.setText(QCoreApplication.translate("ClipProperties_UI", u"Audio index", None))
        self.clip_force_framerate.setText(QCoreApplication.translate("ClipProperties_UI", u"Force frame rate", None))
        self.clip_force_out.setText(QCoreApplication.translate("ClipProperties_UI", u"Force duration", None))
        self.clip_force_colorspace.setText(QCoreApplication.translate("ClipProperties_UI", u"Force colorspace", None))
        self.clip_force_fieldorder.setText(QCoreApplication.translate("ClipProperties_UI", u"Force field order", None))
        self.clip_full_luma.setText(QCoreApplication.translate("ClipProperties_UI", u"Full luma range", None))
        self.label.setText(QCoreApplication.translate("ClipProperties_UI", u":", None))
        self.clip_force_transparency.setText(QCoreApplication.translate("ClipProperties_UI", u"Image background", None))
        self.clip_transparency.setItemText(0, QCoreApplication.translate("ClipProperties_UI", u"Normal", None))
        self.clip_transparency.setItemText(1, QCoreApplication.translate("ClipProperties_UI", u"Transparent", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_advanced), QCoreApplication.translate("ClipProperties_UI", u"Advanced", None))
    # retranslateUi

