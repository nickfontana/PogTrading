import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui_main import Ui_MainWindow
from simpleBot import *

class MainWindow:

    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.MakeMoneyButton.clicked.connect(self.on_MAKEMONEY_click)

    def show(self):
        self.main_win.show()

    def on_MAKEMONEY_click(self):

        # test:
        self.ui.OutputText.setText("POGGERS")

        # Check for non empty inputs for symbol and margins
        ####################

        # Check to make sure account has enough buying power
        ####################

        # Otherwise activate bot

        ####################

if __name__ == '__main__':
    application = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(application.exec_())