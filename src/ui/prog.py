from PySide6.QtCore import ( 
    QObject, Slot, QFileSelector, QSaveFile, QFileSelector, QTemporaryDir, 
    QTemporaryFile, QAbstractItemModel, QAbstractListModel, Signal, QModelIndex,
    QSignalMapper,QTimer,
)
from PySide6.QtGui import (QIcon,
    QImageIOHandler, QImage, QImageReader, QAction, QIcon,
    QImageWriter, QStandardItemModel, QStandardItem, QPalette, QColor, QColorConstants,
)
from PySide6.QtWidgets import ( QWidget,
    QColorDialog,
    QMenuBar,QProgressDialog,
    QApplication, QMainWindow, QPushButton, QLineEdit, QSpinBox, QMessageBox, QFileDialog, QListWidgetItem,
    QListWidget, QTreeWidget, QTableWidget, QLabel, QTabWidget, QComboBox, QTreeWidgetItem, QTableWidgetItem,
    QWizard, QWizardPage, QDialog, QUndoView, QProgressBar, QStyle, QStackedWidget, QGroupBox,
    QInputDialog
)
class Progress(QProgressDialog):
    # Operation constructor
    def __init__(self, parent):
        QObject.__init__(self, parent)
        self.steps = 0

        pd = QProgressDialog("Operation in progress.", "Cancel", 0, 100)
        # QObject.connect(pd, QProgressDialog.canceled, self, Operation.cancel)
        t = QTimer(self)
        # connect(t, QTimer.timeout, self, Operation.perform)
        t.start(0)
    def perform(self):

        # pd.setValue(steps)
        #... perform one percent of the operation
        steps = steps + 1
        # if (steps > pd.maximum())
            # t.stop()
    def cancel(self):
        pass

        # t.stop()
        #... cleanup