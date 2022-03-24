import numpy as np
from typing import Tuple, List, Union, Callable, Any
from isu.operation.render import Format,Render,render
import cv2

def main(): 
    im = np.zeros((512,512,3), dtype=np.uint8)
    h, w = im.shape
    cv2.imshow(im)


def rvid(fps: float = 24.0,
        imgs: str|None = None,
        outd: str = "~/",
        name: str = "out",
        path: str = "~/out.vid",
        len: float = 5.0,
        res: Tuple[int, int] = (512, 512),
        fmt: Format = Format.Mp4
        ) -> cv2.VideoWriter:
    out = cv2.VideoWriter(

            )
    return out


if __name__ == "__main__": 
    main()
