# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wind.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGraphicsView, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QStatusBar, QTabWidget, QTableView, QTableWidget,
    QTableWidgetItem, QToolButton, QTreeView, QUndoView,
    QVBoxLayout, QWidget)
import isu_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1120, 760)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1120, 700))
        MainWindow.setMaximumSize(QSize(16777203, 16777210))
        font = QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(Qt.NoFocus)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(True)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.actionStep = QAction(MainWindow)
        self.actionStep.setObjectName(u"actionStep")
        self.actionOpen_Demo = QAction(MainWindow)
        self.actionOpen_Demo.setObjectName(u"actionOpen_Demo")
        self.actionOpen_Audio = QAction(MainWindow)
        self.actionOpen_Audio.setObjectName(u"actionOpen_Audio")
        self.actionOpen_Script = QAction(MainWindow)
        self.actionOpen_Script.setObjectName(u"actionOpen_Script")
        self.actionSave_Jobs = QAction(MainWindow)
        self.actionSave_Jobs.setObjectName(u"actionSave_Jobs")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionQueue = QAction(MainWindow)
        self.actionQueue.setObjectName(u"actionQueue")
        self.actionJobs_Editor = QAction(MainWindow)
        self.actionJobs_Editor.setObjectName(u"actionJobs_Editor")
        self.actionJobs_Editor.setCheckable(True)
        self.actionJobs_Editor.setChecked(True)
        self.actionXML_Editor = QAction(MainWindow)
        self.actionXML_Editor.setObjectName(u"actionXML_Editor")
        self.actionXML_Editor.setCheckable(True)
        self.actionScript_Editor = QAction(MainWindow)
        self.actionScript_Editor.setObjectName(u"actionScript_Editor")
        self.actionScript_Editor.setCheckable(True)
        self.actionFull_Screen = QAction(MainWindow)
        self.actionFull_Screen.setObjectName(u"actionFull_Screen")
        self.actionFull_Screen.setCheckable(True)
        self.actionRun = QAction(MainWindow)
        self.actionRun.setObjectName(u"actionRun")
        self.actionClear_jobs = QAction(MainWindow)
        self.actionClear_jobs.setObjectName(u"actionClear_jobs")
        self.actionDelete_current_task = QAction(MainWindow)
        self.actionDelete_current_task.setObjectName(u"actionDelete_current_task")
        self.actionDuplicate_current_task = QAction(MainWindow)
        self.actionDuplicate_current_task.setObjectName(u"actionDuplicate_current_task")
        self.actionReset_current_task = QAction(MainWindow)
        self.actionReset_current_task.setObjectName(u"actionReset_current_task")
        self.actionMenubar = QAction(MainWindow)
        self.actionMenubar.setObjectName(u"actionMenubar")
        self.actionMenubar.setCheckable(True)
        self.actionMenubar.setChecked(True)
        self.actionStatusbar = QAction(MainWindow)
        self.actionStatusbar.setObjectName(u"actionStatusbar")
        self.actionStatusbar.setCheckable(True)
        self.actionRun_current_task = QAction(MainWindow)
        self.actionRun_current_task.setObjectName(u"actionRun_current_task")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(True)
        self.verticalLayout_31 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.centralTabs = QStackedWidget(self.centralwidget)
        self.centralTabs.setObjectName(u"centralTabs")
        self.centralTabs.setMouseTracking(True)
        self.centralTabs.setAcceptDrops(True)
        self.centralTabs.setLineWidth(0)
        self.jobsPage = QWidget()
        self.jobsPage.setObjectName(u"jobsPage")
        self.jobsPage.setMouseTracking(True)
        self.jobsPage.setAcceptDrops(True)
        self.jobsPage.setAutoFillBackground(True)
        self.horizontalLayout_3 = QHBoxLayout(self.jobsPage)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 2, 3, 2)
        self.dataLayout = QVBoxLayout()
        self.dataLayout.setSpacing(4)
        self.dataLayout.setObjectName(u"dataLayout")
        self.dataLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.jobsPage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setMaximumSize(QSize(350, 16777215))
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tab_6.setMaximumSize(QSize(16777214, 16777215))
        self.verticalLayout_34 = QVBoxLayout(self.tab_6)
        self.verticalLayout_34.setSpacing(4)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label = QLabel(self.tab_6)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setKerning(True)
        self.label.setFont(font1)
        self.label.setIndent(8)

        self.horizontalLayout_23.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_2)

        self.comboBox_2 = QComboBox(self.tab_6)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_23.addWidget(self.comboBox_2)

        self.browseButton = QPushButton(self.tab_6)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setKerning(True)
        self.browseButton.setFont(font2)
        self.browseButton.setAutoDefault(True)

        self.horizontalLayout_23.addWidget(self.browseButton)


        self.verticalLayout_34.addLayout(self.horizontalLayout_23)

        self.tableWidget_2 = QTableWidget(self.tab_6)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_34.addWidget(self.tableWidget_2)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.browseDemoBtn = QPushButton(self.tab_6)
        self.browseDemoBtn.setObjectName(u"browseDemoBtn")
        self.browseDemoBtn.setAutoDefault(False)
        self.browseDemoBtn.setFlat(False)

        self.horizontalLayout_19.addWidget(self.browseDemoBtn)

        self.browseAudioBtn = QPushButton(self.tab_6)
        self.browseAudioBtn.setObjectName(u"browseAudioBtn")

        self.horizontalLayout_19.addWidget(self.browseAudioBtn)

        self.browseScriptBtn = QPushButton(self.tab_6)
        self.browseScriptBtn.setObjectName(u"browseScriptBtn")

        self.horizontalLayout_19.addWidget(self.browseScriptBtn)

        self.toolButton_12 = QToolButton(self.tab_6)
        self.toolButton_12.setObjectName(u"toolButton_12")

        self.horizontalLayout_19.addWidget(self.toolButton_12)


        self.verticalLayout_34.addLayout(self.horizontalLayout_19)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.verticalLayout_36 = QVBoxLayout(self.tab_10)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_7 = QLabel(self.tab_10)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_30.addWidget(self.label_7)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_7)

        self.pushButton_54 = QPushButton(self.tab_10)
        self.pushButton_54.setObjectName(u"pushButton_54")

        self.horizontalLayout_30.addWidget(self.pushButton_54)


        self.verticalLayout_36.addLayout(self.horizontalLayout_30)

        self.tableWidget_3 = QTableWidget(self.tab_10)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.verticalLayout_36.addWidget(self.tableWidget_3)

        self.widget_7 = QWidget(self.tab_10)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_29 = QVBoxLayout(self.widget_7)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.pushButton_49 = QPushButton(self.widget_7)
        self.pushButton_49.setObjectName(u"pushButton_49")

        self.horizontalLayout_21.addWidget(self.pushButton_49)

        self.pushButton_50 = QPushButton(self.widget_7)
        self.pushButton_50.setObjectName(u"pushButton_50")

        self.horizontalLayout_21.addWidget(self.pushButton_50)

        self.pushButton_51 = QPushButton(self.widget_7)
        self.pushButton_51.setObjectName(u"pushButton_51")

        self.horizontalLayout_21.addWidget(self.pushButton_51)

        self.pushButton_52 = QPushButton(self.widget_7)
        self.pushButton_52.setObjectName(u"pushButton_52")

        self.horizontalLayout_21.addWidget(self.pushButton_52)

        self.toolButton_13 = QToolButton(self.widget_7)
        self.toolButton_13.setObjectName(u"toolButton_13")

        self.horizontalLayout_21.addWidget(self.toolButton_13)


        self.verticalLayout_29.addLayout(self.horizontalLayout_21)


        self.verticalLayout_36.addWidget(self.widget_7)

        self.tabWidget.addTab(self.tab_10, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.verticalLayout_21 = QVBoxLayout(self.tab_13)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget_6 = QWidget(self.tab_13)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_24 = QVBoxLayout(self.widget_6)
        self.verticalLayout_24.setSpacing(4)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_25.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_3)

        self.toolButton_15 = QToolButton(self.widget_6)
        self.toolButton_15.setObjectName(u"toolButton_15")

        self.horizontalLayout_25.addWidget(self.toolButton_15)


        self.verticalLayout_24.addLayout(self.horizontalLayout_25)

        self.tableView = QTableView(self.widget_6)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_24.addWidget(self.tableView)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")

        self.verticalLayout_24.addLayout(self.horizontalLayout_26)


        self.verticalLayout_21.addWidget(self.widget_6)

        self.tabWidget.addTab(self.tab_13, "")

        self.dataLayout.addWidget(self.tabWidget)

        self.tabWidget_3 = QTabWidget(self.jobsPage)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget_3.sizePolicy().hasHeightForWidth())
        self.tabWidget_3.setSizePolicy(sizePolicy1)
        self.tabWidget_3.setMinimumSize(QSize(325, 0))
        self.tabWidget_3.setMaximumSize(QSize(375, 16777215))
        self.tabWidget_3.setCursor(QCursor(Qt.ArrowCursor))
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.verticalLayout_30 = QVBoxLayout(self.tab_11)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_11 = QLabel(self.tab_11)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setIndent(8)

        self.horizontalLayout_35.addWidget(self.label_11)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_11)

        self.comboBox_3 = QComboBox(self.tab_11)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_35.addWidget(self.comboBox_3)

        self.addStepButton = QPushButton(self.tab_11)
        self.addStepButton.setObjectName(u"addStepButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.addStepButton.sizePolicy().hasHeightForWidth())
        self.addStepButton.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setKerning(False)
        self.addStepButton.setFont(font3)
        self.addStepButton.setCursor(QCursor(Qt.ArrowCursor))
        self.addStepButton.setContextMenuPolicy(Qt.PreventContextMenu)
        self.addStepButton.setAcceptDrops(False)
        self.addStepButton.setAutoFillBackground(False)
        self.addStepButton.setIconSize(QSize(16, 16))
        self.addStepButton.setAutoDefault(True)
        self.addStepButton.setFlat(False)

        self.horizontalLayout_35.addWidget(self.addStepButton)


        self.verticalLayout_30.addLayout(self.horizontalLayout_35)

        self.stepsList = QTableWidget(self.tab_11)
        if (self.stepsList.columnCount() < 3):
            self.stepsList.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.stepsList.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.stepsList.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.stepsList.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.stepsList.setObjectName(u"stepsList")
        self.stepsList.setFrameShape(QFrame.StyledPanel)
        self.stepsList.setFrameShadow(QFrame.Sunken)
        self.stepsList.setLineWidth(0)
        self.stepsList.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.stepsList.setTabKeyNavigation(True)
        self.stepsList.setDragEnabled(True)
        self.stepsList.setDragDropOverwriteMode(False)
        self.stepsList.setDragDropMode(QAbstractItemView.DragDrop)
        self.stepsList.setDefaultDropAction(Qt.MoveAction)
        self.stepsList.setAlternatingRowColors(True)
        self.stepsList.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_30.addWidget(self.stepsList)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_5 = QPushButton(self.tab_11)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_5.addWidget(self.pushButton_5)

        self.pushButton_7 = QPushButton(self.tab_11)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_5.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.tab_11)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_5.addWidget(self.pushButton_6)

        self.runButton = QPushButton(self.tab_11)
        self.runButton.setObjectName(u"runButton")
        self.runButton.setAutoFillBackground(False)
        self.runButton.setAutoDefault(True)

        self.horizontalLayout_5.addWidget(self.runButton)

        self.toolButton_2 = QToolButton(self.tab_11)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.horizontalLayout_5.addWidget(self.toolButton_2)


        self.verticalLayout_30.addLayout(self.horizontalLayout_5)

        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.verticalLayout_37 = QVBoxLayout(self.tab_12)
        self.verticalLayout_37.setSpacing(5)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_8 = QLabel(self.tab_12)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_31.addWidget(self.label_8)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_8)

        self.comboBox_4 = QComboBox(self.tab_12)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_31.addWidget(self.comboBox_4)

        self.pushButton_55 = QPushButton(self.tab_12)
        self.pushButton_55.setObjectName(u"pushButton_55")

        self.horizontalLayout_31.addWidget(self.pushButton_55)


        self.verticalLayout_37.addLayout(self.horizontalLayout_31)

        self.tableView_2 = QTableView(self.tab_12)
        self.tableView_2.setObjectName(u"tableView_2")

        self.verticalLayout_37.addWidget(self.tableView_2)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton_45 = QPushButton(self.tab_12)
        self.pushButton_45.setObjectName(u"pushButton_45")

        self.horizontalLayout_20.addWidget(self.pushButton_45)

        self.pushButton_46 = QPushButton(self.tab_12)
        self.pushButton_46.setObjectName(u"pushButton_46")

        self.horizontalLayout_20.addWidget(self.pushButton_46)

        self.pushButton_48 = QPushButton(self.tab_12)
        self.pushButton_48.setObjectName(u"pushButton_48")

        self.horizontalLayout_20.addWidget(self.pushButton_48)

        self.pushButton_47 = QPushButton(self.tab_12)
        self.pushButton_47.setObjectName(u"pushButton_47")

        self.horizontalLayout_20.addWidget(self.pushButton_47)

        self.toolButton_14 = QToolButton(self.tab_12)
        self.toolButton_14.setObjectName(u"toolButton_14")

        self.horizontalLayout_20.addWidget(self.toolButton_14)


        self.verticalLayout_37.addLayout(self.horizontalLayout_20)

        self.tabWidget_3.addTab(self.tab_12, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.tab_14.setMaximumSize(QSize(16777213, 16777215))
        self.tab_14.setFont(font2)
        self.verticalLayout_22 = QVBoxLayout(self.tab_14)
        self.verticalLayout_22.setSpacing(4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_4 = QLabel(self.tab_14)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_24.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_4)

        self.toolButton_16 = QToolButton(self.tab_14)
        self.toolButton_16.setObjectName(u"toolButton_16")

        self.horizontalLayout_24.addWidget(self.toolButton_16)


        self.verticalLayout_22.addLayout(self.horizontalLayout_24)

        self.undoView = QUndoView(self.tab_14)
        self.undoView.setObjectName(u"undoView")

        self.verticalLayout_22.addWidget(self.undoView)

        self.tabWidget_3.addTab(self.tab_14, "")

        self.dataLayout.addWidget(self.tabWidget_3)


        self.horizontalLayout_3.addLayout(self.dataLayout)

        self.opsLayout = QWidget(self.jobsPage)
        self.opsLayout.setObjectName(u"opsLayout")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.opsLayout.sizePolicy().hasHeightForWidth())
        self.opsLayout.setSizePolicy(sizePolicy3)
        self.opsLayout.setMaximumSize(QSize(16777215, 16777212))
        self.opsLayout.setFocusPolicy(Qt.NoFocus)
        self.opsLayout.setLayoutDirection(Qt.LeftToRight)
        self.opsLayout.setAutoFillBackground(False)
        self.verticalLayout_20 = QVBoxLayout(self.opsLayout)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.stepTabs = QTabWidget(self.opsLayout)
        self.stepTabs.setObjectName(u"stepTabs")
        self.stepTabs.setEnabled(True)
        self.stepTabs.setMinimumSize(QSize(350, 0))
        self.stepTabs.setContextMenuPolicy(Qt.CustomContextMenu)
        self.stepTabs.setElideMode(Qt.ElideMiddle)
        self.stepTabs.setDocumentMode(False)
        self.stepTabs.setTabsClosable(True)
        self.stepTabs.setMovable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_14 = QVBoxLayout(self.tab)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalGroupBox_6 = QGroupBox(self.tab)
        self.verticalGroupBox_6.setObjectName(u"verticalGroupBox_6")
        self.verticalGroupBox_6.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.verticalLayout_11 = QVBoxLayout(self.verticalGroupBox_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_17 = QLabel(self.verticalGroupBox_6)
        self.label_17.setObjectName(u"label_17")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy4)

        self.horizontalLayout_11.addWidget(self.label_17)

        self.horizontalSpacer_15 = QSpacerItem(463, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)

        self.label_18 = QLabel(self.verticalGroupBox_6)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_11.addWidget(self.label_18)

        self.comboBox_8 = QComboBox(self.verticalGroupBox_6)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.horizontalLayout_11.addWidget(self.comboBox_8)

        self.toolButton_7 = QToolButton(self.verticalGroupBox_6)
        self.toolButton_7.setObjectName(u"toolButton_7")

        self.horizontalLayout_11.addWidget(self.toolButton_7)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.targetLayout_4 = QHBoxLayout()
        self.targetLayout_4.setObjectName(u"targetLayout_4")
        self.label_21 = QLabel(self.verticalGroupBox_6)
        self.label_21.setObjectName(u"label_21")

        self.targetLayout_4.addWidget(self.label_21)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.targetLayout_4.addItem(self.horizontalSpacer_18)

        self.label_22 = QLabel(self.verticalGroupBox_6)
        self.label_22.setObjectName(u"label_22")

        self.targetLayout_4.addWidget(self.label_22)

        self.spinBox = QSpinBox(self.verticalGroupBox_6)
        self.spinBox.setObjectName(u"spinBox")

        self.targetLayout_4.addWidget(self.spinBox)


        self.verticalLayout_11.addLayout(self.targetLayout_4)

        self.targetLayout_3 = QHBoxLayout()
        self.targetLayout_3.setObjectName(u"targetLayout_3")
        self.label_19 = QLabel(self.verticalGroupBox_6)
        self.label_19.setObjectName(u"label_19")

        self.targetLayout_3.addWidget(self.label_19)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.targetLayout_3.addItem(self.horizontalSpacer_16)

        self.label_20 = QLabel(self.verticalGroupBox_6)
        self.label_20.setObjectName(u"label_20")

        self.targetLayout_3.addWidget(self.label_20)

        self.comboBox_9 = QComboBox(self.verticalGroupBox_6)
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.targetLayout_3.addWidget(self.comboBox_9)

        self.toolButton_8 = QToolButton(self.verticalGroupBox_6)
        self.toolButton_8.setObjectName(u"toolButton_8")

        self.targetLayout_3.addWidget(self.toolButton_8)


        self.verticalLayout_11.addLayout(self.targetLayout_3)


        self.horizontalLayout_10.addWidget(self.verticalGroupBox_6)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_17)

        self.verticalGroupBox_7 = QGroupBox(self.tab)
        self.verticalGroupBox_7.setObjectName(u"verticalGroupBox_7")
        self.verticalLayout_12 = QVBoxLayout(self.verticalGroupBox_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.allDemoCheck_3 = QCheckBox(self.verticalGroupBox_7)
        self.allDemoCheck_3.setObjectName(u"allDemoCheck_3")
        self.allDemoCheck_3.setMaximumSize(QSize(10000, 16777215))

        self.verticalLayout_12.addWidget(self.allDemoCheck_3)

        self.allStepsCheck_3 = QCheckBox(self.verticalGroupBox_7)
        self.allStepsCheck_3.setObjectName(u"allStepsCheck_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.allStepsCheck_3.sizePolicy().hasHeightForWidth())
        self.allStepsCheck_3.setSizePolicy(sizePolicy5)
        self.allStepsCheck_3.setMinimumSize(QSize(180, 0))
        self.allStepsCheck_3.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_12.addWidget(self.allStepsCheck_3)

        self.checkBox_5 = QCheckBox(self.verticalGroupBox_7)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_12.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.verticalGroupBox_7)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_12.addWidget(self.checkBox_6)

        self.matchSubstringCheck_3 = QCheckBox(self.verticalGroupBox_7)
        self.matchSubstringCheck_3.setObjectName(u"matchSubstringCheck_3")

        self.verticalLayout_12.addWidget(self.matchSubstringCheck_3)

        self.lineEdit_3 = QLineEdit(self.verticalGroupBox_7)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_12.addWidget(self.lineEdit_3)


        self.horizontalLayout_10.addWidget(self.verticalGroupBox_7)


        self.verticalLayout_14.addLayout(self.horizontalLayout_10)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget_2 = QStackedWidget(self.groupBox)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_13 = QVBoxLayout(self.page_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.verticalLayout_13.addLayout(self.verticalLayout_4)

        self.stackedWidget_2.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget_2)


        self.verticalLayout_14.addWidget(self.groupBox)

        self.stepTabs.addTab(self.tab, "")

        self.verticalLayout_20.addWidget(self.stepTabs)

        self.tabWidget_31 = QTabWidget(self.opsLayout)
        self.tabWidget_31.setObjectName(u"tabWidget_31")
        self.tabWidget_31.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.tabWidget_31.sizePolicy().hasHeightForWidth())
        self.tabWidget_31.setSizePolicy(sizePolicy6)
        self.tabWidget_31.setMinimumSize(QSize(350, 0))
        self.tabWidget_31.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget_31.setFont(font2)
        self.tabWidget_31.setTabPosition(QTabWidget.North)
        self.tabWidget_31.setTabsClosable(False)
        self.tabWidget_31.setMovable(False)
        self.tabWidget_3Page1 = QWidget()
        self.tabWidget_3Page1.setObjectName(u"tabWidget_3Page1")
        self.horizontalLayout_16 = QHBoxLayout(self.tabWidget_3Page1)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pushButton_36 = QPushButton(self.tabWidget_3Page1)
        self.pushButton_36.setObjectName(u"pushButton_36")

        self.horizontalLayout_16.addWidget(self.pushButton_36)

        self.pushButton_35 = QPushButton(self.tabWidget_3Page1)
        self.pushButton_35.setObjectName(u"pushButton_35")

        self.horizontalLayout_16.addWidget(self.pushButton_35)

        self.pushButton_34 = QPushButton(self.tabWidget_3Page1)
        self.pushButton_34.setObjectName(u"pushButton_34")

        self.horizontalLayout_16.addWidget(self.pushButton_34)

        self.pushButton_37 = QPushButton(self.tabWidget_3Page1)
        self.pushButton_37.setObjectName(u"pushButton_37")

        self.horizontalLayout_16.addWidget(self.pushButton_37)

        self.toolButton_9 = QToolButton(self.tabWidget_3Page1)
        self.toolButton_9.setObjectName(u"toolButton_9")

        self.horizontalLayout_16.addWidget(self.toolButton_9)

        self.tabWidget_31.addTab(self.tabWidget_3Page1, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tabWidget_31.addTab(self.tab_7, "")

        self.verticalLayout_20.addWidget(self.tabWidget_31)


        self.horizontalLayout_3.addWidget(self.opsLayout)

        self.viewLayout = QVBoxLayout()
        self.viewLayout.setSpacing(4)
        self.viewLayout.setObjectName(u"viewLayout")
        self.demoViewTabs = QTabWidget(self.jobsPage)
        self.demoViewTabs.setObjectName(u"demoViewTabs")
        self.demoViewTabs.setEnabled(True)
        self.demoViewTabs.setMinimumSize(QSize(0, 0))
        self.demoViewTabs.setMaximumSize(QSize(16777215, 16777215))
        self.demoViewTabs.setFont(font2)
        self.demoViewTabs.setTabPosition(QTabWidget.North)
        self.demoViewTabs.setTabShape(QTabWidget.Rounded)
        self.demoViewTabs.setElideMode(Qt.ElideLeft)
        self.demoOverviewGroupPage1 = QWidget()
        self.demoOverviewGroupPage1.setObjectName(u"demoOverviewGroupPage1")
        self.demoOverviewGroupPage1.setEnabled(True)
        self.verticalLayout_26 = QVBoxLayout(self.demoOverviewGroupPage1)
        self.verticalLayout_26.setSpacing(6)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_6 = QLabel(self.demoOverviewGroupPage1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(True)

        self.horizontalLayout_28.addWidget(self.label_6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_5)


        self.verticalLayout_26.addLayout(self.horizontalLayout_28)

        self.treeView_5 = QTreeView(self.demoOverviewGroupPage1)
        self.treeView_5.setObjectName(u"treeView_5")
        self.treeView_5.setEnabled(True)

        self.verticalLayout_26.addWidget(self.treeView_5)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.addDemoStepBtn = QPushButton(self.demoOverviewGroupPage1)
        self.addDemoStepBtn.setObjectName(u"addDemoStepBtn")
        self.addDemoStepBtn.setEnabled(True)

        self.horizontalLayout_18.addWidget(self.addDemoStepBtn)

        self.delDemoStepBtn = QPushButton(self.demoOverviewGroupPage1)
        self.delDemoStepBtn.setObjectName(u"delDemoStepBtn")

        self.horizontalLayout_18.addWidget(self.delDemoStepBtn)

        self.dupeDemoStepBtn = QPushButton(self.demoOverviewGroupPage1)
        self.dupeDemoStepBtn.setObjectName(u"dupeDemoStepBtn")

        self.horizontalLayout_18.addWidget(self.dupeDemoStepBtn)

        self.toolButton_11 = QToolButton(self.demoOverviewGroupPage1)
        self.toolButton_11.setObjectName(u"toolButton_11")

        self.horizontalLayout_18.addWidget(self.toolButton_11)


        self.verticalLayout_26.addLayout(self.horizontalLayout_18)

        self.demoViewTabs.addTab(self.demoOverviewGroupPage1, "")
        self.demoMetadataTab = QWidget()
        self.demoMetadataTab.setObjectName(u"demoMetadataTab")
        self.demoViewTabs.addTab(self.demoMetadataTab, "")

        self.viewLayout.addWidget(self.demoViewTabs)

        self.tabWidget_2 = QTabWidget(self.jobsPage)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setMinimumSize(QSize(325, 0))
        self.tabWidget_2.setMaximumSize(QSize(375, 16777215))
        self.tabWidget_2.setFont(font2)
        self.tabWidget_2Page1 = QWidget()
        self.tabWidget_2Page1.setObjectName(u"tabWidget_2Page1")
        self.verticalLayout_5 = QVBoxLayout(self.tabWidget_2Page1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_5 = QLabel(self.tabWidget_2Page1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_29.addWidget(self.label_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_29)

        self.tableWidget = QTableWidget(self.tabWidget_2Page1)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_5.addWidget(self.tableWidget)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_13 = QPushButton(self.tabWidget_2Page1)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout_9.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.tabWidget_2Page1)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.horizontalLayout_9.addWidget(self.pushButton_14)

        self.toolButton_4 = QToolButton(self.tabWidget_2Page1)
        self.toolButton_4.setObjectName(u"toolButton_4")

        self.horizontalLayout_9.addWidget(self.toolButton_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.tabWidget_2.addTab(self.tabWidget_2Page1, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_25 = QVBoxLayout(self.tab_5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.graphicsView = QGraphicsView(self.tab_5)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_25.addWidget(self.graphicsView)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButton_38 = QPushButton(self.tab_5)
        self.pushButton_38.setObjectName(u"pushButton_38")

        self.horizontalLayout_17.addWidget(self.pushButton_38)

        self.pushButton_39 = QPushButton(self.tab_5)
        self.pushButton_39.setObjectName(u"pushButton_39")

        self.horizontalLayout_17.addWidget(self.pushButton_39)

        self.toolButton_10 = QToolButton(self.tab_5)
        self.toolButton_10.setObjectName(u"toolButton_10")

        self.horizontalLayout_17.addWidget(self.toolButton_10)


        self.verticalLayout_25.addLayout(self.horizontalLayout_17)

        self.tabWidget_2.addTab(self.tab_5, "")

        self.viewLayout.addWidget(self.tabWidget_2)


        self.horizontalLayout_3.addLayout(self.viewLayout)

        self.centralTabs.addWidget(self.jobsPage)
        self.centralTabsPage2 = QWidget()
        self.centralTabsPage2.setObjectName(u"centralTabsPage2")
        self.horizontalLayout_2 = QHBoxLayout(self.centralTabsPage2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.centralTabs.addWidget(self.centralTabsPage2)

        self.verticalLayout_31.addWidget(self.centralTabs)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setLayoutDirection(Qt.RightToLeft)
        self.statusbar.setAutoFillBackground(True)
        self.statusbar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1120, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuNew = QMenu(self.menuFile)
        self.menuNew.setObjectName(u"menuNew")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuDemo = QMenu(self.menubar)
        self.menuDemo.setObjectName(u"menuDemo")
        self.menuWindow_2 = QMenu(self.menubar)
        self.menuWindow_2.setObjectName(u"menuWindow_2")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuJobs = QMenu(self.menubar)
        self.menuJobs.setObjectName(u"menuJobs")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuDemo.menuAction())
        self.menubar.addAction(self.menuWindow_2.menuAction())
        self.menubar.addAction(self.menuJobs.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Jobs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_Demo)
        self.menuFile.addAction(self.actionOpen_Audio)
        self.menuFile.addAction(self.actionOpen_Script)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addSeparator()
        self.menuNew.addAction(self.actionStep)
        self.menuNew.addAction(self.actionQueue)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuView.addAction(self.actionJobs_Editor)
        self.menuView.addAction(self.actionXML_Editor)
        self.menuView.addAction(self.actionScript_Editor)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionFull_Screen)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionMenubar)
        self.menuView.addAction(self.actionStatusbar)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionAbout)
        self.menuJobs.addAction(self.actionRun)
        self.menuJobs.addAction(self.actionClear_jobs)
        self.menuJobs.addSeparator()
        self.menuJobs.addAction(self.actionDelete_current_task)
        self.menuJobs.addAction(self.actionDuplicate_current_task)
        self.menuJobs.addAction(self.actionReset_current_task)
        self.menuJobs.addAction(self.actionRun_current_task)

        self.retranslateUi(MainWindow)
        self.actionOpen_Demo.toggled.connect(MainWindow.raise)
        self.browseButton.clicked.connect(self.browseButton.showMenu)
        self.actionFull_Screen.triggered.connect(MainWindow.showFullScreen)

        self.centralTabs.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        self.browseButton.setDefault(True)
        self.browseDemoBtn.setDefault(False)
        self.tabWidget_3.setCurrentIndex(0)
        self.addStepButton.setDefault(True)
        self.runButton.setDefault(True)
        self.stepTabs.setCurrentIndex(0)
        self.tabWidget_31.setCurrentIndex(0)
        self.demoViewTabs.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Impresys Demo Utilities", None))
        self.actionStep.setText(QCoreApplication.translate("MainWindow", u"Step", None))
        self.actionOpen_Demo.setText(QCoreApplication.translate("MainWindow", u"Open Demo", None))
        self.actionOpen_Audio.setText(QCoreApplication.translate("MainWindow", u"Open Audio", None))
#if QT_CONFIG(shortcut)
        self.actionOpen_Audio.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen_Script.setText(QCoreApplication.translate("MainWindow", u"Open Script", None))
#if QT_CONFIG(shortcut)
        self.actionOpen_Script.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_Jobs.setText(QCoreApplication.translate("MainWindow", u"Save Job List", None))
#if QT_CONFIG(shortcut)
        self.actionSave_Jobs.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
#if QT_CONFIG(shortcut)
        self.actionPreferences.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
#if QT_CONFIG(shortcut)
        self.actionUndo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
#if QT_CONFIG(shortcut)
        self.actionRedo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Y", None))
#endif // QT_CONFIG(shortcut)
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionQueue.setText(QCoreApplication.translate("MainWindow", u"Queue", None))
        self.actionJobs_Editor.setText(QCoreApplication.translate("MainWindow", u"Jobs Editor", None))
        self.actionXML_Editor.setText(QCoreApplication.translate("MainWindow", u"XML Editor", None))
        self.actionScript_Editor.setText(QCoreApplication.translate("MainWindow", u"Script Editor", None))
        self.actionFull_Screen.setText(QCoreApplication.translate("MainWindow", u"Full Screen", None))
#if QT_CONFIG(shortcut)
        self.actionFull_Screen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+F", None))
#endif // QT_CONFIG(shortcut)
        self.actionRun.setText(QCoreApplication.translate("MainWindow", u"Run all tasks", None))
#if QT_CONFIG(shortcut)
        self.actionRun.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionClear_jobs.setText(QCoreApplication.translate("MainWindow", u"Clear all tasks", None))
#if QT_CONFIG(shortcut)
        self.actionClear_jobs.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionDelete_current_task.setText(QCoreApplication.translate("MainWindow", u"Delete current task", None))
        self.actionDuplicate_current_task.setText(QCoreApplication.translate("MainWindow", u"Duplicate current task", None))
        self.actionReset_current_task.setText(QCoreApplication.translate("MainWindow", u"Reset current task", None))
        self.actionMenubar.setText(QCoreApplication.translate("MainWindow", u"Menubar", None))
#if QT_CONFIG(shortcut)
        self.actionMenubar.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionStatusbar.setText(QCoreApplication.translate("MainWindow", u"Statusbar", None))
#if QT_CONFIG(shortcut)
        self.actionStatusbar.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionRun_current_task.setText(QCoreApplication.translate("MainWindow", u"Run current task", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Loaded Data", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Demo", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Audio", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Script", None))

        self.browseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Path", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Links", None));
        self.browseDemoBtn.setText(QCoreApplication.translate("MainWindow", u"Demo", None))
        self.browseAudioBtn.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
        self.browseScriptBtn.setText(QCoreApplication.translate("MainWindow", u"Script", None))
        self.toolButton_12.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Task Presets", None))
        self.pushButton_54.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.toolButton_13.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Presets", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Job history", None))
        self.toolButton_15.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"Saved", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Loaded Data", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Demo", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Audio", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Script", None))

        self.addStepButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
#if QT_CONFIG(shortcut)
        self.addStepButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        ___qtablewidgetitem3 = self.stepsList.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Task", None));
        ___qtablewidgetitem4 = self.stepsList.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Demo", None));
        ___qtablewidgetitem5 = self.stepsList.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Steps", None));
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.runButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
#if QT_CONFIG(shortcut)
        self.runButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"Steps", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Loaded Data", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Demo", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Audio", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Script", None))

        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.toolButton_14.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"History", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Undo History", None))
        self.toolButton_16.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"Undo", None))
        self.verticalGroupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Task Info", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Current:", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"Shell", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"Insert", None))
        self.comboBox_8.setItemText(2, QCoreApplication.translate("MainWindow", u"Crop", None))
        self.comboBox_8.setItemText(3, QCoreApplication.translate("MainWindow", u"Section", None))
        self.comboBox_8.setItemText(4, QCoreApplication.translate("MainWindow", u"Add Audio", None))
        self.comboBox_8.setItemText(5, QCoreApplication.translate("MainWindow", u"Pacing", None))
        self.comboBox_8.setItemText(6, QCoreApplication.translate("MainWindow", u"Add Text", None))
        self.comboBox_8.setItemText(7, QCoreApplication.translate("MainWindow", u"Render", None))

        self.toolButton_7.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Index", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Index", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Target", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Demo:", None))
        self.toolButton_8.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.verticalGroupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Step Targets", None))
        self.allDemoCheck_3.setText(QCoreApplication.translate("MainWindow", u"Apply to all demos", None))
        self.allStepsCheck_3.setText(QCoreApplication.translate("MainWindow", u"Apply to all steps", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Apply to all steps of marked sections", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Apply to marked steps", None))
        self.matchSubstringCheck_3.setText(QCoreApplication.translate("MainWindow", u"Apply to steps with title containing:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.stepTabs.setTabText(self.stepTabs.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Task 1", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"Duplicate", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.toolButton_9.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tabWidget_31.setTabText(self.tabWidget_31.indexOf(self.tabWidget_3Page1), QCoreApplication.translate("MainWindow", u"Task", None))
        self.tabWidget_31.setTabText(self.tabWidget_31.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Info", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.addDemoStepBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.delDemoStepBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.dupeDemoStepBtn.setText(QCoreApplication.translate("MainWindow", u"Duplicate", None))
        self.toolButton_11.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.demoViewTabs.setTabText(self.demoViewTabs.indexOf(self.demoOverviewGroupPage1), QCoreApplication.translate("MainWindow", u"Demo Steps", None))
        self.demoViewTabs.setTabText(self.demoViewTabs.indexOf(self.demoMetadataTab), QCoreApplication.translate("MainWindow", u"Metadata", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"More Info", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabWidget_2Page1), QCoreApplication.translate("MainWindow", u"Properties", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"More Info", None))
        self.toolButton_10.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Preview", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuNew.setTitle(QCoreApplication.translate("MainWindow", u"New...", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuDemo.setTitle(QCoreApplication.translate("MainWindow", u"Demo", None))
        self.menuWindow_2.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuJobs.setTitle(QCoreApplication.translate("MainWindow", u"Actions", None))
    # retranslateUi

