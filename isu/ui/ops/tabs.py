from isu.ui import UiLoad
from isu.ui.ops import OpType, to_op_type, to_ui_type, OpUi
from typing import Any, Optional, Type
from PySide6.QtGui import ( QTextTable, )
from PySide6.QtCore import ( 
    Qt, Signal, Slot, QEnum, ClassInfo
)
from PySide6.QtWidgets import (
    QWidget, QStackedWidget, QTabBar, QTabWidget, QTableView,
)
from typing import Optional

class OpTabs(QTabWidget):
    new_tab = Signal()
    ops_stack: QStackedWidget

    def __init__(self, parent: Any):
        super(OpTabs, self).__init__(parent)
        self.setAutoFillBackground(True)
        self.setTabShape(QTabWidget.TabShape.Rounded)
        self.setElideMode(Qt.TextElideMode.ElideRight)
        self.ensurePolished()
        self.load_data(parent)

        # self.currentChanged.connect(self.on_current_changed)

    @Slot(int)
    def on_current_changed(self, idx: int):
        pass

    def current_op_widget(self):
        return self.stepTabs.widget(self.currentIndex())

    def load_data(self, parent: Any):
        self.stepTabs: QTabWidget

    def remove_tab(self, tabi: int):
        self.stepTabs.removeTab(tabi)

    @Slot(int)
    def on_tab_index_change(self, index: int):
        self.stepTabs.setCurrentIndex(index)

    @Slot(int)
    def on_op_removed(self, index: int):
        self.remove_tab(index)

    @Slot(int)
    def add_tab(self, index: int):
        op_type_widget: Type[OpUi] = to_ui_type(index)
        self.ops_stack.addWidget(op_type_widget(parent=self.parent, index=index))

    def stack_push(self, q: QWidget):
        self.ops_stack.addWidget(q)

    def __len__(self):
        return len(self.stepTabs.children())

    def __setitem__(self, i: int, wid: QWidget):
        self.stepTabs.insertTab(i, wid, wid.objectName())

    def __len__(self) -> int:
        return self.stepTabs.count()

    def __popitem__(self) -> QWidget:
        return self.stepTabs.(i)

    def __delitem__(self, i: int):
        self.stepTabs.removeTab(i)

    def __append__(self, wid: QWidget):
        self.stepTabs.addTab(wid, wid.objectName())

    def __getitem__(self, i: int):
        return self.stepTabs.children()[i]

    def stack_remove(self, idx: int) -> QWidget:
        w = self.ops_stack.widget(len(self)-1)
        self.ops_stack.removeWidget(w)
        return w

    def stack_pop(self) -> QWidget:
        w = self.stack_remove(len(self)-1)
        return w