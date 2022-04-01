from PySide6.QtMultimedia import QVideoFrame, QVideoSink, QVideoFrameFormat, QAudio
from PySide6.QtMultimediaWidgets import QVideoWidget, QGraphicsVideoItem
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtCore import *
from qtpy.QtGui import QAccessibleTextInsertEvent

class DemoRenderVideo(QVideoSink):
    def __init__(self, parent = None) -> None:
        super(DemoRenderVideo).__init__(parent)

class DemoRenderFrame(QVideoFrame):
    def __init__(self, parent=None):
        super(DemoRenderFrame, self).__init__(parent)
        self.parent = parent

    