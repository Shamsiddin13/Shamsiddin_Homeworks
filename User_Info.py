from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton,QMainWindow, QGridLayout
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QCheckBox, QComboBox, QMessageBox, QRadioButton
from PyQt5.QtGui import QIcon, QFont,  QGuiApplication
import sys


class Window(QWidget):
    def __init__(self) -> None:
        self.Point = 0
        self.Information = []
        super().__init__()
        self.setGeometry(500,200,700,800)
        self.Start()

    def OwnFont(self, obj, x, y):
        obj.setFont(QFont("Times", 15))
        obj.move(x,y)

    def Start(self):
    
        self.main = QMainWindow(self)
        self.main.setFixedSize(500,500)
        self.main.setWindowTitle('About User')


        self.Country = QLabel("Fill in the information about yourself ?", self)
        self.OwnFont(self.Country, 150,50)
        self.setFont(QFont("Book Antiqua", 40, 80, italic=True))

        self.N1 = QLabel("1) ", self)
        self.OwnFont(self.N1, 120,50)

        self.N2 = QLabel("2) ", self)
        self.OwnFont(self.N2, 120,250)
        self.N2_Question = QLabel("What country are you from ?", self)
        self.OwnFont(self.N2_Question, 150,250)

        self.central_asia_nations = QComboBox(self)
        self.OwnFont(self.central_asia_nations, 200, 300)
        self.central_asia_nations.addItems(['', 'Kazakhstan', 'Uzbekistan', 'Turkmenistan', 'Tajikistan', 'Kyrgyzstan'])
        self.central_asia_nations.setStyleSheet("color:Black; background-color:LightSkyBlue")
        self.central_asia_nations.setFont(QFont("Colibri", 15))
       
        self.N3 = QLabel("3) ", self)
        self.OwnFont(self.N3, 120,350)
        self.N3_Question = QLabel("What province are you from ?", self)
        self.OwnFont(self.N3_Question, 150,350)

        self.InUzb_Province = QComboBox(self)
        self.OwnFont(self.InUzb_Province, 200, 400)
        self.InUzb_Province.addItems(["","Andijan", "Bukhara", "Fergana", "Jizzakh", "Karakalpakstan", "Namangan", "Navoiy", "Qashqadaryo", "Samarqand", "Sirdaryo", "Surxondaryo", "Tashkent Region", "Xorazm", "Tashkent City"])
        self.InUzb_Province.setStyleSheet("color:Black; background-color:Yellow")
        self.InUzb_Province.setFont(QFont("Colibri", 15))
        
        self.N4 = QLabel("4) ", self)
        self.OwnFont(self.N4, 120,450)
        self.N4_Question = QLabel("What districts are you from ?", self)
        self.OwnFont(self.N4_Question, 150,450)

        self.N5 = QLabel("5) ", self)
        self.OwnFont(self.N5, 120,550)
        self.N4_Question = QLabel("Choose A Gender...", self)
        self.OwnFont(self.N4_Question, 150,550)

        self.Genders = QComboBox(self)
        self.OwnFont(self.Genders, 200, 600)
        self.Genders.addItems(["","Male","Female","Another"])
        self.Genders.setStyleSheet("color:Black; background-color:Aqua")
        self.Genders.setFont(QFont("Colibri", 15))

        self.FirstName = QLineEdit(self)
        self.OwnFont(self.FirstName, 200, 100)
        self.FirstName.setStyleSheet("color:Black; background-color:White")
        self.FirstName.setFont(QFont("Colibri", 15))
        self.FirstName.setPlaceholderText("First Name: ")
        self.FirstName.adjustSize()

        self.LastName = QLineEdit(self)
        self.OwnFont(self.LastName, 200, 150)
        self.LastName.setStyleSheet("color:Black; background-color:White")
        self.LastName.setFont(QFont("Colibri", 15))
        self.LastName.setPlaceholderText("Last Name: ")
        self.LastName.adjustSize()


        self.YearsOld = QLineEdit(self)
        self.OwnFont(self.YearsOld, 200, 200)
        self.YearsOld.setStyleSheet("color:Black; background-color:White")
        self.YearsOld.setFont(QFont("Colibri", 15))
        self.YearsOld.setPlaceholderText("Years Old: ")
        self.YearsOld.adjustSize()

        self.FirstCloseButton = QPushButton("Close", self)
        self.OwnFont(self.FirstCloseButton, 500, 600)
        self.setFont(QFont("Colcolas", 30))
        self.FirstCloseButton.setStyleSheet("color:Red; background-color:White")
        self.FirstCloseButton.clicked.connect(self.close)

        self.FirstSubmitButton = QPushButton("Submit", self)
        self.OwnFont(self.FirstSubmitButton, 250, 700)
        self.setFont(QFont("Colcolas", 20))
        self.FirstSubmitButton.setStyleSheet("color:Blue; background-color:White")
        self.FirstSubmitButton.clicked.connect(self.SubmitInformation)

        self.AndijanDistricts = ["",	
    "Andijan City", "Xonobod City", "Andijan", "Asaka", "Baliqchi","Boʻston" "Buloqboshi", "Izboskan", "Jalaquduq", "Marhamat", "Oltinkoʻl", "Paxtaobod",  "Qoʻrgʻontepa", "Shahrixon", "Ulugʻnor", "Xoʻjaobod"]
        
        self.BukharaDistricts = ["","Olot", "Galaosiyo", "Gʻijduvon", "Jondor", "Kogon", "Qorakoʻl", "Qorovulbozor", "Yangibozor", "Romitan", "Shofirkon", "Vobkent"]
        
        self.FerganaDistricts = ["","Oltiariq", "Bagʻdod", "Beshariq", "Ibrat", "Dangʻara", "Chimyon", "Navbahor", "Langar", "Quva", "Rishton", "Ravon", "Toshloq", "Uchkoʻprik", "Yaypan", "Yozyovon"]

        self.JizzakhDistricts = ["","Gʻoliblar", "Oʻsmat", "Doʻstlik", "Bogʻdon", "Gʻallaorol", "Uchtepa", "Gagarin", "Paxtakor", "Balandchaqir", "Zomin", "Zafarobod", "Zarbdor"]

        self.KarakalpakstanDist = ["","Mańg'it", "Beruniy", "Shimbay", "Bostan", "Kegeyli", "Moynaq", "Aqmańg'it", "Qanlikól", "Qońirat", "Qaraózek", "Shomanay", "Taxtakópir", "Tórtkúl", "Xojeli", "Taqiyatas", "Bozataw"]

        self.NamanganDistricts = ["","Chortoq", "Chust", "Kosonsoy", "Joʻmashoʻy", "Toshbuloq", "Haqqulobod", "Pop", "Toʻraqoʻrgʻon", "Uchqoʻrgʻon", "Uychi", "Yangiqoʻrgʻon", "Do'stlik"]

        self.NavoiyDistricts = ["","Konimex", "Qiziltepa", "Yangirabod", "Beshrabot", "Karmana", "Nurota", "Tomdibuloq", "Uchquduq"]

        self.QashqadaryoDistricts = ["","Chiroqchi", "Karashina", "Gʻuzor", "Qamashi", "Beshkent", "Koson", "Mugʻlon", "Kitob", "Yangi Mirishkor", "Muborak", "Yangi Nishon", "Shahrisabz", "Yakkabogʻ"]

        self.SamarqandDistricts = ["","Bulungʻur", "Ishtixon", "Jomboy", "Payshanba", "Qoʻshrabot", "Oqtosh", "Nurobod", "Loyish", "Ziyovuddin", "Payariq", "Juma", "Gulobod", "Toyloq", "Urgut"]

        self.SirdaryoDistricts = ["","Sardoba", "Boyovut", "Dehqonobod", "Xovos", "Navroʻz", "Paxtaobod", "Sayxun", "Sirdaryo"]

        self.SurxondaryoDistricts = ["","Angor", "Bandixon", "Boysun", "Denov", "Jarqoʻrgʻon", "Sariq", "Qumqoʻrgʻon", "Khalkabad", "Qarluq", "Sariosiyo", "Sherobod", "Shoʻrchi", "Uchqizil", "Uzun"]

        self.TashkentRegionDistricts = ["","Zafar", "Gʻazalkent", "Boʻka", "Chinoz", "Qibray", "Ohangaron", "Oqqoʻrgʻon", "Parkent", "Piskent", "Doʻstobod", "Eshonguzar", "Nurafshon", "Yangiyoʻl", "Yangibozor", "Keles"]

        self.XorazmDistricts = ["","Bogʻot", "Gurlan", "Xonqa", "Hazorasp", "Khiva", "Qoʻshkoʻpir", "Shovot", "Qorovul", "Yangiariq", "Yangibozor", "Pitnak"]

        self.TashkentCityDistricts = ["","Bektemir", "Chilanzar", "Yashnobod", "Mirobod", "Mirzo Ulugbek", "Sergeli", "Shayxontoxur", "Olmazor", "Uchtepa", "Yakkasaray", "Yunusabad", "Yangihayot"]
        
        self.InUzb_Districts = QComboBox(self)
        self.OwnFont(self.InUzb_Districts, 200, 500)
        self.InUzb_Districts.addItems(self.AndijanDistricts)
        self.InUzb_Districts.setStyleSheet("color:Black; background-color:Lime")
        self.InUzb_Districts.setFont(QFont("Colibri", 15))

        self.InUzb_Districts.currentIndexChanged.connect(self.Province_Selection_Change)

        self.InUzb_Province.currentIndexChanged.connect(self.SelectionChange)
        
        self.Genders.currentIndexChanged.connect(self.Gender_Current)

        self.central_asia_nations.currentIndexChanged.connect(self.Central_Asia_Current)


        self.User_Data = []
        
        self.province_name = ""
        self.district_name = ""
        self.central_asia_name = ""
        self.gender_name = ""

    def SubmitInformation(self):

        self.User_Data.append(self.FirstName.text())
        self.User_Data.append(self.LastName.text())
        self.User_Data.append(self.YearsOld.text())
        self.User_Data.append(self.central_asia_name)
        self.User_Data.append(self.province_name)
        self.User_Data.append(self.district_name)
        self.User_Data.append(self.gender_name)

        # print(self.User_Data)
        self.NewWindow()
        self.main.show()
        
    def Central_Asia_Current(self):

        self.Asia_Name = self.central_asia_nations.currentText()
        self.central_asia_name = self.Asia_Name

    def Gender_Current(self):

        self.GenderName = self.Genders.currentText()
        self.gender_name = self.GenderName



    def Province_Selection_Change(self):

        self.name = self.InUzb_Districts.currentText()
        self.district_name = self.name

    def SelectionChange(self,i):

        self.Province_Name = self.InUzb_Province.currentText()
        self.province_name = self.Province_Name
        
        if self.Province_Name == "Andijan":
            self.InUzb_Districts.clear()
            self.InUzb_Districts.addItems(self.AndijanDistricts)
            self.InUzb_Districts.adjustSize()

        elif self.Province_Name == "Bukhara":
            self.InUzb_Districts.clear()
            self.InUzb_Districts.addItems(self.BukharaDistricts)
            self.InUzb_Districts.adjustSize()

        elif self.Province_Name == "Fergana":
            self.InUzb_Districts.clear()
            self.InUzb_Districts.addItems(self.FerganaDistricts)
            self.InUzb_Districts.adjustSize()
            
        elif self.Province_Name == "Jizzakh":
            self.InUzb_Districts.clear()
            self.InUzb_Districts.addItems(self.JizzakhDistricts)
            self.InUzb_Districts.adjustSize()
        
        elif self.Province_Name == "Karakalpakstan":
            self.InUzb_Districts.clear()
            self.InUzb_Districts.addItems(self.KarakalpakstanDist)
            self.InUzb_Districts.adjustSize()

        elif self.Province_Name == "Namangan":
            self.InUzb_Districts.clear()
            self.InUzb_Districts.addItems(self.NamanganDistricts)
            self.InUzb_Districts.adjustSize()

        elif self.Province_Name == "Navoiy":
            self.InUzb_Districts.clear()
            self.InUzb_Districts.addItems(self.NavoiyDistricts)
            self.InUzb_Districts.adjustSize()

        elif self.Province_Name == "Qashqadaryo":
            self.InUzb_Districts.clear()
            self.InUzb_Districts.addItems(self.QashqadaryoDistricts)
            self.InUzb_Districts.adjustSize()

        elif self.Province_Name == "Samarqand":
            self.InUzb_Districts.clear()
            self.InUzb_Districts.addItems(self.SamarqandDistricts)
            self.InUzb_Districts.adjustSize()

        elif self.Province_Name == "Sirdaryo":
            self.InUzb_Districts.clear()
            self.InUzb_Districts.addItems(self.SirdaryoDistricts)
            self.InUzb_Districts.adjustSize()

        elif self.Province_Name == "Surxondaryo":
            self.InUzb_Districts.clear()
            self.InUzb_Districts.addItems(self.SurxondaryoDistricts)
            self.InUzb_Districts.adjustSize()

        elif self.Province_Name == "Tashkent Region":
            self.InUzb_Districts.clear()
            self.InUzb_Districts.addItems(self.TashkentRegionDistricts)
            self.InUzb_Districts.adjustSize()

        elif self.Province_Name == "Xorazm":
            self.InUzb_Districts.clear()
            self.InUzb_Districts.addItems(self.XorazmDistricts)
            self.InUzb_Districts.adjustSize()

        elif self.Province_Name == "Tashkent City":
            self.InUzb_Districts.clear()
            self.InUzb_Districts.addItems(self.TashkentCityDistricts)
            self.InUzb_Districts.adjustSize()






    def showMessage(self):

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Information For Submit")
        msg.setText("About Your Information Submited ✅\n   Thank You...")
        msg.setFont(QFont("Colibri", 12))
        msg.buttonClicked.connect(self.DeleteInfo)
        msg.exec_()

    def DeleteInfo(self):
        self.FirstName.setText("")
        self.LastName.setText("")
        self.YearsOld.setText("")


    # def AboutInfo(self):
    #     print(f"Name:{self.Information[0]}\nSurName:{self.Information[1]}\nYears Old:{self.Information[2]}")



    def NewWindow(self):

        self.UserName = QLabel(f"First Name: {self.FirstName.text()}", self.main)
        self.OwnFont(self.UserName, 100,100)
        self.UserName.adjustSize()

        self.UserSurname = QLabel(f"Last Name: {self.LastName.text()}", self.main)
        self.OwnFont(self.UserSurname, 100,150)
        self.UserSurname.adjustSize()

        self.UserAge = QLabel(f"Age: {self.YearsOld.text()}", self.main)
        self.OwnFont(self.UserAge, 100,200)
        self.UserAge.adjustSize()

        self.UserCountry = QLabel(f"Country: {self.central_asia_name}", self.main)
        self.OwnFont(self.UserCountry, 100,250)
        self.UserCountry.adjustSize()

        self.UserProvince = QLabel(f"Province: {self.province_name}", self.main)
        self.OwnFont(self.UserProvince, 100,300)
        self.UserProvince.adjustSize()

        self.UserDistrict = QLabel(f"District: {self.district_name}", self.main)
        self.OwnFont(self.UserDistrict, 100,350)
        self.UserDistrict.adjustSize()

        self.UserGender = QLabel(f"Gender: {self.gender_name}", self.main)
        self.OwnFont(self.UserGender, 100,400)        
        self.UserGender.adjustSize()

if __name__ == "__main__":
    Restaurant = QApplication([])
    window = Window()
    window.setWindowTitle("TEST")  
    window.show()
    Restaurant.exec_()