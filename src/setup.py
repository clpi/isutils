"""
@file setup.py
@author Chris P <clp@clp.is>
"""
# from cx_Freeze import setup, Executable
from __future__ import annotations 
from setuptools import setup
from rich import progress_bar, color, color_triplet, print
import os
import sys
from shutil import copytree, rmtree, copy
import subprocess

PATH = os.path.dirname(os.path.realpath(__file__))

print("[bold green]BEGINNING INSTALLATION...[/bold green]", locals())
print("[green]BEGINNING INSTALLATION...[/green]", locals())

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
