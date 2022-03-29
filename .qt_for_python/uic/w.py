# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'w.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStackedWidget,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

from demopage import DemoPage

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1120, 700)
        self.actionOpen_Ops = QAction(MainWindow)
        self.actionOpen_Ops.setObjectName(u"actionOpen_Ops")
        self.actionOpen_Demo = QAction(MainWindow)
        self.actionOpen_Demo.setObjectName(u"actionOpen_Demo")
        self.actionOpen_Audio = QAction(MainWindow)
        self.actionOpen_Audio.setObjectName(u"actionOpen_Audio")
        self.actionImport_Script = QAction(MainWindow)
        self.actionImport_Script.setObjectName(u"actionImport_Script")
        self.actionSave_Ops = QAction(MainWindow)
        self.actionSave_Ops.setObjectName(u"actionSave_Ops")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionView_metadata = QAction(MainWindow)
        self.actionView_metadata.setObjectName(u"actionView_metadata")
        self.actionRename = QAction(MainWindow)
        self.actionRename.setObjectName(u"actionRename")
        self.actionExport_to_XML = QAction(MainWindow)
        self.actionExport_to_XML.setObjectName(u"actionExport_to_XML")
        self.actionOperations = QAction(MainWindow)
        self.actionOperations.setObjectName(u"actionOperations")
        self.actionMetadata_editor = QAction(MainWindow)
        self.actionMetadata_editor.setObjectName(u"actionMetadata_editor")
        self.actionProduction_editor = QAction(MainWindow)
        self.actionProduction_editor.setObjectName(u"actionProduction_editor")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionHow_to_use = QAction(MainWindow)
        self.actionHow_to_use.setObjectName(u"actionHow_to_use")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionPreferences_2 = QAction(MainWindow)
        self.actionPreferences_2.setObjectName(u"actionPreferences_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.centralTabs = QStackedWidget(self.centralwidget)
        self.centralTabs.setObjectName(u"centralTabs")
        self.centralTabs.setMouseTracking(True)
        self.centralTabs.setAcceptDrops(True)
        self.centralTabs.setLineWidth(0)
        self.editStackPage = QWidget()
        self.editStackPage.setObjectName(u"editStackPage")
        self.horizontalLayout_3 = QHBoxLayout(self.editStackPage)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.dataView = QTabWidget(self.editStackPage)
        self.dataView.setObjectName(u"dataView")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataView.sizePolicy().hasHeightForWidth())
        self.dataView.setSizePolicy(sizePolicy)
        self.dataView.setMinimumSize(QSize(300, 0))
        self.demoDataPage = DemoPage()
        self.demoDataPage.setObjectName(u"demoDataPage")
        self.verticalLayout_6 = QVBoxLayout(self.demoDataPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.groupBox_3 = QGroupBox(self.demoDataPage)
        self.groupBox_3.setObjectName(u"groupBox_3")

        self.verticalLayout_6.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.demoDataPage)
        self.groupBox_4.setObjectName(u"groupBox_4")

        self.verticalLayout_6.addWidget(self.groupBox_4)

        self.dataView.addTab(self.demoDataPage, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.dataView.addTab(self.tab_5, "")

        self.horizontalLayout_3.addWidget(self.dataView)

        self.tabWidget = QTabWidget(self.editStackPage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(False)
        self.tabWidget.setAcceptDrops(True)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)

        self.horizontalLayout_3.addWidget(self.tabWidget)

        self.viewTabs = QTabWidget(self.editStackPage)
        self.viewTabs.setObjectName(u"viewTabs")
        self.viewTabs.setMinimumSize(QSize(0, 0))
        self.viewTabs.setMaximumSize(QSize(16555215, 16777215))
        self.demoViewTab = QWidget()
        self.demoViewTab.setObjectName(u"demoViewTab")
        self.verticalLayout_8 = QVBoxLayout(self.demoViewTab)
        self.verticalLayout_8.setSpacing(1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(4, 4, 4, 4)
        self.groupBox = QGroupBox(self.demoViewTab)
        self.groupBox.setObjectName(u"groupBox")

        self.verticalLayout_8.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.demoViewTab)
        self.groupBox_2.setObjectName(u"groupBox_2")

        self.verticalLayout_8.addWidget(self.groupBox_2)

        self.viewTabs.addTab(self.demoViewTab, "")
        self.metadataViewTab = QWidget()
        self.metadataViewTab.setObjectName(u"metadataViewTab")
        self.viewTabs.addTab(self.metadataViewTab, "")

        self.horizontalLayout_3.addWidget(self.viewTabs)

        self.centralTabs.addWidget(self.editStackPage)
        self.tabWidget.raise_()
        self.dataView.raise_()
        self.viewTabs.raise_()
        self.centralTabsPage2 = QWidget()
        self.centralTabsPage2.setObjectName(u"centralTabsPage2")
        self.horizontalLayout_2 = QHBoxLayout(self.centralTabsPage2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.centralTabs.addWidget(self.centralTabsPage2)

        self.verticalLayout.addWidget(self.centralTabs)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1120, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuDemo = QMenu(self.menubar)
        self.menuDemo.setObjectName(u"menuDemo")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuWindow = QMenu(self.menubar)
        self.menuWindow.setObjectName(u"menuWindow")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuDemo.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen_Ops)
        self.menuFile.addAction(self.actionSave_Ops)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_Demo)
        self.menuFile.addAction(self.actionOpen_Audio)
        self.menuFile.addAction(self.actionImport_Script)
        self.menuFile.addSeparator()
        self.menuEdit.addAction(self.actionPreferences)
        self.menuDemo.addAction(self.actionView_metadata)
        self.menuDemo.addAction(self.actionRename)
        self.menuDemo.addAction(self.actionExport_to_XML)
        self.menuView.addAction(self.actionOperations)
        self.menuView.addAction(self.actionMetadata_editor)
        self.menuView.addAction(self.actionProduction_editor)
        self.menuTools.addAction(self.actionPreferences_2)
        self.menuWindow.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHow_to_use)

        self.retranslateUi(MainWindow)

        self.dataView.setCurrentIndex(1)
        self.viewTabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_Ops.setText(QCoreApplication.translate("MainWindow", u"Open Ops", None))
        self.actionOpen_Demo.setText(QCoreApplication.translate("MainWindow", u"Import Demo", None))
        self.actionOpen_Audio.setText(QCoreApplication.translate("MainWindow", u"Import Audio", None))
        self.actionImport_Script.setText(QCoreApplication.translate("MainWindow", u"Import Script", None))
        self.actionSave_Ops.setText(QCoreApplication.translate("MainWindow", u"Save Ops", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.actionView_metadata.setText(QCoreApplication.translate("MainWindow", u"View metadata", None))
        self.actionRename.setText(QCoreApplication.translate("MainWindow", u"Rename ", None))
        self.actionExport_to_XML.setText(QCoreApplication.translate("MainWindow", u"Export to XML", None))
        self.actionOperations.setText(QCoreApplication.translate("MainWindow", u"Operations", None))
        self.actionMetadata_editor.setText(QCoreApplication.translate("MainWindow", u"Metadata editor", None))
        self.actionProduction_editor.setText(QCoreApplication.translate("MainWindow", u"Production editor", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionHow_to_use.setText(QCoreApplication.translate("MainWindow", u"How to use", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionPreferences_2.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.dataView.setTabText(self.dataView.indexOf(self.demoDataPage), QCoreApplication.translate("MainWindow", u"Data", None))
        self.dataView.setTabText(self.dataView.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Saved", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Demo Overview", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Step Overview", None))
        self.viewTabs.setTabText(self.viewTabs.indexOf(self.demoViewTab), QCoreApplication.translate("MainWindow", u"Overview", None))
        self.viewTabs.setTabText(self.viewTabs.indexOf(self.metadataViewTab), QCoreApplication.translate("MainWindow", u"Metadata", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuDemo.setTitle(QCoreApplication.translate("MainWindow", u"Demo", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

