from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QDir,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTabWidget,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
import sys, os
from isu.ui import UiLoad

class DataLoaded(QWidget):
    def __init__(self, parent: QWidget | None) -> None:
        QWidget.__init__(self, parent)
        UiLoad().loadUi("steps.ui", self, parent)

    uifile = QDir(os.path.dirname(os.path.realpath(__file__)))
    def setupUi(self, dataLoaded):
        if not dataLoaded.objectName():
            dataLoaded.setObjectName("dataLoaded")
        dataLoaded.resize(400, 301)
        self.verticalLayout = QVBoxLayout(dataLoaded)
        self.verticalLayout.setObjectName("verticalLayout")
        self.assetsTabs = QTabWidget(dataLoaded)
        self.assetsTabs.setObjectName("assetsTabs")
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
        self.demoList.setObjectName("demoList")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.demoList.sizePolicy().hasHeightForWidth())
        self.demoList.setSizePolicy(sizePolicy)
        self.verticalLayout_11 = QVBoxLayout(self.demoList)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.browseDemoBtn = QPushButton(self.demoList)
        self.browseDemoBtn.setObjectName("browseDemoBtn")

        self.horizontalLayout_10.addWidget(self.browseDemoBtn)

        self.browseScriptBtn = QPushButton(self.demoList)
        self.browseScriptBtn.setObjectName("browseScriptBtn")

        self.horizontalLayout_10.addWidget(self.browseScriptBtn)

        self.browseAudioBtn = QPushButton(self.demoList)
        self.browseAudioBtn.setObjectName("browseAudioBtn")

        self.horizontalLayout_10.addWidget(self.browseAudioBtn)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)


        self.verticalLayout_11.addLayout(self.verticalLayout_12)

        self.demoListTreeWidget = QTreeWidget(self.demoList)
        self.demoListTreeWidget.setObjectName("demoListTreeWidget")

        self.verticalLayout_11.addWidget(self.demoListTreeWidget)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.infoBtn = QPushButton(self.demoList)
        self.infoBtn.setObjectName("infoBtn")

        self.horizontalLayout_11.addWidget(self.infoBtn)

        self.loadScriptBtn = QPushButton(self.demoList)
        self.loadScriptBtn.setObjectName("loadScriptBtn")

        self.horizontalLayout_11.addWidget(self.loadScriptBtn)

        self.loadAudioBtn = QPushButton(self.demoList)
        self.loadAudioBtn.setObjectName("loadAudioBtn")

        self.horizontalLayout_11.addWidget(self.loadAudioBtn)

        self.removeDemoBtn = QPushButton(self.demoList)
        self.removeDemoBtn.setObjectName("removeDemoBtn")

        self.horizontalLayout_11.addWidget(self.removeDemoBtn)

        self.addDemoBtn = QPushButton(self.demoList)
        self.addDemoBtn.setObjectName("addDemoBtn")

        self.horizontalLayout_11.addWidget(self.addDemoBtn)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.assetsTabs.addTab(self.demoList, "")
        self.scriptOverviewTab = QWidget()
        self.scriptOverviewTab.setObjectName("scriptOverviewTab")
        self.verticalLayout_13 = QVBoxLayout(self.scriptOverviewTab)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.scriptListTreeWidget = QListWidget(self.scriptOverviewTab)
        self.scriptListTreeWidget.setObjectName("scriptListTreeWidget")

        self.verticalLayout_13.addWidget(self.scriptListTreeWidget)

        self.assetsTabs.addTab(self.scriptOverviewTab, "")
        self.audioOverviewTab = QWidget()
        self.audioOverviewTab.setObjectName("audioOverviewTab")
        self.verticalLayout_15 = QVBoxLayout(self.audioOverviewTab)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.audioListTreeWidget = QListWidget(self.audioOverviewTab)
        self.audioListTreeWidget.setObjectName("audioListTreeWidget")

        self.verticalLayout_15.addWidget(self.audioListTreeWidget)

        self.assetsTabs.addTab(self.audioOverviewTab, "")

        self.verticalLayout.addWidget(self.assetsTabs)


        self.retranslateUi(dataLoaded)

        self.assetsTabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(dataLoaded)
    # setupUi

    def retranslateUi(self, dataLoaded):
        dataLoaded.setWindowTitle(QCoreApplication.translate(b"dataLoaded", b"Form", None))
        self.browseDemoBtn.setText(QCoreApplication.translate(b"dataLoaded", b"Demo", None))
        self.browseScriptBtn.setText(QCoreApplication.translate(b"dataLoaded", b"Script", None))
        self.browseAudioBtn.setText(QCoreApplication.translate(b"dataLoaded", b"Audio", None))
        ___qtreewidgetitem = self.demoListTreeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate(b"dataLoaded", b"Script", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate(b"dataLoaded", b"Audio", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate(b"dataLoaded", b"Demo", None));
        self.infoBtn.setText(QCoreApplication.translate(b"dataLoaded", b"Info", None))
        self.loadScriptBtn.setText(QCoreApplication.translate(b"dataLoaded", b"Load Script", None))
        self.loadAudioBtn.setText(QCoreApplication.translate(b"dataLoaded", b"Load audio", None))
        self.removeDemoBtn.setText(QCoreApplication.translate(b"dataLoaded", b"Remove", None))
        self.addDemoBtn.setText(QCoreApplication.translate(b"dataLoaded", b"Add Demo", None))
        self.assetsTabs.setTabText(self.assetsTabs.indexOf(self.demoList), QCoreApplication.translate(b"dataLoaded", b"Demo", None))
#if QT_CONFIG(tooltip)
        self.assetsTabs.setTabToolTip(self.assetsTabs.indexOf(self.demoList), QCoreApplication.translate(b"dataLoaded", b"Demo information", None))
#endif // QT_CONFIG(tooltip)
        self.assetsTabs.setTabText(self.assetsTabs.indexOf(self.scriptOverviewTab), QCoreApplication.translate(b"dataLoaded", b"Script", None))
        self.assetsTabs.setTabText(self.assetsTabs.indexOf(self.audioOverviewTab), QCoreApplication.translate(b"dataLoaded", b"Audio", None))
    # retranslateUi

