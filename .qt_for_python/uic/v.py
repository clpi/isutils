# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QDialog, QFontComboBox, QFrame,
    QGraphicsView, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QListView, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QSplitter, QStackedWidget, QTabWidget,
    QToolButton, QVBoxLayout, QWidget)

from kcolorbutton import KColorButton
from kcombobox import KComboBox

class Ui_TitleWidget_UI(object):
    def setupUi(self, TitleWidget_UI):
        if not TitleWidget_UI.objectName():
            TitleWidget_UI.setObjectName(u"TitleWidget_UI")
        TitleWidget_UI.resize(1096, 726)
        self.gridLayout_7 = QGridLayout(TitleWidget_UI)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonFitZoom = QToolButton(TitleWidget_UI)
        self.buttonFitZoom.setObjectName(u"buttonFitZoom")
        icon = QIcon()
        iconThemeName = u"zoom-fit-best"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.buttonFitZoom.setIcon(icon)
        self.buttonFitZoom.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.buttonFitZoom)

        self.buttonRealSize = QToolButton(TitleWidget_UI)
        self.buttonRealSize.setObjectName(u"buttonRealSize")
        icon1 = QIcon()
        iconThemeName = u"zoom-original"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.buttonRealSize.setIcon(icon1)
        self.buttonRealSize.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.buttonRealSize)

        self.line_8 = QFrame(TitleWidget_UI)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_8)

        self.zoom_slider = QSlider(TitleWidget_UI)
        self.zoom_slider.setObjectName(u"zoom_slider")
        self.zoom_slider.setMinimumSize(QSize(100, 0))
        self.zoom_slider.setMaximumSize(QSize(150, 16777215))
        self.zoom_slider.setMinimum(1)
        self.zoom_slider.setMaximum(1000)
        self.zoom_slider.setPageStep(30)
        self.zoom_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.zoom_slider)

        self.zoom_spin = QSpinBox(TitleWidget_UI)
        self.zoom_spin.setObjectName(u"zoom_spin")
        self.zoom_spin.setKeyboardTracking(False)
        self.zoom_spin.setMinimum(1)
        self.zoom_spin.setMaximum(1000)

        self.horizontalLayout.addWidget(self.zoom_spin)

        self.line_7 = QFrame(TitleWidget_UI)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_7)

        self.displayBg = QCheckBox(TitleWidget_UI)
        self.displayBg.setObjectName(u"displayBg")

        self.horizontalLayout.addWidget(self.displayBg)

        self.bgBox = QComboBox(TitleWidget_UI)
        self.bgBox.addItem("")
        self.bgBox.addItem("")
        self.bgBox.addItem("")
        self.bgBox.setObjectName(u"bgBox")

        self.horizontalLayout.addWidget(self.bgBox)

        self.line_6 = QFrame(TitleWidget_UI)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_6)

        self.label_template = QLabel(TitleWidget_UI)
        self.label_template.setObjectName(u"label_template")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_template.sizePolicy().hasHeightForWidth())
        self.label_template.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_template)

        self.templateBox = KComboBox(TitleWidget_UI)
        self.templateBox.setObjectName(u"templateBox")
        self.templateBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout.addWidget(self.templateBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.createButton = QToolButton(TitleWidget_UI)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.createButton.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.horizontalLayout.addWidget(self.createButton)

        self.cancelButton = QPushButton(TitleWidget_UI)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.gridLayout_7.addLayout(self.horizontalLayout, 9, 0, 1, 9)

        self.frame_properties = QFrame(TitleWidget_UI)
        self.frame_properties.setObjectName(u"frame_properties")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_properties.sizePolicy().hasHeightForWidth())
        self.frame_properties.setSizePolicy(sizePolicy1)
        self.frame_properties.setFrameShape(QFrame.NoFrame)
        self.frame_properties.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frame_properties)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(82, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 8, 1, 1)

        self.zDown = QToolButton(self.frame_properties)
        self.zDown.setObjectName(u"zDown")

        self.gridLayout.addWidget(self.zDown, 0, 10, 1, 1)

        self.value_x = QSpinBox(self.frame_properties)
        self.value_x.setObjectName(u"value_x")
        self.value_x.setMinimum(-5000)
        self.value_x.setMaximum(5000)

        self.gridLayout.addWidget(self.value_x, 0, 1, 1, 1)

        self.origin_x_left = QPushButton(self.frame_properties)
        self.origin_x_left.setObjectName(u"origin_x_left")
        self.origin_x_left.setCheckable(True)
        self.origin_x_left.setChecked(False)

        self.gridLayout.addWidget(self.origin_x_left, 0, 0, 1, 1)

        self.zValue = QSpinBox(self.frame_properties)
        self.zValue.setObjectName(u"zValue")
        self.zValue.setMinimum(-5000)
        self.zValue.setMaximum(5000)

        self.gridLayout.addWidget(self.zValue, 0, 14, 1, 1)

        self.label_zIndex = QLabel(self.frame_properties)
        self.label_zIndex.setObjectName(u"label_zIndex")

        self.gridLayout.addWidget(self.label_zIndex, 0, 13, 1, 1)

        self.origin_y_top = QPushButton(self.frame_properties)
        self.origin_y_top.setObjectName(u"origin_y_top")
        self.origin_y_top.setCheckable(True)
        self.origin_y_top.setChecked(False)

        self.gridLayout.addWidget(self.origin_y_top, 0, 2, 1, 1)

        self.value_h = QSpinBox(self.frame_properties)
        self.value_h.setObjectName(u"value_h")
        self.value_h.setMinimum(-1000)
        self.value_h.setMaximum(5000)

        self.gridLayout.addWidget(self.value_h, 0, 7, 1, 1)

        self.label_height = QLabel(self.frame_properties)
        self.label_height.setObjectName(u"label_height")

        self.gridLayout.addWidget(self.label_height, 0, 6, 1, 1)

        self.zTop = QToolButton(self.frame_properties)
        self.zTop.setObjectName(u"zTop")

        self.gridLayout.addWidget(self.zTop, 0, 11, 1, 1)

        self.zUp = QToolButton(self.frame_properties)
        self.zUp.setObjectName(u"zUp")

        self.gridLayout.addWidget(self.zUp, 0, 9, 1, 1)

        self.zBottom = QToolButton(self.frame_properties)
        self.zBottom.setObjectName(u"zBottom")

        self.gridLayout.addWidget(self.zBottom, 0, 12, 1, 1)

        self.value_w = QSpinBox(self.frame_properties)
        self.value_w.setObjectName(u"value_w")
        self.value_w.setMinimum(-1000)
        self.value_w.setMaximum(5000)

        self.gridLayout.addWidget(self.value_w, 0, 5, 1, 1)

        self.label_width = QLabel(self.frame_properties)
        self.label_width.setObjectName(u"label_width")

        self.gridLayout.addWidget(self.label_width, 0, 4, 1, 1)

        self.value_y = QSpinBox(self.frame_properties)
        self.value_y.setObjectName(u"value_y")
        self.value_y.setMinimum(-5000)
        self.value_y.setMaximum(5000)

        self.gridLayout.addWidget(self.value_y, 0, 3, 1, 1)


        self.gridLayout_7.addWidget(self.frame_properties, 0, 8, 1, 1)

        self.splitter = QSplitter(TitleWidget_UI)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.grid_main = QGridLayout(self.verticalLayoutWidget)
        self.grid_main.setObjectName(u"grid_main")
        self.grid_main.setVerticalSpacing(0)
        self.grid_main.setContentsMargins(0, 0, 0, 0)
        self.use_grid = QCheckBox(self.verticalLayoutWidget)
        self.use_grid.setObjectName(u"use_grid")

        self.grid_main.addWidget(self.use_grid, 3, 5, 1, 1)

        self.buttonSelectRects = QToolButton(self.verticalLayoutWidget)
        self.buttonSelectRects.setObjectName(u"buttonSelectRects")
        self.buttonSelectRects.setEnabled(False)

        self.grid_main.addWidget(self.buttonSelectRects, 3, 4, 1, 1)

        self.buttonSelectImages = QToolButton(self.verticalLayoutWidget)
        self.buttonSelectImages.setObjectName(u"buttonSelectImages")
        self.buttonSelectImages.setEnabled(False)

        self.grid_main.addWidget(self.buttonSelectImages, 3, 0, 1, 1)

        self.buttonSelectText = QToolButton(self.verticalLayoutWidget)
        self.buttonSelectText.setObjectName(u"buttonSelectText")
        self.buttonSelectText.setEnabled(False)

        self.grid_main.addWidget(self.buttonSelectText, 3, 1, 1, 1)

        self.hguides = QSpinBox(self.verticalLayoutWidget)
        self.hguides.setObjectName(u"hguides")
        self.hguides.setEnabled(False)
        self.hguides.setValue(2)

        self.grid_main.addWidget(self.hguides, 3, 8, 1, 1)

        self.vguides = QSpinBox(self.verticalLayoutWidget)
        self.vguides.setObjectName(u"vguides")
        self.vguides.setEnabled(False)
        self.vguides.setMaximum(99)
        self.vguides.setValue(3)

        self.grid_main.addWidget(self.vguides, 3, 7, 1, 1)

        self.messageLayout = QVBoxLayout()
        self.messageLayout.setSpacing(0)
        self.messageLayout.setObjectName(u"messageLayout")
        self.graphicsView = QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.messageLayout.addWidget(self.graphicsView)


        self.grid_main.addLayout(self.messageLayout, 0, 0, 1, 11)

        self.buttonUnselectAll = QToolButton(self.verticalLayoutWidget)
        self.buttonUnselectAll.setObjectName(u"buttonUnselectAll")
        self.buttonUnselectAll.setEnabled(False)

        self.grid_main.addWidget(self.buttonUnselectAll, 3, 2, 1, 1)

        self.spacerBottomStack = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grid_main.addItem(self.spacerBottomStack, 3, 10, 1, 1)

        self.show_guides = QCheckBox(self.verticalLayoutWidget)
        self.show_guides.setObjectName(u"show_guides")

        self.grid_main.addWidget(self.show_guides, 3, 6, 1, 1)

        self.buttonSelectAll = QToolButton(self.verticalLayoutWidget)
        self.buttonSelectAll.setObjectName(u"buttonSelectAll")

        self.grid_main.addWidget(self.buttonSelectAll, 3, 3, 1, 1)

        self.guideColor = KColorButton(self.verticalLayoutWidget)
        self.guideColor.setObjectName(u"guideColor")
        self.guideColor.setEnabled(False)
        self.guideColor.setAutoDefault(True)
        self.guideColor.setFlat(False)
        self.guideColor.setProperty("color", QColor(255, 0, 0))
        self.guideColor.setProperty("defaultColor", QColor(255, 0, 0))

        self.grid_main.addWidget(self.guideColor, 3, 9, 1, 1)

        self.splitter.addWidget(self.verticalLayoutWidget)
        self.verticalLayoutWidget_2 = QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.grid_settings = QGridLayout(self.verticalLayoutWidget_2)
        self.grid_settings.setObjectName(u"grid_settings")
        self.grid_settings.setContentsMargins(6, 0, 6, 0)
        self.itemzoom = QSpinBox(self.verticalLayoutWidget_2)
        self.itemzoom.setObjectName(u"itemzoom")
        self.itemzoom.setMaximum(100000)
        self.itemzoom.setValue(1)

        self.grid_settings.addWidget(self.itemzoom, 1, 1, 1, 1)

        self.label_rotate = QLabel(self.verticalLayoutWidget_2)
        self.label_rotate.setObjectName(u"label_rotate")

        self.grid_settings.addWidget(self.label_rotate, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_rotateX = QLabel(self.verticalLayoutWidget_2)
        self.label_rotateX.setObjectName(u"label_rotateX")

        self.horizontalLayout_3.addWidget(self.label_rotateX)

        self.itemrotatex = QSpinBox(self.verticalLayoutWidget_2)
        self.itemrotatex.setObjectName(u"itemrotatex")
        sizePolicy1.setHeightForWidth(self.itemrotatex.sizePolicy().hasHeightForWidth())
        self.itemrotatex.setSizePolicy(sizePolicy1)
        self.itemrotatex.setMinimum(-360)
        self.itemrotatex.setMaximum(360)

        self.horizontalLayout_3.addWidget(self.itemrotatex)

        self.label_rotateY = QLabel(self.verticalLayoutWidget_2)
        self.label_rotateY.setObjectName(u"label_rotateY")
        self.label_rotateY.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_rotateY)

        self.itemrotatey = QSpinBox(self.verticalLayoutWidget_2)
        self.itemrotatey.setObjectName(u"itemrotatey")
        sizePolicy1.setHeightForWidth(self.itemrotatey.sizePolicy().hasHeightForWidth())
        self.itemrotatey.setSizePolicy(sizePolicy1)
        self.itemrotatey.setMinimum(-360)
        self.itemrotatey.setMaximum(360)

        self.horizontalLayout_3.addWidget(self.itemrotatey)

        self.label_rotateZ = QLabel(self.verticalLayoutWidget_2)
        self.label_rotateZ.setObjectName(u"label_rotateZ")
        self.label_rotateZ.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_rotateZ)

        self.itemrotatez = QSpinBox(self.verticalLayoutWidget_2)
        self.itemrotatez.setObjectName(u"itemrotatez")
        sizePolicy1.setHeightForWidth(self.itemrotatez.sizePolicy().hasHeightForWidth())
        self.itemrotatez.setSizePolicy(sizePolicy1)
        self.itemrotatez.setMinimum(-360)
        self.itemrotatez.setMaximum(360)

        self.horizontalLayout_3.addWidget(self.itemrotatez)


        self.grid_settings.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)

        self.label_duration = QLabel(self.verticalLayoutWidget_2)
        self.label_duration.setObjectName(u"label_duration")

        self.grid_settings.addWidget(self.label_duration, 0, 0, 1, 1)

        self.label_itemzoom = QLabel(self.verticalLayoutWidget_2)
        self.label_itemzoom.setObjectName(u"label_itemzoom")

        self.grid_settings.addWidget(self.label_itemzoom, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(self.verticalLayoutWidget_2)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tab_properties = QWidget()
        self.tab_properties.setObjectName(u"tab_properties")
        self.gridLayout_10 = QGridLayout(self.tab_properties)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.toolbar_stack = QStackedWidget(self.tab_properties)
        self.toolbar_stack.setObjectName(u"toolbar_stack")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.toolbar_stack.sizePolicy().hasHeightForWidth())
        self.toolbar_stack.setSizePolicy(sizePolicy3)
        self.text = QWidget()
        self.text.setObjectName(u"text")
        self.gridLayout_11 = QGridLayout(self.text)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, -1)
        self.scrollArea = QScrollArea(self.text)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy4)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 388, 542))
        self.gridLayout_9 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_9.setSpacing(4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.shadowBox = QGroupBox(self.scrollAreaWidgetContents)
        self.shadowBox.setObjectName(u"shadowBox")
        self.shadowBox.setCheckable(True)
        self.shadowBox.setChecked(False)
        self.gridLayout_3 = QGridLayout(self.shadowBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(0)
        self.label_blur = QLabel(self.shadowBox)
        self.label_blur.setObjectName(u"label_blur")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_blur.sizePolicy().hasHeightForWidth())
        self.label_blur.setSizePolicy(sizePolicy5)

        self.gridLayout_3.addWidget(self.label_blur, 0, 0, 1, 1)

        self.blur_radius = QSpinBox(self.shadowBox)
        self.blur_radius.setObjectName(u"blur_radius")
        self.blur_radius.setValue(3)

        self.gridLayout_3.addWidget(self.blur_radius, 0, 1, 1, 1)

        self.shadowColor = KColorButton(self.shadowBox)
        self.shadowColor.setObjectName(u"shadowColor")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.shadowColor.sizePolicy().hasHeightForWidth())
        self.shadowColor.setSizePolicy(sizePolicy6)
        self.shadowColor.setProperty("color", QColor(0, 0, 0, 100))
        self.shadowColor.setProperty("alphaChannelEnabled", True)

        self.gridLayout_3.addWidget(self.shadowColor, 0, 2, 1, 1)

        self.label_offset = QLabel(self.shadowBox)
        self.label_offset.setObjectName(u"label_offset")
        sizePolicy5.setHeightForWidth(self.label_offset.sizePolicy().hasHeightForWidth())
        self.label_offset.setSizePolicy(sizePolicy5)

        self.gridLayout_3.addWidget(self.label_offset, 1, 0, 1, 1)

        self.shadowX = QSpinBox(self.shadowBox)
        self.shadowX.setObjectName(u"shadowX")
        self.shadowX.setMinimum(-100)
        self.shadowX.setMaximum(100)
        self.shadowX.setValue(3)

        self.gridLayout_3.addWidget(self.shadowX, 1, 1, 1, 1)

        self.shadowY = QSpinBox(self.shadowBox)
        self.shadowY.setObjectName(u"shadowY")
        self.shadowY.setMinimum(-100)
        self.shadowY.setMaximum(100)
        self.shadowY.setValue(3)

        self.gridLayout_3.addWidget(self.shadowY, 1, 2, 1, 1)


        self.gridLayout_9.addWidget(self.shadowBox, 5, 0, 1, 7)

        self.buttonInsertUnicode = QToolButton(self.scrollAreaWidgetContents)
        self.buttonInsertUnicode.setObjectName(u"buttonInsertUnicode")

        self.gridLayout_9.addWidget(self.buttonInsertUnicode, 2, 6, 1, 1)

        self.buttonAlignCenter = QToolButton(self.scrollAreaWidgetContents)
        self.buttonAlignCenter.setObjectName(u"buttonAlignCenter")
        icon2 = QIcon()
        iconThemeName = u"format-justify-center"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.buttonAlignCenter.setIcon(icon2)
        self.buttonAlignCenter.setCheckable(True)
        self.buttonAlignCenter.setAutoExclusive(True)

        self.gridLayout_9.addWidget(self.buttonAlignCenter, 6, 3, 1, 1)

        self.label_lineSpacing = QLabel(self.scrollAreaWidgetContents)
        self.label_lineSpacing.setObjectName(u"label_lineSpacing")

        self.gridLayout_9.addWidget(self.label_lineSpacing, 8, 0, 1, 1)

        self.font_family = QFontComboBox(self.scrollAreaWidgetContents)
        self.font_family.setObjectName(u"font_family")
        sizePolicy.setHeightForWidth(self.font_family.sizePolicy().hasHeightForWidth())
        self.font_family.setSizePolicy(sizePolicy)

        self.gridLayout_9.addWidget(self.font_family, 0, 0, 1, 7)

        self.gradient_color = QRadioButton(self.scrollAreaWidgetContents)
        self.gradient_color.setObjectName(u"gradient_color")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.gradient_color.sizePolicy().hasHeightForWidth())
        self.gradient_color.setSizePolicy(sizePolicy7)

        self.gridLayout_9.addWidget(self.gradient_color, 3, 0, 1, 1)

        self.font_weight_box = KComboBox(self.scrollAreaWidgetContents)
        self.font_weight_box.setObjectName(u"font_weight_box")

        self.gridLayout_9.addWidget(self.font_weight_box, 1, 2, 1, 3)

        self.plain_color = QRadioButton(self.scrollAreaWidgetContents)
        self.plain_color.setObjectName(u"plain_color")
        sizePolicy7.setHeightForWidth(self.plain_color.sizePolicy().hasHeightForWidth())
        self.plain_color.setSizePolicy(sizePolicy7)
        self.plain_color.setChecked(True)

        self.gridLayout_9.addWidget(self.plain_color, 2, 0, 1, 1)

        self.gradients_combo = QComboBox(self.scrollAreaWidgetContents)
        self.gradients_combo.setObjectName(u"gradients_combo")
        self.gradients_combo.setEnabled(False)

        self.gridLayout_9.addWidget(self.gradients_combo, 3, 2, 1, 4)

        self.label_outline = QLabel(self.scrollAreaWidgetContents)
        self.label_outline.setObjectName(u"label_outline")
        sizePolicy5.setHeightForWidth(self.label_outline.sizePolicy().hasHeightForWidth())
        self.label_outline.setSizePolicy(sizePolicy5)

        self.gridLayout_9.addWidget(self.label_outline, 4, 0, 1, 1)

        self.typewriterBox = QGroupBox(self.scrollAreaWidgetContents)
        self.typewriterBox.setObjectName(u"typewriterBox")
        self.typewriterBox.setCheckable(True)
        self.typewriterBox.setChecked(False)
        self.gridLayout_12 = QGridLayout(self.typewriterBox)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_variation = QLabel(self.typewriterBox)
        self.label_variation.setObjectName(u"label_variation")

        self.gridLayout_12.addWidget(self.label_variation, 0, 2, 1, 1)

        self.groupBox_2 = QGroupBox(self.typewriterBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_2.setFlat(True)
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tw_rd_char = QRadioButton(self.groupBox_2)
        self.tw_rd_char.setObjectName(u"tw_rd_char")
        self.tw_rd_char.setChecked(True)

        self.gridLayout_4.addWidget(self.tw_rd_char, 0, 0, 1, 1)

        self.tw_rd_word = QRadioButton(self.groupBox_2)
        self.tw_rd_word.setObjectName(u"tw_rd_word")

        self.gridLayout_4.addWidget(self.tw_rd_word, 0, 1, 1, 1)

        self.tw_rd_line = QRadioButton(self.groupBox_2)
        self.tw_rd_line.setObjectName(u"tw_rd_line")

        self.gridLayout_4.addWidget(self.tw_rd_line, 1, 0, 1, 1)

        self.tw_rd_custom = QRadioButton(self.groupBox_2)
        self.tw_rd_custom.setObjectName(u"tw_rd_custom")

        self.gridLayout_4.addWidget(self.tw_rd_custom, 1, 1, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_2, 2, 0, 1, 4)

        self.label_frameStep = QLabel(self.typewriterBox)
        self.label_frameStep.setObjectName(u"label_frameStep")

        self.gridLayout_12.addWidget(self.label_frameStep, 0, 0, 1, 1)

        self.tw_sb_sigma = QSpinBox(self.typewriterBox)
        self.tw_sb_sigma.setObjectName(u"tw_sb_sigma")
        self.tw_sb_sigma.setMaximum(240)

        self.gridLayout_12.addWidget(self.tw_sb_sigma, 0, 3, 1, 1)

        self.label_seed = QLabel(self.typewriterBox)
        self.label_seed.setObjectName(u"label_seed")

        self.gridLayout_12.addWidget(self.label_seed, 1, 2, 1, 1)

        self.tw_sb_seed = QSpinBox(self.typewriterBox)
        self.tw_sb_seed.setObjectName(u"tw_sb_seed")
        self.tw_sb_seed.setMaximum(9999)

        self.gridLayout_12.addWidget(self.tw_sb_seed, 1, 3, 1, 1)

        self.tw_sb_step = QSpinBox(self.typewriterBox)
        self.tw_sb_step.setObjectName(u"tw_sb_step")
        self.tw_sb_step.setMinimum(1)
        self.tw_sb_step.setMaximum(240)
        self.tw_sb_step.setValue(2)

        self.gridLayout_12.addWidget(self.tw_sb_step, 0, 1, 1, 1)


        self.gridLayout_9.addWidget(self.typewriterBox, 9, 0, 1, 7)

        self.letter_spacing = QSpinBox(self.scrollAreaWidgetContents)
        self.letter_spacing.setObjectName(u"letter_spacing")
        self.letter_spacing.setMinimum(-500)
        self.letter_spacing.setMaximum(500)

        self.gridLayout_9.addWidget(self.letter_spacing, 7, 2, 1, 3)

        self.edit_gradient = QToolButton(self.scrollAreaWidgetContents)
        self.edit_gradient.setObjectName(u"edit_gradient")
        icon3 = QIcon()
        iconThemeName = u"document-edit"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.edit_gradient.setIcon(icon3)

        self.gridLayout_9.addWidget(self.edit_gradient, 3, 6, 1, 1)

        self.textOutlineColor = KColorButton(self.scrollAreaWidgetContents)
        self.textOutlineColor.setObjectName(u"textOutlineColor")
        sizePolicy6.setHeightForWidth(self.textOutlineColor.sizePolicy().hasHeightForWidth())
        self.textOutlineColor.setSizePolicy(sizePolicy6)
        self.textOutlineColor.setProperty("color", QColor(0, 0, 0))

        self.gridLayout_9.addWidget(self.textOutlineColor, 4, 5, 1, 2)

        self.fontColorButton = KColorButton(self.scrollAreaWidgetContents)
        self.fontColorButton.setObjectName(u"fontColorButton")
        sizePolicy6.setHeightForWidth(self.fontColorButton.sizePolicy().hasHeightForWidth())
        self.fontColorButton.setSizePolicy(sizePolicy6)
        self.fontColorButton.setFlat(False)
        self.fontColorButton.setProperty("color", QColor(255, 255, 255))
        self.fontColorButton.setProperty("defaultColor", QColor(255, 255, 255))

        self.gridLayout_9.addWidget(self.fontColorButton, 2, 2, 1, 3)

        self.buttonItalic = QToolButton(self.scrollAreaWidgetContents)
        self.buttonItalic.setObjectName(u"buttonItalic")
        icon4 = QIcon()
        iconThemeName = u"format-text-italic"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.buttonItalic.setIcon(icon4)
        self.buttonItalic.setCheckable(True)

        self.gridLayout_9.addWidget(self.buttonItalic, 1, 6, 1, 1)

        self.label_letterSpacing = QLabel(self.scrollAreaWidgetContents)
        self.label_letterSpacing.setObjectName(u"label_letterSpacing")

        self.gridLayout_9.addWidget(self.label_letterSpacing, 7, 0, 1, 1)

        self.font_size = QSpinBox(self.scrollAreaWidgetContents)
        self.font_size.setObjectName(u"font_size")
        sizePolicy.setHeightForWidth(self.font_size.sizePolicy().hasHeightForWidth())
        self.font_size.setSizePolicy(sizePolicy)
        self.font_size.setMinimum(8)
        self.font_size.setMaximum(10000)
        self.font_size.setValue(20)

        self.gridLayout_9.addWidget(self.font_size, 1, 0, 1, 1)

        self.label_textAlign = QLabel(self.scrollAreaWidgetContents)
        self.label_textAlign.setObjectName(u"label_textAlign")

        self.gridLayout_9.addWidget(self.label_textAlign, 6, 0, 1, 1)

        self.buttonAlignRight = QToolButton(self.scrollAreaWidgetContents)
        self.buttonAlignRight.setObjectName(u"buttonAlignRight")
        icon5 = QIcon()
        iconThemeName = u"format-justify-right"
        if QIcon.hasThemeIcon(iconThemeName):
            icon5 = QIcon.fromTheme(iconThemeName)
        else:
            icon5.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.buttonAlignRight.setIcon(icon5)
        self.buttonAlignRight.setCheckable(True)
        self.buttonAlignRight.setChecked(False)
        self.buttonAlignRight.setAutoExclusive(True)

        self.gridLayout_9.addWidget(self.buttonAlignRight, 6, 4, 1, 1)

        self.buttonAlignLeft = QToolButton(self.scrollAreaWidgetContents)
        self.buttonAlignLeft.setObjectName(u"buttonAlignLeft")
        icon6 = QIcon()
        iconThemeName = u"format-justify-left"
        if QIcon.hasThemeIcon(iconThemeName):
            icon6 = QIcon.fromTheme(iconThemeName)
        else:
            icon6.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.buttonAlignLeft.setIcon(icon6)
        self.buttonAlignLeft.setCheckable(True)
        self.buttonAlignLeft.setChecked(False)
        self.buttonAlignLeft.setAutoExclusive(True)

        self.gridLayout_9.addWidget(self.buttonAlignLeft, 6, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_4, 10, 0, 1, 1)

        self.buttonUnder = QToolButton(self.scrollAreaWidgetContents)
        self.buttonUnder.setObjectName(u"buttonUnder")
        icon7 = QIcon()
        iconThemeName = u"format-text-underline"
        if QIcon.hasThemeIcon(iconThemeName):
            icon7 = QIcon.fromTheme(iconThemeName)
        else:
            icon7.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.buttonUnder.setIcon(icon7)
        self.buttonUnder.setCheckable(True)

        self.gridLayout_9.addWidget(self.buttonUnder, 1, 5, 1, 1)

        self.line_spacing = QSpinBox(self.scrollAreaWidgetContents)
        self.line_spacing.setObjectName(u"line_spacing")
        self.line_spacing.setEnabled(True)
        self.line_spacing.setMinimum(-5000)
        self.line_spacing.setMaximum(5000)

        self.gridLayout_9.addWidget(self.line_spacing, 8, 2, 1, 3)

        self.textOutline = QSpinBox(self.scrollAreaWidgetContents)
        self.textOutline.setObjectName(u"textOutline")
        self.textOutline.setMaximum(5000)

        self.gridLayout_9.addWidget(self.textOutline, 4, 2, 1, 3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_11.addWidget(self.scrollArea, 11, 0, 1, 1)

        self.toolbar_stack.addWidget(self.text)
        self.rectangle = QWidget()
        self.rectangle.setObjectName(u"rectangle")
        self.gridLayout_2 = QGridLayout(self.rectangle)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.plain_rect = QRadioButton(self.rectangle)
        self.plain_rect.setObjectName(u"plain_rect")
        self.plain_rect.setChecked(True)

        self.gridLayout_2.addWidget(self.plain_rect, 0, 0, 1, 1)

        self.rectBColor = KColorButton(self.rectangle)
        self.rectBColor.setObjectName(u"rectBColor")
        sizePolicy6.setHeightForWidth(self.rectBColor.sizePolicy().hasHeightForWidth())
        self.rectBColor.setSizePolicy(sizePolicy6)
        self.rectBColor.setProperty("color", QColor(0, 0, 0))
        self.rectBColor.setProperty("defaultColor", QColor(0, 0, 0))

        self.gridLayout_2.addWidget(self.rectBColor, 0, 1, 1, 1)

        self.gradient_rect = QRadioButton(self.rectangle)
        self.gradient_rect.setObjectName(u"gradient_rect")

        self.gridLayout_2.addWidget(self.gradient_rect, 1, 0, 1, 1)

        self.gradients_rect_combo = QComboBox(self.rectangle)
        self.gradients_rect_combo.setObjectName(u"gradients_rect_combo")
        self.gradients_rect_combo.setEnabled(False)

        self.gridLayout_2.addWidget(self.gradients_rect_combo, 1, 1, 1, 1)

        self.edit_rect_gradient = QToolButton(self.rectangle)
        self.edit_rect_gradient.setObjectName(u"edit_rect_gradient")
        self.edit_rect_gradient.setIcon(icon3)

        self.gridLayout_2.addWidget(self.edit_rect_gradient, 1, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 1, 3, 1, 1)

        self.label_border = QLabel(self.rectangle)
        self.label_border.setObjectName(u"label_border")

        self.gridLayout_2.addWidget(self.label_border, 2, 0, 1, 1)

        self.rectFColor = KColorButton(self.rectangle)
        self.rectFColor.setObjectName(u"rectFColor")
        sizePolicy6.setHeightForWidth(self.rectFColor.sizePolicy().hasHeightForWidth())
        self.rectFColor.setSizePolicy(sizePolicy6)
        self.rectFColor.setProperty("color", QColor(0, 0, 0))
        self.rectFColor.setProperty("defaultColor", QColor(0, 0, 0))

        self.gridLayout_2.addWidget(self.rectFColor, 2, 1, 1, 1)

        self.label_borderWidth = QLabel(self.rectangle)
        self.label_borderWidth.setObjectName(u"label_borderWidth")

        self.gridLayout_2.addWidget(self.label_borderWidth, 3, 0, 1, 1)

        self.rectLineWidth = QSpinBox(self.rectangle)
        self.rectLineWidth.setObjectName(u"rectLineWidth")
        self.rectLineWidth.setMaximum(5000)

        self.gridLayout_2.addWidget(self.rectLineWidth, 3, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 4, 0, 1, 1)

        self.toolbar_stack.addWidget(self.rectangle)
        self.Image = QWidget()
        self.Image.setObjectName(u"Image")
        self.gridLayout_15 = QGridLayout(self.Image)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.preserveAspectRatio = QCheckBox(self.Image)
        self.preserveAspectRatio.setObjectName(u"preserveAspectRatio")
        self.preserveAspectRatio.setEnabled(True)
        self.preserveAspectRatio.setChecked(True)

        self.gridLayout_15.addWidget(self.preserveAspectRatio, 0, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_6, 1, 0, 1, 1)

        self.toolbar_stack.addWidget(self.Image)

        self.gridLayout_10.addWidget(self.toolbar_stack, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_properties, "")
        self.tab_background = QWidget()
        self.tab_background.setObjectName(u"tab_background")
        self.gridLayout_5 = QGridLayout(self.tab_background)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.bgAlphaSlider = QSlider(self.tab_background)
        self.bgAlphaSlider.setObjectName(u"bgAlphaSlider")
        self.bgAlphaSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.bgAlphaSlider, 1, 0, 1, 1)

        self.backgroundAlpha = QSpinBox(self.tab_background)
        self.backgroundAlpha.setObjectName(u"backgroundAlpha")
        self.backgroundAlpha.setMaximum(256)

        self.gridLayout_5.addWidget(self.backgroundAlpha, 1, 1, 1, 1)

        self.backgroundColor = KColorButton(self.tab_background)
        self.backgroundColor.setObjectName(u"backgroundColor")
        sizePolicy6.setHeightForWidth(self.backgroundColor.sizePolicy().hasHeightForWidth())
        self.backgroundColor.setSizePolicy(sizePolicy6)
        self.backgroundColor.setProperty("color", QColor(0, 0, 0))
        self.backgroundColor.setProperty("defaultColor", QColor(0, 0, 0))

        self.gridLayout_5.addWidget(self.backgroundColor, 0, 0, 1, 2)

        self.tabWidget.addTab(self.tab_background, "")
        self.tab_animation = QWidget()
        self.tab_animation.setObjectName(u"tab_animation")
        self.gridLayout_6 = QGridLayout(self.tab_animation)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.anim_start = QToolButton(self.tab_animation)
        self.anim_start.setObjectName(u"anim_start")
        self.anim_start.setCheckable(True)

        self.gridLayout_6.addWidget(self.anim_start, 0, 0, 1, 1)

        self.anim_end = QToolButton(self.tab_animation)
        self.anim_end.setObjectName(u"anim_end")
        self.anim_end.setCheckable(True)

        self.gridLayout_6.addWidget(self.anim_end, 0, 1, 1, 1)

        self.align_box = QGroupBox(self.tab_animation)
        self.align_box.setObjectName(u"align_box")
        self.gridLayout_8 = QGridLayout(self.align_box)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(0)
        self.gridLayout_8.setContentsMargins(0, -1, 0, -1)
        self.label_7 = QLabel(self.align_box)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_8.addWidget(self.label_7, 1, 0, 1, 1)

        self.resize50 = QToolButton(self.align_box)
        self.resize50.setObjectName(u"resize50")

        self.gridLayout_8.addWidget(self.resize50, 2, 0, 1, 1)

        self.resize100 = QToolButton(self.align_box)
        self.resize100.setObjectName(u"resize100")

        self.gridLayout_8.addWidget(self.resize100, 2, 1, 1, 1)

        self.resize200 = QToolButton(self.align_box)
        self.resize200.setObjectName(u"resize200")

        self.gridLayout_8.addWidget(self.resize200, 2, 2, 1, 1)

        self.keep_aspect = QCheckBox(self.align_box)
        self.keep_aspect.setObjectName(u"keep_aspect")

        self.gridLayout_8.addWidget(self.keep_aspect, 0, 0, 1, 3)


        self.gridLayout_6.addWidget(self.align_box, 1, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 2, 0, 1, 2)

        self.tabWidget.addTab(self.tab_animation, "")
        self.tab_patterns = QWidget()
        self.tab_patterns.setObjectName(u"tab_patterns")
        self.verticalLayout = QVBoxLayout(self.tab_patterns)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.patternsList = QListView(self.tab_patterns)
        self.patternsList.setObjectName(u"patternsList")
        self.patternsList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.patternsList.setSpacing(4)
        self.patternsList.setViewMode(QListView.IconMode)
        self.patternsList.setUniformItemSizes(True)

        self.verticalLayout.addWidget(self.patternsList)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_add = QToolButton(self.tab_patterns)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setEnabled(False)
        icon8 = QIcon()
        iconThemeName = u"list-add"
        if QIcon.hasThemeIcon(iconThemeName):
            icon8 = QIcon.fromTheme(iconThemeName)
        else:
            icon8.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btn_add.setIcon(icon8)

        self.horizontalLayout_4.addWidget(self.btn_add)

        self.btn_remove = QToolButton(self.tab_patterns)
        self.btn_remove.setObjectName(u"btn_remove")
        self.btn_remove.setEnabled(False)
        icon9 = QIcon()
        iconThemeName = u"list-remove"
        if QIcon.hasThemeIcon(iconThemeName):
            icon9 = QIcon.fromTheme(iconThemeName)
        else:
            icon9.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btn_remove.setIcon(icon9)

        self.horizontalLayout_4.addWidget(self.btn_remove)

        self.btn_removeAll = QToolButton(self.tab_patterns)
        self.btn_removeAll.setObjectName(u"btn_removeAll")
        icon10 = QIcon()
        iconThemeName = u"edit-delete"
        if QIcon.hasThemeIcon(iconThemeName):
            icon10 = QIcon.fromTheme(iconThemeName)
        else:
            icon10.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btn_removeAll.setIcon(icon10)

        self.horizontalLayout_4.addWidget(self.btn_removeAll)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.scaleSlider = QSlider(self.tab_patterns)
        self.scaleSlider.setObjectName(u"scaleSlider")
        self.scaleSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.scaleSlider)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.tab_patterns, "")

        self.grid_settings.addWidget(self.tabWidget, 4, 0, 1, 2)

        self.align_frame = QFrame(self.verticalLayoutWidget_2)
        self.align_frame.setObjectName(u"align_frame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.align_frame.sizePolicy().hasHeightForWidth())
        self.align_frame.setSizePolicy(sizePolicy8)
        self.align_frame.setFrameShape(QFrame.NoFrame)
        self.align_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.align_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.itemleft = QToolButton(self.align_frame)
        self.itemleft.setObjectName(u"itemleft")
        icon11 = QIcon()
        iconThemeName = u"kdenlive-align-left"
        if QIcon.hasThemeIcon(iconThemeName):
            icon11 = QIcon.fromTheme(iconThemeName)
        else:
            icon11.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.itemleft.setIcon(icon11)

        self.horizontalLayout_2.addWidget(self.itemleft)

        self.itemhcenter = QToolButton(self.align_frame)
        self.itemhcenter.setObjectName(u"itemhcenter")
        icon12 = QIcon()
        iconThemeName = u"kdenlive-align-hor"
        if QIcon.hasThemeIcon(iconThemeName):
            icon12 = QIcon.fromTheme(iconThemeName)
        else:
            icon12.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.itemhcenter.setIcon(icon12)

        self.horizontalLayout_2.addWidget(self.itemhcenter)

        self.itemright = QToolButton(self.align_frame)
        self.itemright.setObjectName(u"itemright")
        icon13 = QIcon()
        iconThemeName = u"kdenlive-align-right"
        if QIcon.hasThemeIcon(iconThemeName):
            icon13 = QIcon.fromTheme(iconThemeName)
        else:
            icon13.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.itemright.setIcon(icon13)

        self.horizontalLayout_2.addWidget(self.itemright)

        self.itemtop = QToolButton(self.align_frame)
        self.itemtop.setObjectName(u"itemtop")
        icon14 = QIcon()
        iconThemeName = u"kdenlive-align-top"
        if QIcon.hasThemeIcon(iconThemeName):
            icon14 = QIcon.fromTheme(iconThemeName)
        else:
            icon14.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.itemtop.setIcon(icon14)

        self.horizontalLayout_2.addWidget(self.itemtop)

        self.itemvcenter = QToolButton(self.align_frame)
        self.itemvcenter.setObjectName(u"itemvcenter")
        icon15 = QIcon()
        iconThemeName = u"kdenlive-align-vert"
        if QIcon.hasThemeIcon(iconThemeName):
            icon15 = QIcon.fromTheme(iconThemeName)
        else:
            icon15.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.itemvcenter.setIcon(icon15)

        self.horizontalLayout_2.addWidget(self.itemvcenter)

        self.itembottom = QToolButton(self.align_frame)
        self.itembottom.setObjectName(u"itembottom")
        icon16 = QIcon()
        iconThemeName = u"kdenlive-align-bottom"
        if QIcon.hasThemeIcon(iconThemeName):
            icon16 = QIcon.fromTheme(iconThemeName)
        else:
            icon16.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.itembottom.setIcon(icon16)

        self.horizontalLayout_2.addWidget(self.itembottom)

        self.horizontalSpacer = QSpacerItem(150, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.grid_settings.addWidget(self.align_frame, 3, 0, 1, 2)

        self.duration_box = QHBoxLayout()
        self.duration_box.setObjectName(u"duration_box")

        self.grid_settings.addLayout(self.duration_box, 0, 1, 1, 1)

        self.splitter.addWidget(self.verticalLayoutWidget_2)

        self.gridLayout_7.addWidget(self.splitter, 8, 0, 1, 9)

        self.frame_toolbar = QFrame(TitleWidget_UI)
        self.frame_toolbar.setObjectName(u"frame_toolbar")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.frame_toolbar.sizePolicy().hasHeightForWidth())
        self.frame_toolbar.setSizePolicy(sizePolicy9)
        self.frame_toolbar.setFrameShape(QFrame.StyledPanel)
        self.frame_toolbar.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.frame_toolbar, 0, 0, 1, 1)

        QWidget.setTabOrder(self.origin_x_left, self.value_x)
        QWidget.setTabOrder(self.value_x, self.origin_y_top)
        QWidget.setTabOrder(self.origin_y_top, self.value_y)
        QWidget.setTabOrder(self.value_y, self.value_w)
        QWidget.setTabOrder(self.value_w, self.value_h)
        QWidget.setTabOrder(self.value_h, self.zUp)
        QWidget.setTabOrder(self.zUp, self.zDown)
        QWidget.setTabOrder(self.zDown, self.zTop)
        QWidget.setTabOrder(self.zTop, self.zBottom)
        QWidget.setTabOrder(self.zBottom, self.zValue)
        QWidget.setTabOrder(self.zValue, self.buttonSelectImages)
        QWidget.setTabOrder(self.buttonSelectImages, self.buttonSelectText)
        QWidget.setTabOrder(self.buttonSelectText, self.buttonUnselectAll)
        QWidget.setTabOrder(self.buttonUnselectAll, self.buttonSelectAll)
        QWidget.setTabOrder(self.buttonSelectAll, self.buttonSelectRects)
        QWidget.setTabOrder(self.buttonSelectRects, self.use_grid)
        QWidget.setTabOrder(self.use_grid, self.show_guides)
        QWidget.setTabOrder(self.show_guides, self.vguides)
        QWidget.setTabOrder(self.vguides, self.hguides)
        QWidget.setTabOrder(self.hguides, self.guideColor)
        QWidget.setTabOrder(self.guideColor, self.buttonFitZoom)
        QWidget.setTabOrder(self.buttonFitZoom, self.buttonRealSize)
        QWidget.setTabOrder(self.buttonRealSize, self.zoom_slider)
        QWidget.setTabOrder(self.zoom_slider, self.zoom_spin)
        QWidget.setTabOrder(self.zoom_spin, self.displayBg)
        QWidget.setTabOrder(self.displayBg, self.bgBox)
        QWidget.setTabOrder(self.bgBox, self.templateBox)
        QWidget.setTabOrder(self.templateBox, self.createButton)
        QWidget.setTabOrder(self.createButton, self.cancelButton)
        QWidget.setTabOrder(self.cancelButton, self.itemrotatex)
        QWidget.setTabOrder(self.itemrotatex, self.itemrotatey)
        QWidget.setTabOrder(self.itemrotatey, self.itemrotatez)
        QWidget.setTabOrder(self.itemrotatez, self.rectBColor)
        QWidget.setTabOrder(self.rectBColor, self.gradient_rect)
        QWidget.setTabOrder(self.gradient_rect, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.font_size)
        QWidget.setTabOrder(self.font_size, self.font_weight_box)
        QWidget.setTabOrder(self.font_weight_box, self.buttonUnder)
        QWidget.setTabOrder(self.buttonUnder, self.buttonItalic)
        QWidget.setTabOrder(self.buttonItalic, self.plain_color)
        QWidget.setTabOrder(self.plain_color, self.fontColorButton)
        QWidget.setTabOrder(self.fontColorButton, self.buttonInsertUnicode)
        QWidget.setTabOrder(self.buttonInsertUnicode, self.gradient_color)
        QWidget.setTabOrder(self.gradient_color, self.gradients_combo)
        QWidget.setTabOrder(self.gradients_combo, self.edit_gradient)
        QWidget.setTabOrder(self.edit_gradient, self.textOutline)
        QWidget.setTabOrder(self.textOutline, self.textOutlineColor)
        QWidget.setTabOrder(self.textOutlineColor, self.shadowBox)
        QWidget.setTabOrder(self.shadowBox, self.blur_radius)
        QWidget.setTabOrder(self.blur_radius, self.shadowColor)
        QWidget.setTabOrder(self.shadowColor, self.shadowX)
        QWidget.setTabOrder(self.shadowX, self.shadowY)
        QWidget.setTabOrder(self.shadowY, self.buttonAlignLeft)
        QWidget.setTabOrder(self.buttonAlignLeft, self.buttonAlignCenter)
        QWidget.setTabOrder(self.buttonAlignCenter, self.buttonAlignRight)
        QWidget.setTabOrder(self.buttonAlignRight, self.letter_spacing)
        QWidget.setTabOrder(self.letter_spacing, self.line_spacing)
        QWidget.setTabOrder(self.line_spacing, self.backgroundColor)
        QWidget.setTabOrder(self.backgroundColor, self.bgAlphaSlider)
        QWidget.setTabOrder(self.bgAlphaSlider, self.backgroundAlpha)
        QWidget.setTabOrder(self.backgroundAlpha, self.anim_start)
        QWidget.setTabOrder(self.anim_start, self.anim_end)
        QWidget.setTabOrder(self.anim_end, self.keep_aspect)
        QWidget.setTabOrder(self.keep_aspect, self.resize50)
        QWidget.setTabOrder(self.resize50, self.resize100)
        QWidget.setTabOrder(self.resize100, self.resize200)
        QWidget.setTabOrder(self.resize200, self.patternsList)
        QWidget.setTabOrder(self.patternsList, self.btn_add)
        QWidget.setTabOrder(self.btn_add, self.btn_remove)
        QWidget.setTabOrder(self.btn_remove, self.btn_removeAll)
        QWidget.setTabOrder(self.btn_removeAll, self.scaleSlider)
        QWidget.setTabOrder(self.scaleSlider, self.rectFColor)
        QWidget.setTabOrder(self.rectFColor, self.font_family)
        QWidget.setTabOrder(self.font_family, self.gradients_rect_combo)
        QWidget.setTabOrder(self.gradients_rect_combo, self.preserveAspectRatio)
        QWidget.setTabOrder(self.preserveAspectRatio, self.edit_rect_gradient)
        QWidget.setTabOrder(self.edit_rect_gradient, self.rectLineWidth)
        QWidget.setTabOrder(self.rectLineWidth, self.plain_rect)

        self.retranslateUi(TitleWidget_UI)
        self.show_guides.toggled.connect(self.hguides.setEnabled)
        self.show_guides.toggled.connect(self.vguides.setEnabled)
        self.show_guides.toggled.connect(self.guideColor.setEnabled)
        self.plain_color.toggled.connect(self.fontColorButton.setEnabled)
        self.gradient_color.toggled.connect(self.gradients_combo.setEnabled)
        self.gradient_rect.toggled.connect(self.gradients_rect_combo.setEnabled)
        self.bgAlphaSlider.valueChanged.connect(self.backgroundAlpha.setValue)
        self.plain_rect.toggled.connect(self.rectBColor.setEnabled)
        self.backgroundAlpha.valueChanged.connect(self.bgAlphaSlider.setValue)

        self.tabWidget.setCurrentIndex(0)
        self.toolbar_stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TitleWidget_UI)
    # setupUi

    def retranslateUi(self, TitleWidget_UI):
        TitleWidget_UI.setWindowTitle(QCoreApplication.translate("TitleWidget_UI", u"Title Clip", None))
        self.buttonFitZoom.setText(QCoreApplication.translate("TitleWidget_UI", u"V", None))
        self.buttonRealSize.setText(QCoreApplication.translate("TitleWidget_UI", u"V", None))
        self.zoom_spin.setSuffix(QCoreApplication.translate("TitleWidget_UI", u"%", None))
        self.displayBg.setText(QCoreApplication.translate("TitleWidget_UI", u"Show background", None))
        self.bgBox.setItemText(0, QCoreApplication.translate("TitleWidget_UI", u"Checkered", None))
        self.bgBox.setItemText(1, QCoreApplication.translate("TitleWidget_UI", u"Black", None))
        self.bgBox.setItemText(2, QCoreApplication.translate("TitleWidget_UI", u"White", None))

        self.label_template.setText(QCoreApplication.translate("TitleWidget_UI", u"Template:", None))
        self.createButton.setText(QCoreApplication.translate("TitleWidget_UI", u"Create", None))
        self.cancelButton.setText(QCoreApplication.translate("TitleWidget_UI", u"Cancel", None))
        self.zDown.setText("")
        self.origin_x_left.setText(QCoreApplication.translate("TitleWidget_UI", u"+X", None))
        self.label_zIndex.setText(QCoreApplication.translate("TitleWidget_UI", u"Z-Index:", None))
        self.origin_y_top.setText(QCoreApplication.translate("TitleWidget_UI", u"+Y", None))
        self.label_height.setText(QCoreApplication.translate("TitleWidget_UI", u"H:", None))
        self.zTop.setText("")
        self.zUp.setText("")
        self.zBottom.setText("")
        self.label_width.setText(QCoreApplication.translate("TitleWidget_UI", u"W:", None))
        self.use_grid.setText(QCoreApplication.translate("TitleWidget_UI", u"Use grid", None))
        self.buttonSelectRects.setText(QCoreApplication.translate("TitleWidget_UI", u"R", None))
        self.buttonSelectImages.setText(QCoreApplication.translate("TitleWidget_UI", u"I", None))
        self.buttonSelectText.setText(QCoreApplication.translate("TitleWidget_UI", u"T", None))
#if QT_CONFIG(tooltip)
        self.hguides.setToolTip(QCoreApplication.translate("TitleWidget_UI", u"Horizontal guides.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vguides.setToolTip(QCoreApplication.translate("TitleWidget_UI", u"Vertical guides.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonUnselectAll.setText(QCoreApplication.translate("TitleWidget_UI", u"N", None))
        self.show_guides.setText(QCoreApplication.translate("TitleWidget_UI", u"Show guides:", None))
#if QT_CONFIG(whatsthis)
        self.buttonSelectAll.setWhatsThis(QCoreApplication.translate("TitleWidget_UI", u"Selects all items on the canvas.", None))
#endif // QT_CONFIG(whatsthis)
        self.buttonSelectAll.setText(QCoreApplication.translate("TitleWidget_UI", u"A", None))
        self.label_rotate.setText(QCoreApplication.translate("TitleWidget_UI", u"Rotate", None))
        self.label_rotateX.setText(QCoreApplication.translate("TitleWidget_UI", u"X:", None))
        self.label_rotateY.setText(QCoreApplication.translate("TitleWidget_UI", u"Y:", None))
        self.label_rotateZ.setText(QCoreApplication.translate("TitleWidget_UI", u"Z:", None))
        self.label_duration.setText(QCoreApplication.translate("TitleWidget_UI", u"Duration:", None))
        self.label_itemzoom.setText(QCoreApplication.translate("TitleWidget_UI", u"Zoom:", None))
        self.shadowBox.setTitle(QCoreApplication.translate("TitleWidget_UI", u"Sha&dow", None))
        self.label_blur.setText(QCoreApplication.translate("TitleWidget_UI", u"Blur:", None))
        self.label_offset.setText(QCoreApplication.translate("TitleWidget_UI", u"Offset:", None))
        self.buttonInsertUnicode.setText(QCoreApplication.translate("TitleWidget_UI", u"...", None))
#if QT_CONFIG(tooltip)
        self.buttonAlignCenter.setToolTip(QCoreApplication.translate("TitleWidget_UI", u"Align center.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonAlignCenter.setText(QCoreApplication.translate("TitleWidget_UI", u"...", None))
        self.label_lineSpacing.setText(QCoreApplication.translate("TitleWidget_UI", u"Line spacing:", None))
        self.gradient_color.setText(QCoreApplication.translate("TitleWidget_UI", u"&Gradient:", None))
        self.plain_color.setText(QCoreApplication.translate("TitleWidget_UI", u"So&lid color:", None))
        self.label_outline.setText(QCoreApplication.translate("TitleWidget_UI", u"Outline:", None))
        self.typewriterBox.setTitle(QCoreApplication.translate("TitleWidget_UI", u"&Typewriter effect", None))
        self.label_variation.setText(QCoreApplication.translate("TitleWidget_UI", u"Variation:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TitleWidget_UI", u"Expansion Mode", None))
        self.tw_rd_char.setText(QCoreApplication.translate("TitleWidget_UI", u"By &char", None))
        self.tw_rd_word.setText(QCoreApplication.translate("TitleWidget_UI", u"By &word", None))
        self.tw_rd_line.setText(QCoreApplication.translate("TitleWidget_UI", u"By &line", None))
        self.tw_rd_custom.setText(QCoreApplication.translate("TitleWidget_UI", u"Custo&m", None))
        self.label_frameStep.setText(QCoreApplication.translate("TitleWidget_UI", u"Frame step:", None))
        self.label_seed.setText(QCoreApplication.translate("TitleWidget_UI", u"Seed:", None))
        self.edit_gradient.setText(QCoreApplication.translate("TitleWidget_UI", u"...", None))
        self.buttonItalic.setText(QCoreApplication.translate("TitleWidget_UI", u"...", None))
        self.label_letterSpacing.setText(QCoreApplication.translate("TitleWidget_UI", u"Letter spacing:", None))
        self.label_textAlign.setText(QCoreApplication.translate("TitleWidget_UI", u"Align:", None))
#if QT_CONFIG(tooltip)
        self.buttonAlignRight.setToolTip(QCoreApplication.translate("TitleWidget_UI", u"Align right.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonAlignRight.setText(QCoreApplication.translate("TitleWidget_UI", u"...", None))
#if QT_CONFIG(tooltip)
        self.buttonAlignLeft.setToolTip(QCoreApplication.translate("TitleWidget_UI", u"Align left.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonAlignLeft.setText(QCoreApplication.translate("TitleWidget_UI", u"...", None))
        self.buttonUnder.setText(QCoreApplication.translate("TitleWidget_UI", u"...", None))
        self.plain_rect.setText(QCoreApplication.translate("TitleWidget_UI", u"So&lid color:", None))
        self.gradient_rect.setText(QCoreApplication.translate("TitleWidget_UI", u"&Gradient:", None))
        self.edit_rect_gradient.setText(QCoreApplication.translate("TitleWidget_UI", u"...", None))
        self.label_border.setText(QCoreApplication.translate("TitleWidget_UI", u"Border ", None))
        self.label_borderWidth.setText(QCoreApplication.translate("TitleWidget_UI", u"Border width", None))
        self.preserveAspectRatio.setText(QCoreApplication.translate("TitleWidget_UI", u"Preserve aspect ratio", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_properties), QCoreApplication.translate("TitleWidget_UI", u"Properties", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_background), QCoreApplication.translate("TitleWidget_UI", u"Background", None))
        self.anim_start.setText(QCoreApplication.translate("TitleWidget_UI", u"Edit start viewport", None))
        self.anim_end.setText(QCoreApplication.translate("TitleWidget_UI", u"Edit end viewport", None))
        self.align_box.setTitle("")
        self.label_7.setText(QCoreApplication.translate("TitleWidget_UI", u"Resize", None))
        self.resize50.setText(QCoreApplication.translate("TitleWidget_UI", u"50%", None))
        self.resize100.setText(QCoreApplication.translate("TitleWidget_UI", u"100%", None))
        self.resize200.setText(QCoreApplication.translate("TitleWidget_UI", u"200%", None))
        self.keep_aspect.setText(QCoreApplication.translate("TitleWidget_UI", u"Keep aspect ratio", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_animation), QCoreApplication.translate("TitleWidget_UI", u"Animation", None))
#if QT_CONFIG(tooltip)
        self.btn_add.setToolTip(QCoreApplication.translate("TitleWidget_UI", u"Add pattern.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_add.setText(QCoreApplication.translate("TitleWidget_UI", u"...", None))
#if QT_CONFIG(tooltip)
        self.btn_remove.setToolTip(QCoreApplication.translate("TitleWidget_UI", u"Delete pattern.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_remove.setText(QCoreApplication.translate("TitleWidget_UI", u"...", None))
#if QT_CONFIG(tooltip)
        self.btn_removeAll.setToolTip(QCoreApplication.translate("TitleWidget_UI", u"Delete all patterns.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_removeAll.setText(QCoreApplication.translate("TitleWidget_UI", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_patterns), QCoreApplication.translate("TitleWidget_UI", u"Patterns", None))
#if QT_CONFIG(tooltip)
        self.itemleft.setToolTip(QCoreApplication.translate("TitleWidget_UI", u"Align item to left.", None))
#endif // QT_CONFIG(tooltip)
        self.itemleft.setText(QCoreApplication.translate("TitleWidget_UI", u"...", None))
#if QT_CONFIG(tooltip)
        self.itemhcenter.setToolTip(QCoreApplication.translate("TitleWidget_UI", u"Align item horizontally.", None))
#endif // QT_CONFIG(tooltip)
        self.itemhcenter.setText(QCoreApplication.translate("TitleWidget_UI", u"...", None))
#if QT_CONFIG(tooltip)
        self.itemright.setToolTip(QCoreApplication.translate("TitleWidget_UI", u"Align item to right.", None))
#endif // QT_CONFIG(tooltip)
        self.itemright.setText(QCoreApplication.translate("TitleWidget_UI", u"...", None))
#if QT_CONFIG(tooltip)
        self.itemtop.setToolTip(QCoreApplication.translate("TitleWidget_UI", u"Align item to top.", None))
#endif // QT_CONFIG(tooltip)
        self.itemtop.setText(QCoreApplication.translate("TitleWidget_UI", u"...", None))
#if QT_CONFIG(tooltip)
        self.itemvcenter.setToolTip(QCoreApplication.translate("TitleWidget_UI", u"Align item vertically.", None))
#endif // QT_CONFIG(tooltip)
        self.itemvcenter.setText(QCoreApplication.translate("TitleWidget_UI", u"...", None))
#if QT_CONFIG(tooltip)
        self.itembottom.setToolTip(QCoreApplication.translate("TitleWidget_UI", u"Align item to bottom.", None))
#endif // QT_CONFIG(tooltip)
        self.itembottom.setText(QCoreApplication.translate("TitleWidget_UI", u"...", None))
    # retranslateUi

