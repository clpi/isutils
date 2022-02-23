"""
TODO: Separate App Window + tabs from Tab  view + create new tab view
TODO: Make right pane tabbed per-demo like the middle is (per step)
TODO: Add op_type indicator for qtreewidgetitems in step list
TODO: Make separate model / item classes for step list OR sep. QTreeWidget for stepsListTreeWidget
TODO: Figure out script/audio/demo association functionality
"""
import sys, os, functools, typing
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Optional, Type, Any
from PySide6.QtCore import ( 
    QObject, Slot, QFileSelector, QSaveFile, QFileSelector, QTemporaryDir, 
    QTemporaryFile, QAbstractItemModel, QAbstractListModel, Signal, QModelIndex,
    QSignalMapper, QProcess
)
from PySide6.QtGui import (QIcon,
    QImageIOHandler, QImage, QImageReader, QAction, QIcon,
    QImageWriter, QStandardItemModel, QStandardItem, QPalette, QColor, QColorConstants,
)
from PySide6.QtDesigner import QPyDesignerCustomWidgetCollection, QFormBuilder
from PySide6.QtMultimedia import QMediaPlayer, QAudio, QMediaFormat
from PySide6.QtMultimediaWidgets import QGraphicsVideoItem, QVideoWidget
from PySide6.QtWidgets import ( QWidget,
    QColorDialog,

    QMenuBar,QProgressDialog,
    QApplication, QMainWindow, QPushButton, QLineEdit, QSpinBox, QMessageBox, QFileDialog, QListWidgetItem,
    QListWidget, QTreeWidget, QTableWidget, QLabel, QTabWidget, QComboBox, QTreeWidgetItem, QTableWidgetItem,
    QWizard, QWizardPage, QDialog, QUndoView, QProgressBar, QStyle, QStackedWidget, QGroupBox,
    QInputDialog
)
from PIL import Image

from models.demo.demo import Demo
from models.operation import Op, ShellOp, InsertOp, SectionOp, AudioOp, CropOp, OP_TYPES
from ui.comp.op import OpWidget
from ui.comp.prefs import Prefs

from PySide6.QtUiTools import QUiLoader

#TODO make function/class which automatically goes thru list of widget names
#     and attaches appropriate functions/functionality
class MainWindow(QWidget):

    def __init__(self, *args, **kwargs) -> None:
        self.cx = Context()
        self.load_btn()
        self.load_data()
        self.menubar.setVisible(True) #type: ignore

    def load_btn(self) -> None:
        self.runBtn: QPushButton # type: ignore
        self.addStepBtn: QPushButton # type: ignore
        self.removeStepBtn: QPushButton # type: ignore
        self.browseDemoBtn: QPushButton # type: ignore
        self.browseAudioBtn: QPushButton # type: ignore
        self.browseScriptBtn: QPushButton # type: ignore
        self.loadScriptBtn: QPushButton # type: ignore
        self.loadAudioBtn: QPushButton # type: ignore
        self.infoBtn: QPushButton # type: ignore
        self.addDemoBtn: QPushButton # type: ignore
        self.removeDemoBtn: QPushButton # type: ignore
        self.stepUpBtn: QPushButton # type: ignore
        self.stepDownBtn: QPushButton # type: ignore

        self.loadScriptBtn.setEnabled(False)
        self.loadAudioBtn.setEnabled(False)
        self.runBtn.setEnabled(False)

        self.runBtn.clicked.connect(self.run_ops) # type: ignore
        self.addStepBtn.clicked.connect(self.add_step) # type: ignore
        self.removeStepBtn.clicked.connect(self.remove_step) # type: ignore
        self.browseDemoBtn.clicked.connect(self.browse_demo) # type: ignore
        self.addDemoBtn.clicked.connect(self.browse_demo) # type: ignore
        self.browseAudioBtn.clicked.connect(self.browse_audio) # type: ignore
        self.browseScriptBtn.clicked.connect(self.browse_script) # type: ignore
        self.loadScriptBtn.clicked.connect(self.browse_script) # type: ignore
        self.loadAudioBtn.clicked.connect(self.browse_audio) # type: ignore
        self.infoBtn.clicked.connect(self.get_demo_info) # type: ignore

        # self.browseInsertBtn.clicked.connect(self.browse_insert)

    def load_data(self):
        self.demoTreeBox: QGroupBox
        self.centralTabs: QTabWidget
        self.stepsTreeWidget: QTreeWidget
        self.applyToTreeWidget: QTreeWidget
        self.metadataTreeWidget: QTreeWidget
        self.demoTreeWidget: QTreeWidget
        self.stepOptionsListWidget: QListWidget

        self.demoListTreeWidget: QTreeWidget #TODO if num items == 0, disable add_step
        self.scriptListTreeWidget: QTreeWidget
        self.audioListTreeWidget: QTreeWidget

        self.centralTabs: QTabWidget
        self.demoSumTitle: QLabel
        self.centralWidget: QWidget

        self.stepTabs: QTabWidget

        self.stepsTreeWidget.currentItemChanged.connect( self.changed_op )
        self.stepTabs.currentChanged.connect(self.changed_step_tab)

    def load_actions(self):
        self.actionPreferences: QAction
        self.actionAbout: QAction
        self.actionNewStep: QAction

        self.actionOpenDemo: QAction

        self.actionNewStep.setShortcut("Ctrl+Shift+S")
        self.actionNewStep.setStatusTip("Add new step to operations")
        self.actionNewStep.triggered.connect(self.add_step)
        self.actionPreferences.triggered.connect(self.show_prefs)
        self.actionAbout.triggered.connect(self.show_about)


    #TODO detach these from class
    def browse_demo(self):
        home_dir = str(Path.home()) + "\\Documents\\My Demos"
        print(home_dir)
        print("TRYING TO GET QFILEDIALOG")
        demo_path, _ok = QFileDialog.getOpenFileName(self,"Browse for .demo files", "","Demo files (*.demo);;All Files (*)")
        # demo_path = QFileDialog.getOpenFileName(self,"Browse for demo files", str(Path.home()))
        # demo_path = QInputDialog.getText(self, "Input", "Enter name")
        # c, ok = QColorDialog.getColor()
        # demo_path, ok = QFileDialog.getOpenFileName(self, "Browse for demo file")
        # demo_p, ok = QFileDialog.get
        if demo_path[0]:
            self.cx.demo_paths.append(demo_path[0])
            print(demo_path[0])
            self.load_demo(demo_path[0])
            self.add_step()
        else:
            print("No demo selected.")

    #TODO implement correcty
    def browse_script(self):
        try:
            script_path, _ = QFileDialog.getOpenFileName(self,"Browse for .docx files", "","Word files (*.docx);;All Files (*)")
            if self.demoListTreeWidget.topLevelItemCount() > 0:
                self.reload_sel_demo(script_path=script_path)
        except:
            msg("Must select a script file", "Error while selecting script", "Must select script")

    #TODO Implement correctly
    def browse_audio(self):
        try:
            audio_dir = QFileDialog.getExistingDirectory(self, "Browse for audio folder")
            if self.demoListTreeWidget.topLevelItemCount() > 0:
                self.reload_sel_demo(audio_dir=audio_dir)
        except:
            msg("Must select a script file", "Error while selecting script", "Must select script")

    def browse_demo_next(self):
        try:
            if self.cx.demo_load[-1] is not None:
                print("Loaded demo")
            else:
                print("Demo not loaded")
        except:
            print("Demo could not be loaded")
        finally:
            pass

    def load_demo(self, demo_path: str):
        demo = Demo(path=demo_path) 
        demo_item = QTreeWidgetItem([demo.path.name, str(False), str(False)])
        self.demoListTreeWidget.addTopLevelItem(demo_item)
        self.cx.demo_load.append(demo)
        for i in range(self.stepsTreeWidget.topLevelItemCount()):
            self.stepTabs.widget(i).demoTargetCombo.clear() # type: ignore
            self.stepTabs.widget(i).demoTargetCombo.addItems(self.cx.get_demo_list_items()) # type: ignore
        self.update_steps()
        self.loadScriptBtn.setEnabled(True)
        self.loadAudioBtn.setEnabled(True)

    def reload_sel_demo(self, script_path: str = "", audio_dir: str = ""):
        print("BEGIN reload_sel_demo")
        sel_demo_idx: int = self.demoListTreeWidget.currentIndex().row()
        print(sel_demo_idx)
        curr_demo: Demo = self.cx.demo_load[sel_demo_idx]
        curr_demo_path: str = self.cx.demo_load[sel_demo_idx].file
        curr_demo_script_path: str = curr_demo.script_path
        curr_demo_audio_dir: str = curr_demo.audio_dir
        if curr_demo.script_path == "" and script_path != "":
            print("ADDING SCRIPT reload_sel_demo")
            new = Demo(path=curr_demo_path, script_path=script_path, audio_dir=curr_demo_audio_dir)
            self.cx.demo_load[sel_demo_idx] = new
            print(new.path.name)
            self.demoListTreeWidget.topLevelItem(sel_demo_idx).setData(0, 0, new.path.name)
            self.demoListTreeWidget.topLevelItem(sel_demo_idx).setData(1, 0, str(new.audio_dir != ""))
            self.demoListTreeWidget.topLevelItem(sel_demo_idx).setData(2, 0, str(True))
            """self.demoListTreeWidget.topLevelItem(sel_demo_idx).addChild([QTreeWidgetItem(\
                Path(script_path).name, \
                str(new.script.num_sections)+" Sect, "+str(new.script.length)+" Steps", \
                str(new.script.num_tp)+" TP"\
            )])"""
        if curr_demo.audio_dir == "" and audio_dir != "":
            print("ADDING AUDIO reload_sel_demo")
            new = Demo(path=curr_demo_path, script_path=curr_demo_script_path, audio_dir=audio_dir)
            self.cx.demo_load[sel_demo_idx] = new
            self.demoListTreeWidget.topLevelItem(sel_demo_idx).setData(0, 0, new.path.name)
            self.demoListTreeWidget.topLevelItem(sel_demo_idx).setData(1, 0, str(True))
            self.demoListTreeWidget.topLevelItem(sel_demo_idx).setData(2, 0, str(new.script_path != ""))
            """self.demoListTreeWidget.topLevelItem(sel_demo_idx).addChild([QTreeWidgetItem(\
                Path(audio_dir).name, \
                str(new.audio.len)+" Soundbites", \
                "" #add alternate indicator?
            )])"""
        self.set_demo_tree(sel_demo_idx)
        print("END reload_sel_demo")

    def get_demo_info(self):
        msg("Hello", "hi", "hello")

    def load_demo_tree(self):
        """
        Populates demo tree with sections/steps selectablbe for ops in rightmost pane
        """
        self.demoTreeWidget.clear()
        pass

    def load_script(self, script_path: str):
        pass

    def load_audio(self, audio_dir: str):
        pass
                
    def add_util_tab(self):
        pass

    def load_state(self):
        print("BEGIN load_state")

    def save_state(self):
        print("BEGIN save_state")
        print("END save_state")

    def run_ops(self):
        print("[Window.run_ops] BEGIN run_ops")
        out = ""
        for i in range(self.stepsTreeWidget.topLevelItemCount()):
            step = self.stepTabs.widget(i)
            demo = self.cx.demo_load[step.demoTargetCombo.currentIndex()]
            step.run_op(demo)
            if step.opCombo.currentIndex() == 2: #section -> destructive to script - demo connection
                self.cx.demo_load[step.demoTargetCombo.currentIndex()] = Demo(path=demo.file, audio_dir=demo.audio_dir, script_path=demo.script_path)
        msg(txt="[Window.run_ops] Finished running operations", inf=out, title="Finished")
        print("[Window.run_ops] END run_ops")

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
        self.stepsTreeWidget.setCurrentItem(self.stepsTreeWidget.topLevelItem(step_num-1))
        self.update_steps()
        self.stepTabs.widget(step_num-1).opCombo.currentIndexChanged.connect(self.update_steps)
        self.stepTabs.widget(step_num-1).demoTargetCombo.currentIndexChanged.connect(self.update_steps)
        self.stepTabs.widget(step_num-1).demoTargetCombo.addItems(self.cx.get_demo_list_items())
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
        self.cx.ops.pop(sel_step.row())
        self.update_steps()
        for i in range(self.stepsTreeWidget.topLevelItemCount()):
            self.stepsTreeWidget.topLevelItem(i).setData(0,0,i+1)
            self.stepTabs.setTabText(i, "Step " + str(i+1))
        #self.stepsTreeWidget.setCurrentIndex(sel_step.siblingAtRow(sel_step.row()-1))
        #self.opsStack.setCurrentIndex(sel_step.row()-1)
        print("END remove_step")

    def update_steps(self):
        if self.stepsTreeWidget.topLevelItemCount() > 0:
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
        if len(self.cx.demo_load) > 0:
            if self.stepTabs.widget(0):
                self.set_demo_tree(self.stepTabs.widget(self.stepsTreeWidget.currentIndex().row()).demoTargetCombo.currentIndex())

    def add_demo_row(self):
        # checkif sect or step
        row = ""

    def changed_op(self):
        curr_step: QModelIndex = self.stepsTreeWidget.currentIndex()
        self.stepTabs.setCurrentIndex(curr_step.row())
        if len(self.cx.demo_load) > 0:
            curr_demo: int = self.stepTabs.widget(curr_step.row()).demoTargetCombo.currentIndex()
            self.set_demo_tree(curr_demo)

    def changed_step_tab(self):
        curr_tab: int = self.stepTabs.currentIndex()
        self.stepsTreeWidget.setCurrentItem(self.stepsTreeWidget.topLevelItem(curr_tab))
        if len(self.cx.demo_load) > 0:
            curr_demo: int = self.stepTabs.widget(curr_tab).demoTargetCombo.currentIndex()
            self.set_demo_tree(curr_demo)
        #self.stepsTreeWidget.setCurrentIndex(curr_tab)

    def update_step_op(self, op_idx: int, step_num: int):
        self.stepsTreeWidget.topLevelItem(step_num).setData(1, 0, str(OP_TYPES[op_idx]()))

    def new_central_tab(self, tab_idx: int):
        if tab_idx == self.centralTabs.count()-1:
            self.centralTabs.addTab(QLabel("Hello!"), "New...")
        #if tab_idx == self.centralTabs.:
            #self.centralTabs.addTab(QLabel("Hello!")) #add new util/browse tab
        pass

    def set_demo_tree(self, demo_idx: int) -> None:
        curr_demo = self.cx.demo_load[demo_idx]
        self.demoTreeWidget.clear()
        self.demoTreeBox.setTitle(curr_demo.title)
        def Q(ls: List[Any]): return [QStandardItem(q) for q in ls]
        demo_title = curr_demo.title
        demo_model = QStandardItemModel(self.demoTreeWidget)
        demo_model.setHorizontalHeaderLabels([demo_title, "Has TP", "Animated"])
        for i, sect in enumerate(curr_demo.sections):
            sect_item = QTreeWidgetItem([sect.title])
            self.demoTreeWidget.addTopLevelItem(sect_item)
            for j, step in enumerate(sect):
                step_item = QTreeWidgetItem(["Step "+str(j), str(step.tp.text!=""), str(step.ci.text!="")])
                self.demoTreeWidget.topLevelItem(i).addChild(step_item)
        #demo_model.itemChanged.connect(self.displayInfo)
        print(curr_demo.title)

    def update_metadata(self, sect_idx: int, step_idx: int):
        pass

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

@Slot(MainWindow)
def msg(txt: str, inf: str, title: str, det: str = "") -> None:
    msg = QMessageBox()
    # msg.setIcon(QMessageBox.Information)
    msg.setText(txt)
    msg.setInformativeText(inf)
    msg.setWindowTitle(title)
    if det != "":
        msg.setDetailedText(det)
    # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.exec()


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

class DemoTreeWidget(QTreeWidget):

    def __init__(self, demo_model: DemoModel):
        signal_mapper = QSignalMapper(self)
        # self.model = demo_model
        pass

class StepMetadata(QStandardItemModel):

    def __init__(self):
        pass

class SectMetadata(QStandardItemModel):

    def __init__(self):
        pass

class DemoList(QAbstractItemModel):

    def __init__(self):
        pass

# def set_fusion(app: QApplication, dark: bool = False):
#     app.setStyle("Fusion")
#     if dark:
#         palette = QPalette()
#         palette.setColor(Qt)
#         palette.setColor(QPalette.Window, QColor(53, 53, 53))
#         palette.setColor(QPalette.WindowText, Qt.white)
#         palette.setColor(QPalette.Base, QColor(25, 25, 25))
#         palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
#         palette.setColor(QPalette.ToolTipBase, Qt.white)
#         palette.setColor(QPalette.ToolTipText, Qt.white)
#         palette.setColor(QPalette.Text, Qt.white)
#         palette.setColor(QPalette.Button, QColor(53, 53, 53))
#         palette.setColor(QPalette.ButtonText, Qt.white)
#         palette.setColor(QPalette.BrightText, Qt.red)
#         palette.setColor(QPalette.Link, QColor(42, 130, 218))
#         palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
#         palette.setColor(QPalette.HighlightedText, Qt.black)
#         app.setPalette(palette)

@dataclass
class Context:
    demo_load: List[Demo] = field(default_factory=list)
    demo_paths: List[str] = field(default_factory=list)
    script_load: List[str] = field(default_factory=list)
    audio_load: List[str] = field(default_factory=list)
    ops: List[QWidget] = field(default_factory=list)
    current_op: int = 0

    def get_demo_list_items(self) -> List[str]:
        out: List[str] = []
        for demo in self.demo_load:
            out.append(demo.path.name)
        return out

# signal whenever new demo is loaded --> add new demo to QItemModel for OpWidget demo selection
def set_op_widget():
    pass

def run():
    app = QApplication(sys.argv)
    loader = QUiLoader()
    loader.registerCustomWidget(MainWindow)
    path = os.path.join(os.path.dirname(__file__), "window.ui")
    ui: QMainWindow = loader.load(path, None)
    # window = MainWindow()
    ui.show()
    sys.exit(app.exec())
