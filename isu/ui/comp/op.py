# """
# TODO: Split off each ops params view into own separate QWidget?
# TODO: Consider having op type selection be before view is created?
# TODO: Consider having op-type params be non-str
# TODO: Make default op view be blank, only show params view when one is selected
# """
# import sys, os, pathlib
# from typing import Optional, List, Dict, Any, Type, Tuple
# from PIL import Image
# from pathlib import Path
# from PyQt6 import uic
# from PyQt6.QtCore import (Qt, QObject, pyqtSlot, pyqtSignal)
# from PyQt6.QtWidgets import (QWidget, QDialog, QListWidget, QPushButton,
#     QComboBox, QListWidgetItem, QTreeWidget, QTreeWidgetItem, 
#     QApplication, QLineEdit, QSpinBox, QStackedWidget, QFileDialog, QCheckBox)
# from isu.operation import Op, Shell, Insert, Section, Audio, Crop, Render, get_op
# from isu.models.demo import Demo

# class OpWidget(QWidget):

#     def __init__(self, op_idx: int=0, parent: Optional[QWidget] = None):
#         """Initializes """

#         self.apply_to_demo: Optional[Demo] = None #Stores in memory the demo which the operation will be performed on
#         self.apply_to_mask: Optional[List[List[bool]]] = None #Maps every step in every section to True/false value to apply op to
#         super().__init__(parent)
#         path = os.path.join(os.path.dirname(__file__), "op.ui")
#         uic.loadUi(path, self)
#         self.set_op(op_idx)
#         self.load_btn()
#         self.load_stack()
#         self.load_data()

#     def load_btn(self): 
#         self.insertBrowseImgBtn: QPushButton
#         self.shellBrowseImgBtn: QPushButton
#         self.resetStepParamsBtn: QPushButton
#         self.saveStepParamsBtn: QPushButton

#         self.shellBrowseImgBtn.clicked.connect(self.browse_shell)
#         self.insertBrowseImgBtn.clicked.connect(self.browse_insert)
#         self.resetStepParamsBtn.clicked.connect(self.reset_step_params)
#         self.saveStepParamsBtn.clicked.connect(self.save_step_params)

#     def load_stack(self):
#         self.opsParamsStack: QStackedWidget

#         self.shellTab: QWidget # 0
#         self.insertTab: QWidget # 1
#         self.sectionTab: QWidget # 2
#         self.audioTab: QWidget # 3
#         self.cropTab: QWidget # 4
#         self.composeTab: QWidget # 5
#         self.resizeTab: QWidget # 6
#         self.pacingTab: QWidget # 7
#         self.animateTab: QWidget # 8
#         self.renderTab: QWidget # 9

#     def load_data(self):
#         self.demoTargetCombo: QComboBox
#         self.opCombo: QComboBox
#         self.allStepsCheck: QCheckBox
#         self.matchSubstringCheck: QCheckBox
#         # 1 Shell ------------------->
#         self.shellImgPath: QLineEdit
#         self.shellFgX: QSpinBox
#         self.shellFgY: QSpinBox
#         self.shellFgW: QSpinBox
#         self.shellFgH: QSpinBox
#         # Insert ----------------->
#         self.insertImgPath: QLineEdit
#         self.insertFgX: QSpinBox
#         self.insertFgY: QSpinBox
#         self.insertFgW: QSpinBox
#         self.insertFgH: QSpinBox
#         # Audio ----------------->
#         # Crop ------------------>
#         # Section --------------->
#         # Apply to -------------->
#         self.applyToTreeWidget: QTreeWidget
#         # Render to video ------->
#         self.renderOutputTitle: QLineEdit
#         self.renderOutputDir: QLineEdit
#         self.renderOutputFormat: QComboBox

#         self.opCombo.currentIndexChanged.connect(self.set_op)
#         self.renderOutputTitle.textChanged[str].connect(self.set_rtitle)

#     def set_rtitle(self, t: str):
#         self.renderOutputTitleStr = t

#     def set_demo(self, demo: Demo):
#         self.apply_to_demo = demo
#         # self.demoTargetCombo.set

#     def set_op(self, op_idx: int):
#         self.op = get_op(op_idx)()
#         self.opsParamsStack.setCurrentIndex(op_idx)

#     #@pyqtSignal(int)
#     def op_changed(self, op_idx: int) -> None:
#         #self.op_idx = self.opCombo.currentIndex()
#         #idx = self.parentWidget().parentWidget().parentWidget().stepsTreeWidget.indexFromItem(self)
#         #self.parentWidget().parentWidget().parentWidget().stepsTreeWidget.topLevelItem(idx.row()).setData(1,0,get_op(op_idx))
#         #self.op = OP_TYPES[op_idx]()
#         print(op_idx)
#         print(self.op)


#     def get_params(self) -> Dict[str, Any]:
#         demo_idx: int = self.demoTargetCombo.currentIndex() #get corr. demo
#         op_idx: int = self.opCombo.currentIndex() 
#         op_type: Type[Op] = get_op(op_idx)
#         params: Dict[str, Any] = op_type().get_params()
#         return params

#     def run_op(self, demo: Demo) -> None:
#         op_idx = self.opCombo.currentIndex()
#         print(f"OP IDX: {op_idx}")
#         op_type = get_op(op_idx)
#         if op_idx == 0: #shell
#             print("RUNNING SHELL OPERATION")
#             s_img_path: str = self.shellImgPath.text()
#             s_fg_coord: Tuple[int, int] = (self.shellFgX.value(), self.shellFgY.value())
#             s_fg_dim: Tuple[int, int] = (self.shellFgW.value(), self.shellFgH.value())
#             ShellOp(img_path=s_img_path, fg_coord=s_fg_coord, fg_dim=s_fg_dim).run(demo)
#         elif op_idx == 1: #insert #TODO fix insert algo in demo model
#             print("RUNNING INSERT OPERATION")
#             i_img_path: str = self.insertImgPath.text()
#             i_fg_coord: Tuple[int, int] = (self.insertFgX.value(), self.insertFgY.value())
#             i_fg_dim: Tuple[int, int] = (self.insertFgW.value(), self.insertFgH.value())
#             InsertOp(img_path=i_img_path, fg_coord=i_fg_coord, fg_dim=i_fg_dim).run(demo)
#         elif op_idx == 2: #section
#             print("RUNNING SECTION OPERATION")
#             SectionOp().run(demo)
#         elif op_idx == 3: #audio
#             print("RUNNING AUDIO OPERATION")
#             AudioOp().run(demo)
#         elif op_idx == 4: #crop
#             pass
#         elif op_idx == 5: #crop
#             pass
#         elif op_idx == 6: #crop
#             pass
#         elif op_idx == 7: #crop
#             pass
#         elif op_idx == 8: #render
#             print("RUNNING  OPERATION")
#         elif op_idx == 9: #render
#             print("RUNNING RENDER OPERATION")
#             print("DIR: " + self.renderOutputDir.text() + ", TITLE: " + self.renderOutputTitle.text())
#             out_title = self.renderOutputTitle.text()
#             out_dir = Path(self.renderOutputDir.text())
#             out_format = "avi"
#             if out_dir.is_dir():
#                 out_path = os.path.join(out_dir, out_title + "." + out_format)
#                 print("OUTPATH: " + out_path)
#                 # out_path: str = self.renderOutputDir.text() + "\\" + self.renderOutputTitle.text()
#                 RenderOp(out_path=pathlib.Path(out_path)).run(demo)
#             else:
#                 print("NOT VALID DIR")

#         else:
#             pass
            

#         # op_type = self.opCombo.currentIndex()
#         params = self.get_params()

#     def add_step(self) -> None:
#         pass

#     def add_sect(self) -> None:
#         pass

#     def get_apply_to(self) -> List[List[bool]]:
#         pass

#     def browse_insert(self):
#         try:
#             fileName, _ = QFileDialog.getOpenFileName(self,"Browse for image files", "","All Files (*);;PNG files (*.png)")
#             self.insertImgPath.setText(fileName)
#             img_tmp = Image.open(fileName)
#             iwidth, iheight = img_tmp.size
#             if self.demo is not None:
#                 if iwidth > self.demo.res[0] or iheight > self.demo.res[1]:
#                     pass
#             #set op img path, def dims
#         except:
#             pass

#     def browse_shell(self):
#         try:
#             fileName, _ = QFileDialog.getOpenFileName(self,"Browse for image files", "","All Files (*);;PNG files (*.png)")
#             self.shellImgPath.setText(fileName)
#             img_tmp = Image.open(fileName)
#             iwidth, iheight = img_tmp.size
#             if self.demo is not None:
#                 if iwidth > self.demo.res[0] or iheight > self.demo.res[1]:
#                     pass
#             #set op img path, def dims
#         except: pass

#     def save_step_params(self):
#         pass

#     def reset_step_params(self):
#         pass


# class OpContext:

#     def __init__(self, op_idx: int):
#         self.op_idx = op_idx

# if __name__ == "__main__":
#     a = QApplication(sys.argv)
#     o = OpWidget()
#     o.show()
#     sys.exit(a.exec())