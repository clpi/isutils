from dataclasses import dataclass


from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QObject
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QTabWidget

@dataclass
class StepsTab(QObject):
    ui: QWidget | None = None

