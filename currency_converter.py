from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    to_rupees = [1, 82.4029, 54.8583, 104.7117, 0.5697]
    from_rupees = [1, 0.0121, 0.0182, 0.0096, 1.7559]
    infield = 1

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(894, 334)
        MainWindow.setStyleSheet("\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:347.1, stop:0 rgba(244, 212, 212, 236), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.unit_1 = QtWidgets.QComboBox(self.centralwidget)
        self.unit_1.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.unit_1.setFont(font)
        self.unit_1.setStyleSheet("background-color: rgb(255, 133, 96);")
        self.unit_1.setEditable(False)
        self.unit_1.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.unit_1.setObjectName("unit_1")
        self.unit_1.addItem("")
        self.unit_1.addItem("")
        self.unit_1.addItem("")
        self.unit_1.addItem("")
        self.unit_1.addItem("")
        self.verticalLayout_3.addWidget(self.unit_1)
        self.value_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.value_1.setMinimumSize(QtCore.QSize(300, 200))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.value_1.setFont(font)
        self.value_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.value_1.setAlignment(QtCore.Qt.AlignCenter)
        self.value_1.setObjectName("value_1")
        self.verticalLayout_3.addWidget(self.value_1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton.setStyleSheet("background-image: url(convert_icon.png);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.unit_2 = QtWidgets.QComboBox(self.centralwidget)
        self.unit_2.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.unit_2.setFont(font)
        self.unit_2.setStyleSheet("background-color: rgb(255, 227, 189);")
        self.unit_2.setEditable(False)
        self.unit_2.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.unit_2.setObjectName("unit_2")
        self.unit_2.addItem("")
        self.unit_2.addItem("")
        self.unit_2.addItem("")
        self.unit_2.addItem("")
        self.unit_2.addItem("")
        self.verticalLayout_4.addWidget(self.unit_2)
        self.value_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.value_2.setMinimumSize(QtCore.QSize(300, 200))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.value_2.setFont(font)
        self.value_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.value_2.setObjectName("value_2")
        self.verticalLayout_4.addWidget(self.value_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 894, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.value_1.setValidator(QtGui.QDoubleValidator())
        self.value_2.setValidator(QtGui.QDoubleValidator())
        self.value_1.textChanged.connect(self.convert1)
        self.value_2.textChanged.connect(self.convert2)
        self.pushButton.clicked.connect(self.calculate)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Currency Converter"))
        self.unit_1.setItemText(0, _translate("MainWindow", "INR"))
        self.unit_1.setItemText(1, _translate("MainWindow", "USD"))
        self.unit_1.setItemText(2, _translate("MainWindow", "AUD"))
        self.unit_1.setItemText(3, _translate("MainWindow", "GBP"))
        self.unit_1.setItemText(4, _translate("MainWindow", "JPY"))
        self.value_1.setText(_translate("MainWindow", "0"))
        self.unit_2.setItemText(0, _translate("MainWindow", "INR"))
        self.unit_2.setItemText(1, _translate("MainWindow", "USD"))
        self.unit_2.setItemText(2, _translate("MainWindow", "AUD"))
        self.unit_2.setItemText(3, _translate("MainWindow", "GBP"))
        self.unit_2.setItemText(4, _translate("MainWindow", "JPY"))
        self.value_2.setText(_translate("MainWindow", "0"))

    def convert1(self):
        self.infield=1
    
    def convert2(self):
        self.infield=2

    def calculate(self):
        if self.infield == 1:
            self.value_2.textChanged.disconnect(self.convert2)
            if self.value_1.text() == "":
                self.value_2.setText("0")
            else:
                v1 = float(self.value_1.text())
                index1 = self.unit_1.currentIndex()
                index2 = self.unit_2.currentIndex()
                value = v1 * self.to_rupees[index1] * self.from_rupees[index2]
                self.value_2.setText(str(round(value, 4)))
            self.value_2.textChanged.connect(self.convert2)
        else:
            self.value_1.textChanged.disconnect(self.convert1)
            if self.value_2.text() == "":
                self.value_1.setText("0")
            else:
                v2 = float(self.value_2.text())
                index1 = self.unit_1.currentIndex()
                index2 = self.unit_2.currentIndex()
                value = v2 * self.to_rupees[index2] * self.from_rupees[index1]
                self.value_1.setText(str(round(value, 4)))
            self.value_1.textChanged.connect(self.convert1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
