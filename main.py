import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem, QAbstractScrollArea
import sqlite3

con = sqlite3.connect('coffee.sqlite')
cur = con.cursor()


def select_all_coffee():
    query = 'select * from coffee'
    result = cur.execute(query).fetchall()
    return result


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.coffee = select_all_coffee()

        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setColumnCount(len(self.coffee[0]))
        self.tableWidget.setRowCount(len(self.coffee))

        for i, elem in enumerate(self.coffee):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
