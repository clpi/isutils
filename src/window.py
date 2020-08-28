import sys, os
from dataclasses import dataclass
from typing import List, Tuple, Dict 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQml import *
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, QSpinBox, QMessageBox, QFileDialog, QListWidgetItem,
    QListWidget, QTreeWidget
)

from models.demo import Demo
from common.op import Operation

from PyQt5 import uic

#TODO make function/class which automatically goes thru list of widget names
#     and attaches appropriate functions/functionality
class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        path = os.path.join(os.path.dirname(__file__), "main.ui")
        uic.loadUi(path, self)
        self.cx = Context()
        self.DEMO_PATH: str = "" 
        self.SCRIPT_PATH: str = "" 
        self.AUDIO_DIR: str = ""
        self.OPS: List[Operation] = []
        self.load_btn()
        self.load_input()
        self.show()

    def load_btn(self):
        self.run_btn = self.findChild(QPushButton, "runBtn")
        self.run_now_btn = self.findChild(QPushButton, "runNowBtn")
        self.clear_btn = self.findChild(QPushButton, "resetBtn")
        self.add_step_btn = self.findChild(QPushButton, "addStepBtn")
        self.remove_step_btn = self.findChild(QPushButton, "removeStepBtn")
        self.add_op_btn = self.findChild(QPushButton, "addOpBtn")
        self.clear_params_btn = self.findChild(QPushButton, "clearParamsBtn")
        self.browse_demo_btn = self.findChild(QPushButton, "browseDemoBtn")
        self.browse_script_btn = self.findChild(QPushButton, "browseScriptBtn")
        self.browse_audio_btn = self.findChild(QPushButton, "browseAudioBtn")
        self.browse_shell_btn = self.findChild(QPushButton, "shellBrowseImgBtn")
        self.browse_insert_btn = self.findChild(QPushButton, "insertBrowseImgBtn")

        self.run_btn.clicked.connect(self.run_ops)
        #self.run_now_btn.clicked.connect(self.run_now)

        self.browse_demo_btn.clicked.connect(self.browse_demo)
        self.browse_script_btn.clicked.connect(self.browse_script)
        self.browse_audio_btn.clicked.connect(self.browse_audio)

    # TODO: do this more programmatically
    def load_input(self):
        #insert
        self.insert_img = self.findChild(QLineEdit, "insertImgPath")
        self.insert_x = self.findChild(QSpinBox, "insertFgX")
        self.insert_y = self.findChild(QSpinBox, "insertFgY")
        self.insert_w = self.findChild(QSpinBox, "insertFgW")
        self.insert_h = self.findChild(QSpinBox, "insertFgH")
        #shell
        self.shell_img = self.findChild(QLineEdit, "shellImgPath")
        self.shell_x = self.findChild(QSpinBox, "shellFgX")
        self.shell_y = self.findChild(QSpinBox, "shellFgY")
        self.shell_w = self.findChild(QSpinBox, "shellFgW")
        self.shell_h = self.findChild(QSpinBox, "shellFgH")

    def load_data(self):
        self.steps = self.findChild(QListWidget, "stepListWidget")
        self.apply_to = self.findChild(QListWidget, "applyToListWidget")
        self.demo_tree = self.findChild(QTreeWidget, "demoTreeWidget")
        self.metadata = self.findChild(QListWidget, "metadataListWidget")
        self.step_options = self.findChild(QListWidget, "stepOptionsListWidget")
        self.demo_sum = self.findChild(QListWidget, "demoSumListWidget")
        self.script_sum = self.findChild(QListWidget, "scriptSumListWidget")
        self.audio_sum = self.findChild(QListWidget, "audioSumListWidget")
        self.cx.ops = self.ops


    def browse_demo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        try:
            self.cx.demo_path, _ = QFileDialog.getOpenFileName(self,"Browse for .demo files", "","Demo files (*.demo);;All Files (*)", options=options)
            self.load_demo()
        except:
            msg("Must select a demo file", "Error while selecting demo", "Must select demo")

    def browse_script(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        try:
            self.cx.script_path, _ = QFileDialog.getOpenFileName(self,"Browse for .docx files", "","Word files (*.docx);;All Files (*)",
            options=options)
            self.load_script()
        except:
            msg("Must select a script file", "Error while selecting script", "Must select script")

    def browse_audio(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        try:
            self.cx.audio_dir, _ = QFileDialog.getExistingDirectory(self, "Browse for audio folder", options=options)
            self.load_audio()
        except:
            msg("Must select a script file", "Error while selecting script", "Must select script")

    def load_audio(self):
        pass        

    def load_demo(self):
        pass

    def load_script(self):
        pass

    def load_state(self):
        pass

    def save_state(self):
        pass

    def run_ops(self):
        pass

    def add_operation(self):
        op = QListWidgetItem("Item" + (len(self.cx.ops) + 1))


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
    script_dir: str
    audio_dir: str
    current_op: str
    ops: List[Operation]

    def __init__(self):
        self.demo_path = ""
        self.script_dir = ""
        self.audio_dir = ""
        self.current_op = ""
        self.ops = []


app = QApplication(sys.argv)
window = MainWindow()
app.exec_()