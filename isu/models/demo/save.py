from PyQt6.QtWidgets import ( QTreeWidget, QTreeWidgetItem, QTreeWidgetItemIterator)
from PyQt6.QtGui import (QAction )
from PyQt6.QtCore import (

    QXmlStreamReader, QXmlStreamAttribute, QXmlStreamNotationDeclaration,
    QXmlStreamAttributes, QXmlStreamEntityDeclaration, QXmlStreamEntityResolver,
    QXmlStreamNamespaceDeclaration, QXmlStreamWriter, 
    QIODevice, QIODeviceBase, 
    QTextStream, QTemporaryDir, QTemporaryFile,
)
from isu.models.demo import Demo

class DemoReader(QXmlStreamReader):
    def __init__(self, file: QIODevice):
        super().__init__(file)
        tree: QTreeWidget = QTreeWidget()
        
        

class DemoWriter(QXmlStreamWriter):
    def __init__(self, demo: Demo, file: QIODevice) -> None:
        """
        Write a demo to a file.
        """
        super().__init__(file)
        tree: QTreeWidget
        self.demo = demo
        self.setAutoFormatting(True)

    def write(self):
        self.writeDTD(u"<!DOCTYPE Demo>")
        self.writeStartElement("Demo")
        self.writeAttribute()
        self.writeEndDocument()