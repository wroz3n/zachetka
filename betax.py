# My Application

import sqlite3
from PyQt5 import QtWidgets
import sasx

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS credit_cardx(number CHAR PRIMARY KEY, name TEXT, expiry_date TEXT, cvv INTEGER)
''')

conn.commit()

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = sasx.Ui_Form()
        self.ui.setupUi(self)
        self.ui.lineEdit.textChanged.connect(self.norma)
        self.ui.lineEdit_2.textChanged.connect(self.norma)
        self.ui.pushButton.clicked.connect(self.credit_card)

    def norma(self):
        try:
            c = float(self.ui.lineEdit.text())
            b = float(self.ui.lineEdit_2.text())
            if c is not None and b is not None:
                self.ui.label_3.setText(f"Depreciation for tax accounting = {str(c * b)}")
        except ValueError:
            self.ui.label_3.setText(f"Depreciation for tax accounting = ")

    def credit_card(self):
        number = self.ui.lineEdit_3.text()
        name = self.ui.lineEdit_4.text()
        expiry_date = self.ui.lineEdit_5.text()
        cvv = self.ui.lineEdit_6.text()

        self.ui.label_4.setText(f"Data: {number} {name} {expiry_date} {cvv}")
        cursor.execute('''
        INSERT OR REPLACE INTO credit_cardx (number, name, expiry_date, cvv) VALUES (?, ?, ?, ?)
        ''', (number, name, expiry_date, cvv))
        conn.commit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
