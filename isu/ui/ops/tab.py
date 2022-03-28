"""
TODO: Split off each ops params view into own separate QWidget?
"""
import sys, os, pathlib
from typing import Optional, List, Dict, Any, Type, Tuple
from PIL import Image
from pathlib import Path
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import (Qt, QObject, Slot, Signal, QFile, QDir)
from PySide6.QtWidgets import (QWidget, QDialog, QListWidget, QPushButton,
    QComboBox, QListWidgetItem, QTreeWidget, QTreeWidgetItem, QTabWidget,
    QApplication, QLineEdit, QSpinBox, QStackedWidget, QFileDialog, QCheckBox)
from isu.operation import OP_TYPES, Shell, Insert, Section, Audio, Crop, Render , Pace, Text
from isu.operation.operation import Op
from isu.models.demo import Demo
from isu.ui import UiLoad
from isu.ui.ops import OpType, ops, shell, section, insert, crop, audio, render, pace, text #  ShellOp, SectionOp, InsertOp, CropOp, AudioOp, RenderOp, PaceOp, TextOp, OP_UI_TYPES
from isu.ui.ops.ops import OpUi, to_op_type, to_ui_type

class TabOp(QWidget):
    """_summary_
    Represents a single step in a multi-demo multi-operation pipeline.

    Args:
        QWidget (_type_): _description_
    """

    demo_index = Signal(int)
    op_index = Signal(int)

    def __init__(self, parent: Optional[QWidget] = None, index: int = 0):
        QWidget.__init__(self, parent)
        UiLoad().loadUi("tab.ui", self, parent)
        self.index: int = index # NOTE: index of the currently selected step
        self.demo_idx: int = 0 # NOTE: index of currently selected demo
        self.apply_to_demo: Optional[Demo] = None #Stores in memory the demo which the operation will be performed on
        self.apply_to_mask: Optional[List[List[bool]]] = None #Maps every step in every section to True/false value to apply op to
        self.load_ui()

    def load_ui(self):
        self.load_btn()
        self.load_stack_data()
        self.load_data()

    def broadcast_demo_idx(self):
        self.demo_index.emit(self.demoCombo.currentIndex())

    def broadcast_op_idx(self):
        self.op_index.emit(self.opCombo.currentIndex())

    def curr_optype(self) -> Type[Op]:
        return to_op_type(self.opCombo.currentIndex())

    def curr_opuitype(self) -> Type[OpUi]:
        return to_ui_type(self.opCombo.currentIndex())

    def curr_opui(self) -> OpUi:
        return self.ops[self.index]
        
    def curr_op(self) -> Op:
        return self.curr_opui().op(self.index)

    @Slot()
    def on_step_update(self) -> None:
        pass

    @Slot()
    def on_op_update(self) -> None:
        pass

    def load_stack_data(self):
        self.ops = [
            shell.ShellOp(parent=self),
            insert.InsertOp(parent=self),
            crop.CropOp(parent=self),
            section.SectionOp(parent=self),
            audio.AudioOp(parent=self),
            pace.PaceOp(parent=self),
            text.TextOp(parent=self),
            render.RenderOp(parent=self),
        ]
        self.shellOp: shell.ShellOp = self.ops[0]
        self.insertOp: insert.InsertOp = self.ops[1]
        self.cropOp: crop.CropOp = self.ops[2]
        self.sectionOp: section.SectionOp = self.ops[3]
        self.audioOp: audio.AudioOp = self.ops[4]
        self.paceOp: pace.PaceOp = self.ops[5]
        self.textOp: text.TextOp = self.ops[6]
        self.renderOp: render.RenderOp = self.ops[7]

        for op in self.ops: self.opsParamsStack.addWidget(op)

        self.opsParamsStack.setCurrentIndex(0)
        self.opCombo.setCurrentIndex(0)
        self.op=self.curr_opui()

    def load_btn(self):
        self.resetStepParamsBtn: QPushButton
        self.saveStepParamsBtn: QPushButton

        self.resetStepParamsBtn.toggle.connect(self.reset_step_params)
        self.saveStepParamsBtn.toggle.connect(self.save_step_params)

    def load_data(self):
        self.opsParamsStack: QStackedWidget
        self.opCombo: QComboBox
        self.demoCombo: QComboBox
        self.allStepsCheck: QCheckBox
        self.matchSubstringCheck: QCheckBox

        # self.applyToTreeWidget: QTreeWidget

        # self.demoCombo.connect()
        self.demoCombo.currentIndex.connect(self.demo_changed)
        # self.opCombo.currentIndex.connect(self.op_changed)

    @Slot(int)
    def demo_changed(self, d_idx: int):
        self.demo_idx = d_idx
        # self.demoCombo.set

    @Slot()
    def op_combo_changed(self) -> None:
        self.index =self.opCombo.currentIndex() 
        self.op_combo_idx_changed(self.index)

    @Slot(int)
    def op_combo_idx_changed(self, idx: int ) -> None:
        self.index=idx
        self.opsParamsStack.setCurrentIndex(self.index)
        self.op = self.curr_op()
        # TODO: Set stepsreeWidget to match up!!
        #self.parentWidget().parentWidget().parentWidget().stepsTreeWidget.topLevelItem(idx.row()).setData(1,0,get_op(op_idx))

    @Slot()
    def run_op(self, demo: Demo) -> None:
        self.curr_op().run(demo)

    def add_step(self) -> None:
        pass

    def add_sect(self) -> None:
        pass

    def get_apply_to(self) -> List[List[bool]]:
        return [[]]

    def save_step_params(self):
        pass

    def reset_step_params(self):
        pass


class OpContext:

    def __init__(self, op_idx: int):
        self.op_idx = op_idx

if __name__ == "__main__":
    a = QApplication(sys.argv)
    o = TabOp()
    o.show()
    sys.exit(a.exec())