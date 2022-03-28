# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pro.ui'
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
    QDialog, QDialogButtonBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
    QToolButton, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

from kcombobox import KComboBox
from ktreewidgetsearchline import KTreeWidgetSearchLine
from kurlrequester import KUrlRequester

class Ui_ProjectSettings_UI(object):
    def setupUi(self, ProjectSettings_UI):
        if not ProjectSettings_UI.objectName():
            ProjectSettings_UI.setObjectName(u"ProjectSettings_UI")
        ProjectSettings_UI.resize(575, 685)
        self.gridLayout_3 = QGridLayout(ProjectSettings_UI)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.buttonBox = QDialogButtonBox(ProjectSettings_UI)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_3.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.tabWidget = QTabWidget(ProjectSettings_UI)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setDocumentMode(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.previewparams = QPlainTextEdit(self.tab)
        self.previewparams.setObjectName(u"previewparams")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previewparams.sizePolicy().hasHeightForWidth())
        self.previewparams.setSizePolicy(sizePolicy)
        self.previewparams.setReadOnly(True)

        self.gridLayout.addWidget(self.previewparams, 7, 0, 1, 4)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.audio_thumbs = QCheckBox(self.tab)
        self.audio_thumbs.setObjectName(u"audio_thumbs")

        self.gridLayout.addWidget(self.audio_thumbs, 5, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.video_tracks = QSpinBox(self.tab)
        self.video_tracks.setObjectName(u"video_tracks")

        self.horizontalLayout_2.addWidget(self.video_tracks)

        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.audio_tracks = QSpinBox(self.tab)
        self.audio_tracks.setObjectName(u"audio_tracks")

        self.horizontalLayout_2.addWidget(self.audio_tracks)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.audio_channels = QComboBox(self.tab)
        self.audio_channels.addItem("")
        self.audio_channels.addItem("")
        self.audio_channels.addItem("")
        self.audio_channels.setObjectName(u"audio_channels")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.audio_channels.sizePolicy().hasHeightForWidth())
        self.audio_channels.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.audio_channels)


        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 4)

        self.horizontalSpacer = QSpacerItem(229, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 3, 1, 1)

        self.profile_box = QGroupBox(self.tab)
        self.profile_box.setObjectName(u"profile_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.profile_box.sizePolicy().hasHeightForWidth())
        self.profile_box.setSizePolicy(sizePolicy2)
        self.profile_box.setFlat(True)

        self.gridLayout.addWidget(self.profile_box, 3, 0, 1, 4)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 4)

        self.video_thumbs = QCheckBox(self.tab)
        self.video_thumbs.setObjectName(u"video_thumbs")

        self.gridLayout.addWidget(self.video_thumbs, 5, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_25 = QLabel(self.tab)
        self.label_25.setObjectName(u"label_25")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.label_25)

        self.preview_profile = KComboBox(self.tab)
        self.preview_profile.setObjectName(u"preview_profile")
        sizePolicy1.setHeightForWidth(self.preview_profile.sizePolicy().hasHeightForWidth())
        self.preview_profile.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.preview_profile)

        self.preview_showprofileinfo = QToolButton(self.tab)
        self.preview_showprofileinfo.setObjectName(u"preview_showprofileinfo")
        self.preview_showprofileinfo.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.preview_showprofileinfo)

        self.preview_manageprofile = QToolButton(self.tab)
        self.preview_manageprofile.setObjectName(u"preview_manageprofile")

        self.horizontalLayout_4.addWidget(self.preview_manageprofile)


        self.gridLayout.addLayout(self.horizontalLayout_4, 6, 0, 1, 4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.custom_folder = QCheckBox(self.tab)
        self.custom_folder.setObjectName(u"custom_folder")

        self.horizontalLayout.addWidget(self.custom_folder)

        self.project_folder = KUrlRequester(self.tab)
        self.project_folder.setObjectName(u"project_folder")
        self.project_folder.setEnabled(False)

        self.horizontalLayout.addWidget(self.project_folder)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 4)

        self.same_folder = QCheckBox(self.tab)
        self.same_folder.setObjectName(u"same_folder")

        self.gridLayout.addWidget(self.same_folder, 2, 0, 1, 4)

        self.tabWidget.addTab(self.tab, "")
        self.label_4.raise_()
        self.profile_box.raise_()
        self.label_2.raise_()
        self.video_thumbs.raise_()
        self.audio_thumbs.raise_()
        self.previewparams.raise_()
        self.same_folder.raise_()
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout = QVBoxLayout(self.tab_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.enable_proxy = QCheckBox(self.tab_4)
        self.enable_proxy.setObjectName(u"enable_proxy")

        self.verticalLayout.addWidget(self.enable_proxy)

        self.proxy_box = QGroupBox(self.tab_4)
        self.proxy_box.setObjectName(u"proxy_box")
        self.proxy_box.setEnabled(False)
        self.proxy_box.setFlat(True)
        self.proxy_box.setCheckable(False)
        self.proxy_box.setChecked(False)
        self.gridLayout_2 = QGridLayout(self.proxy_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.l_relPathProxyToOrig = QLabel(self.proxy_box)
        self.l_relPathProxyToOrig.setObjectName(u"l_relPathProxyToOrig")

        self.gridLayout_2.addWidget(self.l_relPathProxyToOrig, 10, 1, 1, 1)

        self.generate_imageproxy = QCheckBox(self.proxy_box)
        self.generate_imageproxy.setObjectName(u"generate_imageproxy")

        self.gridLayout_2.addWidget(self.generate_imageproxy, 3, 0, 1, 2)

        self.l_prefix_proxy = QLabel(self.proxy_box)
        self.l_prefix_proxy.setObjectName(u"l_prefix_proxy")

        self.gridLayout_2.addWidget(self.l_prefix_proxy, 11, 1, 1, 1)

        self.proxy_imagesize = QSpinBox(self.proxy_box)
        self.proxy_imagesize.setObjectName(u"proxy_imagesize")
        self.proxy_imagesize.setEnabled(False)
        self.proxy_imagesize.setMinimum(200)
        self.proxy_imagesize.setMaximum(100000)
        self.proxy_imagesize.setValue(800)

        self.gridLayout_2.addWidget(self.proxy_imagesize, 4, 2, 1, 4)

        self.label_24 = QLabel(self.proxy_box)
        self.label_24.setObjectName(u"label_24")
        sizePolicy3.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.label_24, 1, 0, 1, 1)

        self.proxy_minsize = QSpinBox(self.proxy_box)
        self.proxy_minsize.setObjectName(u"proxy_minsize")
        self.proxy_minsize.setMaximum(10000)
        self.proxy_minsize.setValue(1000)

        self.gridLayout_2.addWidget(self.proxy_minsize, 0, 2, 1, 4)

        self.l_prefix_clip = QLabel(self.proxy_box)
        self.l_prefix_clip.setObjectName(u"l_prefix_clip")

        self.gridLayout_2.addWidget(self.l_prefix_clip, 8, 1, 1, 1)

        self.proxy_profile = KComboBox(self.proxy_box)
        self.proxy_profile.setObjectName(u"proxy_profile")
        sizePolicy1.setHeightForWidth(self.proxy_profile.sizePolicy().hasHeightForWidth())
        self.proxy_profile.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.proxy_profile, 1, 1, 1, 2)

        self.proxy_showprofileinfo = QToolButton(self.proxy_box)
        self.proxy_showprofileinfo.setObjectName(u"proxy_showprofileinfo")
        self.proxy_showprofileinfo.setCheckable(True)

        self.gridLayout_2.addWidget(self.proxy_showprofileinfo, 1, 4, 1, 1)

        self.generate_proxy = QCheckBox(self.proxy_box)
        self.generate_proxy.setObjectName(u"generate_proxy")

        self.gridLayout_2.addWidget(self.generate_proxy, 0, 0, 1, 2)

        self.proxyparams = QPlainTextEdit(self.proxy_box)
        self.proxyparams.setObjectName(u"proxyparams")
        sizePolicy.setHeightForWidth(self.proxyparams.sizePolicy().hasHeightForWidth())
        self.proxyparams.setSizePolicy(sizePolicy)
        self.proxyparams.setReadOnly(True)

        self.gridLayout_2.addWidget(self.proxyparams, 2, 0, 1, 6)

        self.image_label = QLabel(self.proxy_box)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setEnabled(False)

        self.gridLayout_2.addWidget(self.image_label, 4, 0, 1, 2)

        self.le_relPathProxyToOrig = QLineEdit(self.proxy_box)
        self.le_relPathProxyToOrig.setObjectName(u"le_relPathProxyToOrig")
        self.le_relPathProxyToOrig.setEnabled(False)

        self.gridLayout_2.addWidget(self.le_relPathProxyToOrig, 10, 3, 1, 1)

        self.le_prefix_proxy = QLineEdit(self.proxy_box)
        self.le_prefix_proxy.setObjectName(u"le_prefix_proxy")
        self.le_prefix_proxy.setEnabled(False)

        self.gridLayout_2.addWidget(self.le_prefix_proxy, 11, 3, 1, 1)

        self.l_suffix_proxy = QLabel(self.proxy_box)
        self.l_suffix_proxy.setObjectName(u"l_suffix_proxy")

        self.gridLayout_2.addWidget(self.l_suffix_proxy, 12, 1, 1, 1)

        self.le_prefix_clip = QLineEdit(self.proxy_box)
        self.le_prefix_clip.setObjectName(u"le_prefix_clip")
        self.le_prefix_clip.setEnabled(False)

        self.gridLayout_2.addWidget(self.le_prefix_clip, 8, 3, 1, 1)

        self.le_suffix_proxy = QLineEdit(self.proxy_box)
        self.le_suffix_proxy.setObjectName(u"le_suffix_proxy")
        self.le_suffix_proxy.setEnabled(False)

        self.gridLayout_2.addWidget(self.le_suffix_proxy, 12, 3, 1, 1)

        self.proxy_imageminsize = QSpinBox(self.proxy_box)
        self.proxy_imageminsize.setObjectName(u"proxy_imageminsize")
        self.proxy_imageminsize.setMinimum(500)
        self.proxy_imageminsize.setMaximum(100000)
        self.proxy_imageminsize.setValue(2000)

        self.gridLayout_2.addWidget(self.proxy_imageminsize, 3, 2, 1, 4)

        self.l_suffix_clip = QLabel(self.proxy_box)
        self.l_suffix_clip.setObjectName(u"l_suffix_clip")

        self.gridLayout_2.addWidget(self.l_suffix_clip, 9, 1, 1, 1)

        self.l_relPathOrigToProxy = QLabel(self.proxy_box)
        self.l_relPathOrigToProxy.setObjectName(u"l_relPathOrigToProxy")

        self.gridLayout_2.addWidget(self.l_relPathOrigToProxy, 7, 1, 1, 1)

        self.le_relPathOrigToProxy = QLineEdit(self.proxy_box)
        self.le_relPathOrigToProxy.setObjectName(u"le_relPathOrigToProxy")
        self.le_relPathOrigToProxy.setEnabled(False)

        self.gridLayout_2.addWidget(self.le_relPathOrigToProxy, 7, 3, 1, 1)

        self.external_proxy_profile = QComboBox(self.proxy_box)
        self.external_proxy_profile.setObjectName(u"external_proxy_profile")

        self.gridLayout_2.addWidget(self.external_proxy_profile, 6, 1, 1, 5)

        self.proxy_resize = QSpinBox(self.proxy_box)
        self.proxy_resize.setObjectName(u"proxy_resize")
        self.proxy_resize.setMinimum(200)
        self.proxy_resize.setMaximum(100000)

        self.gridLayout_2.addWidget(self.proxy_resize, 5, 2, 1, 4)

        self.le_suffix_clip = QLineEdit(self.proxy_box)
        self.le_suffix_clip.setObjectName(u"le_suffix_clip")
        self.le_suffix_clip.setEnabled(False)

        self.gridLayout_2.addWidget(self.le_suffix_clip, 9, 3, 1, 1)

        self.external_proxy = QCheckBox(self.proxy_box)
        self.external_proxy.setObjectName(u"external_proxy")

        self.gridLayout_2.addWidget(self.external_proxy, 6, 0, 1, 1)

        self.checkProxy = QToolButton(self.proxy_box)
        self.checkProxy.setObjectName(u"checkProxy")

        self.gridLayout_2.addWidget(self.checkProxy, 1, 3, 1, 1)

        self.label_3 = QLabel(self.proxy_box)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1)

        self.proxy_manageprofile = QToolButton(self.proxy_box)
        self.proxy_manageprofile.setObjectName(u"proxy_manageprofile")

        self.gridLayout_2.addWidget(self.proxy_manageprofile, 1, 5, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 13, 1, 1, 1)


        self.verticalLayout.addWidget(self.proxy_box)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_6 = QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.metadata_list = QTreeWidget(self.tab_3)
        self.metadata_list.setObjectName(u"metadata_list")
        self.metadata_list.setAlternatingRowColors(True)
        self.metadata_list.setRootIsDecorated(False)
        self.metadata_list.setAllColumnsShowFocus(True)
        self.metadata_list.setColumnCount(2)
        self.metadata_list.header().setVisible(False)

        self.gridLayout_6.addWidget(self.metadata_list, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.add_metadata = QToolButton(self.tab_3)
        self.add_metadata.setObjectName(u"add_metadata")

        self.horizontalLayout_3.addWidget(self.add_metadata)

        self.delete_metadata = QToolButton(self.tab_3)
        self.delete_metadata.setObjectName(u"delete_metadata")

        self.horizontalLayout_3.addWidget(self.delete_metadata)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout_6.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.fonts_list = QListWidget(self.tab_2)
        self.fonts_list.setObjectName(u"fonts_list")
        self.fonts_list.setAlternatingRowColors(True)

        self.gridLayout_4.addWidget(self.fonts_list, 5, 0, 1, 5)

        self.files_list = QTreeWidget(self.tab_2)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.files_list.setHeaderItem(__qtreewidgetitem)
        self.files_list.setObjectName(u"files_list")
        self.files_list.setAlternatingRowColors(True)
        self.files_list.setRootIsDecorated(False)
        self.files_list.setItemsExpandable(False)
        self.files_list.setHeaderHidden(True)
        self.files_list.setExpandsOnDoubleClick(False)

        self.gridLayout_4.addWidget(self.files_list, 3, 0, 1, 5)

        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 2)

        self.used_count = QLabel(self.tab_2)
        self.used_count.setObjectName(u"used_count")

        self.gridLayout_4.addWidget(self.used_count, 0, 2, 1, 1)

        self.used_size = QLabel(self.tab_2)
        self.used_size.setObjectName(u"used_size")

        self.gridLayout_4.addWidget(self.used_size, 0, 3, 1, 1)

        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)

        self.unused_count = QLabel(self.tab_2)
        self.unused_count.setObjectName(u"unused_count")

        self.gridLayout_4.addWidget(self.unused_count, 1, 2, 1, 1)

        self.unused_size = QLabel(self.tab_2)
        self.unused_size.setObjectName(u"unused_size")

        self.gridLayout_4.addWidget(self.unused_size, 1, 3, 1, 1)

        self.delete_unused = QPushButton(self.tab_2)
        self.delete_unused.setObjectName(u"delete_unused")

        self.gridLayout_4.addWidget(self.delete_unused, 1, 4, 1, 1)

        self.list_search = KTreeWidgetSearchLine(self.tab_2)
        self.list_search.setObjectName(u"list_search")

        self.gridLayout_4.addWidget(self.list_search, 2, 3, 1, 2)

        self.label_13 = QLabel(self.tab_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_fonts = QLabel(self.tab_2)
        self.label_fonts.setObjectName(u"label_fonts")

        self.gridLayout_4.addWidget(self.label_fonts, 4, 0, 1, 1)

        self.button_export = QPushButton(self.tab_2)
        self.button_export.setObjectName(u"button_export")

        self.gridLayout_4.addWidget(self.button_export, 6, 0, 1, 2)

        self.files_count = QLabel(self.tab_2)
        self.files_count.setObjectName(u"files_count")

        self.gridLayout_4.addWidget(self.files_count, 2, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(ProjectSettings_UI)
        self.buttonBox.accepted.connect(ProjectSettings_UI.accept)
        self.buttonBox.rejected.connect(ProjectSettings_UI.reject)
        self.custom_folder.toggled.connect(self.project_folder.setEnabled)
        self.enable_proxy.toggled.connect(self.proxy_box.setEnabled)
        self.external_proxy.toggled.connect(self.external_proxy_profile.setEnabled)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ProjectSettings_UI)
    # setupUi

    def retranslateUi(self, ProjectSettings_UI):
        ProjectSettings_UI.setWindowTitle(QCoreApplication.translate("ProjectSettings_UI", u"Project Settings", None))
        self.label_2.setText(QCoreApplication.translate("ProjectSettings_UI", u"Thumbnails:", None))
        self.audio_thumbs.setText(QCoreApplication.translate("ProjectSettings_UI", u"Audio", None))
        self.label_7.setText(QCoreApplication.translate("ProjectSettings_UI", u"Video tracks:", None))
        self.label_8.setText(QCoreApplication.translate("ProjectSettings_UI", u"Audio tracks:", None))
        self.label.setText(QCoreApplication.translate("ProjectSettings_UI", u"Audio channels:", None))
        self.audio_channels.setItemText(0, QCoreApplication.translate("ProjectSettings_UI", u"2 Channels (Stereo)", None))
        self.audio_channels.setItemText(1, QCoreApplication.translate("ProjectSettings_UI", u"4 Channels", None))
        self.audio_channels.setItemText(2, QCoreApplication.translate("ProjectSettings_UI", u"6 Channels", None))

        self.label_4.setText(QCoreApplication.translate("ProjectSettings_UI", u"Project folder to store proxy clips, thumbnails, previews", None))
        self.video_thumbs.setText(QCoreApplication.translate("ProjectSettings_UI", u"Video", None))
        self.label_25.setText(QCoreApplication.translate("ProjectSettings_UI", u"Preview profile:", None))
        self.preview_showprofileinfo.setText(QCoreApplication.translate("ProjectSettings_UI", u"...", None))
        self.preview_manageprofile.setText(QCoreApplication.translate("ProjectSettings_UI", u"...", None))
        self.custom_folder.setText(QCoreApplication.translate("ProjectSettings_UI", u"Custom project folder:", None))
        self.same_folder.setText(QCoreApplication.translate("ProjectSettings_UI", u"Use parent folder of the project file as project folder", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("ProjectSettings_UI", u"Settings", None))
        self.enable_proxy.setText(QCoreApplication.translate("ProjectSettings_UI", u"Enable proxy clips", None))
        self.l_relPathProxyToOrig.setText(QCoreApplication.translate("ProjectSettings_UI", u"Relative path from proxy to clip:", None))
        self.generate_imageproxy.setText(QCoreApplication.translate("ProjectSettings_UI", u"Generate for images larger than", None))
        self.l_prefix_proxy.setText(QCoreApplication.translate("ProjectSettings_UI", u"Prefix of proxy:", None))
        self.proxy_imagesize.setSuffix(QCoreApplication.translate("ProjectSettings_UI", u"pixels", None))
        self.label_24.setText(QCoreApplication.translate("ProjectSettings_UI", u"Encoding profile:", None))
        self.proxy_minsize.setSuffix(QCoreApplication.translate("ProjectSettings_UI", u"pixels", None))
        self.l_prefix_clip.setText(QCoreApplication.translate("ProjectSettings_UI", u"Prefix of clip:", None))
        self.proxy_showprofileinfo.setText(QCoreApplication.translate("ProjectSettings_UI", u"...", None))
        self.generate_proxy.setText(QCoreApplication.translate("ProjectSettings_UI", u"Generate for videos larger than", None))
        self.image_label.setText(QCoreApplication.translate("ProjectSettings_UI", u"Proxy image size", None))
        self.l_suffix_proxy.setText(QCoreApplication.translate("ProjectSettings_UI", u"Suffix of proxy:", None))
        self.proxy_imageminsize.setSuffix(QCoreApplication.translate("ProjectSettings_UI", u"pixels", None))
        self.l_suffix_clip.setText(QCoreApplication.translate("ProjectSettings_UI", u"Suffix of clip:", None))
        self.l_relPathOrigToProxy.setText(QCoreApplication.translate("ProjectSettings_UI", u"Relative path from clip to proxy:", None))
        self.proxy_resize.setSuffix(QCoreApplication.translate("ProjectSettings_UI", u"pixels", None))
        self.external_proxy.setText(QCoreApplication.translate("ProjectSettings_UI", u"Use external proxy clips", None))
        self.checkProxy.setText(QCoreApplication.translate("ProjectSettings_UI", u"...", None))
        self.label_3.setText(QCoreApplication.translate("ProjectSettings_UI", u"Proxy video resize (width)", None))
        self.proxy_manageprofile.setText(QCoreApplication.translate("ProjectSettings_UI", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("ProjectSettings_UI", u"Proxy", None))
        ___qtreewidgetitem = self.metadata_list.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("ProjectSettings_UI", u"2", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("ProjectSettings_UI", u"1", None));
        self.add_metadata.setText(QCoreApplication.translate("ProjectSettings_UI", u"...", None))
        self.delete_metadata.setText(QCoreApplication.translate("ProjectSettings_UI", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("ProjectSettings_UI", u"Metadata", None))
        self.label_12.setText(QCoreApplication.translate("ProjectSettings_UI", u"Clips used in project:", None))
        self.used_count.setText("")
        self.used_size.setText("")
        self.label_6.setText(QCoreApplication.translate("ProjectSettings_UI", u"Unused clips:", None))
        self.unused_count.setText("")
        self.unused_size.setText("")
        self.delete_unused.setText(QCoreApplication.translate("ProjectSettings_UI", u"Delete files", None))
        self.label_13.setText(QCoreApplication.translate("ProjectSettings_UI", u"Project files:", None))
        self.label_fonts.setText(QCoreApplication.translate("ProjectSettings_UI", u"Fonts", None))
        self.button_export.setText(QCoreApplication.translate("ProjectSettings_UI", u"Plain Text Export...", None))
        self.files_count.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("ProjectSettings_UI", u"Project Files", None))
    # retranslateUi

