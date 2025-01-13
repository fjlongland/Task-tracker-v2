from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from.database import get_dates

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        x = 30
        y = 40
        width = 1000
        height = 1000
        self.setWindowTitle("Task Tracker")
        self.setGeometry(x, y, width, height)
        self.setWindowIcon(QIcon("imij.jpg"))

        layout = QVBoxLayout()


#////////////////lstbxDates///////////////////////////////////////////////////////////////////////////

        self.list_box = QListWidget(self)
        items = get_dates()
        self.list_box.addItems(items)
        self.list_box.move(20,20)
        self.list_box.setFixedHeight(self.list_box.sizeHintForRow(0)*len(items))
        self.list_box.setFixedWidth(150)
        layout.addWidget(self.list_box)



        self.setLayout(layout)




