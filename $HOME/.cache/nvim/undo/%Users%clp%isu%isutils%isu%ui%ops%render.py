Vim�UnDo� �1�y�A�"gL�XDf��������$a��   d                                  b;-    _�                             ����                                                                                                                                                                                                                                                                                                                                                             b:��     �         j    5��                          g                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             b:��     �         k          5��                         k                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             b:��    �         k          Format.Mkv5��                         f                     5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             b:��     �         l       �         k    5��                          z                     �                          z                     �                          {                     5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             b:�     �         m      AudioFmt = 5��                         �                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             b:�     �         m      AudioFmt = []5��                         �                     5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             b:�     �         m      AudioFmt = [""]5��                         �                     �                        �                    �                         �                     5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             b:�     �         m      AudioFmt = ["mp3", ]5��                         �                     5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             b:�     �         m      AudioFmt = ["mp3", ""]5��                         �                     �                        �                    �                         �                     �                         �                     �                         �                     5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             b:�	    �         m      AudioFmt = ["mp3", "w�         m    5��                         �                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             b:޿     �               m   import os, sys   import pathlib   +from typing import Optional, Sequence, Dict   from PIL import Image   from PyQt6.QtCore import *   Cfrom PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,   +    QFont, QFontDatabase, QGradient, QIcon,   4    QImage, QKeySequence, QLinearGradient, QPainter,   3    QPalette, QPixmap, QRadialGradient, QTransform)   from PyQt6.QtGui import QAction   from PyQt6.QtWidgets import *   from PyQt6 import uic    from isu.models.demo import Demo   from isu.ui.ops.ops import OpUi   /from isu.operation.render import Format, Render       RenderFmt = [       Format.Mp4,       Format.Avi,       Format.Mov,       Format.Mkv,       Format.Mpv,   ]       (AudioFmt = ["mp3", "wav", "flac", "ogg"]       class RenderOp(OpUi):           @staticmethod       def cbidx() -> int:           return 7       H    def __init__(self, parent: Optional[QWidget] = None, index:int = 0):            super().__init__(parent)           self.index = index   C        path = os.path.join(os.path.dirname(__file__), "render.ui")           uic.loadUi(path, self)   ;        self.dir = pathlib.Path(QDir.homePath()) / "Videos"   @        self.title = "Demo" # TODO get from global curr sel demo           self.fps = 24.0           self.loadUi()           def loadUi(self):   &        self.renderTabTabs: QTabWidget   )        self.renderOutputTitle: QLineEdit   *        self.renderOutputFormat: QComboBox   !        self.renderResH: QSpinBox   !        self.renderResW: QSpinBox   (        self.renderFpsSb: QDoubleSpinBox       '        self.withCursorCheck: QCheckBox   &        self.withAudioCheck: QCheckBox   %        self.withTextCheck: QCheckBox       ,        self.renderBrowseDirBtn: QPushButton   '        self.renderOutputDir: QLineEdit       @        self.renderBrowseDirBtn.clicked.connect(self.browse_dir)       '    @pyqtSlot(str, name="renderSetDir")        def set_dir(self, dir: str):   )        self.renderOutputDir.setText(dir)       0    def browse_dir(self) -> pathlib.Path | None:           try:   S            odir = QFileDialog.getExistingDirectory(self,"Select output directory")               self.set_dir(odir)   %            return pathlib.Path(odir)           except:               return None                      def fmt(self) -> Format:   4        sel = self.renderOutputFormat.currentIndex()           return RenderFmt[sel]       )    def outputPath(self) -> pathlib.Path:   )        dir = self.renderOutputDir.text()   -        title = self.renderOutputTitle.text()   U        return pathlib.Path(os.path.join(dir, title + "." + self.fmt().name.lower()))       !    def set_rtitle(self, t: str):   %        self.renderOutputTitleStr = t           def op(self) -> Render:           return Render(   C            res=(self.renderResH.value(), self.renderResW.value()),   )            fps=self.renderFpsSb.value(),   :            dir=pathlib.Path(self.renderOutputDir.text()),               format=self.fmt(),   0            title=self.renderOutputTitle.text(),   6            # with_audio=self.withAudioCb.isChecked(),   8            # with_cursor=self.withCursorCb.isChecked(),   4            # with_text=self.withTextCb.isChecked(),   	        )           # def run(self):    h    #         print("DIR: " + self.renderOutputDir.text() + ", TITLE: " + self.renderOutputTitle.text())   7    #         out_title = self.renderOutputTitle.text()   9    #         out_dir = Path(self.renderOutputDir.text())        #         out_format = "avi"   "    #         if out_dir.is_dir():   P    #             out_path = os.path.join(out_dir, out_title + "." + out_format)   /    #             print("OUTPATH: " + out_path)   f    #             # out_path: str = self.renderOutputDir.text() + "\\" + self.renderOutputTitle.text()   2    #             if (d := self.demo) is not None:   N    #                 return Render(out_path=pathlib.Path(out_path)).run(demo)       #         else:   (    #             print("NOT VALID DIR")5�5�_�                            ����                                                                                                                                                                                                                                                                                                                                                 V       b:��     �                RenderFmt = [       Format.Mp4,       Format.Avi,       Format.Mov,       Format.Mkv,       Format.Mpv,   ]    5��                                a               5�_�                    Y       ����                                                                                                                                                                                                                                                                                                                            Y          Y          V   Q    b;     �   X   Z   e          # def run(self): 5��    X                     %                    5�_�                    Z       ����                                                                                                                                                                                                                                                                                                                            Y          Y          V   Q    b;     �   Y   [   e      h    #         print("DIR: " + self.renderOutputDir.text() + ", TITLE: " + self.renderOutputTitle.text())5��    Y                     8      i       g       5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       b;)     �          e      import os, sys5��                       	                  	       5�_�                            ����                                                                                                                                                                                                                                                                                                                                                v       b;,    �                import pathlib5��                                                5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             b:�     �              5��                          �                     5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                                             b:�     �              5��                          {                     5��