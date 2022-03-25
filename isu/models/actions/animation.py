from dataclasses import dataclass, field
from operator import setitem
from isu.models.step import Step
from isu.models.section import Section
from isu.models.audio import Audio, SoundBite
from pathlib import Path
from PIL import Image
import cv2
import numpy as np
from enum import Enum
from typing import List, Optional, Tuple, Dict
from PySide6.QtCore import (
    QItemSelection, QItemSelectionModel, QItemSelectionRange,
    QObject, Signal, Slot, QEnum,
    QRect, QRectF, QSize, QSizeF, QPoint, QPointF, QLine, QLineF,
    QSaveFile, QThread, QBuffer, QUuid, QUrl, QDir, QEnum, QEasingCurve,
    QTime, QTimeLine, QTimer, QTimerEvent,QElapsedTimer,
    QSequentialAnimationGroup, QAnimationGroup, QParallelAnimationGroup,
)

@dataclass
class Time(object):
    """
    Enum for the time of the animation.
    """
    # elapsed = QElapsedTimer()
    t: float
    end: bool = False

    def __init__(self, t: float = 0.0, end: bool = False):
        self.t = t
        self.elapsed = QElapsedTimer().
        self.end = end


@QEnum
class EasingFn(Enum, QItemSelection):
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

    @dataclass
    class Path(object):

        pos: QPointF
        frame_i: int = 0
        time_i: float = 0.0
        easing: QEasingCurve.Type = QEasingCurve.Type.Linear
        path: QLineF = field(default_factory=QLineF((0.0, 0.0), (0.0, 0.0)))
        frames: List[QPointF] = field(default_factory=list)
        time_max: None | float = 1.0

        def __init__(
                    self, 
                    p1=QPointF(0.0, 0.0),
                    p2=QPointF(0.0, 0.0),
                    res=QSize(1920, 1080),
                    fps=24.0,
                    ease=QEasingCurve.Type.Linear,
                    tmax: None | float = 1.0,
                    ) -> None:
            self.from_line(QLineF(p1, p2), res, fps, ease, tmax)

        def from_ln(self,
                    line: QLineF,
                    res: QSize,
                    fps: float,
                    ease: QEasingCurve.Type,
                    tmax: float | None = None
                    ):
            self.start()
            self.path = ln
            self.res = res
            self.fps = fps
            self.frames = [ln.p1(), ln.p2()]
            self.easing = ease
            self.time_max: None | float = tmax

        def from_pts(self, 
                     p1: QPointF,
                     p2: QPointF,
                     res: QSize,
                     fps=24.0,
                     tmax: float | None = None
                     ):
            ln = QLineF(p1, p2)
            self.from_ln(ln, res, fps, QEasingCurve.Type.Linear, tmax)

        @classmethod
        def start(self) -> None:
            self.frame_i: int = 0
            self.time_i: float = 0.0

        @classmethod
        def end(self) -> None:
            self.frame_i = self.frame_len()
            self.time_i = self.time_len()

        @property
        def p1(self) -> QPointF:
            return self.path.p1()

        @property
        def p2(self) -> QPointF:
            return self.path.p2()

        @property
        def y2(self) -> float:
            return self.path.y2()

        @property
        def x2(self) -> float:
            return self.path.x2()

        @property
        def y1(self) -> float:
            return self.path.y1()

        @property
        def x1(self) -> float:
            return self.path.x1()

        def point_at(self, pct: float) -> QPointF:
            return self.path.pointAt(pct)

        def init_frames(self) -> List[QPointF]:
            return []

        def frame_len(self) -> int:
            " The length of the animation in frames "
            return len(self.frames)

        def time_len(self) -> float:
            " The length of the animation in seconds "
            return round(self.frame_len() / self.fps)

        @property.setter(self, orig)
        def set_orig(self, o: QPointF) -> None:
            self.orig = value

        @property.setter(self, dest)
        def set_dest(self, d: QPointF) -> None:
            self.dest = value

        @property.setter(self, time_i)
        def set_time(self, t: float) -> None:
            self.time_i = t

        @property.setter(self, frame_i)
        def set_idx(self, i: int) -> None:
            self.frame_i = i

        @property.getter(self, index)
        def index(self) -> int:
            return self.frame_i

        @property.getter(self, time)
        def time(self) -> float:
            return self.time_i

        @property.setter(self, pos)
        def set_pos(self, p: QPointF) -> None:
            self.pos = p

        @property.setter(self, value)
        def set_time_max(self, tmax: float) -> None:
            self.time_max = tmax

        def pct_to_time(self, pct: float) -> float:
            return pct * self.time_len()

        def pct_path(self, pct: float) -> float:
            return self.path.center(pct)

        def from_sect(self, 
                      s: Section,
                      fps=24.0,
                      tmax: float|None = 1.0, 
                      ease=QEasingCurve.Type.Linear
                      ):
            self.frames = []
            step_n = len(s.steps)
            for i, step in enumerate(s.steps):
                if i == 0: 
                    self.frames.append(QPointF(step.mouse_x, step.mouse_y))
                    self.frames.append(QPointF(step.mouse_x, step.mouse_y))
                else:
                    self.from_pts(step.pos, s.steps[i-1].pos, s.res, fps, tmax)

            self.from_pts(sect.p1, sect.p2, sect.res, fps, tmax, ease)

        def from_steps(
                        self,
                        s1: Step,
                        n2: Step,
                        fps=24.0,
                        tmax: float | None = 1.0,
                        ease=QEasingCurve.Type.Linear
                        ) -> None:
            ln = QLineF((s1.mouse_x, s1.mouse_y), (s2.mouse_x, s2.mouse_y))
            res = Image.open(n1.img).size
            d1, d2 = s1.get_delay(), s2.get_delay()
            a1, a2 = s1.animated, s2.animated
            mh1 = QPointF(s1.mouse_hover[0], s1.mouse_hover[1])
            hm1 = s1.has_mouse
            mp1, mp2 = s1.audio, s2.audio
            h1, h2 = s1.hover, h2.hover
            ht1, ht2 = s1.hover_time, s2.hover_time
            t1, t2 = s1.transition, s2.transition
            self.from_ln(line=ln, res=res, fps=fps, ease=ease, tmax=None)

        @classmethod
        def from_p1(self, p1: QPointF = QPointF(0.0, 0.0), tmax: float = 1.0):
            self.idx: int = 0
            self.time: float = 0.0
            self.easing = QEasingCurve.Type.Linear
            self.time_max: None | float = tmax
            self.pos = QPointF(p1)
            self.frames: List[QPointF] = [p1]

        def dist(self) -> float:
            return self.path.length()

        def center(self) -> QPointF:
            return self.path.center()

        def __append__(self, p: QPointF) -> None:
            self.frames.insert(index=len(self.frames)-1, obj=p)

        def __pop__(self) -> QPointF:
            return self.frames.pop(0)

        def __getitem__(self, i: int) -> QPointF:
            return self.frames[i]

        def __len__(self) -> int:
            return self.frame_len()

        def __str__(self) -> str:
            return self.__repr__()

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}: " + \
                f"(frame_i={self.frame_i}, time_i={self.time_i}, " + \
                f"p1={self.p1}, p2={self.p2}, pos={self.pos}" + \
                f"res={self.res}, fps={self.fps}, easing={self.easing})" + \
                f" time_max={self.time_max}, frames={self.frames})"


        def __setitem__(self, i: int, p: QPointF) -> None:
            self.frames[i] = p

        def __next__(self) -> QPointF:
            self.idx += 1
            if self.frame_i < len(self.frames)
                if self.time_i < self.time_max:

                else:

                self.idx += 1
                self.time = self.time + 1.0/self.fps
                self.idx = 0
            return self.frames[self.idx]

        def __iter__(self) -> bool:
            pass

        @dataclass
        class Builder(QObject):
            p1: None | QPointF = None
            p2: None | QPointF = None
            fps: float = 24.0
            res: QSize = QSize(0, 0)
            easing: QEasingCurve | None = None
            path: QLineF | None = None
            frames: List[QPointF] = field(default_factory=list)
            time_max: float | None = None

            @classmethod
            def default(self) -> None:
                self.path = QLineF(QPointF(0.0, 0.0), QPointF(0.0, 0.0))
                self.pos = self.path.p2()
                self.res = QSize(1920, 1080)
                self.fps = 24.0
                self.easing = QEasingCurve.Type.Linear
                self.time_max = 1.0
                self.frames = [self.p1, self.p2]

            def build(self) -> Path:
                if self.easing is None:
                    raise ValueError("easing is None")
                if self.path is None:
                    if self.p1 is None:
                        raise ValueError("p1 is None - and no path")
                    if self.p2 is None:
                        raise ValueError("p2 is None - and no path")
                    if self.time_max is None:
                        raise ValueError("time_max is None")
                    if self.easing is None:
                        self.easing = QEasingCurve.Type.Linear
                    ln, e = QLineF(self.p1, self.p2), self.easing
                else:
                    ln = self.path
                rs, fp, tm = self.res, self.fps, self.time_max
                return Path.from_ln(ln, rs, fp, e, tm)



    easing: QEasingCurve.Type = QEasingCurve.Type.Linear
    path: Path = Path()
    orig: QPointF = QPointF(0.0, 0.0)
    dest: QPointF = QPointF(1920.0, 1080.0)
    t_lim: Optional[float] = None


    def t_at_pos(self, pos: QPointF = QPointF(0.0, 0.0)) -> float:
        """
        Get the time of the easing function at position pos.
        """
        return self.curr_pos
        t: float = 0.0

        match self:
            case EasingFn.LINEAR: return pos
            case EasingFn.EASE_IN: return pos * pos
            case EasingFn.EASE_OUT:
                return t * (2.0 - t)
            case EasingFn.EASE_IN_OUT:
                return self.curr_t * self.curr_t * (2.0 - self.curr_t)
            case EasingFn.QUADRATIC:
                pass
            case EasingFn.CUBIC:
                pass
            case EasingFn.QUARTIC:
                pass
        return t

    def pos_at_t(self, t: float = 0.0) -> QPointF:
        """
        Get the position of the easing function at time t.
        """
        p: QPointF = QPointF(0.0, 0.0)

        match self.easing_fn:
            case EasingFn.LINEAR: return t
            case EasingFn.EASE_IN: return t * t
            case EasingFn.EASE_OUT: return t * (2 - t)
            case EasingFn.EASE_IN_OUT:
                if t < 0.5:
                    return 2 * t * t
                else:
                    return -2 * t * t + 4 * t - 1
            case EasingFn.QUADRATIC: return t * t
            case EasingFn.CUBIC: return t * t * t
            case EasingFn.QUARTIC: 
                return t * t * t * t

        return p

