# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabs.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLayout,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_centralWiget(object):
    def setupUi(self, centralWiget):
        if not centralWiget.objectName():
            centralWiget.setObjectName(u"centralWiget")
        centralWiget.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(centralWiget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.centralTabs = QTabWidget(centralWiget)
        self.centralTabs.setObjectName(u"centralTabs")
        self.centralTabs.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralTabs.sizePolicy().hasHeightForWidth())
        self.centralTabs.setSizePolicy(sizePolicy)
        self.centralTabs.setAcceptDrops(True)
        self.centralTabs.setAutoFillBackground(False)
        self.centralTabs.setDocumentMode(True)
        self.centralTabs.setTabsClosable(False)
        self.centralTabs.setMovable(True)
        self.centralTabs.setTabBarAutoHide(False)
        self.demoPage = QWidget()
        self.demoPage.setObjectName(u"demoPage")
        self.demoPageLayout = QHBoxLayout(self.demoPage)
        self.demoPageLayout.setObjectName(u"demoPageLayout")
        self.stepsLayout = QVBoxLayout()
        self.stepsLayout.setSpacing(10)
        self.stepsLayout.setObjectName(u"stepsLayout")
        self.stepsLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.stepsLayout.setContentsMargins(0, 0, 0, 0)

        self.demoPageLayout.addLayout(self.stepsLayout)

        self.centralTabs.addTab(self.demoPage, "")
        self.scriptsPage = QWidget()
        self.scriptsPage.setObjectName(u"scriptsPage")
        self.horizontalLayoutWidget = QWidget(self.scriptsPage)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(210, 120, 71, 24))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.centralTabs.addTab(self.scriptsPage, "")
        self.productionPage = QWidget()
        self.productionPage.setObjectName(u"productionPage")
        self.centralTabs.addTab(self.productionPage, "")

        self.verticalLayout_2.addWidget(self.centralTabs)


        self.retranslateUi(centralWiget)

        self.centralTabs.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(centralWiget)
    # setupUi

    def retranslateUi(self, centralWiget):
        centralWiget.setWindowTitle(QCoreApplication.translate("centralWiget", u"Form", None))
        self.centralTabs.setTabText(self.centralTabs.indexOf(self.demoPage), QCoreApplication.translate("centralWiget", u"Demo Utilities", None))
        self.centralTabs.setTabText(self.centralTabs.indexOf(self.scriptsPage), QCoreApplication.translate("centralWiget", u"Script Studio", None))
        self.centralTabs.setTabText(self.centralTabs.indexOf(self.productionPage), QCoreApplication.translate("centralWiget", u"Production", None))
    # retranslateUi

