'''
cs4400_Group_59
Jingtian Zhang, Tong Jin, Justin Fletcher, Gretchen Rowe
copyright

Notice: you have to use Python 3.4 to run the code. 
        Pymysql should be installed before running
'''

import pymysql



from tkinter import *



from re import match



import datetime



from datetime import datetime, date

import time



from tkinter import messagebox





class App:




    def __init__(self,master):







        self.master=master



        self.LoginPage()



        self.Register()



        self.register.withdraw()



    # Base method to connect to the database
    def Connect(self):



        try:



            db = pymysql.connect( host = 'academic-mysql.cc.gatech.edu',passwd = 'LqtZ6OBk', user = 'cs4400_Group_59', db = 'cs4400_Group_59')



            return db




        except:



            messagebox.showerror("Unable To Connect","Check Your Internet Connection")


    # Login page function       
    def LoginPage(self):




        self.master.title("Login")



        Label(self.master,text="* Customer Username should start with 'c'.").grid(row=5,column=1,sticky=E)



        Label(self.master,text="* Manager Username should start with 'm'.").grid(row=6,column=1,sticky=E)



        Label(self.master,text="Username:").grid(row=2,column=0,sticky=E)



        Label(self.master,text="Password:").grid(row=3,column=0,sticky=E)





        self.entry1=Entry(self.master,width=30)



        self.entry1.grid(row=2,column=1)



        self.entry2=Entry(self.master,width=30,show="*")



        self.entry2.grid(row=3,column=1)







        frame=Frame(self.master)



        frame.grid(row=4,column=1,sticky=E)







        Button(frame,text="Login",command=self.LoginCheck).pack(side=RIGHT)



        Button(frame,text="Create Account",command=self.LoginToRegister).pack(side=RIGHT)










    # Check if login information matches
    def LoginCheck(self):







        db=self.Connect()



        c=db.cursor()



        self.userName=self.entry1.get()



        password=self.entry2.get()







        SQL1="SELECT username,password FROM Customer WHERE username=%s AND password=%s"



        SQL2="SELECT username,password FROM Management WHERE username=%s AND password=%s"







        affected1=c.execute(SQL1,(self.userName,password))



        affected2=c.execute(SQL2,(self.userName,password))



        



        



        if affected1==1 or affected2==1:



 



            messagebox.showinfo("Success","Logged in successfully")



            if affected1==1:



                #self.master.withdraw()



                self.custFunc()



            elif affected2 ==1:



                #self.master.withdraw()



                self.manFunc()



        else:



            messagebox.showerror("Error","The username/password combination is unrecognizable")           



            return None





    def LoginToRegister(self):







        self.register.deiconify()



        #self.master.withdraw()



 


    def Register(self):







        self.register=Toplevel()



        self.register.title("New User Registration")





        Label(self.register,text="Username:").grid(row=2,column=0,sticky=W)



        Label(self.register,text="Password:").grid(row=3,column=0,sticky=W)



        Label(self.register,text="Confirm Password:").grid(row=4,column=0,sticky=W)



        Label(self.register,text="Email:").grid(row=5,column=0,sticky=W)



        



        self.entry3=Entry(self.register,width=30)



        self.entry3.grid(row=2,column=1)



        self.entry4=Entry(self.register,width=30,show="*")



        self.entry4.grid(row=3,column=1)



        self.entry5=Entry(self.register,width=30,show="*")



        self.entry5.grid(row=4,column=1)



        self.entry6=Entry(self.register,width=30)



        self.entry6.grid(row=5,column=1)







        Button(self.register,text="Submit",command=self.RegisterDB).grid(row=6,column=2)



        #Button(self.register,text="Back",command=self.ttttt).grid(row=6,column=3)







    # def ttttt(self):



    #     self.register.withdraw()



    #     self.master.deiconify()







    # method to register new users into database
    def RegisterDB(self):







        userName=self.entry3.get()



        password1=self.entry4.get()



        password2=self.entry5.get()



        email=self.entry6.get()







        if userName=="":







            messagebox.showerror("Error!","Enter the Username")



            return None



        if userName[0] != 'c':



            messagebox.showerror("Error!","Username must start with 'c'!")



            return None





        if password1=="":







            messagebox.showerror("Error!","Enter the Password")



            return None







        if password1!=password2:







            messagebox.showerror("Error!","Password entrered do not match")



            return None







        if email=="":







            messagebox.showerror("Error!", "Enter Email")



            return None







 



        db = pymysql.connect( host = 'academic-mysql.cc.gatech.edu',passwd = 'LqtZ6OBk', user = 'cs4400_Group_59', db = 'cs4400_Group_59') 



        c=db.cursor()







        SQL="SELECT username FROM Customer"







        c.execute(SQL)



        affected = c.fetchall()



        







        nameList = []



        for name in affected:



            nameList.append(name[0])







        if userName in nameList:



            messagebox.showerror("Error!", "Username has already been used")



            self.entry3.delete(0,last=END)



            self.entry4.delete(0,last=END)



            self.entry5.delete(0,last=END)



            return



        else:



            



            messagebox.showinfo("Success", "Registration is complete")







            sql = "INSERT INTO Customer (username,password,email) VALUES (%s,%s,%s)"



            c.execute(sql,(userName,password1,email))



            c.close()



            db.commit()



            db.close()



            self.register.withdraw()

            self.master.deiconify()






    # Customer main page
    def custFunc(self):







        name = self.entry1.get()







        self.cfunct = Toplevel(self.master)



        self.cfunct.title("Choose Functionality")







        Label(self.cfunct, text = "Welcome, {}".format(name)).grid(row=0,sticky=W)







        Button(self.cfunct,text="Make a new reservation",command=self.makeRes).grid(row=1,sticky=EW)



        Button(self.cfunct,text="Update your reservation",command=self.updateReservation).grid(row=2,sticky=EW)



        Button(self.cfunct,text="Cancel Reservation",command=self.cancelReservation).grid(row=3,sticky=EW)



        Button(self.cfunct,text="Provide feedback",command=self.giveReview).grid(row=4,sticky=EW)



        Button(self.cfunct,text="View feedback",command=self.viewReviews).grid(row=5,sticky=EW)










    # Manager main page
    def manFunc(self):







        name = self.entry1.get()







        self.mfunct = Toplevel(self.master)



        self.mfunct.title("Choose Functionality")







        Label(self.mfunct, text = "Welcome, {}".format(name)).grid(row=0,sticky=W)







        Button(self.mfunct,text="View reservation report",command=self.viewResReport).grid(row=1,sticky=EW)



        Button(self.mfunct,text="View popular room category report",command=self.popularRoom).grid(row=2,sticky=EW)



        Button(self.mfunct,text="View revenue report",command=self.revenueReport).grid(row=3,sticky=EW)






    # View Reservation Report
    def viewResReport(self):

        self.resReport = Toplevel(self.mfunct)

        self.resReport.title('Reservation Report')



        # sql="""SELECT MONTH( Start_Date ), Room_Location, COUNT( * ) 

        #     FROM Reservation NATURAL JOIN Reservation_Room

        #     GROUP BY MONTH( Start_Date ) , Room_Location"""

        sql="""SELECT R.date, R.location, COUNT(*)
            FROM(
            SELECT DISTINCT Reservation_ID, MONTH(Start_Date) AS Date, Room_Location AS location
            FROM Reservation
            NATURAL JOIN Reservation_Room
            )
            AS R
            GROUP BY R.date, R.location"""

        db= self.Connect()

        c = db.cursor()

        c.execute(sql)

        res = c.fetchall()

        c.close()

        db.commit()

        db.close()



        Label(self.resReport,text='Month').grid(row=0,column=0,sticky=W)

        Label(self.resReport,text='Location').grid(row=0,column=1,sticky=W)

        Label(self.resReport,text='Total number of reservations').grid(row=0,column=2,sticky=W)

        

        rowCount = 1



        monthDict={1:'January',2:'Feburary',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}

        m=13

        for each in res:

            if each[0] != m:

                m = each[0]

                Label(self.resReport,text=monthDict[m]).grid(row=rowCount,column=0,sticky=W)

            for j in range(1,len(each)):

                Label(self.resReport,text=each[j]).grid(row=rowCount,column=j,sticky=W)

            rowCount+=1





        #print(type(res[0][0]))


    # View popular rooom
    def popularRoom(self):

        sql="""SELECT A.Mon, A.Category, A.Location, MAX( A.num ) 

                FROM (

                SELECT MONTH( Start_Date ) AS Mon, Room_Location AS Location, Room_Category AS Category, COUNT( * ) AS num

                FROM Reservation

                NATURAL JOIN Reservation_Room

                JOIN Room on Reservation_Room.Room_Location = Room.Location AND Reservation_Room.Room_num = Room.Room_num

                GROUP BY MONTH( Start_Date ) , Room_Location, Room_Category

                ) AS A

                GROUP BY A.Location, A.Mon

                ORDER BY A.Mon DESC"""



        db = self.Connect()

        c = db.cursor()

        c.execute(sql)

        res = c.fetchall()

        #print(res)



        self.popular = Toplevel(self.mfunct)

        self.popular.title('Popular Room-Category')

        Label(self.popular,text='Month').grid(row=0,column=0,sticky=W)

        Label(self.popular,text='top room-category').grid(row=0,column=1,sticky=W)

        Label(self.popular,text='Location').grid(row=0,column=2,sticky=W)

        Label(self.popular,text='Total number of reservations for room category').grid(row=0,column=3,sticky=W)

        rowCount = 1



        monthDict={1:'January',2:'Feburary',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}

        m=13

        for each in res:

            if each[0] != m:

                m = each[0]

                Label(self.popular,text=monthDict[m]).grid(row=rowCount,column=0,sticky=W)

            for j in range(1,len(each)):

                Label(self.popular,text=each[j]).grid(row=rowCount,column=j,sticky=W)

            rowCount+=1


    # View revenue report
    def revenueReport(self):

        self.revRep = Toplevel(self.mfunct)

        self.revRep.title("Revenue Report")



        db=self.Connect()

        c=db.cursor()

        sql = """SELECT MONTH( Start_Date ) , Room_Location, SUM( Total_Cost ) 

                FROM Reservation

                NATURAL JOIN Reservation_Room

                GROUP BY MONTH( Start_Date ) , Room_Location;"""      



        c.execute(sql)

        result = c.fetchall()



        rows=0

        Label(self.revRep,text='Month',font=('arial',14,'bold')).grid(row=0,column=0,sticky=EW)

        Label(self.revRep,text='Location',font=('arial',14,'bold')).grid(row=0,column=1,sticky=EW)

        Label(self.revRep,text='Total Revenue',font=('arial',14,'bold')).grid(row=0,column=2,sticky=EW)

        rows+=1

        monthDict={1:'January',2:'Feburary',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}

        m=13

        for i in range(len(result)):

            if result[i][0] != m:

                m = result[i][0]

                Label(self.revRep,text=monthDict[m]).grid(row=rows,column=0,sticky=W)

            for j in range(1,len(result[i])):

                # if rows%2 ==1:

                #     Label(self.revRep,text=result[i][j],bg='grey').grid(row=rows,column=j,sticky=W)

                # else:

                Label(self.revRep,text=result[i][j]).grid(row=rows,column=j,sticky=W)



            rows+=1



        c.close()

        db.commit()

        db.close()


    # Helper method to check if start_Date is before today
    def checkDate(self,startDate):

        date_format = "%Y-%m-%d"

        today = datetime.today()

        today = str(today)[0:10]

        today1 = datetime.strptime(today,"%Y-%m-%d")

        startDate = datetime.strptime(startDate,"%Y-%m-%d")

        delta = startDate - today1

        if delta.days < 0:

            return 1

        else:

            return 0

    # Making reservation 1
    def makeRes(self):




        self.cfunct.withdraw()

        self.search = Toplevel(self.master)



        self.search.title("Search Rooms")



        Label(self.search, text="Location:").grid(row=0,column=0,sticky=W)



        self.cities = StringVar(self.search)



        self.cities.set("Atlanta")



        self.ct = OptionMenu(self.search, self.cities, "Atlanta", "Boston","Chicago","Los Angeles","New York").grid(row=0,column=1,sticky=W)





        self.stDate = StringVar()



        self.endDate = StringVar()



        Label(self.search, text="Start Date:").grid(row=1,column=0,sticky=W)



        Entry(self.search,textvariable=self.stDate,width=30).grid(row=1,column=1,sticky=W)







        Label(self.search, text="End Date:").grid(row=1,column=2,sticky=W)



        Entry(self.search,textvariable=self.endDate,width=30).grid(row=1,column=3,sticky=W)



        Label(self.search, text='Date Format: YYYY-MM-DD').grid(row=2,column=0,columnspan=2)



        Button(self.search, text="Search",command=self.searchRooms).grid(row=3,column=3,sticky=E)


    # Making reservation 2
    def searchRooms(self):

        callback = self.checkDate(self.stDate.get())

        if callback == 1:

            messagebox.showerror("No!","Start date is past!")

            return None


        db=self.Connect()

        c=db.cursor()


        sql = """SELECT * 

                    FROM (

                    SELECT Room_num, Room_Category, num_People, Cost_per_day, Cost

                    FROM Room

                    LEFT JOIN Extra_Bed ON Room.Room_num = Extra_Bed.EB_Room_num

                    AND Room.Location = Extra_Bed.EB_Location

                    WHERE Room.Location =  %s

                    )  AS  R

                    WHERE NOT EXISTS (

                    SELECT Room_num, Room_Location

                    FROM Reservation_Room

                    NATURAL JOIN Reservation

                    WHERE Room_Location =  %s

                    AND Room_num = R.Room_num

                    AND (

                    End_Date >  %s AND Start_Date <  %s

                    )

                    )"""





        c.execute(sql, (self.cities.get(),self.cities.get(),self.stDate.get(),self.endDate.get()))


        self.res = c.fetchall()

        c.close()

        db.commit()

        db.close()

        # If not room found, stop!
        if len(self.res) == 0:

            messagebox.showerror("Sorry!","We cannot find available rooms!")

            return None

        #print(type(self.res[0][4]))

        
        self.roomSearch = Toplevel(self.master)

        self.roomSearch.title("Make a Reservation")


        self.rowCount=0

        Label(self.roomSearch,text='Room Number').grid(row=0,column=0,sticky=W)

        Label(self.roomSearch,text='Room Category').grid(row=0,column=1,sticky=W)

        Label(self.roomSearch,text='#persons allowed').grid(row=0,column=2,sticky=W)

        Label(self.roomSearch,text='cost per day').grid(row=0,column=3,sticky=W)

        Label(self.roomSearch,text='cost of extra bed per day').grid(row=0,column=4,sticky=W)

        Label(self.roomSearch,text='Select Room').grid(row=0,column=5,sticky=W)

        self.rowCount+=1



        self.checkbuttons1=[] # for detail check

        for i in range(len(self.res)):

            for j in range(len(self.res[i])):    

                Label(self.roomSearch,text=self.res[i][j]).grid(row=self.rowCount,column=j,sticky=W+E)

            self.checkbuttons1.append(IntVar())

            Checkbutton(self.roomSearch,variable=self.checkbuttons1[i]).grid(row=self.rowCount,column=5)



            self.rowCount+=1

        Button(self.roomSearch,text='Check Details',command=self.checkDetails).grid(row=self.rowCount,column=5,sticky=W)


    # Making reservation 3
    def checkDetails(self):

        self.rowCount+=1

        Label(self.roomSearch,text='Room Number').grid(row=self.rowCount,column=0,sticky=W)

        Label(self.roomSearch,text='Room Category').grid(row=self.rowCount,column=1,sticky=W)

        Label(self.roomSearch,text='#persons allowed').grid(row=self.rowCount,column=2,sticky=W)

        Label(self.roomSearch,text='cost per day').grid(row=self.rowCount,column=3,sticky=W)

        Label(self.roomSearch,text='cost of extra bed per day').grid(row=self.rowCount,column=4,sticky=W)

        Label(self.roomSearch,text='extra bed').grid(row=self.rowCount,column=5,sticky=W)

        self.rowCount+=1



        self.checkbuttons2=[] # for extra bed check

        self.resRoom = [] # for later INSERT INTO Reservation Room

        buttonNum=0

        for i in range(len(self.checkbuttons1)):

            if self.checkbuttons1[i].get() == 1:

                tmp=[self.res[i][0]]

                for j in range(len(self.res[i])):    

                    Label(self.roomSearch,text=self.res[i][j]).grid(row=self.rowCount,column=j,sticky=W+E)

                self.checkbuttons2.append(IntVar())

                if self.res[i][4] == None:

                    Checkbutton(self.roomSearch,variable=self.checkbuttons2[buttonNum],state='disabled').grid(row=self.rowCount,column=j+1)

                    tmp.append(self.checkbuttons2[buttonNum])

                    buttonNum+=1

                else:

                    Checkbutton(self.roomSearch,variable=self.checkbuttons2[buttonNum]).grid(row=self.rowCount,column=j+1)

                    tmp.append(self.checkbuttons2[buttonNum])

                    buttonNum+=1

                self.rowCount+=1

                self.resRoom.append(tmp)



        

        Button(self.roomSearch,text='Cost',command=self.getCost).grid(row=self.rowCount,column=5)


    # Making reservation 4
    def getCost(self):

        Label(self.roomSearch,text='Start Date').grid(row=self.rowCount,column=0)

        Entry(self.roomSearch,textvariable=self.stDate,state='readonly').grid(row=self.rowCount,column=1)

        Label(self.roomSearch,text='End Date').grid(row=self.rowCount,column=2)

        Entry(self.roomSearch,textvariable=self.endDate,state='readonly').grid(row=self.rowCount,column=3)

        self.rowCount+=1

        d1 = datetime.strptime(self.stDate.get(), "%Y-%m-%d")

        d2 = datetime.strptime(self.endDate.get(), "%Y-%m-%d")

        days = abs((d2 - d1).days)



        totalCost = 0

        for i in range(len(self.checkbuttons1)):

            if self.checkbuttons1[i].get() == 1:

                totalCost+=days*self.res[i][3]

        for j in range(len(self.checkbuttons2)):

            if self.checkbuttons2[j].get() == 1:

                totalCost+=days*self.res[j][4]

        self.totalCost=IntVar()

        self.totalCost.set(totalCost)

        Label(self.roomSearch,text='Total Cost').grid(row=self.rowCount,column=0)

        Entry(self.roomSearch,textvariable=self.totalCost).grid(row=self.rowCount,column=1)



        sql="""SELECT Card_num FROM Payment_Information WHERE Holder=%s"""

        db = self.Connect()

        cursor = db.cursor()

        cursor.execute(sql,self.userName)

        result=cursor.fetchall()

        if len(result) == 0:

            
            messagebox.showinfo("Warning!","Please add a card to finish reservation!")
            
            self.pay0 = IntVar()
            
            self.pay=''

            OptionMenu(self.roomSearch,self.pay0,self.pay).grid(row=self.rowCount)

            Button(self.roomSearch,text='Add Card',command=self.payInfo).grid(row=self.rowCount,column=2)

            self.rowCount+=1

            Button(self.roomSearch,text='Submit',command=self.payInfo).grid(row=self.rowCount,column=5)

        else:

            # Display the 4 digits card
            self.pay0 = StringVar()

            # Store and display 16 digits card number
            self.pay00 = []

            # self.pay00.set(int(result[0][0]))
            fourdigit = int(result[0][0])%10000
            self.pay0.set(str(fourdigit))

            self.pay=[]

            for each in result:

                tmp = int(each[0])%10000

                self.pay00.append(each[0])

                self.pay.append(str(tmp))

            OptionMenu(self.roomSearch,self.pay0,*self.pay).grid(row=self.rowCount)

            Button(self.roomSearch,text='Add Card',command=self.payInfo).grid(row=self.rowCount,column=2)

        # except:

        #     self.pay0 = IntVar()

        #     self.pay=''

        #     OptionMenu(self.roomSearch,self.pay0,self.pay).grid(row=self.rowCount)

        #     Button(self.roomSearch,text='Add Card',command=self.payInfo).grid(row=self.rowCount,column=2)

            self.rowCount+=1


            Button(self.roomSearch,text='Submit',command=self.submit).grid(row=self.rowCount,column=5)


        cursor.close()

        db.commit()

        db.close()


    # Making reservation 5
    def submit(self):

        # if self.pay == None:

        #     messagebox.showerror("Impossible!","Please add one payment method first.")

        #     return None



        sql="""SELECT DISTINCT MAX(Reservation_ID) FROM Reservation"""

        db = self.Connect()

        cursor = db.cursor()

        cursor.execute(sql)

        result=cursor.fetchall()

        ID = result[0][0]

        RID = ID + 1

        sql = """INSERT INTO Reservation (Reservation_ID, Start_Date, End_Date, Is_Cancelled, Total_Cost, Customer, Payment_num) VALUES(%s,%s,%s,%s,%s,%s,%s)"""

        sql2 = """INSERT INTO Reservation_Room VALUES(%s, %s, %s, %s)"""

        card = 0000000000000000
        ##### For test Only #######
        for i in range(len(self.pay00)):

            if self.pay0.get() in self.pay00[i]:

                card = self.pay00[i]

                break
        ############################
        # Insert into Reservation table
        cursor.execute(sql,(RID,self.stDate.get(),self.endDate.get(),0,self.totalCost.get(),self.userName,card))

        cursor.close()

        # Insert into Reservation Room table

        #### For Test Only ########
        # for i in range(len(self.resRoom)):
        #     print(self.resRoom[i][0])
        #     print(self.resRoom[i][1].get())

        ############################

        c = db.cursor()

        for i in range(len(self.resRoom)):

            c.execute(sql2,(RID,self.resRoom[i][0],self.cities.get(),self.resRoom[i][1].get()))

        c.close()

        db.commit()

        db.close()

        self.roomSearch.withdraw()

        self.confScreen(RID)


    # Add card 1
    def payInfo(self):

        self.roomSearch.withdraw()

        self.payment = Toplevel(self.master)



        self.payment.title("Payment Information")





        self.payFrame = Frame(self.payment,relief="flat",bd=1)



        self.payFrame.grid(row=0,column=0,columnspan=4,sticky=EW)







        Label(self.payFrame,text="Add Card").grid(row=0,columnspan=2,sticky=EW)



        



        Label(self.payFrame,text="Name on Card:").grid(row=1,column=0,sticky=W)



        self.nameCard = StringVar()

        Entry(self.payFrame, width=50, textvariable=self.nameCard).grid(row=1,column=1,sticky=W)



        



        Label(self.payFrame,text="Card Number:").grid(row=2,column=0,sticky=W)



        self.numCard = StringVar()

        Entry(self.payFrame, textvariable=self.numCard, width=50).grid(row=2,column=1,sticky=W)



        Label(self.payFrame,text="Expiration Date:").grid(row=3,column=0,sticky=W)



        self.expCard = StringVar()

        Entry(self.payFrame, textvariable=self.expCard,width=30).grid(row=3,column=1,sticky=W)



        Label(self.payFrame,text="Date Format: YYYY-MM-DD").grid(row=4,column=1,sticky=W)



        



        Label(self.payFrame,text="CVV:").grid(row=5,column=0,sticky=W)



        self.cvv = StringVar()

        Entry(self.payFrame, textvariable=self.cvv,width=20).grid(row=5,column=1,sticky=W)







        Button(self.payFrame, text="Save", command = self.insertPayment).grid(row=6,column=1,sticky=W)







        Label(self.payFrame,text="Delete Card").grid(row=0,column=2,columnspan=2,sticky=EW)







        Label(self.payFrame,text="Card Number:").grid(row=1,column=2,sticky=W)





        try:

            sql="""SELECT Card_num FROM Payment_Information WHERE Holder=%s"""

            db = self.Connect()

            cursor = db.cursor()

            cursor.execute(sql,self.userName)

            result=cursor.fetchall()

            self.paymentCardInfo = IntVar()

            self.paymentCardInfo.set(int(result[0][0]))



            cardList = []

            for numbers in result:

                card = numbers[0]

                cardList.append(card)

                

            self.cardToDelete = OptionMenu(self.payFrame,self.paymentCardInfo,*cardList)

            self.cardToDelete.grid(row=1,column=3,sticky=W)





            Button(self.payFrame,text="Delete",command = self.deleteCard).grid(row=6,column=4,sticky=W)

        except:

            None

    
    # Add card 2
    def deleteCard(self):

        sql = """DELETE FROM Payment_Information WHERE Card_num = %s"""



        db = self.Connect()

        cursor = db.cursor()

        cursor.execute(sql,self.paymentCardInfo.get())



        cursor.close()

        db.commit()

        db.close()



        messagebox.showinfo("Sucess!","Card has been deleted!")

        self.payment.withdraw()




    # Add card 3
    def insertPayment(self):

 

        number = self.numCard.get()

        

        name = self.nameCard.get()

        

        cvv = self.cvv.get()

        

        exp = self.expCard.get()

    

        user = self.userName





        if number.isdigit() is False and len(number) != 16:

            messagebox.showerror("Error!", "Enter valid 16-digit card number")

            return None

        

        if cvv.isdigit() is False:

            messagebox.showerror("Error!", "Enter numerical cvv")

            return None

        

        r = re.compile('\d{4}\-\d{2}\-\d{2}')

        



        if r.match(exp) is not None:

            try:

                expDateNew = datetime.strptime(exp,'%Y-%m-%d')

                if datetime.now() > expDateNew:

                    messagebox.showerror("Error!", "Card has expired")

                    return None

                

            

            

            except:

                messagebox.showerror("Error!", "Invalid date")

                return None



            

        try:

            db=self.Connect()

            c=db.cursor()



            sql = """INSERT INTO Payment_Information (Card_num,name,cvv,expDate,Holder) VALUES(%s, %s, %s, %s, %s)"""

            

            c.execute(sql, (number, name, cvv, exp, user))



            c.close()

            db.commit()

            db.close()



            messagebox.showinfo("Success!", "Card has been added")

            self.payment.withdraw()



        except:

            messagebox.showerror("Error!", "Card already exists")

            


    # Confirmation Window when a reservation is made
    def confScreen(self,RID): #confirmation screen with reservation id



        #self.payment.withdraw()

        self.confirm = Toplevel(self.master)

        



        self.confirm.title("Confirmation Screen")



        Label(self.confirm, text="Your Reservation ID:   ").grid(row=0,column=0,sticky=W)



        # db=self.Connect()

        # c=db.cursor()

        # sql = """SELECT MAX(Reservation_ID) FROM Reservation """ 

        # c.execute(sql)

        # maxRes = c.fetchall()

        # newResID = maxRes[0][0]+1

        # c.close()

        # db.commit()

        # db.close()

        newResID = RID

        Label(self.confirm, text=newResID).grid(row=0,column=1,sticky=W)



        Label(self.confirm, text= "Please save this Reservation ID for all further communication.").grid(row=1,columnspan=3,sticky=EW)



        Button(self.confirm, text="Ok", command=self.confirmHelper).grid(row=2,column=1,sticky=EW) #this should go back to customer option window




    def confirmHelper(self):

        self.search.withdraw()
        self.confirm.withdraw()
        self.custFunc()

    # Update reservation 1
    def updateReservation(self):



        self.update = Toplevel(self.master)



        self.update.title("Update Reservation")





        frame1 = Frame(self.update)

        frame1.pack()

        Label(frame1, text="Reservation ID:").grid(row=0,column=0,sticky=W)




        self.resID = Entry(frame1, width = 30)



        self.resID.grid(row=0,column=1,sticky=W)







        #print(self.resID.get())





        Button(frame1, text="Search", command=self.reservationSearch).grid(row=0,column=2,sticky=W)



            
    # Update reservation 2
    def reservationSearch(self):



        frame2 = Frame(self.update)

        frame2.pack()

        db=self.Connect()



        c=db.cursor()





        sql="""SELECT start_date, end_date, Room_Location, Reservation.Reservation_ID

                FROM Reservation NATURAL JOIN Reservation_Room

                WHERE Reservation.Reservation_ID = %s AND Is_Cancelled = 0 AND Customer = %s"""



        c.execute(sql,(self.resID.get(),self.userName))

        #print(self.userName)



        res = c.fetchall()

        #print(res)



        c.close()

        db.commit()

        db.close()

        if len(res) == 0:

            messagebox.showerror("Error!","Invalid Reservation ID or It is already cancelled.")

            return None



        date_format = "%Y-%m-%d"



        # today's date in YYYY-MM-DD

        today = datetime.today()

        today = str(today)[0:10]

        #print(res)

        d1 = str(res[0][0])

        self.today = datetime.strptime(today,date_format)

        d = datetime.strptime(d1,date_format)

        delta = d - self.today



        if delta.days <= 0:

            messagebox.showerror("Error!","The reservation date has passed!")

            return None



        self.room_location = res[0][2]



        Label(frame2,text="Current Start Date: ").grid(row=1,column=0,sticky=W)



        Label(frame2,text="{}".format(res[0][0])).grid(row=1,column=1,columnspan=2,sticky=W)







        Label(frame2,text="Current End Date: ").grid(row=1,column=3,sticky=W)



        Label(frame2,text="{}".format(res[0][1])).grid(row=1,column=4,columnspan=2,sticky=W)







        Label(frame2,text="New Start Date: ").grid(row=2,column=0,sticky=W)



        self.newSDate = Entry(frame2, width = 30)



        self.newSDate.grid(row=2,column=1,columnspan=2,sticky=W)







        Label(frame2,text="New End Date: ").grid(row=2,column=3,sticky=W)



        self.newEDate = Entry(frame2, width = 30)



        self.newEDate.grid(row=2,column=4,columnspan=2,sticky=W)







        Button(frame2, text="Search Availability",command=self.availRooms).grid(row=3, column=1, columnspan=2, sticky=EW)






    # Update reservation 3
    def availRooms(self):



        callback = self.checkDate(self.newSDate.get())

        if callback == 1:

            messagebox.showerror("No!","Start date cannot be past days!")

            return None
        # Need to extract data from DB

        sql="""SELECT * 

                    FROM (

                    SELECT Room.Room_num, Room_Category, num_People, Cost_per_day, Cost, has_ExtraBed

                    FROM Room

                    LEFT JOIN Extra_Bed ON Room.Room_num = Extra_Bed.EB_Room_num

                    AND Room.Location = Extra_Bed.EB_Location

                    JOIN Reservation_Room ON Room.Room_num = Reservation_Room.Room_num AND Room.Location = Reservation_Room.Room_Location

                    NATURAL JOIN Reservation

                    WHERE Reservation_ID =  %s

                    )  AS  R

                    WHERE NOT EXISTS (

                    SELECT Room_num, Room_Location

                    FROM Reservation_Room

                    NATURAL JOIN Reservation

                    WHERE Room_Location =  %s

                    AND Room_num = R.Room_num

                    AND Reservation_ID <> %s

                    AND (

                    Start_Date <  %s

                    AND End_Date >  %s

                    )

                    )"""

        

        db = self.Connect()

        c = db.cursor()

        c.execute(sql,(self.resID.get(),self.room_location,self.resID.get(),self.newEDate.get(),self.newSDate.get()))

        res = c.fetchall()

        num1 = len(res)

        if len(res) == 0:

            messagebox.showerror("Unsuccessful!","You may cancel current reservation and make a new reservation!")

            return None


        sql2 = """SELECT * 

                FROM Reservation NATURAL JOIN Reservation_Room

                WHERE Reservation_ID = %s"""

        c.execute(sql2,self.resID.get())

        res2 = c.fetchall()

        num2 = len(res2)

        if num1 == num2:

            frame3 = Frame(self.update)

            frame3.pack()

            rowCount = 1

            Label(frame3,text="Rooms are available. Please confirm details below before submitting.").grid(column=0,columnspan=6)





            Label(frame3,text="Room Number", font = "bold").grid(row=rowCount,column=0,sticky=W)



            Label(frame3,text="Room Category", font = "bold").grid(row=rowCount,column=1,sticky=W)



            Label(frame3,text="#persons allowed", font = "bold").grid(row=rowCount,column=2,sticky=W)



            Label(frame3,text="cost per day", font = "bold").grid(row=rowCount,column=3,sticky=W)



            Label(frame3,text="cost of extra bed per day", font = "bold").grid(row=rowCount,column=4,sticky=W)



            Label(frame3,text="Select Room", font = "bold").grid(row=rowCount,column=5,sticky=W)

            

            rowCount+=1



            self.checkbuttons=[] # for detail check



            self.costPerday=0



            for i in range(len(res)):



                self.costPerday+=res[i][3]



                for j in range(len(res[i])-1):



                    Label(frame3,text=res[i][j]).grid(row=rowCount,column=j,sticky=W+E)



                tmp = IntVar()

                tmp.set(res[i][len(res[i])-1])

                self.checkbuttons.append(tmp)


                Checkbutton(frame3,variable=self.checkbuttons[i],onvalue=1,offvalue=0).grid(row=rowCount,column=5)


                rowCount+=1



            Button(frame3,text='Cost',command=self.newCost).grid(row=rowCount,column=5)

        else:
            
            messagebox.showinfo("Unsuccessful!","You may cancel current reservation and make a new reservation!")
            
            return None

    # Update reservation 4
    def newCost(self):

        frame4 = Frame(self.update)

        frame4.pack()

        d1 = datetime.strptime(self.newSDate.get(), "%Y-%m-%d")

        d2 = datetime.strptime(self.newEDate.get(), "%Y-%m-%d")

        days = abs((d2 - d1).days)

        self.cost = DoubleVar()

        self.cost.set(days * self.costPerday)

        Label(frame4,text='Total Cost').grid(row=0,column=0,sticky=E)

        Entry(frame4,textvariable=self.cost,state='readonly').grid(row=0,column=1,sticky=W)

        Button(frame4,text='Submit',command=self.updateSubmit).grid(row=1,column=1,sticky=W+E)


    # Update reservation 5
    def updateSubmit(self):

        sql="""UPDATE Reservation

            SET Start_Date = %s, End_Date = %s, Total_Cost = %s

            WHERE Reservation_ID = %s"""

        pass

        db = self.Connect()

        c = db.cursor()
        
        c.execute(sql,(self.newSDate.get(),self.newEDate.get(),self.cost.get(),self.resID.get()))

        c.close()
        
        db.commit()
        
        db.close()

        messagebox.showinfo("Great!","Reservation Updated Successfully!")

        self.update.withdraw()

    # Cancel reservation 1
    def cancelReservation(self): #figure 9


        self.cancel = Toplevel(self.master)

        self.cancel.title("Cancel Reservation")

        frame1 = Frame(self.cancel)

        frame1.pack()

        Label(frame1, text="Reservation ID:").grid(row=0,column=0,sticky=W)

        

        self.cancelID = Entry(frame1, width = 30)

        self.cancelID.grid(row=0,column=1,sticky=W)



        #print(self.cancelID.get())

        

        Button(frame1, text="Search", command=self.cancelSearch).grid(row=0,column=2,sticky=W)




    # Cancel reservation2
    def cancelSearch(self): #reservation information for canceling reservation

        # Check if the reservation has alreay been cancelled

        sql0="""SELECT is_Cancelled FROM Reservation 

                WHERE Reservation_ID = %s AND Is_Cancelled = 0 AND Customer = %s"""

        db=self.Connect()

        c=db.cursor()

        c.execute(sql0,(self.cancelID.get(),self.userName))

        r = c.fetchall()

        c.close()

        if len(r) == 0:

            messagebox.showerror("No!","Invalid Reservation ID Or It has already been cancelled!")
            
            return None

        # if r[0][0] == 1:

        #     messagebox.showerror('Error!','This reservation has already been cancelled!')

        #     return None




        date_format = "%Y-%m-%d"



        # today's date in YYYY-MM-DD

        today = datetime.today()

        today = str(today)[0:10]

        #d3 = datetime.strptime(today,date_format)

        #delta = d3 - d1

        #print(delta.days) 


        c = db.cursor()

        # Get start and end dates of reservation

        sql = """SELECT Start_Date, End_Date FROM Reservation WHERE Reservation_ID = %s"""

        #c.execute(SQL)

        c.execute(sql,self.cancelID.get())

        res = c.fetchall()

        c.close()

        callback = self.checkDate(str(res[0][0]))

        if callback == 1:

            messagebox.showerror("No Way!","The reservation has passed!")

            return None


        # self.cancel2 = Toplevel(self.cancel)

        d1 = str(res[0][0])

        self.today = datetime.strptime(today,date_format)

        d = datetime.strptime(d1,date_format)

        delta = d - self.today



        self.percentage = 1

        if delta.days <= 1:

            self.percentage *= 1
            #messagebox.showerror("Impossible!","There will be No Refund!")

            #print('there will be NO REFUND')

        elif delta.days <= 3:

            self.percentage *= 0.2

            #print('There will be 80 percent REFUND')

        else:

            self.percentage *= 0

            #print('There will be 100 percent REFUND')

        frame2 = Frame(self.cancel)

        frame2.pack()

        Label(frame2,text="Start Date: ").grid(row=1,column=0,sticky=W)

        Label(frame2,text="{}".format(res[0][0])).grid(row=1,column=1,columnspan=2,sticky=W)



        Label(frame2,text="End Date: ").grid(row=1,column=3,sticky=W)

        Label(frame2,text="{}".format(res[0][1])).grid(row=1,column=4,columnspan=2,sticky=W)



        Label(frame2,text='Room Number').grid(row=2,column=0,sticky=W)

        Label(frame2,text='Room Category').grid(row=2,column=1,sticky=W)

        Label(frame2,text='#persons allowed').grid(row=2,column=2,sticky=W)

        Label(frame2,text='cost per day').grid(row=2,column=3,sticky=W)

        Label(frame2,text='cost of extra bed per day').grid(row=2,column=4,sticky=W)

        Label(frame2,text='Select Extra_Bed').grid(row=2,column=5,sticky=W)



        # Get detailed information of Reservation

        sql="""SELECT Room.Room_Num, Room_Category, num_People, Cost_per_day, Cost, has_ExtraBed

                FROM Reservation_Room JOIN Room

                ON Reservation_Room.Room_num = Room.Room_Num AND Reservation_Room.Room_Location = Room.Location

                NATURAL JOIN Reservation

                LEFT JOIN Extra_Bed on Room.Room_Num = Extra_Bed.EB_Room_num AND Room.Location = Extra_Bed.EB_Location

                WHERE Reservation_ID = %s"""



        c = db.cursor()

        c.execute(sql,self.cancelID.get())

        res = c.fetchall()

        c.close()

        db.commit()

        db.close()

        self.rowCount = 2

        self.rowCount+=1

        #print(self.res)

        self.checkbuttons=[] # for detail check

        #print(res)

        for i in range(len(res)):

            for j in range(len(res[i])-1):    

                Label(frame2,text=res[i][j]).grid(row=self.rowCount,column=j,sticky=W+E)
            
            # tmp = IntVar()

            # tmp.set(res[i][len(res[i])-1])

            # self.checkbuttons.append(tmp)



            # Checkbutton(frame3,variable=self.checkbuttons[i],onvalue=1,offvalue=0).grid(row=rowCount,column=5)
            
            tmpbutton = IntVar()
            
            tmpbutton.set(res[i][len(res[i])-1])

            self.checkbuttons.append(tmpbutton)


            Checkbutton(frame2,variable=self.checkbuttons[i],onvalue=1,offvalue=0,state='disabled').grid(row=self.rowCount,column=5)

            self.rowCount+=1

        Button(frame2,text='Refund',command=self.getRefund).grid(row=self.rowCount,column=5,sticky=W)

        self.rowCount+=1


    # Cancel Reservation 3
    def getRefund(self):

        # get previous total cost

        db = self.Connect()

        c = db.cursor()

        sql="""SELECT Total_Cost

        FROM Reservation

        WHERE Reservation_ID = %s"""

        c.execute(sql,self.cancelID.get())

        res = c.fetchall()

        c.close()

        db.commit()

        db.close()



        # GUI for Total Cost, Date of Cancellation, Refunded Amount

        cost = DoubleVar()

        cost.set(res[0][0])

        frame3 = Frame(self.cancel)

        frame3.pack()

        self.rowCount=0

        Label(frame3,text='Total Cost of Reservation').grid(row=self.rowCount,column=0,sticky=E)

        Entry(frame3,textvariable=cost,state='readonly').grid(row=self.rowCount,column=1,sticky=W+E)

        self.rowCount+=1



        Label(frame3,text='Date of Cancellation').grid(row=self.rowCount,column=0,sticky=E)

        today = StringVar()

        today.set(str(self.today)[0:10])

        Entry(frame3,textvariable=today,state='readonly').grid(row=self.rowCount,column=1,sticky=W+E)

        self.rowCount+=1



        Label(frame3,text='Amount to be refunded').grid(row=self.rowCount,column=0,sticky=E)

        refund = DoubleVar()

        refund.set(cost.get()-cost.get()*self.percentage)

        self.totalCost = cost.get() - refund.get()

        Entry(frame3,textvariable=refund).grid(row=self.rowCount,column=1,sticky=W+E)

        self.rowCount+=1



        # Direct to cancel reservation

        Button(frame3,text='Cancel Reservation',command=self.cancelRes).grid()


    # Cancel Reservation 4
    def cancelRes(self):

        # Update the flag of Reservation status

        db = self.Connect()

        c = db.cursor()

        sql="""UPDATE Reservation

            SET is_Cancelled=1, Total_Cost = %s

            WHERE Reservation_Id = %s"""

        c.execute(sql,(self.totalCost,self.cancelID.get()))

        c.close()



        # Delete the previous reserved rooms

        c = db.cursor()

        sql2 = """DELETE FROM Reservation_Room

            WHERE Reservation_ID = %s """

        c.execute(sql2,self.cancelID.get())

        c.close()

        db.commit()

        db.close()




        messagebox.showinfo("Thank you!","Reservation" + str(self.cancelID.get()) +  " is cancelled.")

        #self.cancel2.withdraw()

        self.cancel.withdraw()



    def giveReview(self):



        db=self.Connect()

        c=db.cursor()

        sql = """SELECT Rm.Room_Location FROM Reservation R

               INNER JOIN Reservation_Room Rm ON

               R.Reservation_ID = Rm.Reservation_ID WHERE Customer = %s"""

        c.execute(sql, self.userName)

        res = c.fetchall()



        cityNames = []

        for i in res:

            if i[0] not in cityNames:

                cityNames.append(i[0])



        c.close()

        db.commit()

        db.close()

        if len(cityNames) == 0:

            messagebox.showerror("Error!","Must have previous reservation to give feedback!")

            return None


        self.giveRev = Toplevel(self.master)

        self.giveRev.title("Give Review")



        Label(self.giveRev,text="Location: ").grid(row=0,column=0,sticky=W)



        self.revCity = StringVar()

        self.revCity.set(cityNames[0])

        OptionMenu(self.giveRev,self.revCity,*cityNames).grid(row=0,column=1,sticky=W)



        Label(self.giveRev,text="Rating: ").grid(row=1,column=0,sticky=W)



        self.revOption = StringVar(self.giveRev)

        self.revOption.set("Neutral")

        OptionMenu(self.giveRev,self.revOption,"Poor","Fair","Neutral","Good","Excellent").grid(row=1,column=1,sticky=W)



        Label(self.giveRev,text="Comment: ").grid(row=2,column=0,sticky=W)



        self.revComment = StringVar()

        Entry(self.giveRev, width=50, textvariable=self.revComment).grid(row=2,column=1,columnspan=3,rowspan=2,sticky=W)



        Button(self.giveRev,text="Submit",command=self.submitReview).grid(row=4,column=3,sticky=E)



    def submitReview(self):



        db=self.Connect()

        c=db.cursor()

        sql = """INSERT INTO Hotel_Review (Review_Num, Comment, Rating, Location, Author) VALUES (%s,%s,%s,%s,%s)"""

        sql2 = """SELECT COUNT(Review_Num) FROM Hotel_Review"""



        nums = c.execute(sql2)

        revNumber = c.fetchall()

        self.newRevNumber = revNumber[0][0]+1



        c.execute(sql, (self.newRevNumber,self.revComment.get(),self.revOption.get(),self.revCity.get(),self.userName))

        c.close()

        db.commit()

        db.close()

        messagebox.showinfo("Success!", "Thank you for your feedback!") ###new

        self.giveRev.withdraw() ###new



    def viewReviews(self):



        self.reviews = Toplevel(self.master)



        self.reviews.title("View Review")




        Label(self.reviews, text="Hotel Location:").grid(row=0,column=0,sticky=W)



        self.city = StringVar(self.reviews)



        self.city.set("Atlanta")



        OptionMenu(self.reviews, self.city, "Atlanta", "Boston","Chicago","Los Angeles","New York").grid(row=0,column=1,columnspan=2,sticky=W)



        self.checkRevButton = Button(self.reviews, text="Check Reviews", command=self.reviewList,state="normal")
        
        self.checkRevButton.grid(row=1,column=2,sticky=W)



    def reviewList(self):

        self.checkRevButton.config(state='disabled')
        
        db=self.Connect()

        c=db.cursor()

        sql1 = """SELECT Comment,Rating FROM Hotel_Review WHERE Location = %s"""

        c.execute(sql1, self.city.get())

        res = c.fetchall()

        c.close()

        db.commit()

        db.close()

        if len(res) == 0: #checks length of tuple, if zero then no reviews exist for that city

            messagebox.showerror('Error!', 'Sorry, no reviews exist for the selected hotel location')

            return None

        else:

            rows=0

            Label(self.reviews,text='Rating:').grid(row=0,column=0,sticky=EW)

            Label(self.reviews,text='Comment:').grid(row=0,column=1,columnspan=3,sticky=EW)

            rows+=1

            for i in res:

                comment = i[0]

                rev = i[1]

                Label(self.reviews,text=rev).grid(row=rows+3,column=0,sticky=W)

                Label(self.reviews,text=comment).grid(row=rows+3,column=1,columnspan=2,sticky=W)

                rows+=1

            Button(self.reviews,text="View Another Location",command=self.newCityHelper).grid(row=rows+3,column=1,sticky=EW)
            
            Button(self.reviews,text="Exit",command=self.exitFeedbackWin).grid(row=rows+3,column=0,sticky=EW)

    def newCityHelper(self):
        
        self.reviews.withdraw()
        
        self.viewReviews()

    def exitFeedbackWin(self):
        
        self.reviews.withdraw()

       

root=Tk()



App(root)



root.mainloop()



 



