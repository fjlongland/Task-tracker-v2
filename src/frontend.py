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

                self.SettingsWindow = None


#/////////////////lblDates///////////////////////////////////////////////////////////////////////////\

                self.dateLable = QLabel("Previouse Week: ", self)
                self.dateLable.move(20, 0)

#////////////////lstbxDates///////////////////////////////////////////////////////////////////////////

                self.list_box = QListWidget(self)
                items = get_dates()
                self.list_box.addItems(items)
                self.list_box.move(20,30)
                self.list_box.setFixedHeight(self.list_box.sizeHintForRow(0)*len(items))
                self.list_box.setFixedWidth(150)
                self.list_box.setCurrentRow(0)

#//////////////////Question 1//////////////////////////////////////////////////////////////////////////

                self.lblQuestion1 = QLabel(self)
                self.lblQuestion1.setText("did you code today?")
                self.lblQuestion1.setGeometry(500, 0, 200, 50)

#/////////////////radbtnAnswer1////////////////////////////////////////////////////////////////////////

                self.rbAnswer1 = QRadioButton("Yes", self)
                self.rbAnswer2 = QRadioButton("No", self)
                self.rbAnswer1.setGeometry(500, 25, 100, 100)
                self.rbAnswer2.setGeometry(600, 25, 100, 100)

#//////////////////Settings Button//////////////////////////////////////////////////////////////////////


                self.btnSettings = QPushButton("Settings", self)
                self.btnSettings.setGeometry(900, 900, 100, 100)
                self.btnSettings.clicked.connect(self.settings_on_clicked)

#////////////////////functions//////////////////////////////////////////////////////////////////////////
            
        def settings_on_clicked(self):

                if not self.SettingsWindow:

                        self.SettingsWindow = SettingsWindow()

                self.SettingsWindow.show()
            


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("(settings)")
        self.setGeometry(30, 40, 500, 500)
        self.setWindowIcon(QIcon("imij.jpg"))

        self.lblTitle = QLabel("This is the second window", self)





