
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(300, 530)
        MainWindow.setMinimumSize(QtCore.QSize(300, 530))
        MainWindow.setMaximumSize(QtCore.QSize(300, 530))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Calculator512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.operation_screen = QtWidgets.QLabel(self.centralwidget)
        self.operation_screen.setEnabled(True)
        self.operation_screen.setGeometry(QtCore.QRect(0, 50, 288, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.operation_screen.setFont(font)
        self.operation_screen.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.operation_screen.setAutoFillBackground(False)
        self.operation_screen.setStyleSheet(" font: 75 50pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(12, 16, 25);\n"
"\n"
"")
        self.operation_screen.setTextFormat(QtCore.Qt.AutoText)
        self.operation_screen.setScaledContents(False)
        self.operation_screen.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.operation_screen.setIndent(0)
        self.operation_screen.setObjectName("operation_screen")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(10, 130, 64, 64))
        self.pushButton_clear.setStyleSheet("QPushButton {\n"
" font: 75 25pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(13, 20, 28);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 29, 37);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_arrow = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_arrow.setGeometry(QtCore.QRect(80, 130, 64, 64))
        self.pushButton_arrow.setStyleSheet("QPushButton {\n"
" font: 75 25pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(13, 20, 28);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 29, 37);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_arrow.setObjectName("pushButton_arrow")
        self.pushButton_percent = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_percent.setGeometry(QtCore.QRect(150, 130, 64, 64))
        self.pushButton_percent.setStyleSheet("QPushButton {\n"
" font: 75 25pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(13, 20, 28);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 29, 37);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.pushButton_divide = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_divide.setGeometry(QtCore.QRect(220, 130, 64, 64))
        self.pushButton_divide.setStyleSheet("QPushButton {\n"
" font: 75 30pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(22, 26, 35);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 29, 37);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(150, 210, 64, 64))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
" font: 75 25pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(13, 20, 28);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 29, 37);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(80, 210, 64, 64))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
" font: 75 25pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(13, 20, 28);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 29, 37);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 210, 64, 64))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
" font: 75 25pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(13, 20, 28);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 29, 37);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_multiply.setGeometry(QtCore.QRect(220, 210, 64, 64))
        self.pushButton_multiply.setStyleSheet("QPushButton {\n"
" font: 75 30pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(22, 26, 35);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 29, 37);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 290, 64, 64))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
" font: 75 25pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(13, 20, 28);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 29, 37);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 290, 64, 64))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
" font: 75 25pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(13, 20, 28);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 29, 37);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 290, 64, 64))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
" font: 75 25pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(13, 20, 28);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 29, 37);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_subtract = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_subtract.setGeometry(QtCore.QRect(220, 290, 64, 64))
        self.pushButton_subtract.setStyleSheet("QPushButton {\n"
" font: 75 25pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(22, 26, 35);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 29, 37);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_subtract.setObjectName("pushButton_subtract")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(149, 370, 64, 64))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
" font: 75 25pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(13, 20, 28);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 29, 37);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 370, 64, 64))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
" font: 75 25pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(13, 20, 28);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 29, 37);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 370, 64, 64))
        self.pushButton_1.setStyleSheet("QPushButton {\n"
" font: 75 25pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(13, 20, 28);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 29, 37);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(220, 370, 64, 64))
        self.pushButton_add.setStyleSheet("QPushButton {\n"
" font: 75 30pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(22, 26, 35);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 29, 37);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_decimal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_decimal.setGeometry(QtCore.QRect(149, 450, 64, 64))
        self.pushButton_decimal.setStyleSheet("QPushButton {\n"
" font: 75 25pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(13, 20, 28);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 29, 37);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_decimal.setObjectName("pushButton_decimal")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(80, 450, 64, 64))
        self.pushButton_0.setStyleSheet("QPushButton {\n"
" font: 75 25pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(13, 20, 28);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 29, 37);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_plusMinus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plusMinus.setGeometry(QtCore.QRect(10, 450, 64, 64))
        self.pushButton_plusMinus.setStyleSheet("QPushButton {\n"
" font: 75 25pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(13, 20, 28);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 29, 37);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_plusMinus.setObjectName("pushButton_plusMinus")
        self.pushButton_equals = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equals.setGeometry(QtCore.QRect(220, 450, 64, 64))
        self.pushButton_equals.setStyleSheet("QPushButton {\n"
" font: 75 30pt \"Calibri\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: rgb(240, 37, 40);\n"
" border-style: solid;\n"
" border-radius:32px;\n"
" max-width:64px;\n"
" max-height:64px;\n"
" min-width:64px;\n"
" min-height:64px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(206, 33, 35);\n"
"    color: rgb(138, 142, 145);\n"
"}")
        self.pushButton_equals.setObjectName("pushButton_equals")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 120, 300, 410))
        self.label_2.setStyleSheet("background-color: rgb(13, 20, 28);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(288, 50, 20, 70))
        self.label.setStyleSheet(" color: rgb(255, 255, 255);\n"
" background-color: rgb(12, 16, 25);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.calcHistory = QtWidgets.QLabel(self.centralwidget)
        self.calcHistory.setGeometry(QtCore.QRect(0, 0, 280, 50))
        self.calcHistory.setStyleSheet(" font: 75 30pt \"Calibri\";\n"
" color: rgb(138, 142, 145);\n"
" background-color: rgb(12, 16, 25);\n"
"")
        self.calcHistory.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.calcHistory.setObjectName("calcHistory")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 0, 20, 50))
        self.label_4.setStyleSheet("background-color: rgb(12, 16, 25);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_2.raise_()
        self.operation_screen.raise_()
        self.pushButton_clear.raise_()
        self.pushButton_arrow.raise_()
        self.pushButton_percent.raise_()
        self.pushButton_divide.raise_()
        self.pushButton_9.raise_()
        self.pushButton_8.raise_()
        self.pushButton_7.raise_()
        self.pushButton_multiply.raise_()
        self.pushButton_6.raise_()
        self.pushButton_5.raise_()
        self.pushButton_4.raise_()
        self.pushButton_subtract.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton_1.raise_()
        self.pushButton_add.raise_()
        self.pushButton_decimal.raise_()
        self.pushButton_0.raise_()
        self.pushButton_plusMinus.raise_()
        self.pushButton_equals.raise_()
        self.label.raise_()
        self.calcHistory.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.operation_screen.setText(_translate("MainWindow", ""))
        self.pushButton_clear.setText(_translate("MainWindow", "C"))
        self.pushButton_arrow.setText(_translate("MainWindow", "⌫"))
        self.pushButton_percent.setText(_translate("MainWindow", "%"))
        self.pushButton_divide.setText(_translate("MainWindow", "÷"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_multiply.setText(_translate("MainWindow", "×"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_subtract.setText(_translate("MainWindow", "—"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
        self.pushButton_decimal.setText(_translate("MainWindow", "."))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_plusMinus.setText(_translate("MainWindow", "+/-"))
        self.pushButton_equals.setText(_translate("MainWindow", "="))
        self.calcHistory.setText(_translate("MainWindow", ""))

