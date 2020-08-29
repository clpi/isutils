import sys, os
from dataclasses import dataclass
from typing import List, Tuple, Dict 
from PyQt5.QtCore import (
    QObject, pyqtSlot, QFileSelector, QSaveFile, QFileSelector, QTemporaryDir, QTemporaryFile)
from PyQt5.QtGui import (QIcon, QImageIOHandler, QImage, QImageReader, QImageWriter, QStandardItemModel, QStandardItem,)
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, QSpinBox, QMessageBox, QFileDialog, QListWidgetItem,
    QListWidget, QTreeWidget, QTableWidget, QLabel, QTabWidget, QComboBox, QTreeWidgetItem, QTableWidgetItem,
    QAction, QWizard, QWizardPage, QDialog, QUndoView, QProgressBar,
)

from models.demo import Demo
from common.op import Operation

from PyQt5 import uic

#TODO make function/class which automatically goes thru list of widget names
#     and attaches appropriate functions/functionality
class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        path = os.path.join(os.path.dirname(__file__), "ui\\main.ui")
        uic.loadUi(path, self)
        self.cx = Context()
        self.load_btn()
        self.load_input()
        self.show()

    def load_btn(self):
        self.runBtn: QPushButton = self.runBtn
        self.addStepBtn: QPushButton = self.addStepBtn
        self.runBtn.clicked.connect(self.run_ops)
        self.addStepBtn.clicked.connect(self.add_step)
        self.browseDemoBtn.clicked.connect(self.browse_demo)
        self.browseAudioBtn.clicked.connect(self.browse_audio)
        self.browseScriptBtn.clicked.connect(self.browse_script)
        #self.browseShellBtn.clicked.connect(self.browse_shell)
       # self.browseInsertBtn.clicked.connect(self.browse_insert)

    # TODO: do this more programmatically
    def load_input(self):
        #insert
        self.insert_img: QLineEdit = self.findChild(QLineEdit, "insertImgPath")
        self.insert_x: QSpinBox = self.findChild(QSpinBox, "insertFgX")
        self.insert_y: QSpinBox = self.findChild(QSpinBox, "insertFgY")
        self.insert_w: QSpinBox = self.findChild(QSpinBox, "insertFgW")
        self.insert_h: QSpinBox = self.findChild(QSpinBox, "insertFgH")
        #shell
        self.shell_img: QLineEdit = self.findChild(QLineEdit, "shellImgPath")
        self.shell_x: QSpinBox = self.findChild(QSpinBox, "shellFgX")
        self.shell_y: QSpinBox = self.findChild(QSpinBox, "shellFgY")
        self.shell_w: QSpinBox = self.findChild(QSpinBox, "shellFgW")
        self.shell_h: QSpinBox = self.findChild(QSpinBox, "shellFgH")


    def load_data(self):
        self.steps: QListWidget = self.findChild(QListWidget, "stepListWidget")
        self.apply_to: QListWidget = self.findChild(QListWidget, "applyToListWidget")
        self.demo_tree: QTreeWidget = self.findChild(QTreeWidget, "demoTreeWidget")
        self.metadata: QTreeWidget = self.findChild(QTreeWidget, "metadataTreeWidget")
        self.step_options: QListWidget = self.findChild(QListWidget, "stepOptionsListWidget")
        self.demo_sum: QListWidget = self.findChild(QListWidget, "demoSumListWidget")
        self.demo_sum_title: QLabel = self.findChild(QLabel, "demoSumTitle")
        self.script_sum: QListWidget = self.findChild(QListWidget, "scriptSumListWidget")
        self.audio_sum: QListWidget = self.findChild(QListWidget, "audioSumListWidget")
        self.ops_params_tabs: QTabWidget = self.findChild(QTabWidget, "opsParamsTabs")
        self.ops_combo: QComboBox = self.findChild(QComboBox, "opsCombo")

        self.ops_combo.textActivated.connect(self.changed_op)
        self.cx.ops = self.ops

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
        self.demoSumTitle.setText(self.cx.demo.tite)
        self.demo_sum_title.setText("DFDF")
        self.demoTreeWidget.insertTopLevelItem(QTreeWidgetItem("Demo tite", self.cx.demo.titprint(self.cx.demo)))
        tree: QTreeWidget = self.demoTreeWidget
        sect_items: List[QTreeWidgetItem] = []
        step_items: List[List[QTreeWidgetItems]] = []
        for i, sect in enumerate(self.cx.demo.iter_sect()):
            for j, step in enumerate(sect):
                if step.idx == 0:
                    sect_item: QTreeWidgetItem = QTreeWidgetItem([str(i), sect.tite])
                    sect_items.append(sect_item)
                    self.demoTreeWidget.addTopLevelItem(sect_item)
                else:
                    step_item: QTreeWidgetItem = QTreeWidgetItem([str(j), "Step "+str(j), str(step.tp.text != ""), str(step.ci.text!="")])
                    step_items[i].append(step_item)
                    sect_items[i].addChild(step_item)
        self.demoTreeWidget = tree
                
       

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

def msg(txt: str, inf: str, title: str, det: str = ""):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(txt)
    msg.setInformativeText(inf)
    msg.setWindowTitle(title)
    if det != "":
        msg.setDetailedText(det)
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

class Context:
    demo_path: str
    demo: Demo
    script_path: str
    audio_dir: str
    current_op: str
    active_op: bool
    ops: List[Operation]

    def __init__(self):
        self.demo_path = ""
        self.demo = None
        self.script_path = ""
        self.audio_dir = ""
        self.current_op = ""
        self.ops = []
        active_op = False


app = QApplication(sys.argv)
window = MainWindow()
app.exec_()