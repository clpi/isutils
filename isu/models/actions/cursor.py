from dataclasses import dataclass
from operator import setitem
from pathlib import Path
from PIL import Image
import cv2
import numpy as np
from enum import Enum
from typing import List, Optional, Tuple
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtEnum


@pyqtEnum
class EasingFn(Enum):
    """
    An easing function.
    """
    LINEAR = 0
    EASE_IN = 1
    EASE_OUT = 2
    EASE_IN_OUT = 3
    QUADRATIC = 4
    CUBIC = 5
    QUARTIC = 6

@dataclass
class Easing(QObject):
    easing_fn: EasingFn
    curr_t: float = 0.0
    curr_pos: Tuple[float, float] = (0.0, 0.0)
    lim_t: Optional[float] = None
    lim_pos: Optional[Tuple[float, float]] = None

    def t_at_pos(self, pos: Tuple[float, float] = (0.0, 0.0)) -> float:
        """
        Get the time of the easing function at position pos.
        """
        t = 0.0
        cpos = self.curr_pos

        match self.easing_fn:
            case EasingFn.LINEAR: t = pos
            case EasingFn.EASE_IN: t = pos * pos
            case EasingFn.EASE_OUT:
                t = self.curr_t * (2.0 - self.curr_t)
            case EasingFn.EASE_IN_OUT:
                t = self.curr_t * self.curr_t * (2.0 - self.curr_t)
            case EasingFn.QUADRATIC:
                pass
            case EasingFn.CUBIC:
                pass
            case EasingFn.QUARTIC:
                pass
        return t

    def pos_at_t(self, t: float = 0.0) -> float:
        """
        Get the position of the easing function at time t.
        """
        x, y = 0.0, 0.0
        match self.easing_fn:
            case EasingFn.LINEAR: pos = t
            case EasingFn.EASE_IN: pos = t * t
            case EasingFn.EASE_OUT: pos = t * (2 - t)
            case EasingFn.EASE_IN_OUT:
                if t < 0.5:
                    pos = 2 * t * t
                else:
                    pos = -2 * t * t + 4 * t - 1
            case EasingFn.QUADRATIC: pos = t * t
            case EasingFn.CUBIC: pos = t * t * t
            case EasingFn.QUARTIC: pos = t * t * t * t


@dataclass
class Cursor(QObject):
    large: bool = False
    pos: Tuple[int, int]



@dataclass
class CursorMove(QObject):
    orig: Optional[Cursor] = None
    dest: Optional[Cursor] = None
    easing_fn: Optional[str] = None
    animation: any = []

    @property
    def dist(self):
        return np.linalg.norm(self.orig.pos - self.dest.pos)

    def set_easing(self, easing_fn: EasingFn):
        pass


CURSOR_LG: Path = Path(__file__).parent.parent.parent / "res" / "icons8-cursor-48.png"
CURSOR_LG_ABS: Path = Path(r"C:\Users\chris\is\isutils\res\icons8-cursor-48.png")

CURSOR_SM: Path = Path(__file__).parent.parent.parent / "res" / "icons8-cursor-24.png"
CURSOR_SM_ABS: Path = Path(r"C:\Users\chris\is\isutils\res\icons8-cursor-24.png")

class Cursor(QObject):
    def __init__(self, pos: Tuple[int, int] = (0, 0), large: bool = False):
        # super().__init__()
        self.pos: Tuple[int, int] = pos
        self.size: Tuple[int, int]
        if large: 
            self.size = (48, 48)
            self.img = cv2.imread(CURSOR_LG, -1) # type: ignore
        else: 
            self.img= cv2.imread(CURSOR_SM, -1) # type: ignore
            self.size = (24, 24)

    def set_dest(self, dest: Tuple[int, int]):
        self.dest = dest

    def set_orig(self, orig: Tuple[int, int]):
        self.pos = orig

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def get_pos(self) -> Tuple[int, int]:
        return self.pos

    def set_pos(self, pos: Tuple[int, int]):
        self.pos = pos

    @property
    def x(self) -> int:
        return self.pos[0]

    @property
    def y(self) -> int:
        return self.pos[1]

    def setx(self, x: int):
        self.pos = (x, self.y)

    def array(self)-> np.ndarray:
        return np.asarray(self.img)

    def overlay_image_alpha(self, img):
        alpha_mask = self.img[:, :, 3] / 255.0
        x, y = self.get_pos()

        # Image ranges
        y1, y2 = max(0, y), min(img.shape[0], y + self.img.shape[0])
        x1, x2 = max(0, x), min(img.shape[1], x + self.img.shape[1])

        # Overlay ranges
        y1o, y2o = max(0, -y), min(self.img.shape[0], img.shape[0] - y)
        x1o, x2o = max(0, -x), min(self.img.shape[1], img.shape[1] - x)

        # Exit if nothing to do
        if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
            return

        # Blend overlay within the determined ranges
        img_crop = img[y1:y2, x1:x2]
        img_overlay_crop = self.img[y1o:y2o, x1o:x2o]
        alpha = alpha_mask[y1o:y2o, x1o:x2o, np.newaxis]
        alpha_inv = 1.0 - alpha

        # img_crop[:] = alpha * img_overlay_crop + alpha_inv * img_crop
        return img_crop[:, :, :3]
        # return img_crop

    def paste(self, img: Any) -> Any:
        # simg = self.img
        # limg = img
        # x1, x2 = max(0, self.x), self.x + self.size[0]
        # y1, y2 = max(0, self.y), self.y + self.size[1]
        # asm = self.img[:, :, 3] / 255.0
        # alg = 1.0 - asm
        # for c in range(0, 3):
        #     limg[y1:y2, x1:x2, c] = (asm * self.img[:, :, c] + alg * limg[y1:y2, x1:x2, c])
        # return self.overlay_image_alpha(img)
        return img
        # return limg
