# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xyeta.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(571, 483)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(60, 50, 381, 261))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(150, 40, 91, 31))
        self.label.setStyleSheet("font: 25pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(150, 170, 81, 41))
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(130, 40, 141, 21))
        self.label_2.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.page_2)
        self.radioButton.setGeometry(QtCore.QRect(60, 100, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.page_2)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 130, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 220, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.radioButton_3 = QtWidgets.QRadioButton(self.page_3)
        self.radioButton_3.setGeometry(QtCore.QRect(60, 130, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.page_3)
        self.radioButton_4.setGeometry(QtCore.QRect(60, 160, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.page_3)
        self.radioButton_5.setGeometry(QtCore.QRect(60, 190, 82, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(150, 70, 101, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 220, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.radioButton_6 = QtWidgets.QRadioButton(self.page_4)
        self.radioButton_6.setGeometry(QtCore.QRect(50, 120, 82, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.page_4)
        self.radioButton_7.setGeometry(QtCore.QRect(50, 150, 82, 17))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.page_4)
        self.radioButton_8.setGeometry(QtCore.QRect(50, 180, 82, 17))
        self.radioButton_8.setObjectName("radioButton_8")
        self.label_4 = QtWidgets.QLabel(self.page_4)
        self.label_4.setGeometry(QtCore.QRect(160, 70, 91, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 230, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_5.setGeometry(QtCore.QRect(290, 230, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtWidgets.QLabel(self.page_5)
        self.label_5.setGeometry(QtCore.QRect(160, 50, 121, 21))
        self.label_5.setObjectName("label_5")
        self.radioButton_9 = QtWidgets.QRadioButton(self.page_5)
        self.radioButton_9.setGeometry(QtCore.QRect(60, 120, 82, 17))
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(self.page_5)
        self.radioButton_10.setGeometry(QtCore.QRect(60, 150, 82, 17))
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_11 = QtWidgets.QRadioButton(self.page_5)
        self.radioButton_11.setGeometry(QtCore.QRect(60, 180, 82, 17))
        self.radioButton_11.setObjectName("radioButton_11")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 230, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.radioButton_12 = QtWidgets.QRadioButton(self.page_6)
        self.radioButton_12.setGeometry(QtCore.QRect(40, 120, 82, 17))
        self.radioButton_12.setObjectName("radioButton_12")
        self.radioButton_13 = QtWidgets.QRadioButton(self.page_6)
        self.radioButton_13.setGeometry(QtCore.QRect(40, 160, 82, 17))
        self.radioButton_13.setObjectName("radioButton_13")
        self.radioButton_14 = QtWidgets.QRadioButton(self.page_6)
        self.radioButton_14.setGeometry(QtCore.QRect(40, 200, 82, 17))
        self.radioButton_14.setObjectName("radioButton_14")
        self.label_6 = QtWidgets.QLabel(self.page_6)
        self.label_6.setGeometry(QtCore.QRect(140, 60, 121, 16))
        self.label_6.setObjectName("label_6")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.label_7 = QtWidgets.QLabel(self.page_7)
        self.label_7.setGeometry(QtCore.QRect(80, 60, 231, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_7.setGeometry(QtCore.QRect(290, 230, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.radioButton_15 = QtWidgets.QRadioButton(self.page_7)
        self.radioButton_15.setGeometry(QtCore.QRect(30, 110, 82, 17))
        self.radioButton_15.setObjectName("radioButton_15")
        self.radioButton_16 = QtWidgets.QRadioButton(self.page_7)
        self.radioButton_16.setGeometry(QtCore.QRect(30, 140, 82, 17))
        self.radioButton_16.setObjectName("radioButton_16")
        self.radioButton_17 = QtWidgets.QRadioButton(self.page_7)
        self.radioButton_17.setGeometry(QtCore.QRect(30, 170, 82, 17))
        self.radioButton_17.setObjectName("radioButton_17")
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.label_8 = QtWidgets.QLabel(self.page_8)
        self.label_8.setGeometry(QtCore.QRect(50, 50, 141, 71))
        self.label_8.setStyleSheet("font: 22pt \"Times New Roman\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_8)
        self.label_9.setGeometry(QtCore.QRect(50, 120, 111, 71))
        self.label_9.setStyleSheet("font: 22pt \"Times New Roman\";")
        self.label_9.setObjectName("label_9")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_8)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 230, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.stackedWidget.addWidget(self.page_8)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ТЕСТ "))
        self.pushButton.setText(_translate("Form", "НАЧАТЬ!"))
        self.label_2.setText(_translate("Form", "Тебя зовут Фархат?"))
        self.radioButton.setText(_translate("Form", "ДА"))
        self.radioButton_2.setText(_translate("Form", "НЕТ"))
        self.pushButton_2.setText(_translate("Form", "Далее"))
        self.radioButton_3.setText(_translate("Form", "15"))
        self.radioButton_4.setText(_translate("Form", "31"))
        self.radioButton_5.setText(_translate("Form", "5"))
        self.label_3.setText(_translate("Form", "10+ 5"))
        self.pushButton_3.setText(_translate("Form", "Далее"))
        self.radioButton_6.setText(_translate("Form", "20"))
        self.radioButton_7.setText(_translate("Form", "100"))
        self.radioButton_8.setText(_translate("Form", "50"))
        self.label_4.setText(_translate("Form", "10 * 10"))
        self.pushButton_4.setText(_translate("Form", "Далее"))
        self.pushButton_5.setText(_translate("Form", "Далее"))
        self.label_5.setText(_translate("Form", "Сосал? "))
        self.radioButton_9.setText(_translate("Form", "ДА"))
        self.radioButton_10.setText(_translate("Form", "НЕТ"))
        self.radioButton_11.setText(_translate("Form", "ВОЗМОЖНО"))
        self.pushButton_6.setText(_translate("Form", "Далее"))
        self.radioButton_12.setText(_translate("Form", "РКН"))
        self.radioButton_13.setText(_translate("Form", "Инстаграмм"))
        self.radioButton_14.setText(_translate("Form", "Телерамм"))
        self.label_6.setText(_translate("Form", "Что запрещено в РФ?"))
        self.label_7.setText(_translate("Form", "Когда началась Вторая Мировая Война?"))
        self.pushButton_7.setText(_translate("Form", "Далее"))
        self.radioButton_15.setText(_translate("Form", "01.09.1939"))
        self.radioButton_16.setText(_translate("Form", "22.06.1941"))
        self.radioButton_17.setText(_translate("Form", "02.01.2007"))
        self.label_8.setText(_translate("Form", "Баллы: "))
        self.label_9.setText(_translate("Form", "Оценка:"))
        self.pushButton_8.setText(_translate("Form", "ДОМ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
