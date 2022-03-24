import os, sys, pathlib
from typing import Optional, Sequence, Dict
from PIL import Image
from PyQt6.QtCore import *
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import *
from PyQt6 import uic
from isu.models.demo import Demo
from isu.ui.ops.ops import OpUi
from isu.operation.render import Format, Render

AudioFmt = ["mp3", "wav", "flac", "ogg"]

class RenderOp(OpUi):

    @staticmethod
    def cbidx() -> int:
        return 7

    def __init__(self, parent: Optional[QWidget] = None, index:int = 0):
        super().__init__(parent)
        self.index = index
        path = os.path.join(os.path.dirname(__file__), "render.ui")
        uic.loadUi(path, self)
        self.dir = pathlib.Path(QDir.homePath()) / "Videos"
        self.title = "Demo" # TODO get from global curr sel demo
        self.fps = 24.0
        self.loadUi()

    def loadUi(self):
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

        self.renderBrowseDirBtn.clicked.connect(self.browse_dir)

    @pyqtSlot(str, name="renderSetDir")
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
        return RenderFmt[sel]

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

    def run(self):
            print("DIR: " + self.renderOutputDir.text() + ", TITLE: " + self.renderOutputTitle.text())
    #         out_title = self.renderOutputTitle.text()
    #         out_dir = Path(self.renderOutputDir.text())
    #         out_format = "avi"
    #         if out_dir.is_dir():
    #             out_path = os.path.join(out_dir, out_title + "." + out_format)
    #             print("OUTPATH: " + out_path)
    #             # out_path: str = self.renderOutputDir.text() + "\\" + self.renderOutputTitle.text()
    #             if (d := self.demo) is not None:
    #                 return Render(out_path=pathlib.Path(out_path)).run(demo)
    #         else:
    #             print("NOT VALID DIR")
