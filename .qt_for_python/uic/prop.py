# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prop.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QWidget)

from kurllabel import KUrlLabel

class Ui_ClipProperties_UI(object):
    def setupUi(self, ClipProperties_UI):
        if not ClipProperties_UI.objectName():
            ClipProperties_UI.setObjectName(u"ClipProperties_UI")
        ClipProperties_UI.resize(344, 720)
        self.gridLayout_2 = QGridLayout(ClipProperties_UI)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.buttonBox = QDialogButtonBox(ClipProperties_UI)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Close|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 8, 0, 1, 5)

        self.clip_duration = QLineEdit(ClipProperties_UI)
        self.clip_duration.setObjectName(u"clip_duration")

        self.gridLayout_2.addWidget(self.clip_duration, 5, 1, 1, 1)

        self.clip_path = QLineEdit(ClipProperties_UI)
        self.clip_path.setObjectName(u"clip_path")
        self.clip_path.setReadOnly(True)

        self.gridLayout_2.addWidget(self.clip_path, 2, 0, 1, 5)

        self.verticalSpacer_4 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 7, 2, 1, 2)

        self.label_path = QLabel(ClipProperties_UI)
        self.label_path.setObjectName(u"label_path")

        self.gridLayout_2.addWidget(self.label_path, 1, 0, 1, 5)

        self.clip_description = QLineEdit(ClipProperties_UI)
        self.clip_description.setObjectName(u"clip_description")

        self.gridLayout_2.addWidget(self.clip_description, 4, 0, 1, 5)

        self.label_size = QLabel(ClipProperties_UI)
        self.label_size.setObjectName(u"label_size")

        self.gridLayout_2.addWidget(self.label_size, 5, 3, 1, 1)

        self.label_duration = QLabel(ClipProperties_UI)
        self.label_duration.setObjectName(u"label_duration")

        self.gridLayout_2.addWidget(self.label_duration, 5, 0, 1, 1)

        self.clip_thumb = QLabel(ClipProperties_UI)
        self.clip_thumb.setObjectName(u"clip_thumb")
        self.clip_thumb.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.clip_thumb, 0, 0, 1, 5)

        self.clip_filesize = QLabel(ClipProperties_UI)
        self.clip_filesize.setObjectName(u"clip_filesize")

        self.gridLayout_2.addWidget(self.clip_filesize, 5, 4, 1, 1)

        self.label_description = QLabel(ClipProperties_UI)
        self.label_description.setObjectName(u"label_description")

        self.gridLayout_2.addWidget(self.label_description, 3, 0, 1, 5)

        self.clip_license = KUrlLabel(ClipProperties_UI)
        self.clip_license.setObjectName(u"clip_license")

        self.gridLayout_2.addWidget(self.clip_license, 6, 0, 1, 5)


        self.retranslateUi(ClipProperties_UI)
        self.buttonBox.accepted.connect(ClipProperties_UI.accept)
        self.buttonBox.rejected.connect(ClipProperties_UI.reject)

        QMetaObject.connectSlotsByName(ClipProperties_UI)
    # setupUi

    def retranslateUi(self, ClipProperties_UI):
        ClipProperties_UI.setWindowTitle(QCoreApplication.translate("ClipProperties_UI", u"Clip Properties", None))
        self.label_path.setText(QCoreApplication.translate("ClipProperties_UI", u"Path", None))
        self.label_size.setText(QCoreApplication.translate("ClipProperties_UI", u"Size:", None))
        self.label_duration.setText(QCoreApplication.translate("ClipProperties_UI", u"Duration", None))
        self.clip_filesize.setText(QCoreApplication.translate("ClipProperties_UI", u"File size", None))
        self.label_description.setText(QCoreApplication.translate("ClipProperties_UI", u"Description", None))
        self.clip_license.setText("")
    # retranslateUi

