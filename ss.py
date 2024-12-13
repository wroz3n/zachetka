import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel('', self)
        self.button = QPushButton('SOSAL?', self)
        self.button.setStyleSheet("""
            QPushButton {
  background-color: #0d6efd;
  color: #fff;
  font-weight: 600;
  border-radius: 8px;
  border: 1px solid #0d6efd;
  padding: 5px 15px;
  margin-top: 10px;
  outline: 0px;
}

QPushButton:hover,
QPushButton:focus {
  background-color: #0b5ed7;
  border: 3px solid #9ac3fe;
}
        """)

        self.button.clicked.connect(self.displayText)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setWindowTitle('GAY')
        self.show()

    def displayText(self):
        self.label.setText('YES')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
