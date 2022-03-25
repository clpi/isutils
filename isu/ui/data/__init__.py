""" NOTE :
    The data component of the larger UI module represents the leftmost
    ppart of the screen, anything to do with loading, planning, and reflecting
    the strategy regarding any the order or targets for which their specific
    requested operations (in the middle tab) are to be furnished
"""
from PySide6.QtCore import QObject, QMetaObject
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QTabWidget
from isu.ui import UiLoad


class DataPane(QObject):
    loadedDataTabs: None | QTabWidget = None
    opOrderTabs: None | QTabWidget = None
    