# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLayout,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStackedWidget, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

from demopage import DemoPage

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1120, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1120, 700))
        MainWindow.setMaximumSize(QSize(16777203, 16777210))
        MainWindow.setMouseTracking(True)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(True)
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QMainWindow.AllowNestedDocks|QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks|QMainWindow.GroupedDragging)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralLayout = QVBoxLayout(self.centralwidget)
        self.centralLayout.setSpacing(5)
        self.centralLayout.setObjectName(u"centralLayout")
        self.centralLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.centralLayout.setContentsMargins(5, 5, 5, 5)
        self.centralTabs = QStackedWidget(self.centralwidget)
        self.centralTabs.setObjectName(u"centralTabs")
        self.centralTabs.setMouseTracking(True)
        self.centralTabs.setAcceptDrops(True)
        self.centralTabs.setLineWidth(0)
        self.editStackPage = QWidget()
        self.editStackPage.setObjectName(u"editStackPage")
        self.horizontalLayout_3 = QHBoxLayout(self.editStackPage)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dataView = QTabWidget(self.editStackPage)
        self.dataView.setObjectName(u"dataView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dataView.sizePolicy().hasHeightForWidth())
        self.dataView.setSizePolicy(sizePolicy1)
        self.dataView.setMinimumSize(QSize(300, 0))
        self.demoDataPage = DemoPage()
        self.demoDataPage.setObjectName(u"demoDataPage")
        self.verticalLayout_6 = QVBoxLayout(self.demoDataPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
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
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
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

        self.centralLayout.addWidget(self.centralTabs)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1120, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuWindow = QMenu(self.menubar)
        self.menuWindow.setObjectName(u"menuWindow")
        self.menuDemo = QMenu(self.menubar)
        self.menuDemo.setObjectName(u"menuDemo")
        self.menuWindow_2 = QMenu(self.menubar)
        self.menuWindow_2.setObjectName(u"menuWindow_2")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuDemo.menuAction())
        self.menubar.addAction(self.menuWindow_2.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        self.dataView.setCurrentIndex(0)
        self.viewTabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.dataView.setTabText(self.dataView.indexOf(self.demoDataPage), QCoreApplication.translate("MainWindow", u"Data", None))
        self.dataView.setTabText(self.dataView.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Saved", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Demo Overview", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Step Overview", None))
        self.viewTabs.setTabText(self.viewTabs.indexOf(self.demoViewTab), QCoreApplication.translate("MainWindow", u"Overview", None))
        self.viewTabs.setTabText(self.viewTabs.indexOf(self.metadataViewTab), QCoreApplication.translate("MainWindow", u"Metadata", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuDemo.setTitle(QCoreApplication.translate("MainWindow", u"Demo", None))
        self.menuWindow_2.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

