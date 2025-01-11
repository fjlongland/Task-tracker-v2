from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        x = 30
        y = 40
        width = 1000
        height = 1000
        self.setGeometry(x, y, width, height)
        self.setWindowIcon(QIcon("imij.jpg"))