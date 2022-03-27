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
class StepsView(QTabWidget):
    ui: QWidget

    addStepBtn: QPushButton
    removeStepBtn: QPushButton
    stepUpBtn: QPushButton
    stepDownBtn: QPushButton
    runBtn: QPushButton

    stepsTable: QTableWidget
    stepOptionsTable: QTableWidget


    stepAddedAt = Signal(int)
    stepRemoved = Signal(int)
    stepIndexShifted = Signal(int, int)

    def __init__(self, parent: Any | None = None):
        QTabWidget.__init__(self)
        uidir = QDir(os.path.dirname(__file__))
        loader = UiLoad(name="steps.ui", dir=uidir, parent=parent)
        self.ui: QWidget = loader.load_ui()
        self.addStepBtn = self.ui.findChild(type=QPushButton, name="addStepBtn")
        self.removeStepBtn = self.ui.findChild(type=QPushButton, name="removeStepBtn")
        self.stepUpBtn = self.ui.findChild(QPushButton, "stepUpBtn")
        self.stepDownBtn = self.ui.findChild(QPushButton, "stepDownBtn")
        self.runBtn: QWidget = self.ui.findChild(QPushButton, "runBtn")

        self.load_data()



    def load_data(self):
        self.runBtn.setDisabled(True)
        pass
        # self.stepsTreeWidget: QTreeWidget
        # self.ui.find()
        # self.stepsTreeWidget = self.ui.findChild(QTreeWidget, "stepsTreeWidget")

    def run_ops(self):
        print("[Window.run_ops] BEGIN run_ops")
        out = ""
        self.opprog = Progress(parent=self, len=len(self.cx.ops))
        self.opprog.show()
        for i in range(self.stepsTreeWidget.topLevelItemCount()):
            self.step: TabOp = self.stepTabs.widget(i)
            self.optype: Type[Op] = self.step.curr_optype()
            self.opprog.set_optype(self.optype)
            demo = self.ctx.demo_list[self.step.demoTargetCombo.currentIndex()]
            op: Op = self.step.curr_op()
            op.updated.connect(self.opprog.progress)
            op.finished.connect(self.update_progress)
            op.run(demo)
            if self.step.opCombo.currentIndex() == 2: #section -> destructive to script - demo connection
                self.ctx.demo_list[self.step.demoTargetCombo.currentIndex()] = Demo(path=demo.file, audio_dir=demo.audio_dir, script_path=demo.script_path)
        msg(txt="[Window.run_ops] Finished running operations", inf=out, title="Finished")
        print("[Window.run_ops] END run_ops")


    def add_step(self):
        #TODO create model for new steps QTreeWidgetItem
        #TODO create model for list of steps 
        print("BEGIN add_step")
        step_num: int = len(self.cx.ops) + 1
        tab = TabOp(parent=self, index=step_num)
        self.cx.ops.append(tab)
        op = QTreeWidgetItem([str(step_num), str(OP_TYPES[0]), str(OP_TYPES[0])])
        self.stepsTreeWidget.addTopLevelItem(op)
        self.stepTabs.addTab(self.cx.ops[-1], "Step " + str(step_num))
        self.stepTabs.setCurrentIndex(step_num)
        self.stepsTreeWidget.setCurrentItem(self.stepsTreeWidget.topLevelItem(step_num-1))
        self.update_steps()
        self.stepTabs.widget(step_num-1).opCombo.currentIndexChanged.connect(self.update_steps)
        self.stepTabs.widget(step_num-1).demoTargetCombo.currentIndexChanged.connect(self.update_steps)
        self.stepTabs.widget(step_num-1).demoTargetCombo.addItems(self.cx.demo_list_titles())
        #self.stepsTreeWidget.currentItem().
        self.update_steps()
        self.runBtn.setEnabled(True)
        print("END add_step")

    #TODO fix this
    def remove_step(self):
        print("BEGIN remove_step")
        sel_step: QModelIndex = self.stepsTreeWidget.currentIndex()
        self.stepTabs.removeTab(sel_step.row())
        self.stepsTreeWidget.takeTopLevelItem(sel_step.row())
        self.cx.ops.ops.remove()
        self.update_steps()
        for i in range(self.stepsTreeWidget.topLevelItemCount()):
            self.stepsTreeWidget.topLevelItem(i).setData(0,0,i+1)
            self.stepTabs.setTabText(i, "Step " + str(i+1))
        #self.stepsTreeWidget.setCurrentIndex(sel_step.siblingAtRow(sel_step.row()-1))
        #self.opsStack.setCurrentIndex(sel_step.row()-1)
        print("END remove_step")


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

