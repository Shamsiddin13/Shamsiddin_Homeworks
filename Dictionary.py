from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QListWidget
from PyQt5.QtGui import QIcon, QFont,  QGuiApplication

class Add(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add New Words")
        self.setWindowIcon(QIcon("C:\\Shamsiddin Courses\\New Projects\\Icons\\document.png"))

        self.SearchMsg = QMessageBox()

        self.v_lang_lay = QVBoxLayout()
        self.h_top_lay = QHBoxLayout()
        self.v_main_lay = QVBoxLayout()

        self.eng_edit = QLineEdit()
        self.eng_edit.setPlaceholderText("Eng...")
        self.eng_edit.setFont(QFont("Colcolas",15))

        self.uz_edit = QLineEdit()
        self.uz_edit.setPlaceholderText("Uz...")
        self.uz_edit.setFont(QFont("Colcolas",15))


        self.send_btn = QPushButton("Send")
        self.send_btn.clicked.connect(self.send_method)
        self.send_btn.setFont(QFont("Arial",15, 80))
        self.send_btn.setStyleSheet("color:Black; background-color:Cornsilk")

        


        self.approval_label = QLabel("")
        self.approval_label.setFont(QFont("Colibri",15))


        self.Menu_btn = QPushButton("Menu")
        self.Menu_btn.clicked.connect(self.close_add_win)
        self.Menu_btn.setFont(QFont("Arial",15, 80))
        self.Menu_btn.setStyleSheet("color:Black; background-color:PaleGreen")



        self.Clear_btn = QPushButton("Clear")
        self.Clear_btn.clicked.connect(self.Word_Clear)
        self.Clear_btn.setFont(QFont("Arial",15, 80))
        self.Clear_btn.setStyleSheet("color:Black; background-color:LightCyan")




        self.v_lang_lay.addWidget(self.eng_edit)
        self.v_lang_lay.addWidget(self.uz_edit)
        self.v_lang_lay.addWidget(self.Clear_btn)


        self.h_top_lay.addLayout(self.v_lang_lay)
        self.h_top_lay.addWidget(self.send_btn)
        # self.h_top_lay.addWidget(self.Clear_btn)


        self.v_main_lay.addLayout(self.h_top_lay)
        self.v_main_lay.addWidget(self.approval_label)
        # self.v_main_lay.addWidget(self.Clear_btn)
        self.v_main_lay.addWidget(self.Menu_btn)

        self.setLayout(self.v_main_lay)

    def send_method(self):
        
        self.Add_List_Dict_Data = [] 

        self.Old_Data_Dict = []

        with open("Dictionary.txt", "r+") as Dict_Data:
            self.Add_List_Dict_Data.append(Dict_Data.read().split())

            for lst in self.Add_List_Dict_Data[0]:
                self.Old_Data_Dict.append(lst.split("|"))

        with open("Dictionary.txt", "a+") as Dict_Data:
            self.Add_List_Dict_Data.clear()

            self.Check_Word = []

            self.eng_words = self.eng_edit.text()
            self.uz_words = self.uz_edit.text()

            self.lamp = "No"

            for i in self.Old_Data_Dict:
                if self.eng_words.capitalize() == i[0] or self.uz_words.capitalize() == i[1]:
                    self.lamp = "Yes"

            if self.lamp != "Yes":
                self.Check_Word.clear()

                if self.eng_edit.text().capitalize() != "" and self.uz_edit.text().capitalize() == "" or self.eng_edit.text().capitalize() == "" and self.uz_edit.text().capitalize() != "":

                    self.SearchMsg.setIcon(QMessageBox.Warning)
                    self.SearchMsg.setStyleSheet("color:red")
                    self.SearchMsg.setWindowTitle("Incompleted ...")
                    self.SearchMsg.setText("Please Complete ...")
                    self.SearchMsg.setFont(QFont("Times New Roman",12))
                    self.SearchMsg.exec_()
                
                else:

                    Dict_Data.write(self.eng_edit.text().capitalize() + "|" + self.uz_edit.text().capitalize())
                    Dict_Data.write("\n")
                    self.Check_Word.append(self.eng_words.capitalize())
                    self.Check_Word.append(self.uz_words.capitalize())
                    self.MessageForAdded(self.lamp, self.eng_edit.text().capitalize(), self.uz_edit.text().capitalize())
                    MainWindow.Check_List_Words.append(self.Check_Word)
            else:
                
                # self.approval_label.setText("This word is Exist ...")
                self.MessageForAdded(self.lamp, self.eng_edit.text().capitalize(), self.uz_edit.text().capitalize())


        with open("Dictionary.txt", "r+") as Dict_Data:
            self.Add_List_Dict_Data.append(Dict_Data.read().split())

            for lst in self.Add_List_Dict_Data[0]:
                MainWindow.Add_List_Uzb_Eng_Lang.append(lst.split("|"))
                

    def MessageForAdded(self, lamp, Eng_word, Uzb_Word):
        
        if lamp == "No":

            self.SearchMsg.setIcon(QMessageBox.Information)
            self.SearchMsg.setStyleSheet("Color:Green;")
            self.SearchMsg.setWindowTitle("Added")
            self.SearchMsg.setText(f"""" {Eng_word} " is added ...""")
            self.SearchMsg.setFont(QFont("Times New Roman",12))
            self.SearchMsg.exec_()
            # self.SearchMsg.buttonClicked.connect()

        elif lamp == "Yes" :

            if Eng_word == "":
                self.SearchMsg.setText(f"""" {Uzb_Word} " is exist ...""")
            else:
                self.SearchMsg.setText(f"""" {Eng_word} " is exist ...""")
                
            self.SearchMsg.setIcon(QMessageBox.Warning)
            self.SearchMsg.setStyleSheet("color:red")
            self.SearchMsg.setWindowTitle("Exist")
            self.SearchMsg.setFont(QFont("Times New Roman",12))
            self.SearchMsg.exec_()


    def Word_Clear(self):
        self.eng_edit.clear()
        self.uz_edit.clear()
        self.approval_label.clear()


    def close_add_win(self):
        self.eng_edit.clear()
        self.uz_edit.clear()
        self.approval_label.clear()
        self.close()

class List(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowIcon(QIcon("C:\\Shamsiddin Courses\\New Projects\\Icons\\adddictionary.png"))
        self.setWindowTitle("Vocabulary")


        self.h_lang_lay = QHBoxLayout()
        self.h_lstWidg_lay = QHBoxLayout()
        self.v_main_lay = QVBoxLayout()

        self.eng_label = QLabel("English")
        self.eng_label.setStyleSheet("color:Balck;")
        self.eng_label.setFont(QFont("Arial Black", 15))

        self.uz_label = QLabel("Uzbek")
        self.uz_label.setStyleSheet("color:Balck;")
        self.uz_label.setFont(QFont("Arial Black", 15))
    
        self.h_lang_lay.addWidget(self.eng_label)
        self.h_lang_lay.addWidget(self.uz_label)

        self.eng_list = QListWidget()
        self.uz_list = QListWidget()
        self.eng_list.setFont(QFont("Times New Roman",15))
        self.uz_list.setFont(QFont("Times New Roman",15))


        self.h_lstWidg_lay.addWidget(self.eng_list)
        self.h_lstWidg_lay.addWidget(self.uz_list)

        self.Menu_btn = QPushButton("Menu")
        self.Menu_btn.setStyleSheet("color:Balck; background-color:PaleGreen")
        self.Menu_btn.setFont(QFont("Arial", 15, 80))

        self.Menu_btn.clicked.connect(self.Close_List_Win)

        self.Refresh_btn = QPushButton("Refresh")
        self.Refresh_btn.setStyleSheet("color:Black; background-color:PowderBlue")
        self.Refresh_btn.setFont(QFont("Arial", 15, 80))


        self.v_main_lay.addLayout(self.h_lang_lay)
        self.v_main_lay.addLayout(self.h_lstWidg_lay)
        self.v_main_lay.addWidget(self.Refresh_btn)
        self.v_main_lay.addWidget(self.Menu_btn)

        self.setLayout(self.v_main_lay)

        self.Add_List_Dict_Data = []

        with open("Dictionary.txt", "r") as Dict_Data:
            self.Add_List_Dict_Data.append(Dict_Data.read().split())
    
            for lst in self.Add_List_Dict_Data[0]:
                MainWindow.Add_List_Uzb_Eng_Lang.append(lst.split("|"))

        for i in MainWindow.Add_List_Uzb_Eng_Lang:
            self.eng_list.addItem(i[0])
            self.uz_list.addItem(i[1])

    def Close_List_Win(self):
        self.close()

    def Refresh_Data(self):

        for i in MainWindow.Check_List_Words:
            self.eng_list.addItem(i[0])
            self.uz_list.addItem(i[1])
        self.ShowMessage()
        MainWindow.Check_List_Words.clear()
    
    def ShowMessage(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Added New Words")
        msg.setText(f"Added {len(MainWindow.Check_List_Words)} new words to the dictionary ...")
        msg.setFont(QFont("Times New Roman",12))
        # msg.buttonClicked.connect()
        msg.exec_()


class Search(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Words")
        self.setWindowIcon(QIcon("C:\\Shamsiddin Courses\\New Projects\\Icons\\Dictionary.png"))
        self.Main_V_Layout = QVBoxLayout()
        self.Top_H_Layout = QHBoxLayout()

        self.Uzb_Eng_Search_Edit = QLineEdit()
        self.Uzb_Eng_Search_Edit.setPlaceholderText("Uzb -> Eng or Eng -> Uzb")
        self.Uzb_Eng_Search_Edit.setFont(QFont("Colcolas", 15))


        self.Search_Word_Button = QPushButton("Search")
        self.Search_Word_Button.setStyleSheet("color:Black; background-color:Honeydew")
        self.Search_Word_Button.setFont(QFont("Arial", 15, 80))
        self.Search_Word_Button.clicked.connect(self.Result_Words)

        self.Clear_Word_Button = QPushButton("Clear")
        self.Clear_Word_Button.setStyleSheet("color:Black; background-color:Lightcyan")
        self.Clear_Word_Button.setFont(QFont("Arial", 15, 80))
        self.Clear_Word_Button.clicked.connect(self.Clear_Word)


        self.Top_H_Layout.addWidget(self.Uzb_Eng_Search_Edit)
        self.Top_H_Layout.addWidget(self.Search_Word_Button)

        self.Result_Word = QLabel("Result Words")
        self.Result_Word.setFont(QFont("Times", 20))
        
        self.Search_Menu_Button = QPushButton("Menu")
        self.Search_Menu_Button.setStyleSheet("color:Black; background-color:PaleGreen")
        self.Search_Menu_Button.setFont(QFont("Arial", 15, 80))
        self.Search_Menu_Button.clicked.connect(self.close_search_win)
        

        self.Main_V_Layout.addLayout(self.Top_H_Layout)
        self.Main_V_Layout.addWidget(self.Clear_Word_Button)
        self.Main_V_Layout.addWidget(self.Result_Word)
        self.Main_V_Layout.addWidget(self.Search_Menu_Button)


        self.setLayout(self.Main_V_Layout)

    def Clear_Word(self):
        self.Uzb_Eng_Search_Edit.clear()



    def Result_Words(self):
        
        self.Add_List_Dict_Data = []

        with open("Dictionary.txt", "r+") as Dict_Data:
            self.Add_List_Dict_Data.append(Dict_Data.read().split())

            for lst in self.Add_List_Dict_Data[0]:
                MainWindow.Add_List_Uzb_Eng_Lang.append(lst.split("|"))

        self.Lamp = "No"

        for i in MainWindow.Add_List_Uzb_Eng_Lang:
            self.uzb = self.Uzb_Eng_Search_Edit.text()

            if  self.uzb.capitalize() == i[0]:
                self.Result_Word.setText(f"Uzb: {i[1]}")
                self.Lamp = "Yes"

            if self.uzb.capitalize() == i[1]:
                self.Result_Word.setText(f"Eng: {i[0]}")
                self.Lamp = "Yes"
            
        if self.Lamp == "No":
            self.No_Added_Msg()
        
            
         
    
    def No_Added_Msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon("C:\\Shamsiddin Courses\\New Projects\\Icons\\no-results.png"))
        msg.setWindowTitle("Not Found")
        msg.setText(f"This Word is Not Found ...")
        msg.setFont(QFont("Arial Black", 12))
        msg.setStyleSheet("color:red;")
        # msg.buttonClicked.connect(self.m)
        msg.exec_()

    def close_search_win(self):
        self.Uzb_Eng_Search_Edit.clear()
        self.Result_Word.setText("Result Words...")
        self.close()


class MainWindow(QMainWindow):
    Add_List_Uzb_Eng_Lang = []
    Check_List_Words = []
    def __init__(self):
        super().__init__()
        self.setFixedSize(350,380)
        self.setWindowTitle("Dictionary")
        self.setWindowIcon(QIcon("C:\\Shamsiddin Courses\\New Projects\\Icons\\Book-Dictionary-Mac-Book.png"))
        
        self.add_obj = Add()
        self.search_obj = Search()
        self.lst_obj = List()

        self.add_btn = QPushButton("ADD",self)
        self.add_btn.setGeometry(125, 50, 100, 75)
        self.add_btn.clicked.connect(self.add_win)
        self.add_btn.setFont(QFont("Arial", 12, 80))


        self.search_btn = QPushButton("SEARCH",self)
        self.search_btn.setGeometry(125, 125, 100, 75)
        self.search_btn.clicked.connect(self.search_win)
        self.search_btn.setFont(QFont("Arial", 12, 80))


        self.lst_btn = QPushButton("LIST",self)
        self.lst_btn.setGeometry(125, 200, 100, 75)
        self.lst_btn.clicked.connect(self.lst_win)
        self.lst_btn.setFont(QFont("Arial", 12, 80))



        self.exit_btn = QPushButton("EXIT",self)
        self.exit_btn.setGeometry(125, 275, 100, 75)
        self.exit_btn.clicked.connect(self.close)
        self.exit_btn.setFont(QFont("Arial", 12, 80))


    def add_win(self):
        self.add_obj.setFixedSize(400, 400)
        self.add_obj.show()

    def lst_win(self):
        self.lst_obj.setFixedSize(500, 500)
        self.lst_obj.show()
        self.lst_obj.Refresh_btn.clicked.connect(self.lst_obj.Refresh_Data)

    def search_win(self):
        self.search_obj.show()
        self.search_obj.setFixedSize(400,400)

if __name__ == "__main__":
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec_()
