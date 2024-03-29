"""
TODO: Separate App Window + tabs from Tab  view + create new tab view
TODO: Make right pane tabbed per-demo like the middle is (per step)
TODO: Add op_type indicator for qtreewidgetitems in step list
TODO: Make separate model / item classes for step list OR sep. QTreeWidget for stepsListTreeWidget
TODO: Figure out script/audio/demo association functionality
"""
from email.mime import base
from isu.data.context import OpSeq, DemoList, ScriptList
from isu.ui.tabs import CentralWidget
from isu.ui.views.demo import Ui_demoView
from isu.ui.data.steps import StepData
import sys
import os
# import functools
from pathlib import Path
# from dataclasses import dataclass, field
from isu.ui.ops.tab import OpUi
from typing import AnyStr, List, MutableSequence, Tuple, Dict, Optional, Type, Any
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import (  QDir,
    Signal, Slot,
    QPoint, QAbstractItemModel, QCoreApplication, QEnum, QFlag, Signal,
    QObject, Slot, QFileSelector, QSaveFile, QFileSelector, QTemporaryDir, 
    QTemporaryFile, QAbstractItemModel, QAbstractListModel, QModelIndex,
    QSignalMapper, QFile,
    # QProcess, Qt, QDir, QFile, QFileInfo, QUrl, QUuid
)
from isu.ui import UiLoad
from PySide6.QtGui import (QIcon,
    QDragEnterEvent, QDropEvent,
    QImageIOHandler, QImage, QImageReader, QAction, QIcon, QAction, 
    QActionEvent, QIconEngine,
    QImageWriter,QStandardItemModel, QStandardItem, QPalette, QColor, QColorConstants,
)
# from PySide6.QtMultimediaWidgets import QGraphicsVideoItem, QVideoWidget
from isu.models import Step, Demo
from PySide6 import QtUiTools
from PySide6.QtWidgets import ( QWidget,
    QTabWidget, QTabBar,
    # QColorDialog,
    QApplication, QMainWindow, QPushButton, QLineEdit, QSpinBox, QMessageBox, QFileDialog, QListWidgetItem,
    # QMenuBar,QProgressDialog,
    QListWidget, QTreeWidget, QTableWidget, QLabel, QComboBox, QTreeWidgetItem, QTableWidgetItem,
    QWizard, QWizardPage, QDialog, QUndoView, QProgressBar, QStyle, QStackedWidget, QGroupBox,
    # QInputDialog,
)

from isu.models.demo import Demo
from isu.ui.comp.prog import Progress
from ..operation import Op, Shell, Insert, Section, Audio, Crop, Pace, Text, Render, OP_TYPES
from isu.ui.ops.tab import TabOp
from isu.ui.ops.tabs import OpTabs
from isu.ui.comp.prefs import Prefs
from isu.data import Context

# from PySide6.QtUiTools import QUiLoader

#TODO make function/class which automatically goes thru list of widget names
#     and attaches appropriate functions/functionality
class MainWindow(QMainWindow):

    execute_ops = Signal()
    centralWidget: CentralWidget
    ui: QMainWindow

    def __init__(self, parent: QApplication) -> None:
        QMainWindow.__init__(self)
        UiLoad().loadUi("window.ui", self, parent)
        self.setup_ui()
        self.setup_data()

    def setup_ui(self) -> None:
        cw = CentralWidget(parent=self.ui)
        self.setCentralWidget(cw)

    def setup_data(self):
        self.ui.menubar.setVisible(True) #type: ignore
        self.ui.setAcceptDrops(True)
        # self.load_windows()
        # self.load_btn()
        # self.load_actions()
        # self.load_data()

    @Slot()
    def show_prefs(self):
        prefs = Prefs(parent=self)
        prefs.show()

    @Slot()
    def show_prog(self):
        prog = Progress(parent=self)

#     def load_btn(self) -> None:
#         self.browseDemoBtn: QPushButton # type: ignore
#         self.browseAudioBtn: QPushButton # type: ignore
#         self.browseScriptBtn: QPushButton # type: ignore
#         self.loadScriptBtn: QPushButton # type: ignore
#         self.loadAudioBtn: QPushButton # type: ignore
#         self.infoBtn: QPushButton # type: ignore
#         self.addDemoBtn: QPushButton # type: ignore
#         self.removeDemoBtn: QPushButton # type: ignore

#         self.loadScriptBtn.setEnabled(False)
#         self.loadAudioBtn.setEnabled(False)
#         # self.runBtn.setEnabled(False)

#         self.runBtn.clicked.connect(self.run_ops) # type: ignore
#         self.addStepBtn.clicked.connect(self.add_step) # type: ignore
#         self.removeStepBtn.clicked.connect(self.remove_step) # type: ignore
#         self.browseDemoBtn.clicked.connect(self.browse_demo) # type: ignore
#         self.addDemoBtn.clicked.connect(self.browse_demo) # type: ignore
#         self.browseAudioBtn.clicked.connect(self.browse_audio) # type: ignore
#         self.browseScriptBtn.clicked.connect(self.browse_script) # type: ignore
#         self.loadScriptBtn.clicked.connect(self.browse_script) # type: ignore
#         self.loadAudioBtn.clicked.connect(self.browse_audio) # type: ignore
#         self.infoBtn.clicked.connect(self.get_demo_info) # type: ignore

#         # self.browseInsertBtn.clicked.connect(self.browse_insert)

#     def load_data(self):
#         self.centralTabs: QTabWidget
#         self.stepsTreeWidget: QTreeWidget
#         self.applyToTreeWidget: QTreeWidget
#         self.metadataTreeWidget: QTreeWidget
#         self.demoTreeWidget: QTreeWidget
#         self.stepOptionsListWidget: QListWidget

#         self.demoListTreeWidget: QTreeWidget #TODO if num items == 0, disable add_step
#         self.scriptListTreeWidget: QTreeWidget
#         self.audioListTreeWidget: QTreeWidget

#         self.centralTabs: QTabWidget
#         self.demoSumTitle: QLabel

#         self.stepTabs: QWidget = StepsTabs(parent=self)

#         # self.stepsTreeWidget.currentChanged.connect(self.changed_op)
#         # self.stepTabs.currentChanged.

#     def load_windows(self):
#         self.preferences = Prefs(self)
#         self.browseDemoDialog: QFileDialog
#         self.browseScriptDialog: QFileDialog
#         self.browseAudioDialog: QFileDialog


#     def load_actions(self):
#         self.actionPreferences: QAction
#         self.actionAbout: QAction
#         self.actionNewStep: QAction

#         self.actionOpenDemo: QAction

#         self.actionNewStep.setShortcut("Ctrl+Shift+S")
#         self.actionNewStep.setStatusTip("Add new step to operations")
#         self.actionNewStep.trigger.connect(self.add_step)
#         self.actionPreferences.trigger.connect(self.preferences.open)
#         self.actionAbout.trigger.connect(self.show_about)

#     def add_step(self):
#         self.steps

#     #TODO detach these from class
#     def browse_demo(self):
#         home_dir = str(Path.home()) + "\\Documents\\My Demos"
#         demo_path, ok = QFileDialog.getOpenFileName(self,"Browse for .demo files", "","Demo files (*.demo);;All Files (*)")
#         if ok:
#             # self.ctx.demo_list.append(demo_path)
#             self.load_demo(demo_path)
#             if len(self.stepsTreeWidget.__dict__) == 0: self.add_step()
#         else:
#             print("No demo selected.")

#     #TODO implement correcty
#     def browse_script(self):
#         try:
#             script_path, _ = QFileDialog.getOpenFileName(self,"Browse for .docx files", "","Word files (*.docx);;All Files (*)")
#             if self.demoListTreeWidget.topLevelItemCount() > 0:
#                 self.reload_sel_demo(script_path=script_path)
#         except:
#             self.msg("Must select a script file", "Error while selecting script", "Must select script")

#     #TODO Implement correctly
#     def browse_audio(self):
#         try:
#             audio_dir = QFileDialog.getExistingDirectory(self, "Browse for audio folder")
#             if self.demoListTreeWidget.topLevelItemCount() > 0:
#                 self.reload_sel_demo(audio_dir=audio_dir)
#         except:
#             self.msg("Must select a script file", "Error while selecting script", "Must select script")

#     def browse_demo_next(self):
#         try:
#             if self.ctx.load.demo[-1] is not None:
#                 print("Loaded demo")
#             else:
#                 print("Demo not loaded")
#         except:
#             print("Demo could not be loaded")
#         finally:
#             pass

#     def load_demo(self, demo_path: str):
#         demo = Demo(path=demo_path) 
#         demo_item = QTreeWidgetItem([demo.title, str(False), str(False)])
#         self.demoListTreeWidget.addTopLevelItem(demo_item)
#         self.ctx.demo_list.append(demo)
#         for i in range(self.stepsTreeWidget.topLevelItemCount()):
#             self.stepTabs.widget(i).demoTargetCombo.clear() # type: ignore
#             self.stepTabs.widget(i).demoTargetCombo.addItems(self.cx.get_demo_list_items()) # type: ignore
#         # self.update_steps()
#         self.loadScriptBtn.setEnabled(True)
#         self.loadAudioBtn.setEnabled(True)

#     def reload_sel_demo(self, script_path: str = "", audio_dir: str = ""):
#         print("BEGIN reload_sel_demo")
#         sel_demo_idx: int = self.demoListTreeWidget.currentIndex().row()
#         print(sel_demo_idx)
#         curr_demo: Demo = self.ctx.demo_list[sel_demo_idx]
#         curr_demo_path: str = self.ctx.demo_list[sel_demo_idx].file
#         curr_demo_script_path: str = curr_demo.script_path
#         curr_demo_audio_dir: str = curr_demo.audio_dir
#         if curr_demo.script_path == "" and script_path != "":
#             print("ADDING SCRIPT reload_sel_demo")
#             new = Demo(path=curr_demo_path, script_path=script_path, audio_dir=curr_demo_audio_dir)
#             self.ctx.demo_list[sel_demo_idx] = new
#             print(new.path.name)
#             self.demoListTreeWidget.topLevelItem(sel_demo_idx).setData(0, 0, new.path.name)
#             self.demoListTreeWidget.topLevelItem(sel_demo_idx).setData(1, 0, str(new.audio_dir != ""))
#             self.demoListTreeWidget.topLevelItem(sel_demo_idx).setData(2, 0, str(True))
#             """self.demoListTreeWidget.topLevelItem(sel_demo_idx).addChild([QTreeWidgetItem(\
#                 Path(script_path).name, \
#                 str(new.script.num_sections)+" Sect, "+str(new.script.length)+" Steps", \
#                 str(new.script.num_tp)+" TP"\
#             )])"""
#         if curr_demo.audio_dir == "" and audio_dir != "":
#             print("ADDING AUDIO reload_sel_demo")
#             new = Demo(path=curr_demo_path, script_path=curr_demo_script_path, audio_dir=audio_dir)
#             self.ctx.demo_list[sel_demo_idx] = new
#             self.demoListTreeWidget.topLevelItem(sel_demo_idx).setData(0, 0, new.path.name)
#             self.demoListTreeWidget.topLevelItem(sel_demo_idx).setData(1, 0, str(True))
#             self.demoListTreeWidget.topLevelItem(sel_demo_idx).setData(2, 0, str(new.script_path != ""))
#             """self.demoListTreeWidget.topLevelItem(sel_demo_idx).addChild([QTreeWidgetItem(\
#                 Path(audio_dir).name, \
#                 str(new.audio.len)+" Soundbites", \
#                 "" #add alternate indicator?
#             )])"""
#         self.set_demo_tree(sel_demo_idx)
#         print("END reload_sel_demo")

#     def get_demo_info(self):
#         self.msg("Hello", "hi", "hello")

#     def load_demo_tree(self):
#         """
#         Populates demo tree with sections/steps selectablbe for ops in rightmost pane
#         """
#         self.demoTreeWidget.clear()
#         pass

#     def load_script(self, script_path: str):
#         pass

#     def load_audio(self, audio_dir: str):
#         pass
                
#     def add_util_tab(self):
#         pass

#     def load_state(self):
#         print("BEGIN load_state")

#     def save_state(self):
#         print("BEGIN save_state")
#         print("END save_state")

#     def new_central_tab(self, tab_idx: int):
#         if tab_idx == self.centralTabs.count()-1:
#             self.centralTabs.addTab(QLabel("Hello!"), "New...")
#         #if tab_idx == self.centralTabs.:
#             #self.centralTabs.addTab(QLabel("Hello!")) #add new util/browse tab
#         pass

#     def set_demo_tree(self, demo_idx: int) -> None:
#         curr_demo = self.ctx.demo_list[demo_idx]
#         self.demoTreeWidget.clear()
#         self.demoTreeBox.setTitle(curr_demo.title)
#         def Q(ls: List[Any]): return [QStandardItem(q) for q in ls]
#         demo_title = curr_demo.title
#         demo_model = QStandardItemModel(self.demoTreeWidget)
#         demo_model.setHorizontalHeaderLabels([demo_title, "Has TP", "Animated"])
#         for i, sect in enumerate(curr_demo.sections):
#             sect_item = QTreeWidgetItem([sect.title])
#             self.demoTreeWidget.addTopLevelItem(sect_item)
#             for j, step in enumerate(sect):
#                 step_item = QTreeWidgetItem(["Step "+str(j), str(step.tp.text!=""), str(step.ci.text!="")])
#                 self.demoTreeWidget.topLevelItem(i).addChild(step_item)
#         #demo_model.itemChanged.connect(self.displayInfo)
#         print(curr_demo.title)

#     def update_metadata(self, sect_idx: int, step_idx: int):
#         pass

#     def show_about(self):
#         text = "<center>" \
#                "<h1>ISCUtils</h1>" \
#                "&#8291;" \
#                "</center>" \
#                "<p>Version 0.0.1<br/>" \
#                "Chris P.</p>"
#         QMessageBox.about(self, "About Text Editor", text)


#     def set_op_widget(self, op: str, idx: int = 0):
#         op_wid = TabOp(index=idx, parent=self)
#         """Consider making op param non-string, enum or something"""
#         pass

#     def dragEnterEvent(self, e: QDragEnterEvent) -> None:
#         data = e.mimeData()
#         if data.hasUrls():
#             url = data.urls()[0].toLocalFile()
#             if os.path.splitext(url)[1].lower() == ".demo":
#                 e.accept()

#     # TODO finish
#     def dropEvent(self, e: QDropEvent) -> None:
#         data = e.mimeData()
#         path = data.urls()[0].toLocalFile()
#         self.load_demo(path)

#     @staticmethod
#     @Slot(str, str, str, str)
#     def msg(self, txt: str, inf: str, title: str, det: str = "") -> None:
#         msg = QMessageBox()
#         msg.setIcon(QMessageBox.Icon.Information)
#         msg.setWindowTitle(title)
#         msg.setText(txt)
#         msg.setInformativeText(inf)
#         if det != "":
#             msg.setDetailedText(det)
#         msg.setDefaultButton(QMessageBox.StandardButton.Ok)
#         msg.setStandardButtons(buttons=QMessageBox.StandardButtons())
#         msg.exec()

#     def run_ops(self):
#         print("[Window.run_ops] BEGIN run_ops")
#         out = ""
#         self.opprog = Progress(parent=self, len=len(self.cx.ops))
#         self.opprog.show()
#         for step_num in range(self.stepTabs.tab()):
#             step: Tab = self.stepsTable.rowAt(step_num)
#             self.optype: Type[Op] = self.step.curr_optype()
#             self.opprog.set_optype(self.optype)
#             demo = self.ctx.demo_list[self.step.demoCombo.currentIndex()]
#             op: Op = self.step.curr_op()
#             op.updated.connect(self.opprog.progress)
#             op.finished.connect(self.update_progress)
#             op.run(demo)
#             if self.step.opCombo.currentIndex() == 2: #section -> destructive to script - demo connection
#                 self.ctx.demo_list[self.step.demoTargetCombo.currentIndex()] = Demo(path=demo.file, audio_dir=demo.audio_dir, script_path=demo.script_path)
#         msg(txt="[Window.run_ops] Finished running operations", inf=out, title="Finished")
#         print("[Window.run_ops] END run_ops")


#     def add_step(self):
#         #TODO create model for new steps QTreeWidgetItem
#         #TODO create model for list of steps 
#         print("BEGIN add_step")
#         step_num: int = len(self.cx.ops) + 1
#         tab = TabOp(parent=self, index=step_num)
#         self.cx.ops.append(tab)
#         op = QTreeWidgetItem([str(step_num), str(OP_TYPES[0]), str(OP_TYPES[0])])
#         self.stepsTreeWidget.addTopLevelItem(op)
#         self.stepTabs.addTab(self.cx.ops[-1], "Step " + str(step_num))
#         self.stepTabs.setCurrentIndex(step_num)
#         self.stepsTreeWidget.setCurrentItem(self.stepsTreeWidget.topLevelItem(step_num-1))
#         self.update_steps()
#         self.stepTabs.widget(step_num-1).opCombo.currentIndexChanged.connect(self.update_steps)
#         self.stepTabs.widget(step_num-1).demoTargetCombo.currentIndexChanged.connect(self.update_steps)
#         self.stepTabs.widget(step_num-1).demoTargetCombo.addItems(self.cx.demo_list_titles())
#         #self.stepsTreeWidget.currentItem().
#         self.update_steps()
#         self.runBtn.setEnabled(True)
#         print("END add_step")

#     #TODO fix this
#     def remove_step(self):
#         print("BEGIN remove_step")
#         sel_step: QModelIndex = self.stepsTreeWidget.currentIndex()
#         self.stepTabs.removeTab(sel_step.row())
#         self.stepsTreeWidget.takeTopLevelItem(sel_step.row())
#         self.cx.ops.ops.remove()
#         self.update_steps()
#         for i in range(self.stepsTreeWidget.topLevelItemCount()):
#             self.stepsTreeWidget.topLevelItem(i).setData(0,0,i+1)
#             self.stepTabs.setTabText(i, "Step " + str(i+1))
#         #self.stepsTreeWidget.setCurrentIndex(sel_step.siblingAtRow(sel_step.row()-1))
#         #self.opsStack.setCurrentIndex(sel_step.row()-1)
#         print("END remove_step")


#     # def err(self, err):
#     #     exctype, value, traceback = err
#     #     self.prog.update_progress(1)  # Reset the Pez bar.
#     #     dlg = QMessageBox(self)
#     #     dlg.setText(traceback)
#     #     dlg.setIcon(QMessageBox.Critical)
#     #     dlg.show() 
        
# class AboutDialog(QDialog):
#     def __init__(self, *args, **kwargs):
#         super(QDialog, self).__init__(*args, **kwargs)



# class OpsModel(QAbstractItemModel):

#     def __init__(self, demo: Demo):
#         pass

# class Step(QStandardItem):

#     def __init__(self, op_type: Op):
#         pass

# class Steps(QStandardItemModel):
#     def __init__(self):
#         pass

#     def add_step(self, step: Step):
#         pass

# class DemoModel(QStandardItemModel):

#     def __init__(self, demo: Demo):
#         pass

# # class DemoTreeWidget(QTreeWidget):

# #     def __init__(self, demo_model: DemoModel):
# #         signal_mapper = QSignalMapper(self)
# #         # self.model = demo_model
# #         pass

# class StepMetadata(QStandardItemModel):

#     def __init__(self):
#         pass

# class SectMetadata(QStandardItemModel):

#     def __init__(self):
#         pass

# class DemoList(QAbstractItemModel):

#     def __init__(self):
#         pass


# # signal whenever new demo is loaded --> add new demo to QItemModel for OpWidget demo selection
# def set_op_widget():
#     pass

# def run():
#     app = QApplication(sys.argv)
#     # loader = QUiLoader()
#     # loader.registerCustomWidget(MainWindow)
#     # path = os.path.join(os.path.dirname(__file__), "window.ui")
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())
