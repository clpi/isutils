from moviepy.editor import VideoFileClip, AudioFileClip, ImageClip, ImageSequenceClip, AudioArrayClip, AudioClip
import moviepy.editor as mpy

def render(path: str):
    frames = []
    steps = []
    hovers = []
    sections = []

    curr_sect = [] # steps in section
    sect = ImageSequenceClip(curr_sect, fps=25)
    