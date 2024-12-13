from PyQt5 import QtWidgets
import WW3


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = WW3.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.starttest)
        self.ui.pushButton_2.clicked.connect(self.vopros1)
        self.ui.pushButton_3.clicked.connect(self.vopros2)
        # self.ui.pushButton_4.clicked.connect(self.vopros3)
        # self.ui.pushButton_5.clicked.connect(self.vopros4)
        # self.ui.pushButton_6.clicked.connect(self.vopros5)
        # self.ui.pushButton_7.clicked.connect(self.vopros6)
        # self.ui.pushButton_8.clicked.connect(self.vopros7)
        self.a = 0 
    def starttest(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def vopros1(self):
        if self.ui.radioButton_2.isChecked():
            self.a += 1 
        self.ui.stackedWidget.setCurrentIndex(3)
        
    def vopros2(self):
        if self.ui.radioButton_3.isChecked():
            self.a += 1
        self.ui.stackedWidget.setCurrentIndex(2)

        


    

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
