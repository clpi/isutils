# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadedFLdwWA.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTabWidget,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class DataLoaded(object):
    def setupUi(self, dataLoaded):
        if not dataLoaded.objectName():
            dataLoaded.setObjectName(u"dataLoaded")
        dataLoaded.resize(400, 301)
        self.verticalLayout = QVBoxLayout(dataLoaded)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.assetsTabs = QTabWidget(dataLoaded)
        self.assetsTabs.setObjectName(u"assetsTabs")
        self.assetsTabs.setMinimumSize(QSize(362, 0))
        self.assetsTabs.setMaximumSize(QSize(410, 16777215))
        self.assetsTabs.setMouseTracking(False)
        self.assetsTabs.setLayoutDirection(Qt.LeftToRight)
        self.assetsTabs.setAutoFillBackground(False)
        self.assetsTabs.setTabPosition(QTabWidget.North)
        self.assetsTabs.setTabShape(QTabWidget.Rounded)
        self.assetsTabs.setUsesScrollButtons(False)
        self.assetsTabs.setDocumentMode(False)
        self.assetsTabs.setTabsClosable(False)
        self.assetsTabs.setMovable(False)
        self.assetsTabs.setTabBarAutoHide(False)
        self.demoList = QWidget()
        self.demoList.setObjectName(u"demoList")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.demoList.sizePolicy().hasHeightForWidth())
        self.demoList.setSizePolicy(sizePolicy)
        self.verticalLayout_11 = QVBoxLayout(self.demoList)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.browseDemoBtn = QPushButton(self.demoList)
        self.browseDemoBtn.setObjectName(u"browseDemoBtn")

        self.horizontalLayout_10.addWidget(self.browseDemoBtn)

        self.browseScriptBtn = QPushButton(self.demoList)
        self.browseScriptBtn.setObjectName(u"browseScriptBtn")

        self.horizontalLayout_10.addWidget(self.browseScriptBtn)

        self.browseAudioBtn = QPushButton(self.demoList)
        self.browseAudioBtn.setObjectName(u"browseAudioBtn")

        self.horizontalLayout_10.addWidget(self.browseAudioBtn)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)


        self.verticalLayout_11.addLayout(self.verticalLayout_12)

        self.demoListTreeWidget = QTreeWidget(self.demoList)
        self.demoListTreeWidget.setObjectName(u"demoListTreeWidget")

        self.verticalLayout_11.addWidget(self.demoListTreeWidget)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.infoBtn = QPushButton(self.demoList)
        self.infoBtn.setObjectName(u"infoBtn")

        self.horizontalLayout_11.addWidget(self.infoBtn)

        self.loadScriptBtn = QPushButton(self.demoList)
        self.loadScriptBtn.setObjectName(u"loadScriptBtn")

        self.horizontalLayout_11.addWidget(self.loadScriptBtn)

        self.loadAudioBtn = QPushButton(self.demoList)
        self.loadAudioBtn.setObjectName(u"loadAudioBtn")

        self.horizontalLayout_11.addWidget(self.loadAudioBtn)

        self.removeDemoBtn = QPushButton(self.demoList)
        self.removeDemoBtn.setObjectName(u"removeDemoBtn")

        self.horizontalLayout_11.addWidget(self.removeDemoBtn)

        self.addDemoBtn = QPushButton(self.demoList)
        self.addDemoBtn.setObjectName(u"addDemoBtn")

        self.horizontalLayout_11.addWidget(self.addDemoBtn)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.assetsTabs.addTab(self.demoList, "")
        self.scriptOverviewTab = QWidget()
        self.scriptOverviewTab.setObjectName(u"scriptOverviewTab")
        self.verticalLayout_13 = QVBoxLayout(self.scriptOverviewTab)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.scriptListTreeWidget = QListWidget(self.scriptOverviewTab)
        self.scriptListTreeWidget.setObjectName(u"scriptListTreeWidget")

        self.verticalLayout_13.addWidget(self.scriptListTreeWidget)

        self.assetsTabs.addTab(self.scriptOverviewTab, "")
        self.audioOverviewTab = QWidget()
        self.audioOverviewTab.setObjectName(u"audioOverviewTab")
        self.verticalLayout_15 = QVBoxLayout(self.audioOverviewTab)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.audioListTreeWidget = QListWidget(self.audioOverviewTab)
        self.audioListTreeWidget.setObjectName(u"audioListTreeWidget")

        self.verticalLayout_15.addWidget(self.audioListTreeWidget)

        self.assetsTabs.addTab(self.audioOverviewTab, "")

        self.verticalLayout.addWidget(self.assetsTabs)


        self.retranslateUi(dataLoaded)

        self.assetsTabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(dataLoaded)
    # setupUi

    def retranslateUi(self, dataLoaded):
        dataLoaded.setWindowTitle(QCoreApplication.translate("dataLoaded", u"Form", None))
        self.browseDemoBtn.setText(QCoreApplication.translate("dataLoaded", u"Demo", None))
        self.browseScriptBtn.setText(QCoreApplication.translate("dataLoaded", u"Script", None))
        self.browseAudioBtn.setText(QCoreApplication.translate("dataLoaded", u"Audio", None))
        ___qtreewidgetitem = self.demoListTreeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("dataLoaded", u"Script", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("dataLoaded", u"Audio", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("dataLoaded", u"Demo", None));
        self.infoBtn.setText(QCoreApplication.translate("dataLoaded", u"Info", None))
        self.loadScriptBtn.setText(QCoreApplication.translate("dataLoaded", u"Load Script", None))
        self.loadAudioBtn.setText(QCoreApplication.translate("dataLoaded", u"Load audio", None))
        self.removeDemoBtn.setText(QCoreApplication.translate("dataLoaded", u"Remove", None))
        self.addDemoBtn.setText(QCoreApplication.translate("dataLoaded", u"Add Demo", None))
        self.assetsTabs.setTabText(self.assetsTabs.indexOf(self.demoList), QCoreApplication.translate("dataLoaded", u"Demo", None))
#if QT_CONFIG(tooltip)
        self.assetsTabs.setTabToolTip(self.assetsTabs.indexOf(self.demoList), QCoreApplication.translate("dataLoaded", u"Demo information", None))
#endif // QT_CONFIG(tooltip)
        self.assetsTabs.setTabText(self.assetsTabs.indexOf(self.scriptOverviewTab), QCoreApplication.translate("dataLoaded", u"Script", None))
        self.assetsTabs.setTabText(self.assetsTabs.indexOf(self.audioOverviewTab), QCoreApplication.translate("dataLoaded", u"Audio", None))
    # retranslateUi

