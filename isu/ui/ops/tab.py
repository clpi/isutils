"""
TODO: Split off each ops params view into own separate QWidget?
"""
import sys, os, pathlib
from typing import Optional, List, Dict, Any, Type, Tuple
from PIL import Image
from pathlib import Path
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import (Qt, QObject, Slot, Signal, QFile)
from PySide6.QtWidgets import (QWidget, QDialog, QListWidget, QPushButton,
    QComboBox, QListWidgetItem, QTreeWidget, QTreeWidgetItem, 
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
        super(QWidget, self).__init__(parent)
        self.index: int = index # NOTE: index of the currently selected step
        self.demo_idx: int = 0 # NOTE: index of currently selected demo
        self.apply_to_demo: Optional[Demo] = None #Stores in memory the demo which the operation will be performed on
        self.apply_to_mask: Optional[List[List[bool]]] = None #Maps every step in every section to True/false value to apply op to
        self.ui = UiLoad(name="tab.ui", parent=parent)
        self.load_btn(parent=parent)
        self.load_stack_data(parent=parent)
        self.load_data(parent=parent)

    def broadcast_demo_idx(self):
        self.demo_index.emit(self.demoTargetCombo.currentIndex())

    def broadcast_op_idx(self):
        self.op_index.emit(self.opCombo.currentIndex())

    def curr_optype(self) -> Type[Op]:
        return to_op_type(self.opCombo.currentIndex())

    def curr_opuitype(self) -> Type[OpUi]:
        return to_ui_type(self.opCombo.currentIndex())

    def curr_opui(self) -> OpUi:
        return self.ops[self.opCombo.currentIndex()]
        
    def curr_op(self) -> Op:
        return self.curr_opui().op()

    @Slot()
    def on_step_update(self) -> None:
        pass

    @Slot()
    def on_op_update(self) -> None:
        pass

    def load_stack_data(self, parent: Any):
        self.ops = [
            shell.ShellOp(parent=self, index=self.index),
            insert.InsertOp(parent=self, index=self.index),
            crop.CropOp(parent=self, index=self.index),
            section.SectionOp(parent=self, index=self.index),
            audio.AudioOp(parent=self, index=self.index),
            pace.PaceOp(parent=self, index=self.index),
            text.TextOp(parent=self, index=self.index),
            render.RenderOp(parent=self, index=self.index),
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

    def load_btn(self, parent: None | QWidget = None):
        self.resetStepParamsBtn: QPushButton
        self.saveStepParamsBtn: QPushButton

        self.resetStepParamsBtn.toggle.connect(self.reset_step_params)
        self.saveStepParamsBtn.toggle.connect(self.save_step_params)

    def load_data(self, parent: None | QWidget = None):
        self.opsParamsStack: QStackedWidget
        self.opCombo: QComboBox
        self.demoTargetCombo: QComboBox
        self.allStepsCheck: QCheckBox
        self.matchSubstringCheck: QCheckBox

        # self.applyToTreeWidget: QTreeWidget

        self.demoTargetCombo.connect()
        self.demoTargetCombo.currentIndexChanged.connect(self.demo_changed)
        self.opCombo.currentIndexChanged.connect(self.op_changed)

    @pyqtSlot(int)
    def demo_changed(self, d_idx: int):
        self.demo_idx = d_idx
        # self.demoTargetCombo.set

    @pyqtSlot(int)
    def op_changed(self, op_idx: int) -> None:
        self.index=op_idx
        self.opsParamsStack.setCurrentIndex(op_idx)
        self.op = self.ops[op_idx]
        #self.op_idx = self.opCombo.currentIndex()
        #idx = self.parentWidget().parentWidget().parentWidget().stepsTreeWidget.indexFromItem(self)
        #self.parentWidget().parentWidget().parentWidget().stepsTreeWidget.topLevelItem(idx.row()).setData(1,0,get_op(op_idx))


    def get_params(self) -> Dict[str, Any]:
        demo_idx: int = self.demoTargetCombo.currentIndex() #get corr. demo
        params: Dict[str, Any] = self.curr_op().get_params()
        return params

    @pyqtSlot()
    def run_op(self, demo: Demo) -> None:
        self.curr_op().run(demo)
        # params = self.get_params()
        # op_idx = self.opCombo.currentIndex()
        # print(f"OP IDX: {op_idx}")
        # op_type = OP_TYPES[op_idx]
        # # op.op().run(demo)
            
        # if op_idx == OpKind.Shell:
        #     print("RUNNING INSERT OPERATION")
            
        # elif op_idx == OpKind.Insert: #insert #TODO fix insert algo in demo model
        #     print("RUNNING INSERT OPERATION")
        #     self.op.op().run()
        #     Insert(self.demo()).run()

        # elif op_idx == OpKind.Section: #section
        #     print("RUNNING SECTION OPERATION")
        #     Section().run(demo)

        # elif op_idx == OpKind.Audio: #audio
        #     print("RUNNING AUDIO OPERATION")
        #     Audio().run(demo)

        # elif op_idx == OpKind.Crop: #crop
        #     Crop().run(demo)

        # elif op_idx == OpKind.Pace:
        #     Pace().run(demo)

        # elif op_idx == OpKind.Text:
        #     Text().run(demo)
        
        # elif op_idx == OpKind.Render:
        #     print("RUNNING RENDER OPERATION")
        #     print("DIR: " + self.renderOutputDir.text() + ", TITLE: " + self.renderOutputTitle.text())
        #     out_title = self.renderOutputTitle.text()
        #     out_dir = Path(self.renderOutputDir.text())
        #     out_format = "avi"
        #     if out_dir.is_dir():
        #         out_path = os.path.join(out_dir, out_title + "." + out_format)
        #         print("OUTPATH: " + out_path)
        #         # out_path: str = self.renderOutputDir.text() + "\\" + self.renderOutputTitle.text()
        #         RenderOp(out_path=pathlib.Path(out_path)).run(demo)
        #     else:
        #         print("NOT VALID DIR")

        # else:
        #     pass
            

        # op_type = self.opCombo.currentIndex()

    def add_step(self) -> None:
        pass

    def add_sect(self) -> None:
        pass

    def get_apply_to(self) -> List[List[bool]]:
        return [[]]

    def browse_insert(self):
        try:
            fileName, _ = QFileDialog.getOpenFileName(self,"Browse for image files", "","All Files (*);;PNG files (*.png)")
            self.insertImgPath.setText(fileName)
            img_tmp = Image.open(fileName)
            iwidth, iheight = img_tmp.size
            if self.demo is not None:
                if iwidth > self.demo.res[0] or iheight > self.demo.res[1]:
                    pass
            #set op img path, def dims
        except:
            pass


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