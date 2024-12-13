import sys
from PyQt5 import QtWidgets
# Импортируем сгенерированный файл

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Подключаем кнопку к методу
        self.ui.pushButton.clicked.connect(self.on_button_click)

    def on_button_click(self):
        # Закрываем приложение при нажатии на кнопку
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())