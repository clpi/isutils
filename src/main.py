"""
python-docx
mutagen
pillow
lxml
TODO Consider *drastically* slimming down demo, section, step models so as to only act as lxml etree wrappers
"""
from ui.window import MainWindow, run
from app import *
import os, sys

def main():
    run()

if __name__ == "__main__":
    main()
