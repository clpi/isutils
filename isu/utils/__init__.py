from dataclasses import dataclass
from typing import Any, Optional, Tuple, Union, Sequence, NamedTuple
from PyQt6.QtCore import (
    QObject, QUrl,
    QDataStream, Qt, QByteArray, QIODevice, 
)
from PyQt6.QtGui import (
    QAction, QColor,
)
import inspect, os
from isu import __dbg__

def log(*a: object, module: str = __package__, verbose: bool = True) -> None:
    if __dbg__ and verbose:
        print(f"[{module}] ", end="")
        print(*a)

def check_dstream(stream: QDataStream) -> None:
    status = {
        QDataStream.Status.Ok: "Data stream OK",
        QDataStream.Status.ReadPastEnd: "Read past end",
        QDataStream.Status.ReadCorruptData: "Read corrupt data",
        QDataStream.Status.WriteFailed: "Write failed",
    }
    if stream.status() != QDataStream.Status.Ok:
        raise OSError(status[stream.status()])

_QtSerializable = QObject | QByteArray | QUrl

def serialize(obj: _QtSerializable) -> QByteArray:
    """Serialize an object into a QByteArray."""
    data = QByteArray()
    stream = QDataStream(data, QIODevice.OpenModeFlag.WriteOnly)
    check_dstream(stream)
    stream << obj # type: ignore[operator]
    check_dstream(stream)
    return data


def deserialize(data: QByteArray, obj: _QtSerializable) -> None:
    """Deserialize an object from a QByteArray."""
    stream = QDataStream(data, QIODevice.OpenModeFlag.ReadOnly)
    check_dstream(stream)
    stream >> obj # type: ignore[operator]
    check_dstream(stream)

@dataclass
class Rgba:
    r: int = 0
    g: int = 0
    b: int = 0
    a: int = 100

    def get_pct_interp(self, other: Any, pct: int) -> Any:
        if not 0 <= pct <= 100:
            raise ValueError("pct must be between 0 and 100")
        r = round(self.r + (other.r - self.r) * pct / 100)
        g = round(self.g + (other.g - self.g) * pct / 100)
        b = round(self.b + (other.b - self.b) * pct / 100)
        a = round(self.a + (other.a - self.a) * pct / 100)
        return Rgba(r, g, b, a)

    def interp(self, c0: QColor, c1: QColor, pct: int, cspace: Optional[QColor.Spec] = QColor.Spec.Rgb) -> QColor:
        if cspace is None:
            if pct == 100: return QColor(*c1.getRgb())
            else: return QColor(*c0.getRgb())
        out = QColor()
        if cspace == QColor.Spec.Rgb:
            col1 = Rgba(*c0.getRgb())
            col2 = Rgba(*c1.getRgb())
            comp = col1.get_pct_interp(col2, pct)
            out.setRgb(*comp)
        else:
            raise ValueError("Invalid colorspace")
        out = out.convertTo(c0.spec())
        return out
