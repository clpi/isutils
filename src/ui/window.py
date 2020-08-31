import sys, os, functools, typing
from dataclasses import dataclass
from typing import List, Tuple, Dict, Optional
from PyQt5.QtCore import ( Qt,
    QObject, pyqtSlot, QFileSelector, QSaveFile, QFileSelector, QTemporaryDir, QTemporaryFile, QAbstractItemModel, QAbstractListModel, pyqtSignal)
from PyQt5.QtGui import (QIcon, QImageIOHandler, QImage, QImageReader, QImageWriter, QStandardItemModel, QStandardItem, QPalette, QColor)
from PyQt5.QtWidgets import ( QWidget,
    QApplication, QMainWindow, QPushButton, QLineEdit, QSpinBox, QMessageBox, QFileDialog, QListWidgetItem,
    QListWidget, QTreeWidget, QTableWidget, QLabel, QTabWidget, QComboBox, QTreeWidgetItem, QTableWidgetItem,
    QAction, QWizard, QWizardPage, QDialog, QUndoView, QProgressBar, QStyle
)
from PIL import Image

from models.demo.demo import Demo
from models.op import Op, ShellOp, InsertOp, SectionOp, AudioOp, CropOp

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
        self.load_input()
        

    def load_btn(self) -> None:
        self.runBtn: QPushButton
        self.addStepBtn: QPushButton
        self.browseDemoBtn: QPushButton
        self.browseAudioBtn: QPushButton
        self.browseScriptBtn: QPushButton
        self.shellBrowseImgBtn: QPushButton
        self.saveStepParamsBtn: QPushButton
        self.insertBrowseImgBtn: QPushButton
        self.resetStepParamsBtn: QPushButton

        self.runBtn.clicked.connect(self.run_ops)
        self.addStepBtn.clicked.connect(self.add_step)
        self.saveStepParamsBtn.clicked.connect(self.save_params)
        self.browseDemoBtn.clicked.connect(self.browse_demo)
        self.browseAudioBtn.clicked.connect(self.browse_audio)
        self.browseScriptBtn.clicked.connect(self.browse_script)
        self.shellBrowseImgBtn.clicked.connect(self.browse_shell)
        self.insertBrowseImgBtn.clicked.connect(self.browse_insert)
        self.resetStepParamsBtn.clicked.connect(self.show_about)

       # self.browseInsertBtn.clicked.connect(self.browse_insert)

    # TODO: do this more programmatically
    def load_input(self) -> None:
        self.insertImgPath: QLineEdit
        self.shellImgPath: QLineEdit
        self.insertFgX: QSpinBox
        self.insertFgY: QSpinBox
        self.insertFgW: QSpinBox
        self.insertFgH: QSpinBox
        self.shellFgX: QSpinBox
        self.shellFgY: QSpinBox
        self.shellFgW: QSpinBox
        self.shellFgH: QSpinBox


    def load_data(self):
        self.stepsTreeWidget: QListWidget
        self.applyToTreeWidget: QListWidget
        self.metadataTreeWidget: QTreeWidget
        self.demoTreeWidget: QTreeWidget
        self.stepOptionsListWidget: QListWidget
        self.demoSumListWidget: QListWidget
        self.scriptSumListWidget: QListWidget
        self.audioSumListWidget: QListWidget
        self.opsParamsTabs: QTabWidget
        self.centralTabs: QTabWidget
        self.opsCombo: QComboBox
        self.demoSumTitle: QLabel
        self.centralWidget: QWidget

        #self.demoSumListWidget.setModel()

        self.ops_combo.textActivated.connect(self.changed_op)
        self.cx.ops = self.ops

    def load_signals(self):
        pass

    def load_slots(self):
        pass

    def load_actions(self):
        pass


    #TODO detach these from class
    def browse_demo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        try:
            self.cx.demo_path, _ = QFileDialog.getOpenFileName(self,"Browse for .demo files", "","Demo files (*.demo);;All Files (*)", options=options)
            self.load_demo()
        except:
            msg("Must select a demo file", "Error while selecting demo", "Must select demo")
            self.cx.demo_path = ""

    def browse_script(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        try:
            self.cx.script_path, _ = QFileDialog.getOpenFileName(self,"Browse for .docx files", "","Word files (*.docx);;All Files (*)",
            options=options)
            if self.cx.demo_path != "":
                self.load_demo()
        except:
            msg("Must select a script file", "Error while selecting script", "Must select script")
            return

    def browse_audio(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        try:
            self.cx.audio_dir, _ = QFileDialog.getExistingDirectory(self, "Browse for audio folder", options=options)
            if self.cx.demo_path != "":
                self.load_demo()
        except:
            msg("Must select a script file", "Error while selecting script", "Must select script")
            return

    def browse_insert(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        try:
            fileName, _ = QFileDialog.getOpenFileName(self,"Browse for image files", "","All Files (*);;PNG files (*.png)", options=options)
            img_tmp = Image.open(fileName)
            iwidth, iheight = img_tmp.size
            if self.demo is not None:
                if iwidth > self.demo.res[0] or iheight > self.demo.res[1]:
                    pass
            #set op img path, def dims
        except:
            pass

    def browse_shell(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        try:
            fileName, _ = QFileDialog.getOpenFileName(self,"Browse for image files", "","All Files (*);;PNG files (*.png)", options=options)
            img_tmp = Image.open(fileName)
            iwidth, iheight = img_tmp.size
            if self.demo is not None:
                if iwidth > self.demo.res[0] or iheight > self.demo.res[1]:
                    pass
            #set op img path, def dims
        except: pass

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
        pass

    def save_state(self):
        pass

    def run_ops(self):
        pass

    def add_step(self):
        ops = self.cx.ops
        s: QListWidget = self.stepsListWidget
        op = QListWidgetItem("Item" + str(len(self.cx.ops) + 1))
        s.addItem(op)
        self.opsParamsTabs.setEnabled(True)

    def save_params(self):
        pass

    def add_demo_row(self):
        # checkif sect or step
        row = ""

    def changed_op(self):
        curr = self.ops_combo.currentText()
        if curr == "Shell": self.ops_params_tabs.setCurrentIndex(0)
        if curr == "Insert": self.ops_params_tabs.setCurrentIndex(1)
        if curr == "Section": self.ops_params_tabs.setCurrentIndex(2)
        if curr == "Audio": self.ops_params_tabs.setCurrentIndex(3)
        if curr == "Crop": self.ops_params_tabs.setCurrentIndex(4)
        #if curr == "Move pixels": self.ops_params_tabs.setCurrentIndex(4)
        #if curr == "Resize": self.ops_params_tabs.setCurrentIndex(4)


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

class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

@pyqtSlot(MainWindow)
def msg(txt: str, inf: str, title: str, det: str = ""):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(txt)
    msg.setInformativeText(inf)
    msg.setWindowTitle(title)
    if det != "":
        msg.setDetailedText(det)
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.exec_()

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


class Context:
    demo_path: str
    demo: Demo
    script_path: str
    audio_dir: str
    current_op: str
    active_op: bool
    ops: List[Op]

    def __init__(self):
        self.demo_path = ""
        self.demo = None
        self.script_path = ""
        self.audio_dir = ""
        self.current_op = ""
        self.ops = []
        active_op = False


def run():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    """
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
    """
    window = MainWindow()
    window.show()
    app.exec_()
    

"""
app = QApplication(sys.argv)
#app.setStyle("Fusion")
window = MainWindow()
app.exec_()
"""
