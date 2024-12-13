from PyQt5 import QtWidgets
import authorization, main, registration,Del
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
            # self.ui.label_2.setText("Такого пользователя нет!")
            QtWidgets.QMessageBox.information(None, "Ошибка", "Такого пользователя нет. Повторите попытку", buttons=QtWidgets.QMessageBox.Ok, defaultButton=QtWidgets.QMessageBox.Ok)

        else:
            auto.close()
            main.show()
            # main.ui.label.setText(str(result[0]))
            # main.ui.label_2.setText(str(result[1]))
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
        #######################
        
        # self.ui.lineEdit.setPlaceholderText('Имя')
        # self.ui.lineEdit_2.setPlaceholderText('Фамилия')
        # self.ui.lineEdit_3.setPlaceholderText('Логин')
        # self.ui.lineEdit_4.setPlaceholderText('Пароль')
        #######################
        name = self.ui.lineEdit.text()
        last_name = self.ui.lineEdit_2.text() 
        login = self.ui.lineEdit_4.text()   
        password = self.ui.lineEdit_3.text()
        
        if name  ==  "" or last_name  == ""  or login  == "" or password  == "":
            QtWidgets.QMessageBox.information(None, "Ошибка", "Неверные данные", buttons=QtWidgets.QMessageBox.Ok, defaultButton=QtWidgets.QMessageBox.Ok) 
        else:
            row = (name, last_name, login, password)
            command = "INSERT INTO users (name, last_name, login, password) VALUES (?, ?, ?, ?)" 
            cursor.execute('SELECT login FROM users WHERE login = ?', (login,))

            result = cursor.fetchall()
            if  result:
                msgbox  = QtWidgets.QMessageBox()
                msgbox.setText("Логин уже занят")
                msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msgbox.exec()
            else:
                cursor.execute(command,row)
                msgbox  = QtWidgets.QMessageBox()
                msgbox.setText("Регистрация прошла успешно.")
                msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgbox.exec()
        
        db.commit()
            #QtWidgets.QMessageBox.information(None, "Регистрация", "Вы успешно зарегистрировались",buttons = QtWidgets.QMessageBox.Ok,defaultButton = QtWidgets.QMessageBox.Ok)                         
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit_4.setText("")


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
        self.ui.knopka_add.clicked.connect(self.add)
        self.ui.knopka_delete.clicked.connect(self.delete)
        self.ui.knopka_upd.clicked.connect(self.updata)
        
        #######################
        db = sqlite3.connect("Users.db")
        cursor = db.cursor()
        command = "SELECT * FROM users"
        result = cursor.execute(command)

        self.ui.tableWidget.setRowCount(0)
        for stroka, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(stroka)
            for stolb, data in enumerate(row_data):
                self.ui.tableWidget.setItem(stroka, stolb, QtWidgets.QTableWidgetItem(str(data)))
        #########################
    def add(self):
        reg.show()
        
        
    def updata(self):
        db = sqlite3.connect("Users.db")
        cursor = db.cursor()
        command = "SELECT * FROM users"
        result = cursor.execute(command)

        self.ui.tableWidget.setRowCount(0)
        for stroka, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(stroka)
            for stolb, data in enumerate(row_data):
                self.ui.tableWidget.setItem(stroka, stolb, QtWidgets.QTableWidgetItem(str(data)))
        
    def delete(self):
        dIt.delete2()
    
    
    

class DelForm(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Del.Ui_Dialog()
        self.ui.setupUi(self)
        # self.buttonBox.accepted.connect(self.delete2)
        self.ui.buttonBox.accepted.connect(self.delete2)
        

    def delete2(self):
        text,ok = QtWidgets.QInputDialog.getText(None,"Кого удалим?", "Удалить:", echo=0)
        if ok:
            db = sqlite3.connect("Users.db")
            cursor = db.cursor()
            command = "DELETE FROM users WHERE login =?"
            cursor.execute(command, (text,))
            db.commit()
            main.updata()


if __name__ ==  "__main__":
    import sys
    app = QtWidgets.QApplication (sys.argv) 
    auto = Authorization()
    auto.show()
    reg = Registration()
    main = MainWindow()
    main.updata
    
    dIt = DelForm()
    sys.exit(app.exec_())
        
