import sys
import time
from PyQt5.QtWidgets import QApplication
from .frontend import MainWindow
from .database import update_date

def main():

    update_date()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
