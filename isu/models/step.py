from dataclasses import dataclass
from lxml.etree import CDATA, Element, cleanup_namespaces, Entity, open, parse, ElementTree as ETree
from lxml.objectify import parse, ObjectifiedElement, E, dump, IntElement, StringElement, FloatElement, XML
from PIL import Image
import lxml.etree as ET
import numpy as np
# from uuid import uuid4
from typing import List, Tuple, Dict, Optional, Any, Iterable, Union, TypeVar
from pathlib import WindowsPath, Path
import isu.models.demo_tags as dt
from isu.models.audio import SoundBite
from isu.models.script import TextBox
import shutil
import re
from copy import deepcopy
from PySide6 import QtUiTools
from PySide6.QtCore import QObject, QEasingCurve, Signal, Property, Slot, QPointF, QPoint

_Step = TypeVar("_Step", bound="Step")

# class StepXml(ET.)
class Step(QObject):

    @dataclass
    class Video(QObject):
        pos: Tuple[int, int] = (0, 0)
        size: Tuple[int, int] = (1920, 1080)
        vidsize: Tuple[int, int] = (1920, 1080)

        autoplay: bool = True
        asp_locked: bool = True
        file: str = "Video.mp4"
        dur_ticks: str = "80000000"

    @dataclass
    class Text(QObject):
        font: str = ""
        text: str = ""
        color: str = ""
        size: str = ""

    @dataclass
    class Img(QObject):
        hover: bool = False
        path: str = ""

    @dataclass
    class Hover(QObject):
        img: str = ""
        mouse: QPointF = QPointF(0.0, 0.0)

        def __init__(self, img: str):
            self.img = img

    def __init__(
            self,
            root: ET._Element,
            idx: int = 0,
            copy_root: bool = False,
            demo_dir: str = "",
            verbose: bool = False,
            hover_img_path: str = "",
            click_instr: str = "",
            talking_pt: str = "",
            last_of_sect: bool = False,
            delay: float = 1.0):
        self.root: ET._Element
        match copy_root:
            case True: self.root = deepcopy(root)
            case False: self.root = root
            # ET.ElementTre
        self.sp_el: ET._Element = self.root.find("StartPicture",namespaces=None)
        self.mp_el: ET._Element = self.root.find("MouseEnterPicture",namespaces=None)
        self.demo_dir: str = demo_dir
        self.last_of_sect: bool = last_of_sect
        match demo_dir:
            case None: self.demo_dir = ""
            case dd: self.demo_dir = dd
        # self.is_guided: bool = is_guided
        # self.has_mouse: bool = has_mouse
        # self.is_animated: bool = is_animated
        # self.hover: HoverImg = Hover(hover_img_path)
        self.has_audio: bool
        self.idx: int = idx
        self.verbose: bool = verbose
        self.tp, self.ci = TextBox(talking_pt), TextBox(click_instr)
        self.load()

    def find_root(self, prop: str, namespaces: None | str = None) -> ET._SubElement:
        " Search under the root XML element"
        return self.root.find(prop, namespaces=namespaces)

    def find_startpic(self, prop: str, ns: None | str = None) -> ET._SubElement:
        " Search under the 'StartPicture' XML element"
        return self.sp_el.find(prop, namespaces=ns)

    def find_mouseenter(self, prop: str, ns: None | str = None) -> ET._SubElement:
        " Search under the 'MouseEnterPicture' XML element"
        return self.mp_el.find(prop, namespaces=ns)

    def load(self):
        self.boxes: Dict[str, Dict[str, List[int]]]
        for k, v in dt.BOX_PROPS.items():
            self.boxes[k] = dict.fromkeys({*v["props"], *dt.DIRS}, None)
        asset_rel = Path(self.find_startpic(prop="AssetsDirectory").text)
        img_rel = Path(self.find_startpic(prop="PictureFile").text)
        self.assets = Path(self.demo_dir / asset_rel)
        self.img = Path(self.assets / img_rel)
        print(f"IMAGE: {self.img}")
        hover = self.find_mouseenter("MouseEnterPicture")
        self.time = self.find_mouseenter("Time").text
        self.mouse_enter = hover
        if hover is not None and hover.text is not None:
            print("self.mouse_enter is not NOne")
            self.hover = Path(self.assets, hover.find("PictureFile", None).text)
            if (hover_time := hover.find("Time", None).text):
                self.hover_time = hover_time
            else:
                self.hover_time = ""
            self.mhovx = float(hover.find(dt.MOUSE_X, namespaces=None).text)
            self.mhovy = float(hover.find(dt.MOUSE_Y, namespaces=None).text)
            self.mouse_hover = (self.mhovx, self.mhovy)
        else:
            self.hover = None
        self.mouse_x = float(self.sp_el.find(dt.MOUSE_X, namespaces=None).text)
        self.mouse_y = float(self.sp_el.find(dt.MOUSE_Y, namespaces=None).text)
        self.mouse = self.mouse_x, self.mouse_y
        if (soundbite := self.root.find("SoundBite", namespaces=None)) is not None:
            if self.verbose:
                print(f"SOUNDBITE: {soundbite}")
            self.audio = SoundBite(elem=soundbite, asset_path=str(self.assets))
        else:
            self.audio = None
        for prop, prop_dict in dt.STEP_PROPS.items():
            prop_tag, prop_type = prop_dict["tag"], prop_dict["type"]
            try:
                setattr(self, prop, prop_type(self.root.find(prop_tag, namespaces=None).text))
            except Exception as e:
                print(e)
                setattr(self, prop, None)
        # setattr(self,"delay", float)
        for box_key, box_dict in dt.BOX_PROPS.items():
            box_props = {**box_dict["props"], **dt.DIRS}
            tag = box_dict["tag"]
            props = self.sp_el.findall(tag+"/"+tag[:-1], namespaces=None)
            if props is not None:
                for prop, propv in box_props.items():
                    self.boxes[box_key][prop] = []
                    for i, box in enumerate(props):
                        prop_tag, prop_type = propv["tag"], propv["type"]
                        if (box.find(prop_tag) is not None):
                            box_text = prop_type(box.find(prop_tag).text)
                            self.boxes[box_key][prop].append(box_text)
            if box_key == 'hotspot':
                self.is_hotspot()

    def res(self) -> Tuple[int, int]:
        s: Tuple[int, int] = Image.open(self.img).size
        return s[0], s[1]

    def is_hotspot(self) -> bool:
        hs_x = self.boxes['hotspot']['x1'][0]
        hs_y = self.boxes['hotspot']['y1'][0]
        if (hs_x == dt.DEMO_RES[0] and hs_y == dt.DEMO_RES[1]):
            self.animated = True
            self.set_delay(0.1, False)
            self.boxes['hotspot']['x1'][0] = 0
            self.boxes['hotspot']['y1'][0] = 0
            self.boxes['hotspot']['x2'][0] = dt.DEMO_RES[0]
            self.boxes['hotspot']['y2'][0] = dt.DEMO_RES[1]
            # self.text = {k:dict.fromkeys({*v["props"], *dt.DIRS}, None)
            # for k, v in dt.TEXT_PROPS.items()}
        else:
            self.animated = False
        return self.animated

    # TODO Sometimes mouse coords are ints, sometimes floats, in XML. check it out

    def set_mouse(self, x: float, y: float):
        self.mouse = (x, y)
        self.sp_el.find(dt.MOUSE_X, namespaces=None).text = str(x)
        self.sp_el.find(dt.MOUSE_Y, namespaces=None).text = str(y)

    def set_mouse_hover(self, x: float, y: float):
        self.mouse_hover = (x, y)
        self.sp_el.find("MouseEnterPicture/"+dt.MOUSE_X, namespaces=None).text = str(x)
        self.sp_el.find("MouseEnterPicture/"+dt.MOUSE_X, namespaces=None).text = str(y)

    def set_video_dims(self, x: int, y: int):
        self.sp_el.find("VideoRects/VideoRect/Video/VideoHeight", namespaces=None).text = str(y)
        self.sp_el.find("VideoRects/VideoRect/Video/VideoWidth", namespaces=None).text = str(x)
        self.boxes["video"]["width"][0], self.boxes["video"]["height"][0] = x, y

    def set_box_dims(self, box: str, coords):
        """
        Input: Box type (str, ex "hotspot"), (x0, x1) int tuple, (y0, y1) int tuple
        Output: None. Sets step.box["prop"][dimension] to input value.
        """
        tag = str(dt.BOX_PROPS[box]["tag"])
        xmlbox = self.sp_el.find(tag+"/"+tag[:-1],namespaces=None)
        for i in range(len(self.boxes[box]["x1"])):
            for j, dim in enumerate(coords):
                d = dt.DIR_KEYS[j]
                self.boxes[box][d][i] = dim  # type: ignore
                xmlbox.find(dt.DIRS[d]["tag"]).text = str(int(dim))
                if self.verbose:
                    print(dim, xmlbox.find(dt.DIRS[d]["tag"]).text)

    def transform_coords(self, scale: Tuple[float, float], offset: Tuple[float, float]):
        """
        Transforms all coordinate-based and height/widgth/size based properties of
        this step by a provided scaling and offset factor, LTRB
        """
        (rx, ry) = scale
        (ox, oy) = offset

        def transf(coord: List[int], use_offset: bool = True):
            out = []
            for i, c in enumerate(coord):
                if i % 2 == 0:
                    if use_offset:
                        out.append(float(c * rx + ox))
                    else:
                        out.append(float(c * rx))
                else:
                    if use_offset:
                        out.append(float(c * ry + oy))
                    else:
                        out.append(float(c * ry))
            return out

        # -> [top, bottom, left, right]
        def transform(coords: List[float]) -> List[float]:
            out = []
            if len(coords) > 2:  # if BOX coordinates (T, B, L, R)
                for i in range(4):
                    if i % 2 == 0:
                        out.append(float((coords[i] * ry) + oy))
                    else:
                        out.append(float((coords[i] * rx) + ox))
            elif len(coords) <= 2:  # if CLICK coordinates (X, Y)
                out.append(float(coords[0] * rx + ox))
                out.append(float(coords[1] * ry + oy))
            return out

        for box, box_props in self.boxes.items():
            for i in range(len(box_props['x1'])):
                dims = [box_props[d][i] for d in dt.DIR_KEYS]  # type: ignore
                if self.verbose:
                    print("OLD: " + str(dims))
                coords = transf(dims)
                if self.verbose:
                    print("NEW: " + str(coords))
                self.set_box_dims(box, coords)
                if box == "video":
                    # type: ignore
                    w, h = transf(
                        [box_props["width"][i], box_props["height"][i]], False)
                    self.set_video_dims(w, h)
                if box == "text":
                    tag = "TextRects/TextRect/FontSize"
                    self.boxes[box]["size"][i] *= (rx*ry + 1)  # type: ignore
                    self.sp_el.find(tag, namespaces=None).text = str(
                        box_props["size"][i])  # type: ignore
        self.set_mouse(self.mouse[0]*rx+ox, self.mouse[1]*ry+oy)
        if self.hover is not None:
            if self.mouse_hover:
                self.set_mouse_hover(
                    self.mouse_hover[0]*rx*ox, self.mouse_hover[1]*ry*oy)
        if dt.DEBUG:
            if self.verbose:
                print(f"SHIFTED: Step {self.idx}")

    def set_guided(self, guided: bool):
        pass

    def get_delay(self) -> float:
        sd = self.boxes["StepDelay"]
        return float(sd)  # type: ignore
        # # if self.root.find("StepDelay").attributes["xsi:nil"] == "true"
        # if self.root.find("StepDelay") is not None:
        #     return float(self.root.find("StepDelay").text)
        # else:
        # return 1.0

    def set_delay(self, length: float = 1.0, off: bool = False):
        if off:
            self.find_root("StepDelay").attributes["xsi:nil"] = "true"
        else:
            self.find_root("StepDelay").text = str(length)
        setattr(self, "delay", length)

    def key_ci_phrase_match(self, phrase: str):
        pass

    def get_img_names(self, full_path=False) -> Tuple[str, str]:
        if self.hover:
            return (str(self.img), str(self.hover)) if full_path else (str(self.img.name), str(self.hover.name))
        if full_path:
            num = self.img.name.rsplit()[1][:-4]
            hover_name = self.img.name.replace(str(num), str(num+str(1)))
            hover_path = Path(self.assets, hover_name)
            return (str(self.img), str(hover_path)) if full_path else (str(self.img.name), str(hover_name))
        return (str(self.img), str(self.hover))

    def set_text(self, tp: str = "", ci: str = "", img: str = ""):
        self.tp.text, self.ci.text = tp, ci
        if tp != "":
            self.tp.words = self.tp.get_words()

    def set_audio(self, soundbite: SoundBite):
        source = soundbite.path
        dest = Path(self.assets, 'SoundBite.mp3')
        if not self.assets.exists():
            self.assets.mkdir()
        if not dest.exists():
            shutil.copy(str(source), str(dest))
        index = self.root.index(child=self.find_root("StepFlavor"), start=None, stop=None)+1
        self.root.insert(index, soundbite.get_root())
        self.audio = SoundBite(self.find_root("SoundBite"), asset_path=str(self.assets))

    def set_image(self, img_path: str):
        # BACK UP IMAGE TO ANOTHER FOLDER BEFORE SAVING
        if not self.assets.exists():
            self.assets.mkdir()
        if Path(self.img).exists():
            backup = Path(self.img.parent, self.img.name+"_backup.png")
            shutil.copy(str(self.img), str(backup))
        shutil.copy(img_path, str(self.img))

    def set_video(self, video_path: str):
        pass

    def set_animated(self):
        self.set_box_dims('hotspot', (0, 0, dt.DEMO_RES[0], dt.DEMO_RES[1]))
        for dir_key, ddict in dt.DIRS.items():
            hspot = self.find_startpic(f"Hotspots/Hotspot/{ddict[dir_key]['tag']}")
            hspot.text = str(getattr(self, 'hotspot')[dir_key][0])
        self.find_root(dt.STEP_PROPS['has_mouse']['tag']).text = 'false'
        self.has_mouse = False

    def iter_box_props(self):
        for box, box_props in self.boxes.items():
            for prop, vals in box_props.items():
                yield (prop, vals)

    def remove_audio(self):
        pass

    def add_audio(self):
        pass

    def from_array(self, a: np.ndarray):
        i = Image.fromarray(a, 'RGB')
        i.resize((1920, 1080))
        return i

    def __eq__(self, other):
        return self.idx == other.idx

    def __str__(self):
        return str(self.tp)

    # def __call__(self, tp: str = None, ci: str = None, img: str = None):
    #     pass

    def __getitem__(self, index: int):
        self.idx

    def __setitem__(self, index: int, value):
        pass


@dataclass
class StepBuilder(QObject):
    is_animated: bool
    is_guided: bool
    has_mouse: bool


class StepXml(object):
    class Builder:
        pass

    def __init__(self):
        pass
