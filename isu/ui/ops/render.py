from operator import getitem
import os, sys, pathlib
from typing import Optional, Sequence, Dict, Any
from PIL import Image
from PySide6.QtCore import *
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtGui import QAction
from PySide6.QtWidgets import *
from PySide6 import QtUiTools
from isu.models.demo import Demo
from isu.ui import UiLoad
from isu.ui.ops.ops import OpUi
from isu.operation.render import Format, Render

AudioFmt = ["mp3", "wav", "flac", "ogg"]

class RenderOp(OpUi, QWidget):

    started = Signal(Render)

    def __init__(self, parent: QWidget | None) -> None:
        QWidget.__init__(self, parent)
        UiLoad().loadUi("render.ui", self, parent)
        self.load_tabs()

    def load_tabs(self):
        self.load_data_tab()

    def load_data_tab(self):
        self.renderTabTabs: QTabWidget
        self.renderOutputTitle: QLineEdit
        self.renderOutputFormat: QComboBox
        self.renderResH: QSpinBox
        self.renderResW: QSpinBox
        self.renderFpsSb: QDoubleSpinBox

        self.withCursorCheck: QCheckBox
        self.withAudioCheck: QCheckBox
        self.withTextCheck: QCheckBox

        self.renderBrowseDirBtn: QPushButton
        self.renderOutputDir: QLineEdit

        self.renderBrowseDirBtn.toggle.connect(self.browse_dir)


    @Slot(str, name="renderSetDir")
    def set_dir(self, dir: str):
        self.renderOutputDir.setText(dir)

    def browse_dir(self) -> pathlib.Path | None:
        try:
            odir = QFileDialog.getExistingDirectory(self,"Select output directory")
            self.set_dir(odir)
            return pathlib.Path(odir)
        except:
            return None

        
    def fmt(self) -> Format:
        sel = self.renderOutputFormat.currentIndex()
        return Format(sel)

    def outputPath(self) -> pathlib.Path:
        dir = self.renderOutputDir.text()
        title = self.renderOutputTitle.text()
        return pathlib.Path(os.path.join(dir, title + "." + self.fmt().name.lower()))

    def set_rtitle(self, t: str):
        self.renderOutputTitleStr = t

    def op(self) -> Render:
        return Render(
            res=(self.renderResH.value(), self.renderResW.value()),
            fps=self.renderFpsSb.value(),
            dir=pathlib.Path(self.renderOutputDir.text()),
            format=self.fmt(),
            title=self.renderOutputTitle.text(),
            # with_audio=self.withAudioCb.isChecked(),
            # with_cursor=self.withCursorCb.isChecked(),
            # with_text=self.withTextCb.isChecked(),
        )

    Slot()
    def on_beginning_op(self):
        self.started.emit()


    @staticmethod
    def cbidx() -> int:
        return 7

