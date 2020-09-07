"""
TODO: Separate App Window + tabs from Tab content view + create new tab view
TODO: Add op_type indicator for qtreewidgetitems in step list
TODO: Make separate model / item classes for step list OR sep. QTreeWidget for stepsListTreeWidget
TODO: Figure out script/audio/demo association functionality
"""
import sys, os, functools, typing
from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Optional, Type
from PyQt5.QtCore import ( Qt,
    QObject, pyqtSlot, QFileSelector, QSaveFile, QFileSelector, QTemporaryDir, 
    QTemporaryFile, QAbstractItemModel, QAbstractListModel, pyqtSignal, QModelIndex,
    QSignalMapper
)
from PyQt5.QtGui import (QIcon, QImageIOHandler, QImage, QImageReader, QImageWriter, QStandardItemModel, QStandardItem, QPalette, QColor)
from PyQt5.QtWidgets import ( QWidget,
    QApplication, QMainWindow, QPushButton, QLineEdit, QSpinBox, QMessageBox, QFileDialog, QListWidgetItem,
    QListWidget, QTreeWidget, QTableWidget, QLabel, QTabWidget, QComboBox, QTreeWidgetItem, QTableWidgetItem,
    QAction, QWizard, QWizardPage, QDialog, QUndoView, QProgressBar, QStyle, QStackedWidget
)
from PIL import Image

from models.demo.demo import Demo
from models.operation import Op, ShellOp, InsertOp, SectionOp, AudioOp, CropOp, OP_TYPES
from ui.comp.op import OpWidget
from ui.comp.prefs import Prefs

from PyQt5 import uic

#TODO make function/class which automatically goes thru list of widget names
#     and attaches appropriate functions/functionality
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        path = os.path.join(os.path.dirname(__file__), "main.ui")
        uic.loadUi(path, self)
        self.cx = Context()
        self.load_btn()
        self.load_data()
        self.menubar.setVisible(True)

    def load_btn(self) -> None:
        self.runBtn: QPushButton
        self.addStepBtn: QPushButton
        self.removeStepBtn: QPushButton
        self.browseDemoBtn: QPushButton
        self.browseAudioBtn: QPushButton
        self.browseScriptBtn: QPushButton
        self.stepUpBtn: QPushButton
        self.stepDownBtn: QPushButton

        self.runBtn.clicked.connect(self.run_ops)
        self.addStepBtn.clicked.connect(self.add_step)
        self.removeStepBtn.clicked.connect(self.remove_step)
        self.browseDemoBtn.clicked.connect(self.browse_demo)
        self.browseAudioBtn.clicked.connect(self.browse_audio)
        self.browseScriptBtn.clicked.connect(self.browse_script)

       # self.browseInsertBtn.clicked.connect(self.browse_insert)

    def load_data(self):
        self.centralTabs: QTabWidget
        self.stepsTreeWidget: QTreeWidget
        self.applyToTreeWidget: QTreeWidget
        self.metadataTreeWidget: QTreeWidget
        self.demoTreeWidget: QTreeWidget
        self.stepOptionsListWidget: QListWidget

        self.demoListTreeWidget: QTreeWidget #TODO if num items == 0, disable add_step
        self.scriptListTreeWidget: QTreeWidget
        self.audioListTreeWidget: QTreeWidget

        self.opsParamsTabs: QTabWidget
        self.centralTabs: QTabWidget
        self.opCombo: QComboBox #in op.py
        self.demoSumTitle: QLabel
        self.centralWidget: QWidget

        self.stepTabs: QTabWidget
        self.opsWidget: QWidget #TODO Make this empty w/o a current step active
        self.opsWidget.destroy()
        self.stepTabs.removeTab(0)
        self.stepTabs.clear()

        #self.demoSumListWidget.setModel()
        #self.opCombo.textActivated.connect(self.changed_op)
        self.stepsTreeWidget.currentItemChanged.connect( self.changed_op )
        self.stepTabs.currentChanged.connect(self.changed_step_tab)

    def load_actions(self):
        pass

    #TODO detach these from class
    def browse_demo(self):
        try:
            self.cx.demo_path, _ = QFileDialog.getOpenFileName(self,"Browse for .demo files", "","Demo files (*.demo);;All Files (*)")
            self.load_demo()
        except:
            msg("Must select a demo file", "Error while selecting demo", "Must select demo")
            self.cx.demo_path = ""

    def browse_script(self):
        try:
            self.cx.script_path, _ = QFileDialog.getOpenFileName(self,"Browse for .docx files", "","Word files (*.docx);;All Files (*)")
            if self.cx.demo_path != "":
                self.load_demo()
        except:
            msg("Must select a script file", "Error while selecting script", "Must select script")

    def browse_audio(self):
        try:
            self.cx.audio_dir = QFileDialog.getExistingDirectory(self, "Browse for audio folder")
            if self.cx.demo_path != "":
                self.load_demo()
        except:
            msg("Must select a script file", "Error while selecting script", "Must select script")

    def load_demo(self):
        self.cx.demo = Demo(path=self.cx.demo_path, script_path=self.cx.script_path, audio_dir=self.cx.audio_dir)
        self.demoSumTitle.setText(self.cx.demo.title)
        self.demo_sum_title.setText("DFDF")
        self.demoTreeWidget.insertTopLevelItem(QTreeWidgetItem("Demo tite", self.cx.demo.title))
        tree: QTreeWidget = self.demoTreeWidget
        sect_items: List[QTreeWidgetItem] = []
        step_items: List[QTreeWidgetItem] = []
        for i, sect in enumerate(self.cx.demo.iter_sect()):
            for j, step in enumerate(sect):
                if step.idx == 0:
                    sect_item: QTreeWidgetItem = QTreeWidgetItem([str(i), sect.tite])
                    sect_items.append(sect_item)
                    self.demoTreeWidget.addTopLevelItem(sect_item)
                else:
                    step_item: QTreeWidgetItem = QTreeWidgetItem([str(j), "Step "+str(j), str(step.tp.text != ""), str(step.ci.text!="")])
                    step_items.append(step_item)
                    sect_items[i].addChild(step_item)
        self.demoTreeWidget = tree
                
    def add_util_tab(self):
        pass

    def load_state(self):
        print("BEGIN load_state")

    def save_state(self):
        print("BEGIN save_state")
        print("END save_state")

    def run_ops(self):
        print("BEGIN run_ops")
        out = ""
        for i in range(self.stepsTreeWidget.topLevelItemCount()):
            step = self.stepTabs.widget(i)
            op_type = str(step.op)
            out += op_type
            out += "\n"
        msg(txt=out, inf=out, title="Run")
        print("END run_ops")

    def add_step(self):
        #TODO create model for new steps QTreeWidgetItem
        #TODO create model for list of steps 
        print("BEGIN add_step")
        step_num: int = len(self.cx.ops) + 1
        self.cx.ops.append(OpWidget(parent=self, op_idx=0))
        op = QTreeWidgetItem([str(step_num), str(OP_TYPES[0]()), str(OP_TYPES[0])])
        self.stepsTreeWidget.addTopLevelItem(op)
        self.stepTabs.addTab(self.cx.ops[-1], "Step " + str(step_num))
        self.stepTabs.setCurrentIndex(step_num)
        self.opsParamsTabs.setEnabled(True)
        self.stepsTreeWidget.setCurrentItem(self.stepsTreeWidget.topLevelItem(step_num-1))
        self.update_steps()
        self.stepTabs.widget(step_num-1).opCombo.currentIndexChanged.connect(self.update_steps)
        #self.stepsTreeWidget.currentItem().
        print("END add_step")

    #TODO fix this
    def remove_step(self):
        print("BEGIN remove_step")
        sel_step: QModelIndex = self.stepsTreeWidget.currentIndex()
        self.stepTabs.removeTab(sel_step.row())
        self.stepsTreeWidget.takeTopLevelItem(sel_step.row())
        self.cx.ops.pop(sel_step.row())
        self.update_steps()
        for i in range(self.stepsTreeWidget.topLevelItemCount()):
            self.stepsTreeWidget.topLevelItem(i).setData(0,0,i+1)
            self.stepTabs.setTabText(i, "Step " + str(i+1))
        
        #self.stepsTreeWidget.setCurrentIndex(sel_step.siblingAtRow(sel_step.row()-1))
        #self.opsStack.setCurrentIndex(sel_step.row()-1)
        print("END remove_step")

    def update_steps(self):
        for i in range(self.stepsTreeWidget.topLevelItemCount()):
            step = self.stepTabs.widget(i)
            op_type = str(step.op)
            op_target = str(step.opCombo.currentText())
            demo_target = str(step.demoTargetCombo.currentText())
            self.stepsTreeWidget.topLevelItem(i).setData(0,0,i+1)
            self.stepsTreeWidget.topLevelItem(i).setData(1,0,op_target)
            if demo_target is not None:
                self.stepsTreeWidget.topLevelItem(i).setData(2,0,demo_target)
            else:
                self.stepsTreeWidget.topLevelItem(i).setData(2,0,"No demo")
            self.stepTabs.setTabText(i, "Step " + str(i+1))
            self.stepTabs.setCurrentIndex(self.stepsTreeWidget.currentIndex().row())


    def add_demo_row(self):
        # checkif sect or step
        row = ""

    def changed_op(self):
        curr_step: QModelIndex = self.stepsTreeWidget.currentIndex()
        self.stepTabs.setCurrentIndex(curr_step.row())

    def changed_step_tab(self):
        curr_tab: int = self.stepTabs.currentIndex()
        self.stepsTreeWidget.setCurrentItem(self.stepsTreeWidget.topLevelItem(curr_tab))
        #self.stepsTreeWidget.setCurrentIndex(curr_tab)

    def update_step_op(self, op_idx: int, step_num: int):
        self.stepsTreeWidget.topLevelItem(step_num).setData(1, 0, str(OP_TYPES[op_idx]()))

    def new_central_tab(self, tab_idx: int):
        if tab_idx == self.centralTabs.count()-1:
            self.centralTabs.addTab(QLabel("Hello!"), "New...")
        #if tab_idx == self.centralTabs.:
            #self.centralTabs.addTab(QLabel("Hello!")) #add new util/browse tab
        pass

    def browse(self, target: str): #general browse fn instead of re-making over
        if target == "demo":
            self.cx.demo_path, _ = QFileDialog.getOpenFileName(self,"Browse for .docx files", "","Word files (*.docx);;All Files (*)")
        elif target == "script":
            self.cx.script_path, _ = QFileDialog.getOpenFileName(self,"Browse for .docx files", "","Word files (*.docx);;All Files (*)")
        elif target == "audio":
            pass
        elif target == "shell":
            pass
        elif target == "insert":
            pass
        else: pass

        pass

    def set_demo_tree(self, demo: Demo) -> None:
        tree_model: DemoModel = DemoModel(demo=demo)

    def show_about(self):
        text = "<center>" \
               "<h1>ISCUtils</h1>" \
               "&#8291;" \
               "</center>" \
               "<p>Version 0.0.1<br/>" \
               "Chris P.</p>"
        QMessageBox.about(self, "About Text Editor", text)

    def show_prefs(self):
        prefs = Prefs(parent=self)
        prefs.show()

    def set_op_widget(self, op: str):
        op_wid = OpWidget()
        """Consider making op param non-string, enum or something"""
        pass
        

class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

@pyqtSlot(MainWindow)
def msg(txt: str, inf: str, title: str, det: str = "") -> None:
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(txt)
    msg.setInformativeText(inf)
    msg.setWindowTitle(title)
    if det != "":
        msg.setDetailedText(det)
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.exec_()

class DemoTreeWidget(QTreeWidget):

    def __init__(self, demo_model: DemoModel):
        signal_mapper = QSignalMapper(self)
        self.model = demo_model
        pass

class OpsModel(QAbstractItemModel):

    def __init__(self, demo: Demo):
        pass

class Step(QStandardItem):

    def __init__(self, op_type: Op):
        pass

class Steps(QStandardItemModel):
    def __init__(self):
        pass

    def add_step(self, step: Step):
        pass

class DemoModel(QStandardItemModel):

    def __init__(self, demo: Demo):
        pass

class StepMetadata(QStandardItemModel):

    def __init__(self):
        pass

class SectMetadata(QStandardItemModel):

    def __init__(self):
        pass

def set_fusion(app: QApplication, dark: bool = False):
    app.setStyle("Fusion")
    if dark:
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        app.setPalette(palette)

@dataclass
class Context:
    demo_load: List[Demo] = field(default_factory=list)
    demo_paths: List[str] = field(default_factory=list)
    script_load: List[str] = field(default_factory=list)
    audio_load: List[str] = field(default_factory=list)
    ops: List[QWidget] = field(default_factory=list)
    current_op: int = 0


def run():
    app = QApplication(sys.argv)
    set_fusion(app, dark=False)
    window = MainWindow()
    window.show()
    app.exec_()