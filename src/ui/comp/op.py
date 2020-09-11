"""
TODO: Split off each ops params view into own separate QWidget?
TODO: Consider having op type selection be before view is created?
TODO: Consider having op-type params be non-str
TODO: Make default op view be blank, only show params view when one is selected
"""
import sys, os
from typing import Optional, List, Dict, Any, Type
from PyQt5 import uic
from PyQt5.QtCore import (Qt, QObject, pyqtSlot, pyqtSignal)
from PyQt5.QtWidgets import (QWidget, QDialog, QListWidget, QPushButton,
    QComboBox, QListWidgetItem, QTreeWidget, QTreeWidgetItem, 
    QApplication, QLineEdit, QSpinBox, QStackedWidget, QFileDialog, QCheckBox)
from models.operation import Op, ShellOp, InsertOp, SectionOp, AudioOp, CropOp, get_op
from models.demo.demo import Demo

class OpWidget(QWidget):

    def __init__(self, op_idx: int=0, parent: Optional[QWidget] = None):
        """Initializes """

        self.apply_to_demo: Optional[Demo] = None #Stores in memory the demo which the operation will be performed on
        self.apply_to_mask: Optional[List[List[bool]]] = None #Maps every step in every section to True/false value to apply op to
        super().__init__(parent)
        path = os.path.join(os.path.dirname(__file__), "op.ui")
        uic.loadUi(path, self)
        self.set_op(op_idx)
        self.load_btn()
        self.load_stack()
        self.load_data()

    def load_btn(self): 
        self.insertBrowseImgBtn: QPushButton
        self.shellBrowseImgBtn: QPushButton
        self.resetStepParamsBtn: QPushButton
        self.saveStepParamsBtn: QPushButton

        self.shellBrowseImgBtn.clicked.connect(self.browse_shell)
        self.insertBrowseImgBtn.clicked.connect(self.browse_insert)
        self.resetStepParamsBtn.clicked.connect(self.reset_step_params)
        self.saveStepParamsBtn.clicked.connect(self.save_step_params)

    def load_stack(self):
        self.opsParamsStack: QStackedWidget
        self.shellTab: QWidget
        self.insertTab: QWidget
        self.sectionTab: QWidget
        self.audioTab: QWidget
        self.cropTab: QWidget

    def load_data(self):
        self.demoTargetCombo: QComboBox
        self.opCombo: QComboBox
        self.allStepsCheck: QCheckBox
        self.matchSubstringCheck: QCheckBox
        # Shell ------------------->
        self.shellImgPath: QPushButton
        self.shellFgX: QSpinBox
        self.shellFgY: QSpinBox
        self.shellFgW: QSpinBox
        self.shellFgH: QSpinBox
        # Insert ----------------->
        self.insertImgPath: QPushButton
        self.insertFgX: QSpinBox
        self.insertFgY: QSpinBox
        self.insertFgW: QSpinBox
        self.insertFgH: QSpinBox
        # Audio ----------------->
        # Crop ------------------>
        # Section --------------->
        # Apply to -------------->
        self.applyToTreeWidget: QTreeWidget

        self.opCombo.currentIndexChanged.connect(self.op_changed)

    def set_demo(self, demo: Demo):
        self.apply_to_demo = demo
        self.demoTargetCombo.set

    def set_op(self, op_idx: int):
        self.op = get_op(op_idx)()
        self.opsParamsStack.setCurrentIndex(op_idx)

    #@pyqtSignal(int)
    def op_changed(self, op_idx: int) -> None:
        #self.op_idx = self.opCombo.currentIndex()
        #idx = self.parentWidget().parentWidget().parentWidget().stepsTreeWidget.indexFromItem(self)
        #self.parentWidget().parentWidget().parentWidget().stepsTreeWidget.topLevelItem(idx.row()).setData(1,0,get_op(op_idx))
        #self.op = OP_TYPES[op_idx]()
        print(op_idx)
        print(self.op)


    def get_params(self) -> Dict[str, Any]:
        demo_idx: int = self.demoTargetCombo.currentIndex() #get corr. demo
        op_idx: int = self.opCombo.currentIndex() 
        op_type: Type[Op] = get_op(op_idx)
        params: Dict[str, Any] = op_type().get_params()
        return params

    def run_op(self) -> None:
        params = self.get_params()

    def add_step(self) -> None:
        pass

    def add_sect(self) -> None:
        pass

    def get_apply_to(self) -> List[List[bool]]:
        pass

    def browse_insert(self):
        try:
            fileName, _ = QFileDialog.getOpenFileName(self,"Browse for image files", "","All Files (*);;PNG files (*.png)")
            img_tmp = Image.open(fileName)
            iwidth, iheight = img_tmp.size
            if self.demo is not None:
                if iwidth > self.demo.res[0] or iheight > self.demo.res[1]:
                    pass
            #set op img path, def dims
        except:
            pass

    def browse_shell(self):
        try:
            fileName, _ = QFileDialog.getOpenFileName(self,"Browse for image files", "","All Files (*);;PNG files (*.png)")
            img_tmp = Image.open(fileName)
            iwidth, iheight = img_tmp.size
            if self.demo is not None:
                if iwidth > self.demo.res[0] or iheight > self.demo.res[1]:
                    pass
            #set op img path, def dims
        except: pass

    def save_step_params(self):
        pass

    def reset_step_params(self):
        pass


class OpContext:

    def __init__(self, op_idx: int):
        self.op_idx = op_idx

