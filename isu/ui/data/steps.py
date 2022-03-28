from isu.ui import UiLoad
from isu.ui.ops.tabs import OpTabs
from isu.ui.ops.tab import TabOp
import os, sys
from dataclasses import dataclass
from typing import List, MutableSequence, Tuple, Dict, Optional, Type, Any
from isu.models.demo import Demo
from isu.ui.comp.prog import Progress
from PySide6.QtCore import (
    QCoreApplication, QDate, QDateTime, QLocale, QObject,
    QDir, Signal, SignalInstance, QBuffer, QSaveFile, Slot, SLOT, SIGNAL
)
from PySide6.QtWidgets import (
    QWidget, QPushButton, QLabel, QTabWidget,
    QTreeWidget, QTableWidget, 
)

@dataclass
class StepData(QTabWidget):
    step: TabOp
    current_step = Signal(TabOp)

    # addStepBtn: QPushButton
    # removeStepBtn: QPushButton
    # stepUpBtn: QPushButton
    # stepDownBtn: QPushButton
    # runBtn: QPushButton

    stepsTable: QTableWidget
    stepOptionsTable: QTableWidget


    stepAddedAt = Signal(int)
    stepRemoved = Signal(int)
    stepIndexShifted = Signal(int, int)

    def __init__(self, parent: QWidget | None) -> None:
        QWidget.__init__(self, parent)
        UiLoad().loadUi("steps.ui", self, parent)
        self.load_data()
        # self.

        self.addStepBtn = self.widget(0).findChild(QPushButton, "addStepBtn")
        self.removeStepBtn = self.findChild(type=QPushButton, name="removeStepBtn")
        self.stepUpBtn = self.findChild(QPushButton, "stepUpBtn")
        self.stepDownBtn = self.findChild(QPushButton, "stepDownBtn")
        self.runBtn = self.findChild(QPushButton, "runBtn")

        self.load_data()



    def load_data(self):
        self.runBtn.setDisabled(True)
        pass
        # self.stepsTreeWidget: QTreeWidget
        # self.ui.find()
        # self.stepsTreeWidget = self.ui.findChild(QTreeWidget, "stepsTreeWidget")

    def add_demo_row(self):
        # checkif sect or step
        row = ""

    def changed_op(self):
        curr_step: QModelIndex = self.stepsTreeWidget.currentIndex()
        wid=self.stepTabs.widget(curr_step.row())
        self.stepTabs.setCurrentIndex(curr_step.row())
        if len(self.ctx.demo_list) > 0:
            curr_demo: int = wid.demoTargetCombo.currentIndex() # type: ignore
            self.set_demo_tree(curr_demo)

    def changed_step_tab(self):
        curr_tab: int = self.stepTabs.currentIndex()
        wid = self.stepTabs.widget(curr_tab)
        self.stepsTreeWidget.setCurrentItem(self.stepsTreeWidget.topLevelItem(curr_tab))
        if len(self.ctx.load.demo) > 0:
            curr_demo: int = wid.demoTargetCombo.currentIndex() # type: ignore
            self.set_demo_tree(curr_demo)
        #self.stepsTreeWidget.setCurrentIndex(curr_tab)

    @Slot(int)
    def get_selected_demo(self):
        pass


    def update_step_op(self, op_idx: int, step_num: int):
        self.stepsTreeWidget.topLevelItem(step_num).setData(1, 0, str(OP_TYPES[op_idx]()))

