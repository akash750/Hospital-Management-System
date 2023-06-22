import mysql.connector

passwd = str(input("ENTER THE MYSQL PASSWORD:"))

mysql = mysql.connector.connect(host = "localhost",user = "root",password = passwd,database ="hospital",auth_plugin = "mysql_native_password",)

mycursor = mysql.cursor()






#functions for the project(LOGIN),MAIN MENU

def Main_menu():
    print('''--------------------------------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
--------------------------------------------------------------------------------------------

                                 WELCOME TO COMMAND HOSPITAL

--------------------------------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
--------------------------------------------------------------------------------------------
                                            1:LOGIN

                                            2:REGISTER
         ''')
    r = int(input("ENTER YOUR CHOICE:"))

    if r == 1:
        print('''___________________________________________________________________________

                                     LOGIN YOURSELF
___________________________________________________________________________
        ''')
        Login()

    elif r == 2:
        print('''_________________________________________________________________________________________
                                        REGISTER YOURSELF
_________________________________________________________________________________________
        ''')
        Registration()
    else:
        print('''_______________________________________________________________________________________________
                                        PLEASE TRY AGAIN
_______________________________________________________________________________________________
       ''')
        Main_menu()



#function for registration

def Registration():
    us = input("ENTER USERNAME:")
    pw = input("ENTER PASSWORD(STRONG):")
    mycursor.execute("insert into User_Data values ('{}','{}')".format(us,pw,))
    mysql.commit()
    print("ADDED SUCCESSFULLY")
    Main_menu()



#function for login
def Login():
    us = input('ENTER YOUR USERNAME:')
    ps = input('ENTER YOUR PASSWORD:')
    
    mycursor.execute("select password from User_Data where Username = '{}'".format(us,))
    row = mycursor.fetchall()
    for i in row:
        a = list(i)
        if a[0] == str(ps):
            while(True):
                print('''------------------------------------------------------------------------------------
                                                   LOGGED IN SUCCESSFULLY!!!!
                --------------------------------------------------------------------------------
                ''')
                Main_page()

            else:
                print("WRONG PASSWORD OR USERNAME!!!!!!!")
                Login()





#function for the main_page
def Main_page():
    print('''


                1.ADMINISTRATION

                2.PATIENT

                3.APPOINTMENT

                4.SIGN OUT

          ''')
    a = int(input("ENTER YOUR CHOICE:"))

    if a == 1:
        Administration()

    elif a == 2:
        Patient()

    elif a == 3:
        Appointment()
        
    elif a == 4:
        Main_menu()

    else:
        print("Please Try Again!!!!!")
        Main_page()

#function for administration
def Administration():
    print('''

                1.SHOW DETAILS OF DOCTORS

                2.ADD NEW DOCTOR

                3.DELETE DATA OF DOCTOR

                4.EXIT

          ''')
    b = int(input("ENTER YOUR CHOICE:"))
    if b == 1:
            mycursor.execute("select * from doctors")
            row = mycursor.fetchall()  
            for i in row:
                v = list(i)
                k = ["NAME","SPECIALIZATION", "ROOM NO."]
                d = dict(zip(k,v))
                print(d)

    elif b == 2:
            name = input("ENTER DOCTOR NAME:")
            spe = input("ENTER SPECIALIZATION:")
            room = int(input("ENTER A ROOM NO.:"))
            mycursor.execute("select ROOM_NO from doctors")
            roomno = mycursor.fetchall()
            row=[]
            for i in roomno:
                     print(i)
                     for x in i:
                           row.append(x)
            print(row)
            if (room in row):
                    print("The room is already occupied. Please re-enter with new details.")
                    Administration()
                    
            else:
                    mycursor.execute("insert into doctors values('{}','{}','{}')".format(name,spe,room)) 
                    mysql.commit()
                    print("SUCCESSFULLY ADDED!!!!!")

    elif b == 3:
            name = input("ENTER NAME OF DOCTOR WHOSE DATA IS TO BE DELETED:")
            mycursor.execute("select NAME_OF_DOCTORS from doctors")
            row = mycursor.fetchall()
            doc = []
            for t in row:
                for x in t:
                     doc.append(x)
            if (name in doc):
                    mycursor.execute("delete from doctors where NAME_OF_DOCTORS = '{}'".format(name,))
                    mysql.commit()
                    print("----SUCCESSFULLY DELETED----")
            else:
                print("---Error! Name doesn't exist in database---")
                input("Press enter to return to Administration")
                Administration()

    elif b == 4:
        Main_page()

    else:
        print("Please Try Again!!!!")
        Administration()
    input("""             ________________________________________________________________________

                                   Press Enter to continue:
             ________________________________________________________________________""")
    Administration()
#function for patient
def Patient():
    print('''

                1.SHOW PATIENT DETAILS

                2.ADD NEW PATIENT

                3.DISCHARGE PATIENT

                4.EXIT

          ''')
    b = int(input("ENTER YOUR CHOICE:"))

    if b == 1:
        mycursor.execute("select * from Patient_details")
        row = mycursor.fetchall()
        for i in row:
                v = list(i)
                k = ["NAME","SEX","AGE","CONTACT"]
                patient_list = dict(zip(k,v)) 
                print(patient_list)

    elif b == 2:
        name = str(input("ENTER NAME:"))
        sex = str(input("ENTER SEX:"))
        age = int(input("ENTER AGE:"))
        contact = int(input("CONTACT NUMBER:"))
        mycursor.execute("insert into Patient_details values('{}','{}','{}','{}')".format(name,sex,age,contact,))
        mysql.commit()
        print('-----ADDED SUCCESSFULLY!!!!!!-----')
       

    elif b == 3:
        name = str(input("ENTER NAME:"))
        mycursor.execute("select NAME_OF_DOCTORS from doctors") #not DOCTORS, replace with PATIENT NAME, printout waale mei galti
        row = mycursor.fetchall()
        patient = []
        for t in row:
            for x in t:
                 patient.append(x)
        if (name in patient):
                mycursor.execute("delete from Patient_details where name = '{}'".format(name,))
                mysql.commit()
                print("----PATIENT SUCCESSFULLY DISCHARGED------")
        else:
            print("---Error! Name doesn't exist in database---")
            input("Press enter to return to Patient Menu")
            Patient()

    elif b==4:
        Main_page()

    else:
        print("PLEASE TRY AGAIN")
        Patient()
    input("""              ________________________________________________________________________

                                   Press Enter to continue:
            ________________________________________________________________________""")
    Patient()
    
        
   
    
#function for appointment()
def Appointment():
    mycursor.execute("select name from Patient_details")
    pat_list = mycursor.fetchall()
    print(pat_list)
    #pat_list.lower()
    ask_pat = input("Enter Patient's full name:")
    for i in pat_list:
        a = list(i)
        if a[0] == ask_pat:
              def doctorselection():
                    mycursor.execute("select distinct department from doctors")
                    row = mycursor.fetchall()
                    dep = []
                    for t in row:
                        for x in t:
                            dep.append(x)
                    print(dep)
                    ask_spe = input("Which specialist does the patient will need to see:")    
                    if (ask_spe in dep):
                            mycursor.execute("select * from doctors where department='{}'".format(ask_spe,))
                            row2 = mycursor.fetchall()
                            for j in row2:
                                    v = list(j)
                                    k = ["NAME","DEPARTMENT","ROOM NO."]
                                    patient_spe = dict(zip(k,v)) 
                                    print(patient_spe)
                            ask_doc = input("Enter Doctor's name:")
                            mycursor.execute("select name_of_doctors from doctors where department='{}'".format(ask_spe,))
                            docname = list(mycursor.fetchall())
                            doc = []
                            for i in docname:
                                for x in i:
                                    doc.append(x)
                            print(doc)
                            if (ask_doc in doc):                              
                                        print('''You have succesfully chosen your doctor.''')
                                        mycursor.execute("select room_no from doctors where name_of_doctors='{}'".format(ask_doc,))
                                        room = list(mycursor.fetchone())[0]
                                        print('Your appointment with', ask_doc, 'is set in room number',room,'.')
                                        print('Please provide the following details now')
                                        appointment_date()
                            else:
                                        print('''---------------The Doctor's name did not match in our database-----------
                    -------------------------Please try again------------------------''')
                                        doctorselection()
                    else:
                            print("ERROR!!!. Please Try Again")
                            doctorselection()
              def appointment_date():
                           print("Choose date for appointment:")
                           year = int(input("Enter year:"))
                           month = int(input("Enter month:"))
                           date = int(input("Enter date of the month:"))
                           time = input("Enter time in hh:mm:ss (24 hour format):")
                           
                           if date <32 or month <=12:
                                   app_date = str(year) + '-' + str(month) + '-' + str(date)
                                   mycursor.execute("insert into appointment values('{}','{}')".format(app_date, time))
                                   print("Appointment set succesfully on",date, "-", month, "-", year, "at", time,)
                                   mysql.commit()
                                   input("Press enter to go main page.")
                                   Main_page()
                           else:
                                   print("Enter valid date")
                                   appointment_date()
              doctorselection()
    else:
           print("Name does not match in the records. Please try again.")
           Appointment()
                        
                    
                        
                        
                    
        


Main_menu()
            
    
    



            
