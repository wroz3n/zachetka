from PyQt5 import QtWidgets
import authorization, main, registration
import sqlite3
conn = sqlite3.connect('Users.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(name TEXT , last_name TEXT,login TEXT,password TEXT)
''')
class Authorization(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = authorization.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.reg_form)
        self.ui.pushButton.clicked.connect(self.auto)
        self.ui.lineEdit.setPlaceholderText('Enter your login')
        self.ui.lineEdit_2.setPlaceholderText('Enter your password')




    def reg_form(self):
        auto.close()
        reg.show()

    def auto(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()

        conn = sqlite3.connect('Users.db')
        cursor = conn.cursor()

        cursor.execute(f'SELECT name,last_name FROM users WHERE login = "{name}"and password = "{passw}"')
        result = cursor.fetchone()

        if result is None:
            self.ui.label_2.setText("Такого пользователя нет!")

        else:
            auto.close()
            main.show()
            main.ui.label.setText(str(result[0]))
            main.ui.label_2.setText(str(result[1]))
class Registration(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = registration.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.zareg)
        self.ui.pushButton_2.clicked.connect(self.back)
    
    def zareg(self):
        db = sqlite3.connect("Users.db") 
        cursor = db.cursor()

        name = self.ui.lineEdit.text()
        last_name = self.ui.lineEdit_2.text() 
        login = self.ui.lineEdit_3.text()   
        password = self.ui.lineEdit_4.text()
        row = (name, last_name, login, password)
        command = "INSERT INTO users (name, last_name, login, password) VALUES (?, ?, ?, ?)" 
        cursor.execute(command, row)

        db.commit()

        QtWidgets.QMessageBox.information(None, "Регистрация", "Вы успешно зарегистрировались",buttons = QtWidgets.QMessageBox.Ok,defaultButton = QtWidgets.QMessageBox.Ok)                         


        reg.close() 
        auto.show()

    def back(self):
        reg.close() 
        auto.show()

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main.Ui_Form()
        self.ui.setupUi(self)

if __name__ ==  "__main__":
    import sys
    app = QtWidgets.QApplication (sys.argv) 
    auto = Authorization()
    auto.show()
    reg = Registration()
    main = MainWindow()

    sys.exit(app.exec_())
        


















if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    auto = QtWidgets.QWidget()
    auto.show()
    reg = Registration()
    main = MainWindow()
    sys.exit(app.exec_())