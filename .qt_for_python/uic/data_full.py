# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_full.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLayout,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QTabWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(529, 777)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stepsLayout = QVBoxLayout()
        self.stepsLayout.setSpacing(10)
        self.stepsLayout.setObjectName(u"stepsLayout")
        self.stepsLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.stepsLayout.setContentsMargins(0, 0, 0, 0)
        self.assetsTabs = QTabWidget(Form)
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

        self.stepsLayout.addWidget(self.assetsTabs)

        self.opsTabs = QTabWidget(Form)
        self.opsTabs.setObjectName(u"opsTabs")
        self.opsTabs.setEnabled(True)
        self.opsTabs.setMaximumSize(QSize(410, 16777215))
        self.stepsTab = QWidget()
        self.stepsTab.setObjectName(u"stepsTab")
        sizePolicy.setHeightForWidth(self.stepsTab.sizePolicy().hasHeightForWidth())
        self.stepsTab.setSizePolicy(sizePolicy)
        self.stepsTab.setMinimumSize(QSize(200, 278))
        self.stepsTab.setAutoFillBackground(False)
        self.verticalLayout_2 = QVBoxLayout(self.stepsTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 11, -1, -1)
        self.stepsTreeWidget = QTreeWidget(self.stepsTab)
        self.stepsTreeWidget.setObjectName(u"stepsTreeWidget")

        self.verticalLayout_2.addWidget(self.stepsTreeWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stepDownBtn = QPushButton(self.stepsTab)
        self.stepDownBtn.setObjectName(u"stepDownBtn")

        self.horizontalLayout_3.addWidget(self.stepDownBtn)

        self.stepUpBtn = QPushButton(self.stepsTab)
        self.stepUpBtn.setObjectName(u"stepUpBtn")

        self.horizontalLayout_3.addWidget(self.stepUpBtn)

        self.removeStepBtn = QPushButton(self.stepsTab)
        self.removeStepBtn.setObjectName(u"removeStepBtn")

        self.horizontalLayout_3.addWidget(self.removeStepBtn)

        self.addStepBtn = QPushButton(self.stepsTab)
        self.addStepBtn.setObjectName(u"addStepBtn")

        self.horizontalLayout_3.addWidget(self.addStepBtn)

        self.runBtn = QPushButton(self.stepsTab)
        self.runBtn.setObjectName(u"runBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.runBtn.sizePolicy().hasHeightForWidth())
        self.runBtn.setSizePolicy(sizePolicy1)
        self.runBtn.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setBold(False)
        self.runBtn.setFont(font)
        self.runBtn.setCheckable(False)
        self.runBtn.setFlat(False)

        self.horizontalLayout_3.addWidget(self.runBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.opsTabs.addTab(self.stepsTab, "")
        self.optionsTab = QWidget()
        self.optionsTab.setObjectName(u"optionsTab")
        self.optionsTab.setAutoFillBackground(True)
        self.verticalLayout_17 = QVBoxLayout(self.optionsTab)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.stepOptionsTreeWidget = QTreeWidget(self.optionsTab)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.stepOptionsTreeWidget.setHeaderItem(__qtreewidgetitem)
        self.stepOptionsTreeWidget.setObjectName(u"stepOptionsTreeWidget")

        self.verticalLayout_17.addWidget(self.stepOptionsTreeWidget)

        self.opsTabs.addTab(self.optionsTab, "")
        self.templatesTab = QWidget()
        self.templatesTab.setObjectName(u"templatesTab")
        self.verticalLayout_19 = QVBoxLayout(self.templatesTab)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.treeWidget = QTreeWidget(self.templatesTab)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem1)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout_19.addWidget(self.treeWidget)

        self.opsTabs.addTab(self.templatesTab, "")

        self.stepsLayout.addWidget(self.opsTabs)


        self.verticalLayout.addLayout(self.stepsLayout)


        self.retranslateUi(Form)

        self.assetsTabs.setCurrentIndex(0)
        self.opsTabs.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.browseDemoBtn.setText(QCoreApplication.translate("Form", u"Demo", None))
        self.browseScriptBtn.setText(QCoreApplication.translate("Form", u"Script", None))
        self.browseAudioBtn.setText(QCoreApplication.translate("Form", u"Audio", None))
        ___qtreewidgetitem = self.demoListTreeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Form", u"Script", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"Audio", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"Demo", None));
        self.infoBtn.setText(QCoreApplication.translate("Form", u"Info", None))
        self.loadScriptBtn.setText(QCoreApplication.translate("Form", u"Load Script", None))
        self.loadAudioBtn.setText(QCoreApplication.translate("Form", u"Load audio", None))
        self.removeDemoBtn.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.addDemoBtn.setText(QCoreApplication.translate("Form", u"Add Demo", None))
        self.assetsTabs.setTabText(self.assetsTabs.indexOf(self.demoList), QCoreApplication.translate("Form", u"Demo", None))
#if QT_CONFIG(tooltip)
        self.assetsTabs.setTabToolTip(self.assetsTabs.indexOf(self.demoList), QCoreApplication.translate("Form", u"Demo information", None))
#endif // QT_CONFIG(tooltip)
        self.assetsTabs.setTabText(self.assetsTabs.indexOf(self.scriptOverviewTab), QCoreApplication.translate("Form", u"Script", None))
        self.assetsTabs.setTabText(self.assetsTabs.indexOf(self.audioOverviewTab), QCoreApplication.translate("Form", u"Audio", None))
        ___qtreewidgetitem1 = self.stepsTreeWidget.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("Form", u"Target", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("Form", u"Operation", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Form", u"#", None));
        self.stepDownBtn.setText(QCoreApplication.translate("Form", u"<", None))
        self.stepUpBtn.setText(QCoreApplication.translate("Form", u">", None))
        self.removeStepBtn.setText(QCoreApplication.translate("Form", u"-", None))
        self.addStepBtn.setText(QCoreApplication.translate("Form", u"+", None))
        self.runBtn.setText(QCoreApplication.translate("Form", u"Run", None))
        self.opsTabs.setTabText(self.opsTabs.indexOf(self.stepsTab), QCoreApplication.translate("Form", u"Steps", None))
        self.opsTabs.setTabText(self.opsTabs.indexOf(self.optionsTab), QCoreApplication.translate("Form", u"Options", None))
        self.opsTabs.setTabText(self.opsTabs.indexOf(self.templatesTab), QCoreApplication.translate("Form", u"Templates", None))
    # retranslateUi

