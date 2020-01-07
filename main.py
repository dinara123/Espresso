import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem, QAbstractScrollArea, QPushButton
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
        self.load()
        self.take = Take()
        self.pushButton_2.clicked.connect(self.new)

    def load(self):
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setColumnCount(len(self.coffee[0]))
        self.tableWidget.setRowCount(len(self.coffee))

        for i, elem in enumerate(self.coffee):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def new(self):
        self.take.show()


class Take(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.coffee = select_all_coffee()
        self.pushButton.clicked.connect(self.submit)

    def submit(self):
        name = self.lineEdit.text()
        f_d = self.lineEdit_2.text()
        beans = self.lineEdit_3.text()
        taste = self.lineEdit_4.text()
        price = self.lineEdit_5.text()
        volume = self.lineEdit_6.text()
        cur.execute("INSERT INTO coffee(name, frying_degree, beans, taste, price, volume) VALUES (?, ?, ?, ?, ?, ?)",
                    (name, f_d, beans, taste, price, volume))
        con.commit()
        main_window = MyWidget()
        main_window.show()
        self.close()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
