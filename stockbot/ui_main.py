# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 409)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.stockSymbol = QtWidgets.QLineEdit(self.layoutWidget)
        self.stockSymbol.setObjectName("stockSymbol")
        self.verticalLayout.addWidget(self.stockSymbol)
        self.lookupButton = QtWidgets.QPushButton(self.layoutWidget)
        self.lookupButton.setObjectName("lookupButton")
        self.verticalLayout.addWidget(self.lookupButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(110, 16))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.desiredMargins = QtWidgets.QLineEdit(self.layoutWidget)
        self.desiredMargins.setObjectName("desiredMargins")
        self.verticalLayout_2.addWidget(self.desiredMargins)
        self.MakeMoneyButton = QtWidgets.QPushButton(self.layoutWidget)
        self.MakeMoneyButton.setObjectName("MakeMoneyButton")
        self.verticalLayout_2.addWidget(self.MakeMoneyButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.OutputText = QtWidgets.QTextBrowser(self.layoutWidget)
        self.OutputText.setObjectName("OutputText")
        self.verticalLayout_4.addWidget(self.OutputText)
        self.verticalLayout_5.addWidget(self.splitter)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.setBuddy(self.stockSymbol)
        self.label_2.setBuddy(self.desiredMargins)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.stockSymbol, self.desiredMargins)
        MainWindow.setTabOrder(self.desiredMargins, self.lookupButton)
        MainWindow.setTabOrder(self.lookupButton, self.MakeMoneyButton)
        MainWindow.setTabOrder(self.MakeMoneyButton, self.OutputText)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:64pt;\">PogTrading</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Stock"))
        self.lookupButton.setText(_translate("MainWindow", "Lookup"))
        self.label_2.setText(_translate("MainWindow", "Desired margins"))
        self.MakeMoneyButton.setText(_translate("MainWindow", "MAKE MONEY"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

