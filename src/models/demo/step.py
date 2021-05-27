from PIL import Image
import re
from uuid import uuid4
from typing import List, Tuple, Dict, Optional, Any, Iterable, Union
from pathlib import Path, PurePath
import models.demo.demo_tags as dt
from models.demo.audio import SoundBite
from models.demo.script import TextBox
import shutil
from copy import deepcopy

class Step:

    #TODO check if step delaya is None if not specified
    def __init__(self,
                elem = None,
                copy: bool = False,
                demo_dir: str = None,
                idx: int = -1,
                demo_idx: int = -1,
                img_path: str = "",
                hover_img_path: str = "",
                click_instr: str = "",
                talking_pt: str = "",
                audio_path: str = "",
                animated: bool = False,
                guided: bool = False,
                step_delay: float = 1.0):
        if not copy:
            self.root = elem
        else:
            self.root = deepcopy(elem)
        self.idx = idx
        self.demo_idx = demo_idx
        self.demo_dir = demo_dir
        self.tp, self.ci = TextBox(talking_pt), TextBox(click_instr)
        self.load()

    def load(self):
        s = []
        self.props = self.root.find("StartPicture")
        self.boxes = {k:dict.fromkeys({*v["props"], *dt.DIRS}, None) for k, v in dt.BOX_PROPS.items()}
        self.assets = Path(self.demo_dir, self.props.find("AssetsDirectory").text)
        self.img = PurePath(self.assets, self.props.find("PictureFile").text)
        self.time = self.props.find("Time").text
        if (hover := self.props.find("MouseEnterPicture")) is not None and hover.text is not None:
            self.hover = PurePath(self.assets, hover.find("PictureFile").text)
            self.hover_time = hover.find("Time").text
            self.mouse_hover = (float(hover.find(dt.MOUSE_X).text), float(hover.find(dt.MOUSE_Y).text))
        else:
            self.hover = None
        self.mouse = (float(self.props.find(dt.MOUSE_X).text), float(self.props.find(dt.MOUSE_Y).text))
        if (soundbite := self.root.find("SoundBite")) is not None:
            self.audio = SoundBite(elem=soundbite, asset_path=str(self.assets))
        else:
            self.audio = None
        for prop, prop_dict in dt.STEP_PROPS.items():
            prop_tag, prop_type = prop_dict["tag"], prop_dict["type"]
            try:
                setattr(self, prop, prop_type(self.root.find(prop_tag).text))
            except:
                setattr(self, prop, None)
        for box_key, box_dict in dt.BOX_PROPS.items():
            box_props = {**box_dict["props"], **dt.DIRS}
            tag = box_dict["tag"]
            props = (self.props.findall(tag+"/"+tag[:-1]))
            if props is not None:
                for prop, prop_vals in box_props.items():
                    self.boxes[box_key][prop]: List[str] = []
                    for i, box in enumerate(props):
                        prop_tag, prop_type = prop_vals["tag"], prop_vals["type"]
                        if (box.find(prop_tag) is not None):
                            box_text = prop_type(box.find(prop_tag).text)
                            self.boxes[box_key][prop].append(box_text)
            if box_key == 'hotspot':
                if (self.boxes[box_key]['x1'][0] == dt.DEMO_RES[0] and
                    self.boxes[box_key]['y1'][0] == dt.DEMO_RES[1]):
                    self.animated = True
                else:
                    self.animated = False
        self.loaded = True

    #TODO Sometimes mouse coords are ints, sometimes floats, in XML. check it out
    def set_mouse(self, x: float, y: float):
        self.mouse = (x, y)
        self.props.find(dt.MOUSE_X).text = str(x)
        self.props.find(dt.MOUSE_Y).text = str(y)

    def set_mouse_hover(self, x: float, y: float):
        self.mouse_hover = (x, y)
        self.props.find("MouseEnterPicture/"+dt.MOUSE_X).text = str(x)
        self.props.find("MouseEnterPicture/"+dt.MOUSE_X).text = str(y)


    def set_video_dims(self, x: int, y: int):
        self.props.find("VideoRects/VideoRect/Video/VideoHeight").text = str(y)
        self.props.find("VideoRects/VideoRect/Video/VideoWidth").text = str(x)
        self.boxes["video"]["width"], self.boxes["video"]["height"] = x, y

    def set_box_dims(self, box: str, coords):
        """
        Input: Box type (str, ex "hotspot"), (x0, x1) int tuple, (y0, y1) int tuple
        Output: None. Sets step.box["prop"][dimension] to input value.
        """
        tag = str(dt.BOX_PROPS[box]["tag"])
        xmlbox = self.props.find(tag+"/"+tag[:-1])
        for i in range(len(self.boxes[box]["x1"])):
            for j, dim in enumerate(coords):
                d = dt.DIR_KEYS[j]
                self.boxes[box][d][i] = dim
                xmlbox.find(dt.DIRS[d]["tag"]).text = str(int(dim))
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
                if i%2 == 0:
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

        def transform(coords: List[float]) -> List[float]: #-> [top, bottom, left, right]
            out = []
            if len(coords) > 2: # if BOX coordinates (T, B, L, R)
                for i in range(4):
                    if i % 2 == 0: out.append(float((coords[i] * ry) + oy))
                    else: out.append(float((coords[i] * rx) + ox))
            elif len(coords) <= 2: # if CLICK coordinates (X, Y)
                out.append(float(coords[0] * rx + ox))
                out.append(float(coords[1] * ry + oy))
            return out

        for box, box_props in self.boxes.items():
            for i in range(len(box_props['x1'])):
                dims = [box_props[d][i] for d in dt.DIR_KEYS]
                print("OLD: " + str(dims))
                coords = transf(dims)
                print("NEW: " + str(coords))
                self.set_box_dims(box, coords)
                if box == "video":
                    w, h = transf([box_props["width"][i], box_props["height"][i]], False)
                    self.set_video_dims(w, h)
                if box == "text":
                    tag = "TextRects/TextRect/FontSize"
                    self.boxes[box]["size"][i] *= (rx*ry + 1)
                    self.props.find(tag).text = str(box_props["size"][i])
        self.set_mouse(self.mouse[0]*rx+ox, self.mouse[1]*ry+oy)
        if self.hover is not None:
            self.set_mouse_hover(self.mouse_hover[0]*rx*ox, self.mouse_hover[1]*ry*oy)
        if dt.DEBUG:
            print(f"SHIFTED: Step {self.idx}")



    def set_guided(self, guided: bool):
        pass

    def set_delay(self, length: float = 1.0, off: bool = False):
        if off:
            self.root.find("StepDelay").attributes["xsi:nil"] = "true"
        else:
            self.root.find("StepDelay").text = str(length)
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
        index = self.root.index(self.root.find("StepFlavor"))+1
        self.root.insert(index, soundbite.get_root())
        self.audio = SoundBite(self.root.find("SoundBite"), asset_path=str(self.assets))

    def set_image(self, img_path: str):
        # BACK UP IMAGE TO ANOTHER FOLDER BEFORE SAVING
        if not self.assets.exists():
            self.assets.mkdir()
        if Path(self.img).exists():
            backup = Path(self.img.parent, self.img.name+"_backup.png") #check this
            shutil.copy(str(self.img), str(backup))
        shutil.copy(img_path, str(self.img))

    def set_video(self, video_path: str):
        pass

    def set_animated(self):
        self.set_box_dims('hotspot', (0, 0, dt.DEMO_RES[0], dt.DEMO_RES[1]))
        for dir_key, ddict in dt.DIRS.items():
            hspot = self.props.find(f"Hotspots/Hotspot/{ddict[dir_key]['tag']}")
            hspot.text = str(getattr(self, 'hotspot')[dir_key][0])
        setattr(self, 'has_mouse', False)
        self.root.find(dt.STEP_PROPS['has_mouse']['tag']).text = 'false'

    def iter_box_props(self):
        for box, box_props in self.boxes.items():
            for prop, vals in box_props.items():
                yield (prop, vals)

    def remove_audio(self):
        pass

    def add_audio(self):
        pass

    def __eq__(self, other):
        return self.idx == other.idx

    def __str__(self):
        return str(self.tp)

    def __call__(self, tp: str = None, ci: str = None, img: str = None):
        pass

    def __getitem__(self, index: int):
        self.idx

