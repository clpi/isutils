from ctypes import Union
from typing import Optional, Tuple
import cv2
import ffmpeg
from PIL import Image
import subprocess, tempfile
import io
from pathlib import WindowsPath, Path
from typing import Sequence
import numpy as np
import PIL

class Video:
    dur: int = 0
    fps: int = 24
    # clips: Sequence[av.container.Container]
    res: Tuple[int, int] = (1920, 1080)
    len: int = dur * fps
    pixf: str = 'yuv420p'
    raw: io.BytesIO = io.BytesIO()
    # fmt: av.VideoFormat

    def __init__(self, iimg: Optional[WindowsPath] = None):
        # self.st = av.open()
        # self.st.codec_context.thread_type = "AUTO"

        # self.f = f = av.open(
        #     rate=self.fps, 
        #     width=self.res[0], 
        #     height=self.res[1], 
        #     format=self.pixf
        # )
        # if iimg: self.st = av.open(iimg)
        pass

class VideoStep:
    # f: av.VideoFrame = av.VideoFrame(1920, 1080, 'rgb24')
    f: int

class Img:
    def __init__(self, path: str | Path):
        pass
