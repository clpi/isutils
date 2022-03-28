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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QSizePolicy,
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget)

from demopage import DemoPage

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1161, 777)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(1100, 700))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.centralTabs = QStackedWidget(Form)
        self.centralTabs.setObjectName(u"centralTabs")
        self.centralTabs.setMouseTracking(True)
        self.centralTabs.setAcceptDrops(True)
        self.centralTabs.setLineWidth(0)
        self.editStackPage_2 = QWidget()
        self.editStackPage_2.setObjectName(u"editStackPage_2")
        self.horizontalLayout_4 = QHBoxLayout(self.editStackPage_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.dataView_2 = QTabWidget(self.editStackPage_2)
        self.dataView_2.setObjectName(u"dataView_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dataView_2.sizePolicy().hasHeightForWidth())
        self.dataView_2.setSizePolicy(sizePolicy1)
        self.dataView_2.setMinimumSize(QSize(300, 0))
        self.demoDataPage_2 = DemoPage()
        self.demoDataPage_2.setObjectName(u"demoDataPage_2")
        self.verticalLayout_7 = QVBoxLayout(self.demoDataPage_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.dataView_2.addTab(self.demoDataPage_2, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.dataView_2.addTab(self.tab_6, "")

        self.horizontalLayout_4.addWidget(self.dataView_2)

        self.tabWidget_2 = QTabWidget(self.editStackPage_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setEnabled(False)
        self.tabWidget_2.setAcceptDrops(True)
        self.tabWidget_2.setElideMode(Qt.ElideNone)
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setMovable(True)
        self.tabWidget_2.setTabBarAutoHide(False)

        self.horizontalLayout_4.addWidget(self.tabWidget_2)

        self.viewTabs_2 = QTabWidget(self.editStackPage_2)
        self.viewTabs_2.setObjectName(u"viewTabs_2")
        self.viewTabs_2.setMinimumSize(QSize(0, 0))
        self.viewTabs_2.setMaximumSize(QSize(16555215, 16777215))
        self.demoViewTab_2 = QWidget()
        self.demoViewTab_2.setObjectName(u"demoViewTab_2")
        self.verticalLayout_9 = QVBoxLayout(self.demoViewTab_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_3 = QGroupBox(self.demoViewTab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")

        self.verticalLayout_9.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.demoViewTab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")

        self.verticalLayout_9.addWidget(self.groupBox_4)

        self.viewTabs_2.addTab(self.demoViewTab_2, "")
        self.metadataViewTab_2 = QWidget()
        self.metadataViewTab_2.setObjectName(u"metadataViewTab_2")
        self.viewTabs_2.addTab(self.metadataViewTab_2, "")

        self.horizontalLayout_4.addWidget(self.viewTabs_2)

        self.centralTabs.addWidget(self.editStackPage_2)
        self.centralTabsPage2_2 = QWidget()
        self.centralTabsPage2_2.setObjectName(u"centralTabsPage2_2")
        self.horizontalLayout_5 = QHBoxLayout(self.centralTabsPage2_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)

        self.centralTabs.addWidget(self.centralTabsPage2_2)

        self.verticalLayout.addWidget(self.centralTabs)


        self.retranslateUi(Form)

        self.dataView_2.setCurrentIndex(0)
        self.viewTabs_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.dataView_2.setTabText(self.dataView_2.indexOf(self.demoDataPage_2), QCoreApplication.translate("Form", u"Data", None))
        self.dataView_2.setTabText(self.dataView_2.indexOf(self.tab_6), QCoreApplication.translate("Form", u"Saved", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Demo Overview", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Step Overview", None))
        self.viewTabs_2.setTabText(self.viewTabs_2.indexOf(self.demoViewTab_2), QCoreApplication.translate("Form", u"Overview", None))
        self.viewTabs_2.setTabText(self.viewTabs_2.indexOf(self.metadataViewTab_2), QCoreApplication.translate("Form", u"Metadata", None))
    # retranslateUi

