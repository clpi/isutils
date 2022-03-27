# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoKrSzmt.ui'
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
    QPushButton, QSizePolicy, QStackedWidget, QTabWidget,
    QToolButton, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(403, 803)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.viewTabs = QTabWidget(Form)
        self.viewTabs.setObjectName(u"viewTabs")
        self.viewTabs.setDocumentMode(False)
        self.viewTabs.setMovable(True)
        self.demoView = QWidget()
        self.demoView.setObjectName(u"demoView")
        self.verticalLayout_9 = QVBoxLayout(self.demoView)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.demoViewGroupBox = QGroupBox(self.demoView)
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


        self.verticalLayout_9.addWidget(self.demoViewGroupBox)

        self.dataFrame = QGroupBox(self.demoView)
        self.dataFrame.setObjectName(u"dataFrame")
        self.dataFrame.setMaximumSize(QSize(16777215, 300))
        self.dataFrame.setFlat(True)
        self.dataFrame.setCheckable(False)
        self.verticalLayout_8 = QVBoxLayout(self.dataFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(4, 4, 4, 4)
        self.dataStack = QStackedWidget(self.dataFrame)
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


        self.verticalLayout_9.addWidget(self.dataFrame)

        self.viewTabs.addTab(self.demoView, "")
        self.objectViewTabWPage2_2 = QWidget()
        self.objectViewTabWPage2_2.setObjectName(u"objectViewTabWPage2_2")
        self.viewTabs.addTab(self.objectViewTabWPage2_2, "")

        self.verticalLayout.addWidget(self.viewTabs)


        self.retranslateUi(Form)

        self.viewTabs.setCurrentIndex(0)
        self.dataStack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.demoViewGroupBox.setTitle(QCoreApplication.translate("Form", u"Demo (None loaded)", None))
        ___qtreewidgetitem = self.demoTreeView.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Form", u"CI", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"TP", None));
        self.demoDuplicateBtn.setText(QCoreApplication.translate("Form", u"Duplicate", None))
        self.demoInsertSectionBtn.setText(QCoreApplication.translate("Form", u"Insert section", None))
        self.demoDeleteBtn.setText(QCoreApplication.translate("Form", u"-", None))
        self.demoAddStepBtn.setText(QCoreApplication.translate("Form", u"+", None))
        self.demoOverflowBtn.setText(QCoreApplication.translate("Form", u"...", None))
        self.dataFrame.setTitle(QCoreApplication.translate("Form", u"Metadata", None))
        ___qtreewidgetitem1 = self.metadataTreeWidget.headerItem()
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("Form", u"Value", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Form", u"Property", None));
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Set animated", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Add highlight", None))
        self.toolButton.setText(QCoreApplication.translate("Form", u"...", None))
        ___qtreewidgetitem2 = self.sectionDataTreeW.headerItem()
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("Form", u"Value", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Form", u"Property", None));
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Set Animated", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Set Guided", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Set Scroll", None))
        self.toolButton_2.setText(QCoreApplication.translate("Form", u"...", None))
        self.viewTabs.setTabText(self.viewTabs.indexOf(self.demoView), QCoreApplication.translate("Form", u"Info", None))
        self.viewTabs.setTabText(self.viewTabs.indexOf(self.objectViewTabWPage2_2), QCoreApplication.translate("Form", u"Preview", None))
    # retranslateUi

