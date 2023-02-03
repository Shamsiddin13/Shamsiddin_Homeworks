from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton,QMainWindow, QGridLayout, QGroupBox
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QCheckBox, QComboBox, QMessageBox, QRadioButton, QBoxLayout
from PyQt5.QtGui import QIcon, QFont,  QGuiApplication
import sys
from random import *

class Window(QWidget):
    def __init__(self) -> None:
        self.Checking = False
        super().__init__()
        self.setWindowTitle("Box-Game")
        self.setFixedSize(440, 510)

        self.msg = QMessageBox()
        self.msg.setWindowTitle("WINNER")
        self.msg.setFont(QFont("Arial Balck",12))

        self.Grid_Layout = QGridLayout()

        self.Numbers_Window = QGroupBox("NUMBERS")
        self.Numbers_Window.setFont(QFont("Arial Black", 10))
        self.Numbers_Window.setStyleSheet("color:Black; background-color:LightGray;")

        self.H_Buttons_Layout = QHBoxLayout()
        self.H_Space_Layout = QHBoxLayout()

        self.V_Main_Layout = QVBoxLayout()


        self.Check_Button = QPushButton("CHECK")
        self.Check_Button.setFont(QFont("Arial Black",15))
        self.Check_Button.setStyleSheet("color:Black; background-color:Lime;")

        self.Start_Button = QPushButton("START")
        self.Start_Button.setFont(QFont("Arial Black",15))
        self.Start_Button.setStyleSheet("color:Black; background-color:Aqua;")


        self.Reset_Button = QPushButton("RESET")
        self.Reset_Button.setFont(QFont("Arial Black",15))
        self.Reset_Button.setStyleSheet("color:Black; background-color:LightSkyBlue;")


        self.Close_Button = QPushButton("CLOSE")
        self.Close_Button.setFont(QFont("Arial Black",15))
        self.Close_Button.setStyleSheet("color:Red; background-color:White;")


        self.H_Buttons_Layout.addWidget(self.Start_Button)
        self.H_Buttons_Layout.addWidget(self.Reset_Button)
        self.H_Buttons_Layout.addWidget(self.Close_Button)

        self.H_Space_Layout.addStretch()
        self.H_Space_Layout.addWidget(self.Check_Button)
        self.H_Space_Layout.addStretch()


        self.btn1 = QPushButton("1")
        self.btn2 = QPushButton("2")
        self.btn3 = QPushButton("3")
        self.btn4 = QPushButton("4")
        self.btn5 = QPushButton("5")
        self.btn6 = QPushButton("6")
        self.btn7 = QPushButton("7")
        self.btn8 = QPushButton("8")
        self.btn9 = QPushButton("9")
        self.btn10 = QPushButton("10")
        self.btn11 = QPushButton("11")
        self.btn12 = QPushButton("12")
        self.btn13 = QPushButton("13")
        self.btn14 = QPushButton("14")
        self.btn15 = QPushButton("15")
        self.btn16 = QPushButton("")

        self.Lst_Buttons = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9, self.btn10, self.btn11, self.btn12, self.btn13, self.btn14, self.btn15, self.btn16] 

        self.Lst_Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ""]
        self.Old_Lst_Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ""]

        
        self.Start_Button.clicked.connect(self.Click_Start)
        self.Reset_Button.clicked.connect(self.Click_Reset)
        self.Close_Button.clicked.connect(self.close)
        self.Check_Button.clicked.connect(self.Result_Check)




        self.str_style = """QPushButton {
            color:Arial Black;
            background-color:LightCyan;
            font: bold 20pt;
            }"""

        index = 0
        for i in range(4):
            for j in range(4):
                self.Grid_Layout.addWidget(self.Lst_Buttons[index], i, j)
                self.Lst_Buttons[index].setFixedSize(96,82)
                self.Lst_Buttons[index].setStyleSheet(self.str_style)
                self.Lst_Buttons[index].setFont(QFont("Arial Balck",15))
                self.Lst_Buttons[index].setDisabled(True)

                index+=1

        self.Numbers_Window.setLayout(self.Grid_Layout)

        # self.V_Main_Layout.addLayout(self.Grid_Layout)
        self.V_Main_Layout.addWidget(self.Numbers_Window)
        self.V_Main_Layout.addLayout(self.H_Space_Layout)
        self.V_Main_Layout.addLayout(self.H_Buttons_Layout)
        
        self.setLayout(self.V_Main_Layout)

        self.btn1.clicked.connect(self.Btn1_Click)
        self.btn2.clicked.connect(self.Btn2_Click)
        self.btn3.clicked.connect(self.Btn3_Click)
        self.btn4.clicked.connect(self.Btn4_Click)
        self.btn5.clicked.connect(self.Btn5_Click)
        self.btn6.clicked.connect(self.Btn6_Click)
        self.btn7.clicked.connect(self.Btn7_Click)
        self.btn8.clicked.connect(self.Btn8_Click)
        self.btn9.clicked.connect(self.Btn9_Click)
        self.btn10.clicked.connect(self.Btn10_Click)
        self.btn11.clicked.connect(self.Btn11_Click)
        self.btn12.clicked.connect(self.Btn12_Click)
        self.btn13.clicked.connect(self.Btn13_Click)
        self.btn14.clicked.connect(self.Btn14_Click)
        self.btn15.clicked.connect(self.Btn15_Click)
        self.btn16.clicked.connect(self.Btn16_Click)

    def Btn1_Click(self):
        # print(self.btn1.text())
        if self.btn2.text() == "":
            self.btn2.setText(str(self.btn1.text()))
            self.btn1.setText("")
            pass
        elif self.btn5.text() == "":
            self.btn5.setText(str(self.btn1.text()))
            self.btn1.setText("")
        self.Result_Check()


    def Btn2_Click(self):
        # print(self.btn2.text())
        if self.btn1.text() == "":
            self.btn1.setText(str(self.btn2.text()))
            self.btn2.setText("")
            
        elif self.btn3.text() == "":
            self.btn3.setText(str(self.btn2.text()))
            self.btn2.setText("")

        elif self.btn6.text() == "":
            self.btn6.setText(str(self.btn2.text()))
            self.btn2.setText("")

        self.Result_Check()
    
    def Btn3_Click(self):
        # print(self.btn3.text())
        if self.btn2.text() == "":
            self.btn2.setText(str(self.btn3.text()))
            self.btn3.setText("")
            
        elif self.btn4.text() == "":
            self.btn4.setText(str(self.btn3.text()))
            self.btn3.setText("")

        elif self.btn7.text() == "":
            self.btn7.setText(str(self.btn3.text()))
            self.btn3.setText("")

        self.Result_Check()

    def Btn4_Click(self):
        # print(self.btn4.text())
        if self.btn3.text() == "":
            self.btn3.setText(str(self.btn4.text()))
            self.btn4.setText("")
            
        elif self.btn8.text() == "":
            self.btn8.setText(str(self.btn4.text()))
            self.btn4.setText("")
        self.Result_Check()

    def Btn5_Click(self):
        # print(self.btn5.text())
        if self.btn1.text() == "":
            self.btn1.setText(str(self.btn5.text()))
            self.btn5.setText("")
            
        elif self.btn6.text() == "":
            self.btn6.setText(str(self.btn5.text()))
            self.btn5.setText("")

        elif self.btn9.text() == "":
            self.btn9.setText(str(self.btn5.text()))
            self.btn5.setText("")
        
        self.Result_Check()

    def Btn6_Click(self):
        # print(self.btn6.text())
        if self.btn2.text() == "":
            self.btn2.setText(str(self.btn6.text()))
            self.btn6.setText("")
            
        elif self.btn5.text() == "":
            self.btn5.setText(str(self.btn6.text()))
            self.btn6.setText("")

        elif self.btn7.text() == "":
            self.btn7.setText(str(self.btn6.text()))
            self.btn6.setText("")

        elif self.btn10.text() == "":
            self.btn10.setText(str(self.btn6.text()))
            self.btn6.setText("")
        
        self.Result_Check()

    def Btn7_Click(self):
        # print(self.btn7.text())
        if self.btn3.text() == "":
            self.btn3.setText(str(self.btn7.text()))
            self.btn7.setText("")
            
        elif self.btn6.text() == "":
            self.btn6.setText(str(self.btn7.text()))
            self.btn7.setText("")

        elif self.btn8.text() == "":
            self.btn8.setText(str(self.btn7.text()))
            self.btn7.setText("")

        elif self.btn11.text() == "":
            self.btn11.setText(str(self.btn7.text()))
            self.btn7.setText("")

        self.Result_Check()

    def Btn8_Click(self):
        # print(self.btn8.text())
        if self.btn4.text() == "":
            self.btn4.setText(str(self.btn8.text()))
            self.btn8.setText("")
            
        elif self.btn7.text() == "":
            self.btn7.setText(str(self.btn8.text()))
            self.btn8.setText("")

        elif self.btn12.text() == "":
            self.btn12.setText(str(self.btn8.text()))
            self.btn8.setText("")
        
        self.Result_Check()

    def Btn9_Click(self):
        # print(self.btn9.text())
        if self.btn5.text() == "":
            self.btn5.setText(str(self.btn9.text()))
            self.btn9.setText("")
            
        elif self.btn10.text() == "":
            self.btn10.setText(str(self.btn9.text()))
            self.btn9.setText("")

        elif self.btn13.text() == "":
            self.btn13.setText(str(self.btn9.text()))
            self.btn9.setText("")
        
        self.Result_Check()

    def Btn10_Click(self):
        # print(self.btn10.text())

        if self.btn6.text() == "":
            self.btn6.setText(str(self.btn10.text()))
            self.btn10.setText("")
            
        elif self.btn9.text() == "":
            self.btn9.setText(str(self.btn10.text()))
            self.btn10.setText("")

        elif self.btn11.text() == "":
            self.btn11.setText(str(self.btn10.text()))
            self.btn10.setText("")

        elif self.btn14.text() == "":
            self.btn14.setText(str(self.btn10.text()))
            self.btn10.setText("")
        
        self.Result_Check()

    def Btn11_Click(self):
        # print(self.btn11.text())

        if self.btn7.text() == "":
            self.btn7.setText(str(self.btn11.text()))
            self.btn11.setText("")
            
        elif self.btn10.text() == "":
            self.btn10.setText(str(self.btn11.text()))
            self.btn11.setText("")

        elif self.btn12.text() == "":
            self.btn12.setText(str(self.btn11.text()))
            self.btn11.setText("")

        elif self.btn15.text() == "":
            self.btn15.setText(str(self.btn11.text()))
            self.btn11.setText("")
        
        self.Result_Check()

    def Btn12_Click(self):
        # print(self.btn12.text())

        if self.btn8.text() == "":
            self.btn8.setText(str(self.btn12.text()))
            self.btn12.setText("")
            
        elif self.btn11.text() == "":
            self.btn11.setText(str(self.btn12.text()))
            self.btn12.setText("")

        elif self.btn16.text() == "":
            self.btn16.setText(str(self.btn12.text()))
            self.btn12.setText("")
        
        self.Result_Check()

    def Btn13_Click(self):
        # print(self.btn13.text())

        if self.btn9.text() == "":
            self.btn9.setText(str(self.btn13.text()))
            self.btn13.setText("")
            
        elif self.btn14.text() == "":
            self.btn14.setText(str(self.btn13.text()))
            self.btn13.setText("")
        
        self.Result_Check()

    def Btn14_Click(self):
        # print(self.btn14.text())

        if self.btn10.text() == "":
            self.btn10.setText(str(self.btn14.text()))
            self.btn14.setText("")
            
        elif self.btn13.text() == "":
            self.btn13.setText(str(self.btn14.text()))
            self.btn14.setText("")

        elif self.btn15.text() == "":
            self.btn15.setText(str(self.btn14.text()))
            self.btn14.setText("")
        
        self.Result_Check()

    def Btn15_Click(self):
        # print(self.btn15.text())

        if self.btn11.text() == "":
            self.btn11.setText(str(self.btn15.text()))
            self.btn15.setText("")
            
        elif self.btn14.text() == "":
            self.btn14.setText(str(self.btn15.text()))
            self.btn15.setText("")

        elif self.btn16.text() == "":
            self.btn16.setText(str(self.btn15.text()))
            self.btn15.setText("")
        
        self.Result_Check()

    def Btn16_Click(self):
        # print(self.btn16.text())

        if self.btn12.text() == "":
            self.btn12.setText(str(self.btn16.text()))
            self.btn16.setText("")
            
        elif self.btn15.text() == "":
            self.btn15.setText(str(self.btn16.text()))
            self.btn16.setText("")
        
        self.Result_Check()


    def Click_Reset(self):
        self.Checking = False

        index = 0
        for i in range(16):
            if i != 15:
                self.Lst_Buttons[index].setText(f"{i+1}")
            else:
                self.Lst_Buttons[index].setText("")
            self.Lst_Buttons[index].setDisabled(True)
            index +=1


    def Result_Check(self):

        self.List_New_Numbers = []

        if self.Checking == True: 

            for i in self.Lst_Buttons:   
                    if i.text() == '':
                        self.List_New_Numbers.append(i.text())
                    else:
                        self.List_New_Numbers.append(int(i.text()))


            if  self.List_New_Numbers == self.Old_Lst_Numbers:
                self.msg.setIcon(QMessageBox.Information)
                # self.msg.buttonClicked.connect(self.close)
                self.msg.setText("You Are Winner !")
                self.msg.exec_()
            



    def Click_Start(self):
        
        self.Checking = True

        shuffle(self.Lst_Numbers)
        index = 0
        for num in self.Lst_Numbers: 
            self.Lst_Buttons[index].setText(str(num))
            self.Lst_Buttons[index].setDisabled(False)

            index+=1

if __name__ == "__main__":
    Box_Game = QApplication([])
    Game_Window = Window()
    Game_Window.setWindowTitle("Box-Game")  
    Game_Window.show()
    Box_Game.exec_()




