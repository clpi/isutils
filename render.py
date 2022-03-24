"""
Operation to stitch together images of demo to form exported mp4 file
"""
from cv2 import VideoWriter_fourcc
from isu.utils import log
from PIL import Image
import numpy as np
# from av import VideoFormat, VideoFrame, buffer 
import cv2, pathlib, enum, os, ffmpeg, mutagen
from pathlib import WindowsPath, Path
from typing import Sequence, Optional, List, Dict, Any, Tuple
# import moviepy.editor as mpy
from isu.operation import Op
from dataclasses import dataclass
from isu.models.demo import Demo
from PyQt6.QtCore import (
    pyqtEnum, pyqtSignal, pyqtBoundSignal, pyqtSlot, QDir, QObject, QRunnable
)
from isu.models.step import Step
from isu.models.audio import Audio
from isu.models.actions.cursor import Cursor
RenderFmt = [
]

@pyqtEnum
class Format(enum.Enum):
    Mp4, Avi, Mkv, Mov, Mpv = range(4)

    def __list__(self):
        return [
            Format.Mp4,
            Format.Avi,
            Format.Mov,
            Format.Mkv,
            Format.Mpv,
        ]

    def to_codec(self):
        match self:
            case Format.Mpv:
                return cv2.VideoWriter_fourcc(*'MP42')
            case Format.Avi:
                return cv2.VideoWriter_fourcc(*'XVID')
            case Format.Mov:
                return cv2.VideoWriter_fourcc(*"x264")
            case Format.Mkv:
                return cv2.VideoWriter_fourcc(*"mk4v")
            case Format.Mpv:
                return cv2.VideoWriter_fourcc(*"mp4v")
            case _:
                return Format.Mp4.to_codec()

# def render(path: str):
#     cmd = os.path.join(os.getcwd(), "ffmpeg")
#     pass


@dataclass
class RenderContext(object):
    """
    Low-level (not user-visible) info for making context-aware render calculations
    such as animation position, relative duration to next img, etc.
    """
    animated: bool = False
    cursor: Optional[Tuple[int, int]] = None
    textbox: Optional[Textbox] = None
    highlight: Optional[Highlight] = None
    jumpbox: Optional[Jumpbox] = None
    audio: Optional[Audio] = None


@dataclass
class Render(Op):
    qprog = pyqtSignal(float)

    fps: float = 20.0
    with_audio = True
    with_cursor = True
    with_text = True
    with_hl: bool = True
    dir: Path = Path(QDir.homePath()) / "Videos"
    res: Tuple[int, int] = (1920, 1080)
    title: str = "out"
    format: Format = Format.Mp4

    def __str__(self) -> str:
        return "render"

    def run(self, demo: Demo):
        """

        """
        # TODO add sect discrim fxn
        super().run(demo)
        log("[RenderOp.run] RUNNING RENDER OP on " + demo.title)
        self.started()
        self.render_video(demo)
        self.finished()

    @property
    def path(self):
        return self.dir / Path(f"{self.title}.{self.format.name}")

    @property
    def writer(self):
        return cv2.VideoWriter(
            filename=str(self.path),
            fourcc=self.format.to_codec(),
            apiPreference=cv2.CAP_FFMPEG,
            isColor=True,
            fps=self.fps,
            frameSize=self.res,
        )


    def render_video(self, demo: Demo, verbose=False):
        """
        Renders composite of all demo's images into video using python mmpeg
        """
        log("[Demo.render_video] RUNNING render_video to path " + str(self.path))
        # imgs: List[Image] = []
        imgs: List[str] = []
        for sect_i, sect in enumerate(demo):
            for step_i, step in enumerate(sect.steps):
                if step.img is not None:
                    sd: float = 1.0
                    # hov = None
                    mouse: Cursor | None = None
                    animated = False
                    log(f"\nSECTION {str(sect_i)}, STEP {str(step_i)} info: ")
                    if step.img:
                        log("IMAGE: " + str(step.img))
                    if step.hover:
                        log("HOVER: " + str(step.hover))
                        # hov = cv2.imread(str(step.hover))
                        if step.hover_time: 
                            log("HOVER TIME: " + str(step.hover_time))
                    if step.audio:
                        log("AUDIO: " + str(step.audio))
                        au = step.audio
                    if step.animated: 
                        log("ANIMATED: " + str(step.animated))
                        # animated = True
                    if (m:=step.mouse) is not None:
                        log("MOUSE:     (" + str(m[0]) + ", " + str(m[1]) + ")")
                        mouse = Cursor((int(step.mouse[0]), int(step.mouse[1])))
                    if (mh := step.mouse_hover) is not None:
                        log("MOUSE HOV: (" + str(step.mouse_hover[0]) + ", " + str(step.mouse_hover[1]) + ")")
                    if (dl := step.delay): 
                        log("DELAY: " + str(dl), verbose)
                        sd = float(dl)
                    if step.time: 
                        log("TIME: " + str(step.time))
                    if step.transition: 
                        log("TRANSITION: " + str(step.transition))
                    if step.boxes["hotspot"]:
                        log("HOTSPOT:   (" + str(step.boxes["hotspot"]["x1"]) + ", " + str(step.boxes["hotspot"]["y1"]) + ")")
                    if step.boxes["highlight"]:
                        log("HIGHLIGHT: (" + str(step.boxes["highlight"]["x1"]) + ", " + str(step.boxes["highlight"]["y1"]) + "), color: " + str(step.boxes["highlight"]["color"]))
                    if step.boxes["text"]:
                        log("TEXT:      (" + str(step.boxes["text"]["text"]) + " (font: " + str(step.boxes["text"]["font"]) + ", size: " + str(step.boxes["text"]["size"]) + ", color: " + str(step.boxes["text"]["color"]) + ")")
                    nframes: int = round(self.fps * sd)
                    simg =  cv2.imread(str(step.img))
                    # simg = cv2.cvtColor(simg, cv2.COLOR_BGR2RGB)
                    if step.audio:
                        au = str(step.audio)
                    if mouse:
                        img = mouse.paste(simg)
                    h, w, layers = simg.shape
                    for i in range(round(nframes)):
                        imgs.append(img)
                    
                # if step.hover is not None:
                #     pass
        for i, img in enumerate(imgs):
            out.write(img)
            pct: float = (i / len(imgs)) * 100
            log("[render_video] ", pct, "% complete.")
            # self.qprog.emit(pct)
        out.release()

# def write_step(out: cv2.VideoWriter, fps: float, step: Step):
#     nframes: int = round(fps * float(step.delay.text))
#     arr = step.img
#     simg = cv2.imread(str(step.img))
#     if step.hover: 
#         shov = cv2.imread(str(step.hover))
#     h, w, layers = simg.shape
#     for j in range(round(nframes)):
#         out.write(simg)
