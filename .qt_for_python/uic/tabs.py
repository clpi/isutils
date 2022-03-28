# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabs.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_centralTabs(object):
    def setupUi(self, centralTabs):
        if not centralTabs.objectName():
            centralTabs.setObjectName(u"centralTabs")
        centralTabs.setEnabled(True)
        centralTabs.resize(342, 286)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(centralTabs.sizePolicy().hasHeightForWidth())
        centralTabs.setSizePolicy(sizePolicy)
        centralTabs.setAcceptDrops(True)
        centralTabs.setAutoFillBackground(False)
        centralTabs.setDocumentMode(True)
        centralTabs.setTabsClosable(False)
        centralTabs.setMovable(True)
        centralTabs.setTabBarAutoHide(False)
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

        centralTabs.addTab(self.demoPage, "")
        self.scriptsPage = QWidget()
        self.scriptsPage.setObjectName(u"scriptsPage")
        self.horizontalLayoutWidget = QWidget(self.scriptsPage)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(210, 120, 74, 26))
        self.scriptsLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.scriptsLayout.setObjectName(u"scriptsLayout")
        self.scriptsLayout.setContentsMargins(0, 0, 0, 0)
        centralTabs.addTab(self.scriptsPage, "")
        self.productionPage = QWidget()
        self.productionPage.setObjectName(u"productionPage")
        centralTabs.addTab(self.productionPage, "")

        self.retranslateUi(centralTabs)

        centralTabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(centralTabs)
    # setupUi

    def retranslateUi(self, centralTabs):
        centralTabs.setWindowTitle(QCoreApplication.translate("centralTabs", u"Form", None))
        centralTabs.setTabText(centralTabs.indexOf(self.demoPage), QCoreApplication.translate("centralTabs", u"Demo Utilities", None))
        centralTabs.setTabText(centralTabs.indexOf(self.scriptsPage), QCoreApplication.translate("centralTabs", u"Script Studio", None))
        centralTabs.setTabText(centralTabs.indexOf(self.productionPage), QCoreApplication.translate("centralTabs", u"Production", None))
    # retranslateUi

