from PyQt5 import QtWidgets
from ui_calculator import Ui_Calculator


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):

    firstNum = None
    zeroDivision = False
    resultDisplayed = False
    multiple_operations = False
    multiple_operations_times = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Ui == Ui_Calculator
        self.show()
        # Connect buttons
        self.pushButton_0.clicked.connect(self.digit_pressed)
        self.pushButton_1.clicked.connect(self.digit_pressed)
        self.pushButton_2.clicked.connect(self.digit_pressed)
        self.pushButton_3.clicked.connect(self.digit_pressed)
        self.pushButton_4.clicked.connect(self.digit_pressed)
        self.pushButton_5.clicked.connect(self.digit_pressed)
        self.pushButton_6.clicked.connect(self.digit_pressed)
        self.pushButton_7.clicked.connect(self.digit_pressed)
        self.pushButton_8.clicked.connect(self.digit_pressed)
        self.pushButton_9.clicked.connect(self.digit_pressed)

        self.pushButton_decimal.clicked.connect(self.decimal_pressed)

        self.pushButton_plusMinus.clicked.connect(self.plusMinus_pressed)
        self.pushButton_percent.clicked.connect(self.percent_pressed)

        self.pushButton_add.clicked.connect(self.binary_operation_pressed)
        self.pushButton_subtract.clicked.connect(self.binary_operation_pressed)
        self.pushButton_multiply.clicked.connect(self.binary_operation_pressed)
        self.pushButton_divide.clicked.connect(self.binary_operation_pressed)

        self.pushButton_equals.clicked.connect(self.equals_pressed)

        self.pushButton_add.setCheckable(True)         # ┐
        self.pushButton_subtract.setCheckable(True)   # │╲ buttons can be checked
        self.pushButton_multiply.setCheckable(True)    # │╱ buttons can be checked
        self.pushButton_divide.setCheckable(True)      # ┘

        self.pushButton_clear.clicked.connect(self.clear_screen)

        self.pushButton_arrow.clicked.connect(self.rmv_last_digit)

    def digit_pressed(self):
        button = self.sender()
        if len(self.operation_screen.text().replace(',', '')) < 15:  # if there are less than 18 characters
            if self.zeroDivision:  # if Error is on the screen
                newLabel = button.text()
                self.calcHistory.setText("")
                self.zeroDivision = False
            else:  # if Error is not on the screen
                newLabel = self.operation_screen.text().replace(',', '') + button.text()
                if self.resultDisplayed:
                    self.calcHistory.setText("")
                    self.resultDisplayed = False

            self.operation_screen.setText(self.addComma(newLabel))
            self.fit_digits()

    def decimal_pressed(self):
        if len(self.operation_screen.text()) < 14:  # if there are less than 14 characters on the screen
            if '.' not in self.operation_screen.text():  # if there isn't another '.' on the screen
                if self.operation_screen.text() != "Error":  # if Error is on the screen
                    if '%' not in self.operation_screen.text():  # if there is % already on the screen
                        self.operation_screen.setText(self.operation_screen.text() + '.')
                        if self.operation_screen.text()[0] == '.':  # if the first character on the screen is '.'
                            self.operation_screen.setText('0.')
                else:  # if Error is on the screen
                    self.operation_screen.setText('0.')
                    self.zeroDivision = False

    def plusMinus_pressed(self):
        if self.operation_screen.text() == '-':  # if '-' is the only character on the screen
            self.operation_screen.setText('')

        elif self.operation_screen.text() != '':  # if the screen is not blank
            if self.operation_screen.text() != "Error":  # if Error isn't on the screen
                if '%' not in self.operation_screen.text():  # if % is not on the screen
                    labelNumber = float(self.operation_screen.text().replace(',', ''))

                    labelNumber = labelNumber * -1

                    newLabel = format(labelNumber, '.15g')

                    self.operation_screen.setText(self.addComma(newLabel))

                else:  # if % is the last character on the screen
                    if self.operation_screen.text().replace(',', '')[-1] == '%':  # if the last character on the screen is %
                        labelNumber = float(self.operation_screen.text().replace(',', '')[:-1])

                        labelNumber = labelNumber * -1

                        newLabel = format(labelNumber, '.15g') + '%'

                        self.operation_screen.setText(self.addComma(newLabel))
                    else:  # if there is a number after the %
                        percent_index = self.operation_screen.text().replace(',', '').index('%')
                        percent_number = self.operation_screen.text().replace(',', '')[percent_index:]
                        number = float(self.operation_screen.text().replace(',', '')[:percent_index])
                        number = number * -1

                        newLabel = format(number, '.15g') + percent_number
                        self.operation_screen.setText(self.addComma(newLabel))
            else:  # if Error is on the screen
                self.operation_screen.setText('-')
                self.zeroDivision = False

        else:  # if the screen is blank
            self.operation_screen.setText('-')

    def percent_pressed(self):
        if self.operation_screen.text() != '' and '%' not in self.operation_screen.text():  # if the screen is not blank and if
            labelPercent = self.operation_screen.text() + '%'                               # there isn't another %
            self.operation_screen.setText(labelPercent)
            self.fit_digits()

    def binary_operation_pressed(self):
        button = self.sender()
        if not self.multiple_operations:  # if operation button was pressed only one time
            if self.operation_screen.text() != '' and self.operation_screen.text() != "Error":  # if the screen is not blank and
                if '%' not in self.operation_screen.text():                                     # Error isn't on the screen

                    self.firstNum = float(self.operation_screen.text().replace(',', ''))
                    if self.operation_screen.text() != '0.':  # if firstNum ins't 0.
                        if button.text() == '—':  # if the operation is subtraction
                            self.calcHistory.setText(f'{self.addComma(self.operation_screen.text())}  -')
                        else:  # if the operation is not subtraction
                            self.calcHistory.setText(f'{self.addComma(self.operation_screen.text())} {button.text()}')
                    else:  # if firstNum is 0.
                        if button.text() == '—':  # if the operation is subtraction
                            self.calcHistory.setText('0  -')
                        else:  # if the operation is not subtraction
                            self.calcHistory.setText(f'0 {button.text()}')
                    button.setChecked(True)

                    self.operation_screen.setText("")
                else:  # if percent is in first number
                    self.firstNum = float(self.calculate_percent())

                    if button.text() == '—':  # if the operation is subtraction
                        self.calcHistory.setText(f"{self.addComma(self.firstNum)}  -")
                    else:  # if the operation is not subtraction
                        self.calcHistory.setText(f"{self.addComma(str(self.firstNum).replace('.0', ''))} {button.text()}")

                    button.setChecked(True)
                    self.operation_screen.setText("")

            elif self.operation_screen.text() == "Error":  # if Error is on screen
                self.zeroDivision = False
                self.firstNum = None
                self.operation_screen.setText('')
        else:  # if button is already checked (if multiple operations straight are made)
            self.multiple_operations = True

    def equals_pressed(self):
        if (self.pushButton_add.isChecked() or self.pushButton_subtract.isChecked() or  # if the operation buttons were pressed
                self.pushButton_multiply.isChecked() or self.pushButton_divide.isChecked()) and self.firstNum is not None:
            if self.operation_screen.text() != '':  # if second num isn't blank

                if '%' in self.operation_screen.text():  # if % is in second num
                    secondNum = float(self.calculate_percent())
                else:  # if % isn't in second num
                    secondNum = float(self.operation_screen.text().replace(',', ''))
                self.calcHistory.setText(f"{self.calcHistory.text()} {self.addComma(str(secondNum).replace('.0', ''))}")

                if self.pushButton_add.isChecked():  # add button was pressed
                    labelNumber = self.firstNum + secondNum
                    newLabel = format(labelNumber, '.15g')
                    if len(newLabel) > 15:
                        newLabel = self.exponent_factor(newLabel)
                    self.operation_screen.setText(self.addComma(newLabel))
                    self.pushButton_add.setChecked(False)
                    self.resultDisplayed = True
                    self.fit_digits()

                elif self.pushButton_subtract.isChecked():  # subtract button was pressed
                    labelNumber = self.firstNum - secondNum
                    newLabel = format(labelNumber, '.15g')
                    self.operation_screen.setText(self.addComma(newLabel))
                    self.pushButton_subtract.setChecked(False)
                    self.resultDisplayed = True
                    self.fit_digits()

                elif self.pushButton_multiply.isChecked():  # multiply button was pressed
                    labelNumber = self.firstNum * secondNum
                    newLabel = format(labelNumber, '.15g')
                    # if len(newLabel) > 15:
                    #     newLabel = self.exponent_factor(newLabel)
                    self.operation_screen.setText(self.addComma(newLabel))
                    self.pushButton_multiply.setChecked(False)
                    self.resultDisplayed = True
                    self.fit_digits()

                elif self.pushButton_divide.isChecked():  # divide button was pressed
                    if secondNum != 0:  # if the second num isn't 0
                        labelNumber = self.firstNum / secondNum
                        newLabel = format(labelNumber, '.15g')
                        self.operation_screen.setText(self.addComma(newLabel))
                        self.pushButton_divide.setChecked(False)
                        self.resultDisplayed = True
                        self.fit_digits()
                    else:  # if the second num is 0
                        self.operation_screen.setText("Error")
                        self.pushButton_divide.setChecked(False)
                        self.zeroDivision = True

            else:  # if the second num is blank
                if self.firstNum is not None:
                    self.operation_screen.setText(self.addComma(format(self.firstNum, '.15g')))
                    self.calcHistory.setText('')
                    self.pushButton_add.setChecked(False)
                    self.pushButton_subtract.setChecked(False)
                    self.pushButton_divide.setChecked(False)
                    self.pushButton_multiply.setChecked(False)

        elif '%' in self.operation_screen.text():
            number = self.calculate_percent()
            self.calcHistory.setText(f'{self.operation_screen.text()} =')
            self.operation_screen.setText(self.addComma(number))
            self.resultDisplayed = True

    def clear_screen(self):
        self.operation_screen.setText('')
        self.calcHistory.setText('')
        self.operation_screen.setStyleSheet(" font: 75 50pt \"Calibri\";\n"
                                            " color: rgb(255, 255, 255);\n"
                                            " background-color: rgb(12, 16, 25);\n")
        self.firstNum = None
        self.resultDisplayed = False

    def rmv_last_digit(self):
        if self.operation_screen.text() != "Error":  # if Error isn't on the screen
            # if not self.resultDisplayed:  # if the result isn't displayed on the screen
            last_digit_removed = self.operation_screen.text().replace(',', '')[:-1]
            self.operation_screen.setText(self.addComma(last_digit_removed))
            if self.resultDisplayed:  # if the result isn't displayed on the screen
                self.firstNum = None
                self.calcHistory.setText("")
            self.resultDisplayed = False
            self.fit_digits()

        else:  # if Error is on the screen
            self.operation_screen.setText("")
            self.calcHistory.setText("")
            self.firstNum = None

    def calculate_percent(self):
        if self.operation_screen.text()[-1] == '%':  # if the last character on the screen is %
            number = float(self.operation_screen.text()[:-1].replace(',', ''))
            result = number * 0.01
            newLabel = format(result, '.15g')

        else:  # if there is a number after the %
            percent_index = self.operation_screen.text().replace(',', '').index('%')
            number = float(self.operation_screen.text().replace(',', '')[:percent_index])
            percent = float(self.operation_screen.text().replace(',', '')[percent_index + 1:])
            result = number / 100 * percent
            newLabel = format(result, '.15g')

        return newLabel

    def exponent_factor(self, num):  # adds the e notation to numbers bigger that 15 diigts
        num = str(num).replace(',', '')
        if len(num) > 15:
            newLabel = format(num, '.3e')
            return newLabel
        else:
            pass

    def addComma(self, num):
        if '.' in str(num):  # if is float
            num = str(num)
            num = str(num.replace(',', ''))
            point_index = num.index('.')
            if '%' not in num:  # if % isn't in num
                post = num[point_index + 1:]
                num = num[:point_index]
            else:  # if % is in num
                percent_index = num.index('%')
                post = num[point_index + 1:percent_index]
                if num[-1] == '%':  # if % is the last character on the screen
                    num = num[:point_index] + '%'
                else:  # if there is a number after %
                    num = num[:point_index] + num[percent_index:]
            num = list(num)
            num.reverse()

            count1 = 0
            list1 = []
            count2 = 0
            list2 = []
            if '-' not in num:  # if number is positive
                if '%' not in num:  # if % isn't in num
                    for i in num:
                        count1 += 1
                        if count1 % 3 == 0:
                            list1.append(i)
                            list1.append(',')
                        else:
                            list1.append(i)

                    list1.reverse()

                    return ''.join(list1).strip(',') + '.' + post
                else:  # if % is in num
                    if num[0] == '%':  # if % was the last character in num
                        num.remove('%')
                        for i in num:
                            count1 += 1
                            if count1 % 3 == 0:
                                list1.append(i)
                                list1.append(',')
                            else:
                                list1.append(i)

                        list1.reverse()

                        return ''.join(list1).strip(',') + '.' + post + '%'
                    else:  # if there was a number after %
                        percent_index = num.index('%')
                        percent_number = num[0:percent_index]
                        for i in percent_number:
                            count2 += 1
                            if count2 % 3 == 0:
                                list2.append(i)
                                list2.append(',')
                            else:
                                list2.append(i)

                        list2.reverse()

                        del num[:percent_index + 1]
                        for i in num:
                            count1 += 1
                            if count1 % 3 == 0:
                                list1.append(i)
                                list1.append(',')
                            else:
                                list1.append(i)

                        list1.reverse()

                        return ''.join(list1).strip(',') + '.' + post + '%' + ''.join(list2).strip(',')

            else:  # if number is negative
                num.remove('-')
                if '%' not in num:  # if % isn't in num
                    for i in num:
                        count1 += 1
                        if count1 % 3 == 0:
                            list1.append(i)
                            list1.append(',')
                        else:
                            list1.append(i)

                    list1.reverse()

                    return '-' + ''.join(list1).strip(',') + '.' + post
                else:  # if % is in num
                    if num[0] == '%':  # if % was the last character in num
                        num.remove('%')
                        for i in num:
                            count1 += 1
                            if count1 % 3 == 0:
                                list1.append(i)
                                list1.append(',')
                            else:
                                list1.append(i)

                        list1.reverse()

                        return '-' + ''.join(list1).strip(',') + '.' + post + '%'
                    else:  # if there was a number after %
                        percent_index = num.index('%')
                        percent_number = num[0:percent_index]
                        for i in percent_number:
                            count2 += 1
                            if count2 % 3 == 0:
                                list2.append(i)
                                list2.append(',')
                            else:
                                list2.append(i)

                        list2.reverse()

                        del num[:percent_index + 1]
                        for i in num:
                            count1 += 1
                            if count1 % 3 == 0:
                                list1.append(i)
                                list1.append(',')
                            else:
                                list1.append(i)

                        list1.reverse()

                        return '-' + ''.join(list1).strip(',') + '.' + post + '%' + ''.join(list2).strip(',')
        else:  # if is int
            num = str(num)
            num = str(num.replace(',', ''))
            num = list(num)
            num.reverse()

            count1 = 0
            list1 = []
            count2 = 0
            list2 = []
            if '-' not in num:  # if number is positive
                if '%' not in num:  # if % isn't in num
                    for i in num:
                        count1 += 1
                        if count1 % 3 == 0:
                            list1.append(i)
                            list1.append(',')
                        else:
                            list1.append(i)

                    list1.reverse()

                    return ''.join(list1).strip(',')
                else:  # if % is in num
                    if num[0] == '%':  # if % was the last character in num
                        num.remove('%')
                        for i in num:
                            count1 += 1
                            if count1 % 3 == 0:
                                list1.append(i)
                                list1.append(',')
                            else:
                                list1.append(i)

                        list1.reverse()

                        return ''.join(list1).strip(',') + '%'
                    else:  # if there was a number after %
                        percent_index = num.index('%')
                        percent_number = num[0:percent_index]
                        for i in percent_number:
                            count2 += 1
                            if count2 % 3 == 0:
                                list2.append(i)
                                list2.append(',')
                            else:
                                list2.append(i)

                        list2.reverse()

                        del num[:percent_index + 1]
                        for i in num:
                            count1 += 1
                            if count1 % 3 == 0:
                                list1.append(i)
                                list1.append(',')
                            else:
                                list1.append(i)

                        list1.reverse()

                        return ''.join(list1).strip(',') + '%' + ''.join(list2).strip(',')

            else:  # if number is negative
                num.remove('-')
                if '%' not in num:  # if % isn't in num
                    for i in num:
                        count1 += 1
                        if count1 % 3 == 0:
                            list1.append(i)
                            list1.append(',')
                        else:
                            list1.append(i)

                    list1.reverse()

                    return '-' + ''.join(list1).strip(',')
                else:  # if % is in num
                    if num[0] == '%':  # if % was the last character in num
                        num.remove('%')
                        for i in num:
                            count1 += 1
                            if count1 % 3 == 0:
                                list1.append(i)
                                list1.append(',')
                            else:
                                list1.append(i)

                        list1.reverse()

                        return '-' + ''.join(list1).strip(',') + '%'
                    else:  # if there was a number after %
                        percent_index = num.index('%')
                        percent_number = num[0:percent_index]
                        for i in percent_number:
                            count2 += 1
                            if count2 % 3 == 0:
                                list2.append(i)
                                list2.append(',')
                            else:
                                list2.append(i)

                        list2.reverse()

                        del num[:percent_index + 1]
                        for i in num:
                            count1 += 1
                            if count1 % 3 == 0:
                                list1.append(i)
                                list1.append(',')
                            else:
                                list1.append(i)

                        list1.reverse()

                        return '-' + ''.join(list1).strip(',') + '%' + ''.join(list2).strip(',')

    def fit_digits(self):
        if len(self.operation_screen.text().replace('-', '')) == 16:
            self.operation_screen.setStyleSheet(" font: 75 24pt \"Calibri\";\n"
                                                " color: rgb(255, 255, 255);\n"
                                                " background-color: rgb(12, 16, 25);\n")
        elif len(self.operation_screen.text().replace('-', '')) == 15:
            self.operation_screen.setStyleSheet(" font: 75 26pt \"Calibri\";\n"
                                                " color: rgb(255, 255, 255);\n"
                                                " background-color: rgb(12, 16, 25);\n")
        elif len(self.operation_screen.text().replace('-', '')) == 14:
            self.operation_screen.setStyleSheet(" font: 75 28pt \"Calibri\";\n"
                                                " color: rgb(255, 255, 255);\n"
                                                " background-color: rgb(12, 16, 25);\n")
        elif len(self.operation_screen.text()) == 13:
            self.operation_screen.setStyleSheet(" font: 75 31pt \"Calibri\";\n"
                                                " color: rgb(255, 255, 255);\n"
                                                " background-color: rgb(12, 16, 25);\n")
        elif len(self.operation_screen.text().replace('-', '')) == 12:
            self.operation_screen.setStyleSheet(" font: 75 34pt \"Calibri\";\n"
                                                " color: rgb(255, 255, 255);\n"
                                                " background-color: rgb(12, 16, 25);\n")
        elif len(self.operation_screen.text().replace('-', '')) == 11:
            self.operation_screen.setStyleSheet(" font: 75 36.4pt \"Calibri\";\n"
                                                " color: rgb(255, 255, 255);\n"
                                                " background-color: rgb(12, 16, 25);\n")
        elif len(self.operation_screen.text().replace('-', '')) == 10:
            self.operation_screen.setStyleSheet(" font: 75 40pt \"Calibri\";\n"
                                                " color: rgb(255, 255, 255);\n"
                                                " background-color: rgb(12, 16, 25);\n")
        elif len(self.operation_screen.text().replace('-', '')) == 9:
            self.operation_screen.setStyleSheet(" font: 75 45pt \"Calibri\";\n"
                                                " color: rgb(255, 255, 255);\n"
                                                " background-color: rgb(12, 16, 25);\n")
        else:
            self.operation_screen.setStyleSheet(" font: 75 50pt \"Calibri\";\n"
                                                " color: rgb(255, 255, 255);\n"
                                                " background-color: rgb(12, 16, 25);\n")
