# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'section.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QListWidget,
    QListWidgetItem, QSizePolicy, QWidget)
class Ui_Form(object):
    def setupUi(self, sectionOp):
        if not sectionOp.objectName():
            sectionOp.setObjectName(u"sectionOp")
        self.formLayout_6 = QFormLayout(sectionOp)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.sectionRulesListWidget = QListWidget(sectionOp)
        QListWidgetItem(self.sectionRulesListWidget)
        QListWidgetItem(self.sectionRulesListWidget)
        QListWidgetItem(self.sectionRulesListWidget)
        QListWidgetItem(self.sectionRulesListWidget)
        QListWidgetItem(self.sectionRulesListWidget)
        QListWidgetItem(self.sectionRulesListWidget)
        QListWidgetItem(self.sectionRulesListWidget)
        self.sectionRulesListWidget.setObjectName(u"sectionRulesListWidget")
        self.sectionRulesListWidget.setMaximumSize(QSize(16777215, 100))

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.sectionRulesListWidget)

        self.label_10 = QLabel(sectionOp)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 20))

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.label_10)

        self.sectionCoverageLabel = QLabel(sectionOp)
        self.sectionCoverageLabel.setObjectName(u"sectionCoverageLabel")
        self.sectionCoverageLabel.setMaximumSize(QSize(16777215, 20))

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.sectionCoverageLabel)

        self.label_11 = QLabel(sectionOp)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 20))

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.label_11)


        self.retranslateUi(sectionOp)

        QMetaObject.connectSlotsByName(sectionOp)
    # setupUi

    def retranslateUi(self, sectionOp):

        __sortingEnabled = self.sectionRulesListWidget.isSortingEnabled()
        self.sectionRulesListWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.sectionRulesListWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"Step has TP, next step without TP", None));
        ___qlistwidgetitem1 = self.sectionRulesListWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"Step has TP, next step with TP", None));
        ___qlistwidgetitem2 = self.sectionRulesListWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"Step has TP, previous step without TP", None));
        ___qlistwidgetitem3 = self.sectionRulesListWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Form", u"Step has TP, previous step with TP", None));
        ___qlistwidgetitem4 = self.sectionRulesListWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Form", u"Step has fade-in", None));
        ___qlistwidgetitem5 = self.sectionRulesListWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Form", u"Step has jump box", None));
        ___qlistwidgetitem6 = self.sectionRulesListWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Form", u"Step TP contains text pattern...", None));
        self.sectionRulesListWidget.setSortingEnabled(__sortingEnabled)

        self.label_10.setText(QCoreApplication.translate("Form", u"Insert new section on...", None))
        self.sectionCoverageLabel.setText(QCoreApplication.translate("Form", u"Covers 0 steps in selected sections/steps", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"May not match number of audio soundbites (audio not imported)", None))
        pass
    # retranslateUi

