from asyncio.log import logger
from pathlib import Path, WindowsPath
from logging import Logger
import sqlite3
from PySide6.QtSql import QSqlDatabase, QSql, QSqlQuery
from PySide6.QtCore import *
from datetime import datetime, time

class Db(QObject):

    name: str = "isu-data"
    db: QSqlDatabase 
    path: QFile
    is_connected = Signal

    def __init__(self, 
                 name: str | None = None,
                 direc: Path | None = None):
        match name:
            case None: self.name = "isu-db"
            case n: self.name = n
        match direc:
            case None: self.directory = QDir(".")
            case d: self.directory = QDir(d)
        self.db = QSqlDatabase.database()
        self.db.setDatabaseName(self.name)
        self.path = QFile(self.connect())
        

    def connect(self) -> str:
        if not self.db.isValid():
            self.db = QSqlDatabase.addDatabase("QSQLITE")
            if not self.db.isValid():
                logger.error("Cannot add db")
        write_dir = QDir("")
        if not write_dir.mkpath("."):
            logger.error("Failed to create writable directory")

        return write_dir.absoluteFilePath(f"{self.name}.db")


    def init_demo_table(self): 
        q = QSqlQuery(query="""
        CREATE TABLE IF NOT EXISTS OpExecution (
            id integer primary key autoincrement
            status text not null default "pending"
            completed int default null, 
            scheduled int default null
        )
        CREATE TABLE IF NOT EXISTS Demo (
            id integer primary key autoincrement
            title text not null default ''
            path text not null
            created int not null default (strftime('%s', 'now'))
            updated int not null default (strftime('%s', 'now'))
        )

        CREATE TABLE IF NOT EXISTS OpSequence (
            id integer primary key autoincrement
            created int not null default (strftime('%s', 'now'))
            updated int not null default (strftime('%s', 'now'))
        )

        CREATE TABLE IF NOT EXISTS OpStep (
            id integer primary key autoincrement
            name text default ""
            seq_id integer not null
            op_id integer not null
            order_index integer not null
            created int not null default (strftime('%s', 'now'))
            updated int not null default (strftime('%s', 'now'))

            foreign key('op_id') references Ops('id')
            foreign key('seq_id') references OpSequence('id')
        )
        """)
        # self.db.exec()
        # query = QSqlQuery(db=self, other=None, query="")
    pass

if __name__=="__main__":
    pass