"""
Operation to stitch together images of demo to form exported mp4 file
"""
from pathlib import WindowsPath
from typing import Sequence, Optional, Tuple
import enum
import mutagen
from moviepy.editor import VideoFileClip, AudioFileClip, ImageClip, ImageSequenceClip, AudioArrayClip, AudioClip
import moviepy.editor as mpy
import ffmpeg
from numpy import float64, uint64
import os
from dataclasses import dataclass

def render(path: str):
    command = os.path.join(os.getcwd(), "ffmpeg")
    pass

class Format(enum.Enum):
    Mp4, Avi, Mkv = range(3)

class Clip:
    pass

class StepClip(Clip):
    img: str
    hover: Optional[str] = None
    delay: float
    animated: bool = False
    audio: Optional[str] = None

    def __init__(self, 
            img: str, 
            hover: Optional[str] = None, 
            animated: bool = False, 
            audio: Optional[str] = None
    ):
        self.hover = hover
        self.img = img
        self.animated = animated
        self.audio = audio

    def __len__(self):
        if self.audio:
            mp3 = mutagen.File(self.audio)
            return len(mp3) + self.delay
        return self.delay

    def render(self, fmt: Format) -> ffmpeg.Stream | ffmpeg.Error:
        inp = ffmpeg.input(self.img)
        return inp
        
        
    
class SectionClip(Clip):
    idx: int
    audio: Optional[str]
    clips: Sequence[StepClip]

    def __len__(self):
        if self.audio:
            mp3 = mutagen.File(self.audio)
            # plus sum of all lens
            return len(mp3) + self.delay
        return self.delay

    def add_text(self, s: str):
        pass

    def add_rect(self, x: int, y: int, h: int, w: int):
        pass

    def overlay(self, img: str):
        proc = (
            ffmpeg.input(self.clips[0].img)
                .output("pipe:", vcodec="copy", pix_fmt="rgb24", format="rawvideo")
                .run_async(pipe_stdout=True, pipe_stderer=True)
        )
        pass

    def path(self, base: WindowsPath, fmt: Format) -> str:
        res =  f"{base}{self.idx}.{fmt.name}"
        return res

    def render(self, base: WindowsPath, fmt: Format) -> ffmpeg.Stream | ffmpeg.Error:
        inp = self.clips[0].render(fmt)
        out = ffmpeg.output(self.path(base, Format.Mp4))
        if self.audio:
            audio = ffmpeg.input(self.audio)
            ffmpeg.concat(inp, audio)
        return out
            
        
    
class DemoVid:
    path: WindowsPath
    target: str
    resolution: Tuple[int, int]
    format: Format
    sections: Sequence[SectionClip]
    fps: int = 24

    def render(self):
        try:
            ffmpeg.output(self.target).overwrite_output().run()
        except Exception as e:
            print(e)


def build_playlist_movie(
    tmp_file_paths, movie_file_path, width=None, height=1080, fps="24.00"
):
    """
    Build a single movie file from a playlist.
    """
    in_files = []
    if len(tmp_file_paths) > 0:
        (first_movie_file_path, _) = tmp_file_paths[0]
        if width is None:
            (width, height) = get_movie_size(first_movie_file_path)

        for tmp_file_path, file_name in tmp_file_paths:
            if not has_soundtrack(tmp_file_path):
                add_empty_soundtrack(tmp_file_path)

        for tmp_file_path, file_name in tmp_file_paths:
            in_file = ffmpeg.input(tmp_file_path)
            in_files.append(
                in_file["v"]
                .filter("setsar", "1/1")
                .filter("scale", width, height)
            )
            in_files.append(in_file["a"])

        joined = ffmpeg.concat(*in_files, v=1, a=1).node
        video = joined[0]
        audio = joined[1]

        try:
            ffmpeg.output(
                audio, video, movie_file_path
            ).overwrite_output().run()
        except Exception as e:
            print(e)
            return {"success": False, "message": str(e)}
    return {"success": True} 

def get_video_size(filename):
    logger.info('Getting video size for {!r}'.format(filename))
    probe = ffmpeg.probe(filename)
    video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
    width = int(video_info['width'])
    height = int(video_info['height'])
    return width, height 