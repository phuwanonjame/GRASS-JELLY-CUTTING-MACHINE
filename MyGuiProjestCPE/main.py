a= "10/20"
b=len(a)
print("จำนวนของ a =",b)

#นับจากด้านหน้าไปจากถึง()
z=a.find('/')
print("z = ",z)

#นับจากด้านหลังที่เจอใน()ไปจนหน้าสุด
y=a.rfind('/')
print("y = ",y)

c=""
v=""
for i in range (b):
    if a[i]!="/":
        c=c+a[i]
    else:
        v=v+a[i]
print("x = ",c,"v =",v)

# *-----Pass!-------* #
Square=""
Wavy=""
for r in range (b):
    if r < a.find('/'):
        Square=Square+a[r]
    elif r > a.find('/'):
        Wavy=Wavy+a[r]
print("r = ",r,"a1 = ",Square,"a2 = ",Wavy)
# *-----------------* #

import datetime as dt
datenow = dt.datetime.now()
print("Date Full: ",datenow)
print("Date Now m/d/y : ",datenow.strftime("%x"))
print("Time Now : ",datenow.strftime("%X"))
print("Date Now d/m/y !!! : ",datenow.strftime("%d/%m/%Y"))

result =  [('23/06/2021', '01:54:43', 'Custom Owner', '-W-', 'Wavy', '20', '1200'),
            ('25/06/2021', '00:36:09', 'fdgsdfds', 'awdqsdq', 'Square', '10', '600'),
            ('25/06/2021', '00:36:29', 'Hello', 'World', 'Square/Wavy', '5/5', '600'),
            ('25/06/2021', '02:04:52', 'BBBBaz', 'dDA', 'Square', '10', '600'),
            ('25/06/2021', '02:05:46', 'Hello', 'World', 'Square/Wavy', '5/5', '600')]

# ----------------label Weight-------------------#
Wight_sum = 0
for w in range(len(result)):
    Weight_N = result[w][5]
    Model_N = result[w][4]
    print("\nWeight = ", Weight_N)
    SquareW = "0"
    WavyW = "0"
    if Model_N == "Square":
        SquareW = Weight_N
        print("Model = ", Model_N)
    elif Model_N == "Wavy":
        WavyW = Weight_N
        print("Model = ", Model_N)
    else:
        for r in range(len(Weight_N)):
            print(len(Weight_N))
            if r < Weight_N.find('/'):
                SquareW = SquareW + Weight_N
            elif r > Weight_N.find('/'):
                WavyW = WavyW + Weight_N
        print("r = ", r, "Square = ", SquareW, "Wavy = ", WavyW)
        # ---------------------------------------------#
print("End", "Square = ", SquareW, "Wavy = ", WavyW)
# self.label_AllWeight.setText()
# -----------------------------------------------#

"""
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QComboBox
from PyQt5.QtCore import QSize, QRect

class ExampleWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 140))
        self.setWindowTitle("Combobox example")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        # Create combobox and add items.
        self.comboBox = QComboBox(centralWidget)
        self.comboBox.setGeometry(QRect(40, 40, 491, 31))
        self.comboBox.setObjectName(("comboBox"))
        self.comboBox.addItem("PyQt")
        self.comboBox.addItem("Qt")
        self.comboBox.addItem("Python")
        self.comboBox.addItem("Example")

        self.comboBox1 = QComboBox(centralWidget)
        self.comboBox1.setGeometry(QRect(40, 80, 491, 30))
        self.comboBox1.setObjectName(("comboBox"))
        #options = ["Athens", "Bruxelles", "Chengmai", "Dover"]
        for option in range (31):
            self.comboBox1.addItem(str(option))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ExampleWindow()
    mainWin.show()
    sys.exit( app.exec_() )
"""

"""     
        #----------- single label   
        *( 
        self.label_showQ.setText("รายการที่กำลังทำ : "+Username_N +" "+ Lastname_N + " " + Model_N + " " + Weight_N) 
        )*
        self.label_showQ = QtWidgets.QLabel(self.centralwidget)
        self.label_showQ.setGeometry(QtCore.QRect(350, 240, 421, 31))
        font = QtGui.QFont()
        font.setFamily("TH SarabunPSK")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_showQ.setFont(font)
        self.label_showQ.setStyleSheet("background-color: rgb(255, 255, 255);
                                        border: 1px solid rgb(122, 122, 122);")
        self.label_showQ.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_showQ.setLineWidth(1)
        self.label_showQ.setText("")
        self.label_showQ.setAlignment(QtCore.Qt.AlignCenter)
        self.label_showQ.setObjectName("label_showQ")
        
        #-------- Multi label
        *(
        self.label_showQ_name.setText(Username_N)
        self.label_showQ_lastname.setText(Lastname_N)
        self.label_showQ_model.setText(Model_N)
        self.label_showQ_weight.setText(Weight_N)
        )*
        self.label_showQ_name = QtWidgets.QLabel(self.centralwidget)
        self.label_showQ_name.setGeometry(QtCore.QRect(350, 240, 101, 31))
        font = QtGui.QFont()
        font.setFamily("TH SarabunPSK")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_showQ_name.setFont(font)
        self.label_showQ_name.setStyleSheet("background-color: rgb(255, 255, 255);"
                                            "border-top : 1px solid rgb(122, 122, 122);"
                                            "border-bottom: 1px solid rgb(122, 122, 122);"
                                            "border-left: 1px solid rgb(122, 122, 122);")
        self.label_showQ_name.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_showQ_name.setLineWidth(1)
        self.label_showQ_name.setText("")
        self.label_showQ_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_showQ_name.setObjectName("label_showQ_name")
        self.label_showQ_lastname = QtWidgets.QLabel(self.centralwidget)
        self.label_showQ_lastname.setGeometry(QtCore.QRect(450, 240, 101, 31))
        font = QtGui.QFont()
        font.setFamily("TH SarabunPSK")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_showQ_lastname.setFont(font)
        self.label_showQ_lastname.setStyleSheet("background-color: rgb(255, 255, 255);"
                                            "border-top : 1px solid rgb(122, 122, 122);"
                                            "border-bottom: 1px solid rgb(122, 122, 122);")
        self.label_showQ_lastname.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_showQ_lastname.setLineWidth(1)
        self.label_showQ_lastname.setText("")
        self.label_showQ_lastname.setAlignment(QtCore.Qt.AlignCenter)
        self.label_showQ_lastname.setObjectName("label_showQ_lastname")
        self.label_showQ_model = QtWidgets.QLabel(self.centralwidget)
        self.label_showQ_model.setGeometry(QtCore.QRect(550, 240, 101, 31))
        font = QtGui.QFont()
        font.setFamily("TH SarabunPSK")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_showQ_model.setFont(font)
        self.label_showQ_model.setStyleSheet("background-color: rgb(255, 255, 255);"
                                            "border-top : 1px solid rgb(122, 122, 122);"
                                            "border-bottom: 1px solid rgb(122, 122, 122);")
        self.label_showQ_model.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_showQ_model.setLineWidth(1)
        self.label_showQ_model.setText("")
        self.label_showQ_model.setAlignment(QtCore.Qt.AlignCenter)
        self.label_showQ_model.setObjectName("label_showQ_model")
        self.label_showQ_weight = QtWidgets.QLabel(self.centralwidget)
        self.label_showQ_weight.setGeometry(QtCore.QRect(650, 240, 121, 31))
        font = QtGui.QFont()
        font.setFamily("TH SarabunPSK")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_showQ_weight.setFont(font)
        self.label_showQ_weight.setStyleSheet("background-color: rgb(255, 255, 255);"
                                            "border-top : 1px solid rgb(122, 122, 122);"
                                            "border-bottom: 1px solid rgb(122, 122, 122);"
                                            "border-right: 1px solid rgb(122, 122, 122);")
        self.label_showQ_weight.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_showQ_weight.setLineWidth(1)
        self.label_showQ_weight.setText("")
        self.label_showQ_weight.setAlignment(QtCore.Qt.AlignCenter)
        self.label_showQ_weight.setObjectName("label_showQ_weight")
"""

"""
หน้า Ownerpage def Confirmbtn
            # --------- รวมน้ำหนัก Square Wavy ----------------#
            M = len(ModelOwner)
            if M != 2:
                ModelS = str(ModelOwner[0])
                Weight = (SquareWOwner) + (WavyWOwner)
            elif M == 2:
                ModelS = (ModelOwner[0]) + "/" + (ModelOwner[1])
                Weight = (SquareWOwner) + "/" + (WavyWOwner)
            # ------------------------------- ---------------#
"""

"""     
หน้า Ownerpage def Confirmbtn ตรงเงื่อนไขเพิ่มหรืออัพเดท
                if rowtable != None :
                    print("yes")
                    print(rowtable[0])
                    cur.execute(
                        "UPDATE ownerpage SET Username='%s', Lastname='%s', Model='%s', Weight='%s' , Phone='%s' WHERE ID='%s' " % (
                            UsernameOwner, LastnameOwner, ModelS, Weight, PhoneOwner, rowtable[0]))
                    cnx.commit()
                else:
                    print("no")
                    cur.execute(
                        "INSERT INTO ownerpage(Username, Lastname , Model, Weight, Phone) VALUES ('%s','%s','%s','%s','%s')" % (
                            UsernameOwner, LastnameOwner, ModelS, Weight, PhoneOwner))
                    cnx.commit()
"""

"""
หน้า Ownerpage def  Editbtn ตรงแก้ไข
    def Editbtn(self):
        print("Edit!")
        rowUser = self.tableOwner_owner.currentRow()
        if rowUser != "" and rowUser != -1:
            print(rowUser)
            print(Owner_N[rowUser][1])
            Model = Owner_N[rowUser][3]
            MWeight = Owner_N[rowUser][4]
            Square = ""
            Wavy = ""
            if Model == "Square":
                print("Model = ", Model)
                self.lineEdit_SquareW.setText(MWeight)
                self.lineEdit_WavyW.clear()
            elif Model == "Wavy":
                print("Model = ", Model)
                self.lineEdit_WavyW.setText(MWeight)
                self.lineEdit_SquareW.clear()
            else:
                # --------- แยกน้ำหนัก Square Wavy ---------------#
                for r in range(len(MWeight)):
                    if r < MWeight.find('/'):
                        Square = Square + MWeight[r]
                    elif r > MWeight.find('/'):
                        Wavy = Wavy + MWeight[r]
                print("r = ", r, "Square = ", Square, "Wavy = ", Wavy)
                # ---------------------------------------------#
                self.lineEdit_SquareW.setText(Square)
                self.lineEdit_WavyW.setText(Wavy)
            self.lineEdit_Nameowner.setText(Owner_N[rowUser][1])
            self.lineEdit_Lastnameowner.setText(Owner_N[rowUser][2])
            self.lineEdit_Phoneowner.setText(Owner_N[rowUser][5])
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText("กรุณาเลือกข้อมูลที่ต้องการแก้ไข")
            msgBox.exec_()
"""

"""
cnx.connect()
print("Num Phone = ", len(PhoneOwner))
cur.execute(
    "SELECT ID, Username, Lastname , Phone FROM ownerpage WHERE Username='%s'OR Lastname='%s'OR Phone='%s' " % (
        UsernameOwner, LastnameOwner, PhoneOwner))
rowtable = cur.fetchone()

if rowtable == None:
    if len(PhoneOwner) <= 10:
        Check_Z = lambda z: "0" if (int(z) + 0) == 0 else str(z)
        Check_Empty = lambda e: "0" + e if e == "" else str(e)
        Check_NumF1 = lambda n: str(int(n)) if n[0] == "0" else str(n)

        Check_Square = Check_Z(Check_Empty(SquareWOwner))
        Check_Wavy = Check_Z(Check_Empty(WavyWOwner))

        Check_Zline = (Check_Square != "0" and Check_Wavy != "0") or (
                    (Check_Square != "" and Check_Wavy != "0") or (Check_Square != "0" and Check_Wavy != "")) or \
                      ((Check_Square != "" and Check_Wavy != "0") and (Check_Square != "0" and Check_Wavy != ""))
        if UsernameOwner != "" and LastnameOwner != "" and PhoneOwner != "" and (
                SquareWOwner != "" or WavyWOwner != "") and Check_Zline:
            if SquareWOwner != "":
                ModelOwner.append("Square")
            if WavyWOwner != "":
                ModelOwner.append("Wavy")
            # --------- รวมน้ำหนัก Square Wavy ----------------#
            M = len(ModelOwner)
            if M != 2:
                ModelS = str(ModelOwner[0])
                if ModelS == "Square":
                    Weight = Check_NumF1(SquareWOwner)
                elif ModelS == "Wavy":
                    Weight = Check_NumF1(WavyWOwner)
            elif M == 2:
                if Check_Wavy == "0":
                    ModelS = ModelOwner[0]
                    Weight = Check_NumF1(SquareWOwner)
                elif Check_Square == "0":
                    ModelS = ModelOwner[1]
                    Weight = Check_NumF1(WavyWOwner)
                else:
                    ModelS = (ModelOwner[0]) + "/" + (ModelOwner[1])
                    Weight = Check_NumF1(SquareWOwner) + "/" + Check_NumF1(WavyWOwner)
            # ------------------------------- ---------------#

            cur.execute(
                "INSERT INTO ownerpage(Username, Lastname , Model, Weight, Phone) VALUES ('%s','%s','%s','%s','%s')" % (
                    UsernameOwner, LastnameOwner, ModelS, Weight, PhoneOwner))
            cnx.commit()

            self.lineEdit_Nameowner.clear()
            self.lineEdit_Lastnameowner.clear()
            self.lineEdit_Phoneowner.clear()
            self.lineEdit_SquareW.clear()
            self.lineEdit_WavyW.clear()
            Ui_OwnerPage.LoadDataTable(Table)
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText("กรุณากรอกชื่อ นามสกุล เบอร์โทรศัทพ์ ให้ครบถ้วน และกำหนดน้ำหนักให้ถูกต้อง")
            msgBox.exec_()
    else:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Error")
        msgBox.setText("เบอร์โทรเกิน 10 ตัว")
        msgBox.exec_()
elif rowtable != None:
    if UsernameOwner == rowtable[1] and LastnameOwner == rowtable[2] and PhoneOwner == rowtable[3]:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Error")
        msgBox.setText("มีชื่อ นามสกุล และเบอร์โทรศัทพ์ ชุดนี้ในรายการแล้ว")
        msgBox.exec_()

"""

"""
    def ExportOwner(self):  #บัค ข้อมูลที่ส่งออกเมื่อกดแล้วจะส่งออกทั้งหมดไม่สามารถค้นหาเพื่อส่งออกได้
        print("Export!")
        #path = "C:/Users/Watcharanon Kerdkaew/PycharmProjects/MyGuiProjestCPE/Export/outputFile.csv"
        dt_N = dt.datetime.now()
        Date_N = str(dt_N.strftime("%d%m%y"))
        Time_N = str(dt_N.strftime("%H%M%S"))
        fileName = "C:/Users/Watcharanon Kerdkaew/PycharmProjects/MyGuiProjestCPE/Export"
        path = fileName+"/OwnerFile_" + Date_N + "_" + Time_N +".csv"
        print(path)
        cur.execute("SELECT 'ID', 'Username', 'Lastname', 'Model', 'Weight', 'Phone' UNION "
                    "SELECT * FROM ownerpage INTO OUTFILE '%s' FIELDS TERMINATED BY ',' "
                    "OPTIONALLY ENCLOSED BY '""' LINES TERMINATED BY '\r\n'"%(path))

"""

"""
    def Exportbtn(self):    #บัค ข้อมูลที่ส่งออกเมื่อกดแล้วจะส่งออกทั้งหมดไม่สามารถค้นหาเพื่อส่งออกได้ ต้องเพิ่มช่องค้นหาวันและเวลา
        print("Export !!!")
        #path = "C:/Users/Watcharanon Kerdkaew/PycharmProjects/MyGuiProjestCPE/Export/outputFile.csv"
        dt_N = dt.datetime.now()
        Date_N = str(dt_N.strftime("%d%m%y"))
        Time_N = str(dt_N.strftime("%H%M%S"))
        fileName = "C:/Users/Watcharanon Kerdkaew/PycharmProjects/MyGuiProjestCPE/Export"
        path = fileName + "/DataSellFile_" + Date_N + "_" + Time_N + ".csv"
        print(path)
        cur.execute("SELECT 'ID','Date', 'Time', 'Username', 'Lastname', 'Model', 'Weight', 'Price' UNION "
                    "SELECT * FROM datasellpage INTO OUTFILE '%s' FIELDS TERMINATED BY ',' "
                    "OPTIONALLY ENCLOSED BY '""' LINES TERMINATED BY '\r\n'"%(path))
"""

"""
#-----------------------------------------Excel Pandas-------------------------------------#

#---------------------- Connection Database Mysql ---------------------------#
import mysql.connector
cnx = mysql.connector.connect(host="localhost", user="root", password="", database="wprojectcpe62")       # connect to MySql database
cur = cnx.cursor()
#----------------------------------------------------------------------------#

cur.execute("SELECT * FROM ownerpage " )
rowtable = cur.fetchall()
row1 = rowtable[0]
print(row1)

Id_User = []
Name_User = []
Last_User = []
Model_User = []
Weight_User = []
Phone_User = []
for r1 in range (len(rowtable)):
    print("round = ", r1)
    for r2 in range (len(rowtable[r1])):
        if r2 == 0 :
            Id_User.append(rowtable[r1][r2])
        elif r2 == 1 :
            Name_User.append(rowtable[r1][r2])
        elif r2 == 2 :
            Last_User.append(rowtable[r1][r2])
        elif r2 == 3 :
            Model_User.append(rowtable[r1][r2])
        elif r2 == 4 :
            Weight_User.append(rowtable[r1][r2])
        elif r2 == 5 :
            Phone_User.append(rowtable[r1][r2])
print("Id_User    : ",Id_User,"\nName_User  : ",Name_User,"\nLast_User  : ",Last_User,"\nModel_User  : ",Model_User,"\nWeight_User : ",Weight_User,"\nPhone_User : ",Phone_User)

import xlsxwriter
import pandas as pd
dt_N = dt.datetime.now()
Date_N = str(dt_N.strftime("%d%m%y"))
Time_N = str(dt_N.strftime("%H%M%S"))
# สร้าง DataFrame ที่มี 1 คอลัมน์ชื่อ 'Data'
dataframe = pd.DataFrame({'ID': Id_User,
                           'Username': Name_User,
                           'Lastname': Last_User,
                           'Model': Model_User,
                           'Weight': Weight_User,
                           'Phone': Phone_User})

dataSecond = pd.DataFrame({'sd' : ['10','30','20','10'],
                           'sa' : ['15','34','25','15']})

# สร้าง Pandas Excel Writer เพื่อใช้เขียนไฟล์ Excel โดยใช้ Engine เป็น xlsxwriter
# โดยตั้งชื่อไฟล์ว่า 'simple_data.xlsx'
fileName = "C:/Users/Watcharanon Kerdkaew/PycharmProjects/MyGuiProjestCPE/Export/"
writer = pd.ExcelWriter(fileName+'simple_data.xlsx', engine='xlsxwriter')

# นำข้อมูลที่สร้างไว้ในตัวแปร dataframe เขียนลงไฟล์ ||+Date_N+'_'+Time_N+
dataframe.to_excel(writer)
dataSecond.to_excel(writer, startcol=10, startrow=2)
# จบการทำงาน Pandas Excel writer และเซฟข้อมูลออกมาเป็นไฟล์ Excel
writer.save()

#------------------------------------------------------------------------------------------#
"""

"""
class WeightFixedInput(QtWidgets.QDialog):
        # *----ปุ่มกดเลือกแม่แบบ-----* #
        self.pushButton_one.setCheckable(True)
        self.pushButton_one.setChecked(False)
        self.pushButton_one.clicked.connect(self.one_btn)
        self.pushButton_two.setCheckable(True)
        self.pushButton_two.setChecked(False)
        self.pushButton_two.clicked.connect(self.two_btn)
        self.pushButton_three.setCheckable(True)
        self.pushButton_three.setChecked(False)
        self.pushButton_three.clicked.connect(self.three_btn)
        self.pushButton_four.setCheckable(True)
        self.pushButton_four.setChecked(False)
        self.pushButton_four.clicked.connect(self.four_btn)

    def one_btn(self):
        if self.pushButton_one.isChecked() == True:
            self.pushButton_two.setEnabled(False)
            self.pushButton_two.setFlat(True)
            self.pushButton_three.setEnabled(False)
            self.pushButton_three.setFlat(True)
            self.pushButton_four.setEnabled(False)
            self.pushButton_four.setFlat(True)
            Squaremodel = "1"
            print(Squaremodel)
        else:
            self.pushButton_two.setEnabled(True)
            self.pushButton_two.setFlat(False)
            self.pushButton_three.setEnabled(True)
            self.pushButton_three.setFlat(False)
            self.pushButton_four.setEnabled(True)
            self.pushButton_four.setFlat(False)
            Squaremodel = ""
            print(Squaremodel)

    def two_btn(self):
        if self.pushButton_two.isChecked() == True:
            self.pushButton_one.setEnabled(False)
            self.pushButton_one.setFlat(True)
            self.pushButton_three.setEnabled(False)
            self.pushButton_three.setFlat(True)
            self.pushButton_four.setEnabled(False)
            self.pushButton_four.setFlat(True)
            Wavymodel = "2"
            print(Wavymodel)
        else:
            self.pushButton_one.setEnabled(True)
            self.pushButton_one.setFlat(False)
            self.pushButton_three.setEnabled(True)
            self.pushButton_three.setFlat(False)
            self.pushButton_four.setEnabled(True)
            self.pushButton_four.setFlat(False)
            Wavymodel = ""
            print(Wavymodel)

    def three_btn(self):
        if self.pushButton_three.isChecked() == True:
            self.pushButton_one.setEnabled(False)
            self.pushButton_one.setFlat(True)
            self.pushButton_two.setEnabled(False)
            self.pushButton_two.setFlat(True)
            self.pushButton_four.setEnabled(False)
            self.pushButton_four.setFlat(True)
            Squaremodel = "3"
            print(Squaremodel)
        else:
            self.pushButton_one.setEnabled(True)
            self.pushButton_one.setFlat(False)
            self.pushButton_two.setEnabled(True)
            self.pushButton_two.setFlat(False)
            self.pushButton_four.setEnabled(True)
            self.pushButton_four.setFlat(False)
            Squaremodel = ""
            print(Squaremodel)

    def four_btn(self):
        if self.pushButton_four.isChecked() == True:
            self.pushButton_one.setEnabled(False)
            self.pushButton_one.setFlat(True)
            self.pushButton_two.setEnabled(False)
            self.pushButton_two.setFlat(True)
            self.pushButton_three.setEnabled(False)
            self.pushButton_three.setFlat(True)
            Wavymodel = "4"
            print(Wavymodel)
        else:
            self.pushButton_one.setEnabled(True)
            self.pushButton_one.setFlat(False)
            self.pushButton_two.setEnabled(True)
            self.pushButton_two.setFlat(False)
            self.pushButton_three.setEnabled(True)
            self.pushButton_three.setFlat(False)
            Wavymodel = ""
            print(Wavymodel)

"""

"""
    def Startbtn(self):
        global Price_Square,Price_Wavy,Check_btn
        cur.execute("SELECT ID, Username, Lastname, Model, Weight FROM qorderpage")
        orderq = cur.fetchall()
        if orderq != []:
            if Check_btn == "Start":
                print("Start !!!")
                self.timer.start(1000)
                timeee = self.progressbar.value()
                print(timeee)
                print("No")
                # ------------การเพิ่มข้อมูลลงหน้าต่าง Datasell และลบข้อมูลในหน้าต่าง Qorder----------------------#
                orderq_N = orderq[0]  # ID
                dt_N = dt.datetime.now()
                Date_N = str(dt_N.strftime("%d/%m/%Y"))
                Time_N = str(dt_N.strftime("%X"))
                cnx.connect()
                ID_N = orderq_N[0]
                Username_N = orderq_N[1]
                Lastname_N = orderq_N[2]
                Model_N = orderq_N[3]
                Weight_N = orderq_N[4]

                self.label_showQ_name.setText(Username_N)
                self.label_showQ_lastname.setText(Lastname_N)
                self.label_showQ_model.setText(Model_N)
                self.label_showQ_weight.setText(Weight_N)
                # --------- แยกน้ำหนัก Square Wavy ---------------#
                SquareW = "0"
                WavyW = "0"
                if Model_N == "Square":
                    SquareW = Weight_N
                    print("Model = ", Model_N)
                elif Model_N == "Wavy":
                    WavyW=Weight_N
                    print("Model = ", Model_N)
                else:
                    for r in range(len(Weight_N)):
                        if r < Weight_N.find('/'):
                            SquareW = SquareW + Weight_N[r]
                        elif r > Weight_N.find('/'):
                            WavyW = WavyW + Weight_N[r]
                    print("r = ", r, "Square = ", SquareW, "Wavy = ", WavyW)
                # ----------------------------------------------#

                self.timer.start(1000)
                
                Price_N = ((int(SquareW) * int(Price_Square))+(int(WavyW) * int(Price_Wavy)))   # นำค่าน้ำหนักที่แยกได้มาคูณกับราคาพื้นฐานแล้วเก็บไว้
                print(ID_N,Date_N,Time_N,Username_N,Lastname_N,Model_N,Weight_N,Price_N)
                cur.execute(
                   "INSERT INTO datasellpage(Date, Time, Username, Lastname, Model ,Weight ,Price) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (
                  Date_N,Time_N, Username_N, Lastname_N, Model_N, Weight_N, Price_N))
                cnx.commit()
                cur.execute("DELETE FROM qorderpage WHERE ID='%s'" % (ID_N))
                cnx.commit()
                Ui_MainPage.LoadDataTableQorder(Table)
                # -----------------------------------------------------------------------------------#
                Check_btn = "Start"
            elif Check_btn == "Stop":
                print("Continue")
                self.timer.start(1000)
                timeee = self.progressbar.value()
                print(timeee)
                print("no")
                Check_btn = "Start"
            else:
                print("Error")
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText("ไม่พบข้อมูลในคิวออเดอร์")
            msgBox.exec_()
"""

"""
    def Startbtn(self):
        global Price_Square,Price_Wavy,SquareW,WavyW,Check_btn,DataOwner
        cur.execute("SELECT ID, Username, Lastname, Model, Weight FROM qorderpage")
        orderq = cur.fetchall()
        if orderq != [] or DataOwner != []:
            if Check_btn == "Start":        #กดเริ่มครั้งแรก
                print("Start !!!")
                # ------------การเพิ่มข้อมูลลงหน้าต่าง Datasell และลบข้อมูลในหน้าต่าง Qorder----------------------#
                orderq_N = orderq[0]  # ID
                dt_N = dt.datetime.now()
                Date_N = str(dt_N.strftime("%d/%m/%Y"))
                Time_N = str(dt_N.strftime("%X"))
                cnx.connect()
                ID_N = orderq_N[0]
                Username_N = orderq_N[1]
                Lastname_N = orderq_N[2]
                Model_N = orderq_N[3]
                Weight_N = orderq_N[4]

                self.label_showQ_name.setText(Username_N)
                self.label_showQ_lastname.setText(Lastname_N)
                self.label_showQ_model.setText(Model_N)
                self.label_showQ_weight.setText(Weight_N)

                # --------- แยกน้ำหนัก Square Wavy ---------------#
                SquareW = "0"   #ตัวแปรที่ใช้นำมาเก็บค่าน้ำหนักแบบสี่เหลี่ยม
                WavyW = "0"     #ตัวแปรที่ใช้นำมาเก็บค่าน้ำหนักแบบหยัก
                if Model_N == "Square":
                    SquareW = Weight_N
                    print("Model = ", Model_N)
                elif Model_N == "Wavy":
                    WavyW=Weight_N
                    print("Model = ", Model_N)
                else:
                    for r in range(len(Weight_N)):
                        if r < Weight_N.find('/'):
                            SquareW = SquareW + Weight_N[r]
                        elif r > Weight_N.find('/'):
                            WavyW = WavyW + Weight_N[r]
                    print("r = ", r, "Square = ", SquareW, "Wavy = ", WavyW)
                # ----------------------------------------------#
                SquareW = int(SquareW)
                WavyW = int(WavyW)
                self.timer.start(1000)
                Price_N = ((SquareW * int(Price_Square))+(WavyW * int(Price_Wavy)))   # นำค่าน้ำหนักที่แยกได้มาคูณกับราคาพื้นฐานแล้วเก็บไว้
                DataOwner = [ID_N,Date_N,Time_N,Username_N,Lastname_N,Model_N,Weight_N,Price_N]
                print(DataOwner)
                cur.execute("DELETE FROM qorderpage WHERE ID='%s'" % (ID_N))
                cnx.commit()
                Ui_MainPage.LoadDataTableQorder(Table)
                # -----------------------------------------------------------------------------------#
                Check_btn = "doing"
                #self.pushButton_Start.setEnabled(False)
            
            elif Check_btn == "Stop":   #กดเริ่มหลังจากกดหยุด
                print("Continue")
                self.timer.start(1000)
                timeee = self.progressbar.value()
                print(timeee)
                print("no")
                print(DataOwner)
                Check_btn = "doing" 
            else:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Error")
                msgBox.setText("ยังทำรายการไม่เสร็จ กรุณารอ")
                msgBox.exec_()
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText("ไม่พบข้อมูลในคิวออเดอร์")
            msgBox.exec_()

"""
Input_Z = lambda x:"0"+str(x) if (len(x)==1) else False    #เพิ่ม 0 ข้างหน้า
print(Input_Z("1"))

Check_Z = lambda z : "0" if (int(z) + 0) == 0  else str(z)  #เช็ค 0 และ รวม 000 เป็น 0
print(Check_Z("10"),Check_Z("0000"))

Check_Empty = lambda e: "0"+e if e == "" else str(e)    #หากพบช่องว่างทำให้เป็น 0
print(Check_Empty(""))

Check_NumF1 = lambda n: str(int(n)) if n[0] == "0" else str(n) #หากมี 0 ข้างหน้าจะทำการลบออก
print(Check_NumF1("00011112"),Check_NumF1("2221"))

las="fwa"
faw="sfw"


allaroud = [las,faw]

print(allaroud)