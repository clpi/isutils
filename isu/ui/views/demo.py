# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoHtgYss.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QStackedWidget, QToolButton,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_demoView(object):
    def setupUi(self, demoView):
        if not demoView.objectName():
            demoView.setObjectName(u"demoView")
        demoView.resize(570, 550)
        self.verticalLayout_2 = QVBoxLayout(demoView)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.demoViewGroupBox = QGroupBox(demoView)
        self.demoViewGroupBox.setObjectName(u"demoViewGroupBox")
        self.demoViewGroupBox.setFlat(True)
        self.verticalLayout_6 = QVBoxLayout(self.demoViewGroupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.demoTreeView = QTreeWidget(self.demoViewGroupBox)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Step");
        self.demoTreeView.setHeaderItem(__qtreewidgetitem)
        self.demoTreeView.setObjectName(u"demoTreeView")

        self.verticalLayout_6.addWidget(self.demoTreeView)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.demoDuplicateBtn = QPushButton(self.demoViewGroupBox)
        self.demoDuplicateBtn.setObjectName(u"demoDuplicateBtn")

        self.horizontalLayout_5.addWidget(self.demoDuplicateBtn)

        self.demoInsertSectionBtn = QPushButton(self.demoViewGroupBox)
        self.demoInsertSectionBtn.setObjectName(u"demoInsertSectionBtn")

        self.horizontalLayout_5.addWidget(self.demoInsertSectionBtn)

        self.demoDeleteBtn = QPushButton(self.demoViewGroupBox)
        self.demoDeleteBtn.setObjectName(u"demoDeleteBtn")

        self.horizontalLayout_5.addWidget(self.demoDeleteBtn)

        self.demoAddStepBtn = QPushButton(self.demoViewGroupBox)
        self.demoAddStepBtn.setObjectName(u"demoAddStepBtn")

        self.horizontalLayout_5.addWidget(self.demoAddStepBtn)

        self.demoOverflowBtn = QToolButton(self.demoViewGroupBox)
        self.demoOverflowBtn.setObjectName(u"demoOverflowBtn")

        self.horizontalLayout_5.addWidget(self.demoOverflowBtn)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.demoViewGroupBox)

        self.metadataGroupBox = QGroupBox(demoView)
        self.metadataGroupBox.setObjectName(u"metadataGroupBox")
        self.metadataGroupBox.setMaximumSize(QSize(16777215, 300))
        self.metadataGroupBox.setFlat(True)
        self.metadataGroupBox.setCheckable(False)
        self.verticalLayout_8 = QVBoxLayout(self.metadataGroupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(4, 4, 4, 4)
        self.dataStack = QStackedWidget(self.metadataGroupBox)
        self.dataStack.setObjectName(u"dataStack")
        self.stepDataL = QWidget()
        self.stepDataL.setObjectName(u"stepDataL")
        self.verticalLayout_14 = QVBoxLayout(self.stepDataL)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.metadataTreeWidget = QTreeWidget(self.stepDataL)
        self.metadataTreeWidget.setObjectName(u"metadataTreeWidget")

        self.verticalLayout_14.addWidget(self.metadataTreeWidget)

        self.stepDataBtnL = QHBoxLayout()
        self.stepDataBtnL.setObjectName(u"stepDataBtnL")
        self.pushButton_2 = QPushButton(self.stepDataL)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.stepDataBtnL.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.stepDataL)
        self.pushButton.setObjectName(u"pushButton")

        self.stepDataBtnL.addWidget(self.pushButton)

        self.toolButton = QToolButton(self.stepDataL)
        self.toolButton.setObjectName(u"toolButton")

        self.stepDataBtnL.addWidget(self.toolButton)


        self.verticalLayout_14.addLayout(self.stepDataBtnL)

        self.dataStack.addWidget(self.stepDataL)
        self.sectDataL = QWidget()
        self.sectDataL.setObjectName(u"sectDataL")
        self.verticalLayout_16 = QVBoxLayout(self.sectDataL)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.sectionDataTreeW = QTreeWidget(self.sectDataL)
        self.sectionDataTreeW.setObjectName(u"sectionDataTreeW")

        self.verticalLayout_16.addWidget(self.sectionDataTreeW)

        self.sectionDataBtnL = QHBoxLayout()
        self.sectionDataBtnL.setObjectName(u"sectionDataBtnL")
        self.pushButton_4 = QPushButton(self.sectDataL)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.sectionDataBtnL.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.sectDataL)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.sectionDataBtnL.addWidget(self.pushButton_3)

        self.pushButton_5 = QPushButton(self.sectDataL)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.sectionDataBtnL.addWidget(self.pushButton_5)

        self.toolButton_2 = QToolButton(self.sectDataL)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.sectionDataBtnL.addWidget(self.toolButton_2)


        self.verticalLayout_16.addLayout(self.sectionDataBtnL)

        self.dataStack.addWidget(self.sectDataL)

        self.verticalLayout_8.addWidget(self.dataStack)


        self.verticalLayout_2.addWidget(self.metadataGroupBox)


        self.retranslateUi(demoView)

        self.dataStack.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(demoView)
    # setupUi

    def retranslateUi(self, demoView):
        demoView.setWindowTitle(QCoreApplication.translate("demoView", u"Form", None))
        self.demoViewGroupBox.setTitle(QCoreApplication.translate("demoView", u"Demo (None loaded)", None))
        ___qtreewidgetitem = self.demoTreeView.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("demoView", u"CI", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("demoView", u"TP", None));
        self.demoDuplicateBtn.setText(QCoreApplication.translate("demoView", u"Duplicate", None))
        self.demoInsertSectionBtn.setText(QCoreApplication.translate("demoView", u"Insert section", None))
        self.demoDeleteBtn.setText(QCoreApplication.translate("demoView", u"-", None))
        self.demoAddStepBtn.setText(QCoreApplication.translate("demoView", u"+", None))
        self.demoOverflowBtn.setText(QCoreApplication.translate("demoView", u"...", None))
        self.metadataGroupBox.setTitle(QCoreApplication.translate("demoView", u"Metadata", None))
        ___qtreewidgetitem1 = self.metadataTreeWidget.headerItem()
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("demoView", u"Value", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("demoView", u"Property", None));
        self.pushButton_2.setText(QCoreApplication.translate("demoView", u"Set animated", None))
        self.pushButton.setText(QCoreApplication.translate("demoView", u"Add highlight", None))
        self.toolButton.setText(QCoreApplication.translate("demoView", u"...", None))
        ___qtreewidgetitem2 = self.sectionDataTreeW.headerItem()
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("demoView", u"Value", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("demoView", u"Property", None));
        self.pushButton_4.setText(QCoreApplication.translate("demoView", u"Set Animated", None))
        self.pushButton_3.setText(QCoreApplication.translate("demoView", u"Set Guided", None))
        self.pushButton_5.setText(QCoreApplication.translate("demoView", u"Set Scroll", None))
        self.toolButton_2.setText(QCoreApplication.translate("demoView", u"...", None))
    # retranslateUi

