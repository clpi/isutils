#!/usr/bin/env python
# from cx_Freeze import setup, Executable
from __future__ import annotations 
from setuptools import setup
from collections import OrderedDict
from rich import progress_bar, color, color_triplet, print
import os, io, sys
from shutil import copytree, rmtree, copy
import subprocess

VERS = "0.1.0"
PATH = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(PATH, "README.md")) as f:
    README = f.read()


print("[bold green]BEGINNING INSTALLATION...[/bold green]", locals())
print("[green]BEGINNING INSTALLATION...[/green]", locals())

def build():
    print("BUILDING")

def test():
    print("TESTING")

def set():
    setup(
        name="isutils",
        version=VERS,
        author="Chris Pecunies",
        author_email="chris.pecunies@impresys.com",
        long_description=README,
        description="Utilities for demo production",
        include_package_data=True,
        
    )

# buildOptions = dict(packages = [], excludes = [])

# base = 'Win32GUI' if sys.platform=='win32' else None

# executables = [
#     Executable('main.py', base=base, targetName = 'isutils')
# ]

# setup(name='impresys utils',
#       version = '0.1',
#       description = '',
#       options = dict(build_exe = buildOptions),
#       executables = executables)
