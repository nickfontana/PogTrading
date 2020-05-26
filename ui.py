import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QLineEdit
from ui_main import Ui_MainWindow
from api import get_current_stock_price
from marginBot import marginBot

class MainWindow:

    def __init__(self, parent = None):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.MakeMoneyButton.clicked.connect(self.on_MAKEMONEY_click)
        self.ui.lookupButton.clicked.connect(self.on_LOOKUP_click)


    def show(self):
        self.main_win.show()

    def on_LOOKUP_click(self):
        userSymbol = self.ui.stockSymbol.text().upper()
        lookup_info = "Current price of " + userSymbol + ": " + str(get_current_stock_price(userSymbol))
        self.ui.OutputText.setText(lookup_info)

    def on_MAKEMONEY_click(self):
        if self.ui.stockSymbol.hasAcceptableInput() == False:
            self.ui.OutputText.setText("Please enter a valid stock symbol")
        if self.ui.desiredMargins.text().isdigit() == False:
            self.ui.OutputText.setText("Please enter a number greater than 0")
        userSymbol = self.ui.stockSymbol.text().upper()
        userMargins = float(self.ui.desiredMargins.text())/100
        self.ui.OutputText.setText(marginBot(userSymbol, userMargins))
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

# exec python -m PyQt5.uic.pyuic mainwindow.ui -o ui_main.py -x

