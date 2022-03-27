import os, sys
from pathlib import Path
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QDir, QFile,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QTabWidget, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
from typing import Any, List

class StepsData(QWidget):

    ui: QWidget
    loader: QUiLoader

    addStepsBtn: QPushButton
    removeStepBtn: QPushButton
    stepUpBtn: QPushButton
    stepDownBtn: QPushButton

    def __init__(self, parent: None | QWidget = None):
        super(StepsData, self).__init__(parent)
        self.load_ui()
        self.setup_ui()

    def load_ui(self):
        self.loader = QUiLoader(self)
        uifile = QFile(os.path.dirname(__file__) / Path("steps.ui"))
        self.ui = self.loader.load(uifile, parentWidget=self)
        uifile.close()
        self.setup_ui()

    def load_data(self):
        self.widgets: List[str] = self.loader.availableWidgets()
        self.layouts: List[str] = self.loader.availableLayouts()
        for widgetName in self.loader.availableWidgets():
            self.loader.createWidget(widgetName, parent=self, name="")

    def setup_ui(self):
        if not self.objectName():
            self.setObjectName(u"stepsListView")
        self.resize(400, 300)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.opsTabs = QTabWidget(self)
        self.opsTabs.setObjectName(u"opsTabs")
        self.opsTabs.setEnabled(True)
        self.opsTabs.setMaximumSize(QSize(410, 16777215))
        self.stepsTab = QWidget()
        self.stepsTab.setObjectName(u"stepsTab")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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
        __qtreewidgetitem.setText(0, r"1")
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
        __qtreewidgetitem1.setText(0, r"1")
        self.treeWidget.setHeaderItem(__qtreewidgetitem1)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout_19.addWidget(self.treeWidget)

        self.opsTabs.addTab(self.templatesTab, "")

        self.verticalLayout.addWidget(self.opsTabs)


        # self.retranslateUi()

        self.opsTabs.setCurrentIndex(0)
        self.setWindowTitle("stepsListView")



        QMetaObject.connectSlotsByName(self)
        self.stepUpBtn.setText("Up")
        self.stepDownBtn.setText("Down")

    # def retranslateUi(self):
    #     self.setWindowTitle(QCoreApplication.translate(b"stepsListView", b"stepsListView", None))
    #     ___qtreewidgetitem = self.stepsTreeWidget.headerItem()
    #     ___qtreewidgetitem.setText(2, QCoreApplication.translate(b"stepsListView", b"Target", None));
    #     ___qtreewidgetitem.setText(1, QCoreApplication.translate(b"stepsListView", b"Operation", None));
    #     ___qtreewidgetitem.setText(0, QCoreApplication.translate(b"stepsListView", b"#", None));
    #     self.stepDownBtn.setText(QCoreApplication.translate(b"stepsListView", b"<", None))
    #     self.stepUpBtn.setText(QCoreApplication.translate(b"stepsListView", b">", None))
    #     self.removeStepBtn.setText(QCoreApplication.translate(b"stepsListView", b"-", None))
    #     self.addStepBtn.setText(QCoreApplication.translate(b"stepsListView", b"+", None))
    #     self.runBtn.setText(QCoreApplication.translate(b"stepsListView", b"Run", None))
    #     self.opsTabs.setTabText(self.opsTabs.indexOf(self.stepsTab), QCoreApplication.translate(b"stepsListView", b"Steps", None))
    #     self.opsTabs.setTabText(self.opsTabs.indexOf(self.optionsTab), QCoreApplication.translate(b"stepsListView", b"Options", None))
    #     self.opsTabs.setTabText(self.opsTabs.indexOf(self.templatesTab), QCoreApplication.translate(b"stepsListView", b"Templates", None))

if __name__ == "__main__":
    a = QApplication(sys.argv)
    w = StepsData()
    w.show()
    sys.exit(a.exec())