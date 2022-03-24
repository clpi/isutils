import argparse
import sys, os
import isu
from isu.app import MainApp

def args() -> argparse.ArgumentParser:
    """ Get args """
    p = argparse.ArgumentParser(prog="isu", description=isu.__description__)
    p.add_argument('-D', '--dir', help="Directory to run isu on")
    p.add_argument('-V', '--version', action='version', version=f"%(prog)s {isu.__version__}")
    p.add_argument('-C', '--config', help="Config file to use")
    p.add_argument('-H', '--headless', action='store_true', help="Run in headless mode")
    p.add_argument('-d', '--debug', action='store_true', help="Run in debug mode")
    return p
    

def main():
    # argv = sys.argv[1:]
    # parser: argparse.ArgumentParser = args()
    # args: argparse.Namespace = parser.parse_args(argv)
    app = MainApp()
    app.run()
