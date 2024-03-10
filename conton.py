import time
from time import sleep
import RPi.GPIO as GPIO
#---------------------- Connection Database Mysql ---------------------------#
import mysql.connector
cnx = mysql.connector.connect(host="localhost", user="root1", password="123456789", database="wprojectcpe62")       # connect to MySql database
cur = cnx.cursor()
#----------------------------------------------------------------------------#
model1 = 'Square'
model2 = 'Wavy'
model3 = 'Square/Wavy'
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
i=0
N1=0
status1 = False
status = False
modelSW = False
status3 = False
modelSW1 = True
while True:
    #--------------------------------------------------ชุดเรียกข้อมูลจากฐานข้อมูล--------------------------#
        mycursor = cnx.cursor()
        mycursor.execute("SELECT contro FROM STOP")
        myresult = mycursor.fetchall()
        contro1 = myresult [0][:1][0]
        cnx.connect()
        print('รอคำสั่งจากGUI')
        print(contro1)
        while contro1 != 0 :
            mycursor = cnx.cursor()
            mycursor.execute("SELECT ID FROM qdataownerpage")
            myresult = mycursor.fetchall()
            ID = myresult [0][:1][0]
            cnx.connect()
            mycursor = cnx.cursor()
            mycursor.execute("SELECT Model FROM qdataownerpage")
            myresult = mycursor.fetchall()
            model = myresult [0][:1][0]
            cnx.connect()
            print(model)
            #เรียกแบบ
            mycursor = cnx.cursor()
            mycursor.execute("SELECT Weight FROM qdataownerpage")
            myresult = mycursor.fetchall()
            weight = myresult [0][0][0:2]
            print (weight)
            cnx.connect()
            int(weight)
            #น้ำหนักที่รับคำสั่ง
            mycursor = cnx.cursor()
            mycursor.execute("SELECT sweight FROM loadcell")
            myresult = mycursor.fetchall()
            sweight = myresult [0][:1][0]
            cnx.connect()
            mycursor = cnx.cursor()
            mycursor.execute("SELECT kweight FROM loadcell")
            myresult = mycursor.fetchall()
            kweight = myresult [0][:1][0]
            cnx.connect()
            #น้ำหนักในถังพักสี่เหลี่ยม
            mycursor = cnx.cursor()
            mycursor.execute("SELECT outweight FROM loadcell")
            myresult = mycursor.fetchall()
            outweight = myresult [0][:1][0]
            cnx.connect
            
#-------------------------------------------------เริ่มชุดคอนโทรน------------------------------------------------#
            #คำสั่งที่แบบสี่เหลี่ยม#
            if model == model1: #เช็คแบบสี่เหลี่ยม
                #------ คำสั่งหยุดและทำงานต่อ-----------#
                mycursor = cnx.cursor()
                mycursor.execute("SELECT Motor FROM STOP")
                myresult = mycursor.fetchall()
                m = myresult [0][:1][0]
                cnx.connect()
                mycursor = cnx.cursor()
                mycursor.execute("SELECT stsp FROM STOP")
                myresult = mycursor.fetchall()
                stsp = myresult [0][:1][0]
                cnx.connect()
                #-------------------------------------------#
                if outweight <= int(weight): #เช็คน้ำหนักจ่ายออก/ออกตามคำสั่งน้ำหนักที่รับมา
                    N2=int(weight)-outweight
                    print('----------------------')
                    print(status)
                    print('แบบสี่เหล่ี่ยม')
                    print('น้ำหนักในถังพักแบบสี่เหลี่ยม =',sweight)
                    print ('ส่วนที่เหลือต้องปั้ม =',N2)
                    print('น้ำหนักทีีสั่ง =',weight)
                    print('นน.ที่out =',outweight)
                    print('ขั้นตอนที่ = ',m)
                    print('คำสั่งเริ่มหยุดขั้นตอน =',stsp)
                    print('----------------------')
                    sleep(5)
                    if int(weight) < 20:
                        if status1 != True:
                            if outweight <= int(weight): #น้ำหนักถังพักมากกว่าอินพุต/จ่ายตามโมเดล
                                status = True
                                print('น้ำหนักในถังมากกว่าคำสั่งรับ')
                                sleep (3)  
                        if status != True:#น้ำหนักถังพักน้อยกว่าอินพุต/ปั้มตามจำนวนอนนพุต
                            if sweight <= N2:
                                print('น้ำหนักถังน้อยกว่ารับ')
                                #------------ ชุดตัดเฉาก๊วย ----------------#
                                if m == 1:
                                    if stsp == 1:
                                        mycursor = cnx.cursor()
                                        mycursor.execute("SELECT stsp FROM STOP")
                                        myresult = mycursor.fetchall()
                                        stsp = myresult [0][:1][0]
                                        cnx.connect()
                                        print('stspm1=',stsp)
                                        sleep(5)
                                        '''print (GPIO.output(32, 0),'ด้านบนปิด')
                                        sleep(2)
                                        print (GPIO.output(32, 1),'ด้านบนหยุด')
                                        sleep(3)
                                        print (GPIO.output(35, 0),'ด้านล่างเปิด')
                                        sleep(2)
                                        print (GPIO.output(35, 1),'ด้านล่างหยุด')
                                        sleep(3)
                                        print(GPIO.output(33, 0), 'ด้านล่างปิด')
                                        sleep(2)
                                        print(GPIO.output(33, 1), 'ด้านล่างหยุด')
                                        sleep(3)
                                        print(GPIO.output(31, 0), 'ด้านบนเปิด')
                                        sleep(2)
                                        print(GPIO.output(31, 1), 'ด้านบนหยุด')
                                        sleep(3)
                                        continue'''
                                        cur.execute("UPDATE STOP SET Motor = '2'")
                                        cnx.commit()
                                #------------ ชุดตัดเฉาก๊วย ----------------#
                                #------------ ชุดเลื่อน ----------------#
                                if m == 2:
                                    if stsp == 1:
                                        mycursor = cnx.cursor()
                                        mycursor.execute("SELECT stsp FROM STOP")
                                        myresult = mycursor.fetchall()
                                        stsp = myresult [0][:1][0]
                                        cnx.connect()
                                        print('stspm2=',stsp)
                                        sleep(5)
                                        '''print(GPIO.output(24, 0), 'ตัวเลื่อนไปข้างหน้า')
                                        sleep(2)
                                        print(GPIO.output(24, 1), 'ตัวเลื่อนหยุด')
                                        sleep(3)
                                        print(GPIO.output(26, 0), 'ตัวเลื่อนกลับ')
                                        sleep(2)
                                        print(GPIO.output(26, 1), 'ตัวเลื่อนหยุด')
                                        sleep(3)
                                        continue'''
                                        cur.execute("UPDATE STOP SET Motor = '3'")
                                        cnx.commit()
                                #------------ ชุดเลื่อน ----------------#
                                if m == 3:
                                    if stsp == 1:
                                        mycursor = cnx.cursor()
                                        mycursor.execute("SELECT stsp FROM STOP")
                                        myresult = mycursor.fetchall()
                                        stsp = myresult [0][:1][0]
                                        cnx.connect()
                                        print('stspm3=',stsp)
                                        sleep(5)
                                        '''print (GPIO.output(38, 0),'เลื่อนลง')
                                        sleep(3)
                                        print (GPIO.output(38, 1),'เลื่อนลงหยุด')
                                        sleep(3)
                                        print (GPIO.output(36, 0),'เลื่อนขึ้น')
                                        sleep(3)
                                        print (GPIO.output(36, 1),'เลื่อนขึ้นหยุด')
                                        sleep(3)
                                        continue'''
                                        cur.execute("UPDATE STOP SET Motor = '4'")
                                        cnx.commit()
                                if m == 4:
                                    if stsp == 1:
                                        mycursor = cnx.cursor()
                                        mycursor.execute("SELECT stsp FROM STOP")
                                        myresult = mycursor.fetchall()
                                        stsp = myresult [0][:1][0]
                                        cnx.connect()
                                        print('stspm4=',stsp)
                                        sleep(5)
                                        '''print (GPIO.output(13, 0),'5.1')#ตัวเลื่อนเปิด
                                        sleep(7)
                                        print (GPIO.output(13, 1),'5.2')
                                        sleep(3)
                                        print (GPIO.output(11, 0),'6.1')#ตัวเลื่อนกลับตำแหน่งรอรับเฉา
                                        sleep(7)
                                        print (GPIO.output(11, 1),'6.2')
                                        sleep(3)'''
                                        cur.execute("UPDATE STOP SET Motor = '1'")
                                        cnx.commit()
                            else:
                                status1 = True
                else :
                    status = False
                    print('รอ')
                    print (weight)
                    cur.execute("DELETE FROM qdataownerpage WHERE ID='%s'" % (ID))
                    cur.execute("UPDATE loadcell SET contro = '0'")
                    cur.execute("UPDATE STOP SET contro = '0'")
                    cur.execute("UPDATE STOP SET Motor = '0'")
                    cur.execute("UPDATE STOP SET stsp = '0'")
                    cur.execute("UPDATE loadcell SET sweight = '0'")
                    cur.execute("UPDATE loadcell SET outweight = '0'")
                    cnx.commit()
                    print(ID) #จุดเคลียร์ค่าทุกอย่างและรอคำสั่งชุดใหม่
                    print(status)
                    print(status1)
                    sleep (2)
                    print ('สำเร็จ')
                break  
#--------------------------------------------------------------------------------------------                                
            #คำสั่งที่แบบหยัก#
            if model == model2:#แบบหยัก
                mycursor = cnx.cursor()
                mycursor.execute("SELECT Motor FROM STOP")
                myresult = mycursor.fetchall()
                m = myresult [0][:1][0]
                cnx.connect()
                mycursor = cnx.cursor()
                mycursor.execute("SELECT stsp FROM STOP")
                myresult = mycursor.fetchall()
                stsp = myresult [0][:1][0]
                cnx.connect()
                if outweight <= int(weight): #เช็คน้ำหนักจ่ายออก/ออกตามคำสั่งน้ำหนักที่รับมา
                        N2=int(weight)-outweight
                        print('----------------------')
                        print(status)
                        print('แบบหยัก')
                        print('น้ำหนักในถังพักแบบหยัก =',kweight)
                        print ('ส่วนที่เหลือต้องจ่าย =',N2)
                        print('น้ำหนักทีีสั่ง =',weight)
                        print('นน.ที่out =',outweight)
                        print('ขั้นตอนที่ = ',m)
                        print('คำสั่งเริ่มหยุดขั้นตอน =',stsp)
                        print('สถานะจ่ายออก',status1)
                        print('สถานะขั้นตอนปั้ม',status)
                        print('----------------------')
                        if int(weight) < 20:
                            if status1 != False:
                                if outweight <= int(weight): #น้ำหนักถังพักมากกว่าอินพุต/จ่ายตามโมเดล
                                    status = True
                                    print('น้ำหนักในถังมากกว่าคำสั่งรับ')       
                            if status != True:#น้ำหนักถังพักน้อยกว่าอินพุต/ปั้มตามจำนวนอนนพุต
                                if kweight <= N2:
                                    print('น้ำหนักถังน้อยกว่ารับ')
                                    #------------ ชุดตัดเฉาก๊วย ----------------#
                                    if m == 1:
                                        if stsp == 1:
                                            mycursor = cnx.cursor()
                                            mycursor.execute("SELECT stsp FROM STOP")
                                            myresult = mycursor.fetchall()
                                            stsp = myresult [0][:1][0]
                                            cnx.connect()
                                            print('stspm1=',stsp)
                                            sleep(5)
                                            ''' print (GPIO.output(32, 0),'ด้านบนปิด')
                                            sleep(2)
                                            print (GPIO.output(32, 1),'ด้านบนหยุด')
                                            sleep(3)
                                            print (GPIO.output(35, 0),'ด้านล่างเปิด')
                                            sleep(2)
                                            print (GPIO.output(35, 1),'ด้านล่างหยุด')
                                            sleep(3)
                                            print (GPIO.output(33, 0),'ด้านล่างปิด')
                                            sleep(2)
                                            print (GPIO.output(33, 1),'ด้านล่างหยุด')
                                            sleep(3)
                                            print (GPIO.output(31, 0),'ด้านบนเปิด')
                                            sleep(2)
                                            print (GPIO.output(31, 1),'ด้านบนหยุด')
                                            sleep(3)
                                            continue'''
                                            cur.execute("UPDATE STOP SET Motor = '2'")
                                            cnx.commit()
                                    #------------ ชุดตัดเฉาก๊วย ----------------#
                                    #------------ ชุดเลื่อน ----------------#
                                    if m == 2:
                                        if stsp == 1:
                                            mycursor = cnx.cursor()
                                            mycursor.execute("SELECT stsp FROM STOP")
                                            myresult = mycursor.fetchall()
                                            stsp = myresult [0][:1][0]
                                            cnx.connect()
                                            print('stspm2=',stsp)
                                            sleep(5)
                                            '''print(GPIO.output(24, 0), 'ตัวเลื่อนไปข้างหน้า')
                                            sleep(2)
                                            print(GPIO.output(24, 1), 'ตัวเลื่อนหยุด')
                                            sleep(3)
                                            print(GPIO.output(26, 0), 'ตัวเลื่อนกลับ')
                                            sleep(2)
                                            print(GPIO.output(26, 1), 'ตัวเลื่อนหยุด')
                                            sleep(3)'''
                                            cur.execute("UPDATE STOP SET Motor = '3'")
                                            cnx.commit()
                                    #------------ ชุดเลื่อน ----------------#
                                    if m == 3:
                                        if stsp == 1:
                                            mycursor = cnx.cursor()
                                            mycursor.execute("SELECT stsp FROM STOP")
                                            myresult = mycursor.fetchall()
                                            stsp = myresult [0][:1][0]
                                            cnx.connect()
                                            print('stspm3=',stsp)
                                            sleep(5)
                                            '''print (GPIO.output(38, 0),'เลื่อนลง')
                                            sleep(3)
                                            print (GPIO.output(38, 1),'เลื่อนลงหยุด')
                                            sleep(3)
                                            print (GPIO.output(36, 0),'เลื่อนขึ้น')
                                            sleep(3)
                                            print (GPIO.output(36, 1),'เลื่อนขึ้นหยุด')
                                            sleep(3)'''
                                            cur.execute("UPDATE STOP SET Motor = '4'")
                                            cnx.commit()
                                    if m == 4:
                                        if stsp == 1:
                                            mycursor = cnx.cursor()
                                            mycursor.execute("SELECT stsp FROM STOP")
                                            myresult = mycursor.fetchall()
                                            stsp = myresult [0][:1][0]
                                            cnx.connect()
                                            print('stspm4=',stsp)
                                            sleep(5)
                                            '''print (GPIO.output(13, 0),'5.1')#ตัวเลื่อนเปิด
                                            sleep(7)
                                            print (GPIO.output(13, 1),'5.2')
                                            sleep(3)
                                            print (GPIO.output(11, 0),'6.1')#ตัวเลื่อนกลับตำแหน่งรอรับเฉา
                                            sleep(7)
                                            print (GPIO.output(11, 1),'6.2')
                                            sleep(3)'''
                                            cur.execute("UPDATE STOP SET Motor = '1'")
                                            cnx.commit()
                                else:
                                    status1 = True
                                    
                            
                else :
                    status = False
                       
                    print('รอ')
                    print (weight)
                    cur.execute("DELETE FROM qdataownerpage WHERE ID='%s'" % (ID))
                    cur.execute("UPDATE loadcell SET contro = '0'")
                    cur.execute("UPDATE STOP SET contro = '0'")
                    cur.execute("UPDATE STOP SET Motor = '0'")
                    cur.execute("UPDATE STOP SET stsp = '0'")
                    cur.execute("UPDATE loadcell SET kweight = '0'")
                    cur.execute("UPDATE loadcell SET outweight = '0'")
                    cnx.commit()
                    print(ID) #จุดเคลียร์ค่าทุกอย่างและรอคำสั่งชุดใหม่
                    print(status)
                    print(status1)
                    sleep (2)
                    print ('สำเร็จ')
                break        
#-------------------------------------------------------------------------------------------------------------                            
            #คำสั่งที่มาทั้งสองแบบ# 
            if status3 != True:
                if model == model3:
                    print('แบบทั้งสองแบบ')
                    mycursor = cnx.cursor()
                    mycursor.execute("SELECT weight FROM qorderpage")
                    myresult = mycursor.fetchall()
                    weight = myresult [0][0][0:2]
                    print (weight,'sss')
                    cnx.connect()
                    int(weight)
                    print(modelSW)
                    if outweight <= int(weight):
                        print('น้ำหนักทีีสั่ง',weight)
                        print(outweight,'นน.ที่out')
                        N2=int(weight)-outweight
                        print (N2,'ส่วนที่เหลือต้องปั้ม')
                        print('.......................................')
                        sleep(3)
                        if modelSW != True:
                            mycursor = cnx.cursor()
                            mycursor.execute("SELECT model FROM qorderpage")
                            myresult = mycursor.fetchall()
                            modelS = myresult [0][:1][0][0:6]
                            cnx.connect()
                            print(modelS)
                            print('.......................................')
                            print(status)
                            print('.......................................')
                            if modelS == model1:
                                print('----------------------')
                                print('แบบส่่เหล่ี่ยม')
                                print('----------------------')
                                if int(weight) < 20:
                                    if status1 != True:
                                        print('101010')
                                        if sweight >= N2: #น้ำหนักถังพักมากกว่าอินพุต/จ่ายตามโมเดล
                                            status = True
                                            print('น้ำหนักในถังมากกว่าคำสั่งรับ2')
                                            sleep (1)
                                            
                                    if status != True:#น้ำหนักถังพักน้อยกว่าอินพุต/ปั้มตามจำนวนอนนพุต
                                        if sweight <= N2:
                                            print('น้ำหนักถังน้อยกว่ารับ2')
                                            sleep (2)
                    else:
                        status4 = True
                        print('สำเร็จ1')    
            if status4 != False:
                print('เริ่มทำส่วนที่สอง')
                mycursor = cnx.cursor()
                mycursor.execute("SELECT weight FROM qorderpage")
                myresult = mycursor.fetchall()
                weight = myresult [0][0][3:5]
                print (weight)
                cnx.connect()
                int(weight)
                                
                if outweight <= int(weight):
                    print('น้ำหนักทีีสั่ง',weight)
                    print(outweight,'นน.ที่out')
                    N2=int(weight)-outweight
                    print (N2,'ส่วนที่เหลือต้องปั้ม')
                    print('.......................................')
                    sleep(3)
                    mycursor = cnx.cursor()
                    mycursor.execute("SELECT model FROM qorderpage")
                    myresult = mycursor.fetchall()
                    modelS = myresult [0][:1][0][7:11]
                    cnx.connect()
                    print(modelS)
                    print('.......................................')
                    print(status3)
                    print('.......................................')
                    if modelS == model2:
                        print('----------------------')
                        print('models')
                        print('----------------------')
                        if int(weight) < 20:
                            if status1 != True:
                                print('202020')
                                if sweight >= N2: #น้ำหนักถังพักมากกว่าอินพุต/จ่ายตามโมเดล
                                    status = True
                                    print('น้ำหนักในถังมากกว่าคำสั่งรับ3')
                                    sleep (1)
                                                        
                            if status != True:#น้ำหนักถังพักน้อยกว่าอินพุต/ปั้มตามจำนวนอนนพุต
                                if sweight <= N2:
                                    print('น้ำหนักถังน้อยกว่ารับ3')
                                    sleep (2)                    
                        
                else:
                    status3 = True
                    status4 = False
                    print('สำเร็จ33')
                                            
                   
                    
                
                   
                    
            
                
                
            
            
            
            
        
        
        
        
       
                
            
