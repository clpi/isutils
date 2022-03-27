import os, sys

from typing import Any
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QDir,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLayout,
    QMainWindow,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)
from ..ui import UiLoad

class CentralWidget(QWidget):
    ui: QWidget
    centralTabs: QTabWidget
    scriptsPage: QWidget
    productionPage: QWidget
    demoPage: QWidget

    def __init__(self, parent: Any):
        QWidget.__init__(parent)
        uidir = QDir(os.path.dirname(__file__))
        uiload = UiLoad(name="tabs.ui",dir=uidir, parent=parent)
        self.ui: QWidget = uiload.load_ui()
        self.setupUi(parent)



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


        self.centralTabs.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(centralWiget)

if __name__ == "__main__":
    QApplication(sys.argv)
    nw = QMainWindow()
    c = CentralWidget(nw)
    nw.setCentralWidget(widget=c)
    c.show()
    QApplication.exec()
    # setupUi
