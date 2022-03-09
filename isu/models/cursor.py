from operator import setitem
from PyQt6.QtCore import QObject
from pathlib import Path
from typing import Any, Tuple
import PIL.Image as PImg
import cv2
import numpy as np

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
            self.img = cv2.imread(str(CURSOR_LG), -1)
            self.size = (48, 48)
        else: 
            self.img= cv2.imread(str(CURSOR_SM), -1)
            self.size = (24, 24)

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