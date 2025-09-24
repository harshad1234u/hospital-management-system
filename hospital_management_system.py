@app.function(
    image=modal.Image.debian_slim()
        .pip_install(["mysql.connector","time","datetime","tabulate"]),
    gpu="A10G",
    timeout=300, # 5m
)
import mysql.connector as ms
import random
import time 
import datetime
from tabulate import tabulate
x=ms.connect(host='localhost',user='root',passwd='root')
def create_cursor():
    cur=x.cursor(buffered=True)
def current_time():
    currentDT = datetime.datetime.now()
    print (' '*130+str(currentDT))
def sign_in(user,passwd):
    create_cursor()
    cur.execute("select exists (select * from user where  user='{}' and passwd='{}')".format(user,passwd))
    data=cur.fetchone()
    if data[0]==1:
        print('sucessfully sign in ')
    else:
        print('invalid user or password')
        print('please sign up first')
def new():
    print('='*50)
def loading():
    try:
        print('loading..',end='')
        time.sleep(0.3)
        print('..',end='')
        time.sleep(0.3)
        print('..')
    except:
        print('loading....')
def sign_up():
    global ans
    uid=random.randint(0,10000)
    if uid not in l:
        l.append(uid)
    else:
        uid=random.randint(0,10000)
        print('#'*20,'WELCOME TO XYZ',"#"*20)
        print()
        user=input('user name         :: ')
        passwd=input(user+' password  :: ')
        create_cursor()
        cur.execute('insert into user values ({},"{}","{}")'.format(uid,user,passwd))
        x.commit()
        print('')
        print(10*'#',
              '''user profile is created sucessfull''',10*"#")
        print('user ->',user)
        print('password ->',"*"*len(passwd))
        sign_in(user,passwd)
        ans='n'
a='y'
while a=='y':
    print('-_'*50)
    print('-_'*20,'XYZ HOSTPITAL','-_'*20)
    print('-_'*50)
    print('')
    s=input('ENTER THE DATABASE PASSWORD :: ')
    current_time()
    if s.lower()=='admin':
        if x.is_connected():
            print()
            cur =x.cursor()
            cur.execute("create database if not exists hospitalmanagement2024")
            cur.execute("use hospitalmanagement2024")
            cur.execute('''
                            create table if not exists user 
                            (
                                 u_id int not null primary key,
                                user varchar(30 ),
                                passwd varchar(20)
                            )
                        ''')
            cur.execute('''
                            create table if not exists room 
                            ( 
                                room_number varchar(10) not null primary key,
                                room_type varchar(30),
                                feeperday int
                             ) 
                        ''')
            cur.execute('''
                            create table if not exists nurse 
                            ( 
                                n_id varchar(10) not null primary key , 
                                first_name  varchar(40) , 
                                last_name  varchar(40),
                                phonenumber int(12),
                                age int, 
                                gender char(3), 
                                qualifation varchar(20), 
                                date_of_joining varchar(20), 
                                experience int ,  
                                salary int, 
                                email varchar(40), 
                                address varchar(40)
                            )
                        ''')
            cur.execute('''
                            create table if not exists doctor 
                            ( 
                                d_id varchar(10) primary key , 
                                first_name varchar(40) ,
                                last_name varchar(40), 
                                phonenumber int(12), 
                                Qualification varchar(40),
                                date_of_joining varchar(10), 
                                specialist varchar(30), 
                                age int ,
                                fee int, 
                                experience int, 
                                salary int, 
                                email varchar(40), 
                                address varchar(40)
                            )
                        ''')
            cur.execute('''
                            CREATE TABLE if not exists Patient 
                            (
                                PID varchar(20) not null,
                                FName VARCHAR(30),
                                LName varchar(30),
                                Age INT,
                                Gender CHAR(1) check( gender in('f','m') ),
                                ContactNumber VARCHAR(15),
                                Address VARCHAR(40),
                                currentroom varchar(10),
                                PRIMARY KEY (PID),
                                foreign key (currentroom) references room(room_number)
                            )
                            '''  )
            cur.execute('''
                        CREATE TABLE if not exists Billinfo
                        (
                            BID CHAR(5) PRIMARY KEY,
                            PID varchar(20) not null,
                            TotalAmount DECIMAL(10, 2),
                            PaymentStatus VARCHAR(50),
                            BillingDate DATE,
                            FOREIGN KEY (PID) REFERENCES Patient(PID)
                        )
                        ''') 
            cur.execute('''
                        CREATE TABLE IF NOT EXISTS lab_tests 
                        (
                            test_id char(6) PRIMARY KEY,
                            test_name VARCHAR(40),
                            pid varchar(20),
                            patient_fname VARCHAR(40) ,
                            patient_lname VARCHAR(40) ,
                            result VARCHAR(40),
                            FOREIGN KEY (PID) REFERENCES Patient (PID)
                        )
                        ''')
            cur.execute('''
                        create table if not exists Appointments
                        (
                            AID char(8) primary key,
                            PID varchar(20) not null,
                            did varchar(10) not null,
                            app_date date,
                            app_time varchar(10),
                            FOREIGN KEY (PID) REFERENCES Patient(PID),
                            FOREIGN KEY (did) REFERENCES Doctor(D_ID)
                        )
                        ''')
            print('database is connected sucessfully')
            l=u=[]
            ans='y'
            while ans=='y':
                print('press 1 - "SIGN IN"')
                print('press 2 - "SIGN UP"')
                ch=int(input('ENTER YOUR CHOICE :: '))
                current_time()
                if ch==1 or ch==2:
                    while ans=='y':
                        if ch==2:
                            sign_up()
                            if ans=='n':
                                print('#'*20,'WELCOME BACK TO XYZ',"#"*20)
                                u=input('user name      :: ')
                                p=input(u+' password  :: ')
                                sign_in(u,p)
                                ans='n'
                                break
                            else:
                                ans="y"
                        elif ch==1:
                            print('#'*20,'WELCOME BACK TO XYZ',"#"*20)
                            u=input('user name      :: ')
                            p=input(u+' password  :: ')
                            sign_in(u,p)
                            ans='n'
                            break
                else:
                    print('invalid  choice')
                    ans=input('do you want to continue press - "y"and to no press - "N"')
            ans='y'
            while ans=='y':
                print("-_"*20,' MENU','_-'*20)
                print("press -1 ADMINISTRATION")
                time.sleep(0.3)
                print('press -2 PATIENT DETAIL AND TEST REPORT')
                time.sleep(0.3)
                print('press -3 ABOUT XYZ HOSPITAL')
                time.sleep(0.3)
                print('press -4 SIGN OUT ')
                time.sleep(0.3)
                ch=int(input('ENTER YOUR CHOICE  ::'))
                current_time()
                new()
                if ch==1:
                    while True:
                        print('press -1 STAFF MANAGEMENT')
                        time.sleep(0.3)
                        print('press -2 ROOM MANAGEMENT')
                        time.sleep(0.3)
                        print('press -3 TO GO BACK')
                        time.sleep(0.3)
                        s=int(input('ENTER YOUR CHOICE :: '))
                        current_time()
                        new()
                        if s==1:
                            while True:
                                print("press -1 ADD NEW MEMBER")
                                time.sleep(0.3)
                                print("press -2 SHOW DETAILS")
                                time.sleep(0.3)
                                print("press -3 DELETE THE EXISTING ONE")
                                time.sleep(0.3)
                                print("press -4 TO GO MENU")
                                time.sleep(0.3)
                                ch1=int(input('enter your chocie :: '))
                                current_time()
                                new()
                                if ch1==2:
                                    while True:
                                        print('who detail you want ')
                                        print('press 1 - DOCTOR')
                                        time.sleep(0.3)
                                        print('press 2 - NUSERS')
                                        time.sleep(0.3)
                                        print('press 3 - TO GO BACK')
                                        time.sleep(0.3)
                                        ch2=int(input('ENTER YOUR CHOICE :: '))
                                        current_time()
                                        new()
                                        loading()
                                        new()
                                        if ch2==1:
                                            while True:
                                                print('press -1 SPECIFIC DOCTOR DETAIL')
                                                time.sleep(0.3)
                                                print('press -2 ALL DOCTOR DETAIL ')
                                                time.sleep(0.3)
                                                print('press -3 TO GO BACK')
                                                time.sleep(0.3)
                                                ch3=int(input('ENTER YOUR CHOICE :: '))
                                                current_time()
                                                new()
                                                loading()
                                                new()
                                                if ch3==1:
                                                    create_cursor()
                                                    doc=input('ENTER DOCTOR FIRST NAME :: ')
                                                    cur.execute("select exists (select * from doctor where  first_name='{}')".format(doc))
                                                    data=cur.fetchone()
                                                    new()
                                                    loading()
                                                    new()
                                                    if data[0]==1:
                                                        cur.execute("select * from doctor where first_name='{}'".format(doc))
                                                        data=cur.fetchall()
                                                        h=[ 'doctor_id','first_name','last_name', 'phonenumber','qualifiaction','date_of_join','specialist','age',' fees', 'experience', 'salary' ,'email ',' address' ]
                                                        print(tabulate (data ,headers=h ,tablefmt='psql'))
                                                        new()
                                                    else:
                                                        print('doctor not found !!!!!')
                                                elif ch3==2:
                                                    create_cursor()
                                                    cur.execute('select * from doctor')
                                                    data=cur.fetchall()
                                                    h=[ 'doctor_id','first_name','last_name', 'phonenumber','qualifiaction','date_of_join','specialist','age',' fees', 'experience', 'salary' ,'email ',' address' ]
                                                    print(tabulate (data ,headers=h ,tablefmt='psql'))
                                                    new()
                                                elif ch3==3:
                                                    new()
                                                    break
                                                else:
                                                    print("invalid choice")
                                                    time.sleep(0.3)
                                                    new()
                                        elif ch2==2:
                                            while True:
                                                print('press -1 SPECIFIC NURSE DETAIL')
                                                time.sleep(0.3)
                                                print('press -2 NURSE DETAIL ')
                                                time.sleep(0.3)
                                                print('press -3 TO GO BACK')
                                                time.sleep(0.3)
                                                ch3=int(input('ENTER YOUR CHOICE  :: '))
                                                new()
                                                if ch3==1:
                                                    new()
                                                    loading()
                                                    new()
                                                    create_cursor()
                                                    name=input('ENTER NURSE FIRST NAME :: ')
                                                    cur.execute("select exists (select * from nurse where  first_name=\'"+name+"\')")
                                                    data=cur.fetchone()
                                                    if data[0]==1:
                                                        cur.execute('select * from nurse where  first_name="{}"'.format(name))
                                                        data=cur.fetchall()
                                                        h=[ 'nurse_id','first_name','last_name','phonenuber','age','gender','qualifiaction','date_of_join','experience', 'salary' ,'email ',' address' ]
                                                        print(tabulate (data ,headers=h ,tablefmt='psql'))
                                                    else:
                                                        print('NURSE NOT FOUND !!!')
                                                elif ch3==2:
                                                    new()
                                                    loading()
                                                    new()
                                                    create_cursor()
                                                    cur.execute('select * from nurse')
                                                    data=cur.fetchall()
                                                    h=[ 'nurse_id','first_name','last_name','phonenuber','age','gender','qualifiaction','date_of_join','experience', 'salary' ,'email ',' address' ]
                                                    print(tabulate (data ,headers=h ,tablefmt='psql'))
                                                elif ch3==3:
                                                    new()
                                                    loading()
                                                    new()
                                                    break  
                                                else:
                                                    print("INVALID INPUT TRY AGAIN")
                                                    new()
                                                    loading()
                                                    new()
                                        elif ch2==3:
                                            new()
                                            loading()
                                            new()
                                            break
                                elif ch1==1:
                                    while True:
                                        print('press -1 TO ADD NEW DOCTOR')
                                        time.sleep(0.3)
                                        print('press -2 TO ADD NEW NURSE')
                                        time.sleep(0.3)
                                        print("press -3 EXITS")
                                        time.sleep(0.3)
                                        ch2=int(input('ENTER YOUR CHOICE :: '))
                                        current_time()
                                        new()
                                        if ch2==1:
                                            create_cursor()
                                            loading()
                                            new()
                                            fname=input('ENTER THE DOCTOR FIRST NAME :: ')
                                            lname=input('ENTER THE DOCTOR LAST NAME :: ')
                                            ph=int(input('ENTER THE PHONE NUMBER  :: '))
                                            sp=input('ENTER THE JOIN DATE (YYYY-MM-DD)')
                                            q=input('ENTER QUALIFICATION :: ')
                                            specialist=input('ENTER SPECIALISATION :: ')
                                            age=int(input('ENTER '+fname.upper()+' AGE :: '))
                                            experience=input(('ENTER '+fname.upper()+' EXPERIENCE :: ' ))
                                            fee=int(input('ENTER FEE ::'))
                                            if int(fee ) > 5000:
                                                print('fee should be BELOW 5000 !!!!')
                                                fee=int(input('ENTER FEE :: '))
                                            salary=int(input('ENTER SALARY OF '+fname+' ::'))
                                            Add=input('ENTER ADDRESS  OF '+fname +' ::')
                                            email=input('ENTER E-MAIL ID')
                                            d=random.randint(100,999)
                                            did="d"+str(d)
                                            a='insert into DOCTOR values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '
                                            values=[did ,fname,lname,ph,q,sp,specialist,age,fee,experience,salary,email,Add]
                                            try:
                                                cur.execute(a,values)
                                                x.commit()
                                                print('DATA ADDDED SUCESSFULLY')
                                                new()
                                            except:
                                                print('!!!! DATA NOT ADDED !!!!!')
                                                x.rollback()
                                                new()
                                                loading()
                                                
                                                new()
                                        elif ch2==2:
                                            loading
                                            new()
                                            create_cursor()
                                            n=random.randint(100,9999)
                                            nid='n'+str(n)
                                            fname=input('ENTER THE NURSE FIRST NAME :: ')
                                            lname=input('ENTER THE NURSE LAST NAME :: ')
                                            age= int(input('ENTER '+fname.upper()+' AGE :: '))
                                            gender=input('ENTER '+fname.upper()+' GENDER :: ')
                                            ph=int(input('ENTER THE PHONE NUMBER  :: '))
                                            qua=input('ENTER THE QUALIFICATION :: ')
                                            sp=input('ENTER THE JOIN DATE (YYYY-MM-DD) :: ')         
                                            exp=input('ENTER EXPERIENCE :: ')
                                            salary=int(input('ENTER SALARY :: '))
                                            email=input('ENTER E-MAIL ID :: ')
                                            add=input('ENTER ADDRESS :: ')
                                            a='insert into nurse values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                                            values=[nid,fname,lname,ph,age,gender,qua,sp,exp,salary,email,add]
                                            try:
                                                cur.execute(a,values)
                                                x.commit()
                                                print('DATA ADDED SUCESSFULLY')
                                                new()
                                                loading()
                                                new()
                                            except:
                                                print('!!!! DATA NOT ADDED !!!!!')
                                                x.rollback()
                                                new()
                                                loading()
                                                new()
                                        elif ch2==3:
                                            new()
                                            loading()
                                            new()
                                            break
                                        else:
                                            print('INVALID INPUT')
                                            new()
                                            loading()
                                            new()
                                elif ch1==3:
                                    while True:
                                        loading()
                                        new()
                                        print('press -1 DELETE DOCTOR DETAIL')
                                        time.sleep(0.3)
                                        print('press -2 DELETE NURSE DETAIL')
                                        time.sleep(0.3)
                                        print('press -3 GO TO BACK')
                                        time.sleep(0.3)
                                        ch2=int(input('ENTER YOUR CHOICE :: '))
                                        current_time()
                                        new()
                                        if ch2==1:
                                                create_cursor()
                                                name = input("Enter Doctor's First Name :: ")
                                                cur.execute("select * from doctor where first_name='" + name + "'")
                                                data=cur.fetchall()
                                                h=[ 'doctor_id','first_name','last_name', 'phonenumber','qualifiaction','date_of_join','specialist','age',' fees', 'experience', 'salary' ,'email ',' address' ]
                                                print(tabulate (data ,headers=h ,tablefmt='psql'))
                                                p = input("you really wanna delete this data? (y/n):")
                                                if p == "y":
                                                    cur.execute("delete from doctor where first_name=\'" + name + "\'")
                                                    x.commit()
                                                    print("SUCCESSFULLY DELETED")
                                                else:
                                                    print("!!! NOT DELETED !!!")
                                        elif ch2==2:
                                            create_cursor()
                                            name = input("Enter Nurse's Name :: ")
                                            cur.execute("select * from nurse where first_name='" + name + "'")
                                            row = cur.fetchall()
                                            h=[ 'doctor_id','first_name','last_name', 'phonenumber','qualifiaction','date_of_join','specialist','age',' fees', 'experience', 'salary' ,'email ',' address' ]
                                            print(tabulate (row ,headers=h ,tablefmt='psql'))
                                            p = input("you really wanna delete this data? (y/n):".upper())
                                            if p == "y":
                                                try:
                                                    cur.execute("delete from nurse where first_name=\'" + name + "\'")
                                                    x.commit()
                                                    print("SUCCESSFULLY DELETED!!")
                                                except:
                                                    x.rollback()
                                                    print('THERE IS ERROR FOUND IN PROCESSING')
                                            else:
                                                print("NOT DELETED")
                                        elif ch2==3:
                                            new()
                                            loading()
                                            new()
                                            break
                                        else:
                                            print('!!!!  INVALID INPUT !!!!!!')  
                                elif ch1==4:
                                    new()
                                    loading()
                                    new()
                                    break    
                                else:
                                    new()
                                    print('!!!!  INVALID INPUT !!!!!!')
                                    loading()
                                    new()
                        elif s==2:
                            while True:
                                print('press -1 ADD NEW ROOM')
                                time.sleep(0.3)
                                print('press -2 VIEW ROOMS AS PER ROOM TYPE ')
                                time.sleep(0.3)
                                print('press -3 EDIT ROOM TYPE AND COST OF ROOM')
                                time.sleep(0.3)
                                print('press -4 DELETE ROOM')
                                time.sleep(0.3)
                                print('press -5 TO GO BACK')
                                time.sleep(0.3)
                                ch1=int(input('ENTER YOUR CHOICE :: '))
                                current_time()
                                new()
                                loading()
                                new()
                                if ch1==1:
                                    print('#'*50)
                                    print(' WELCOME TO ROOM MANAGMENT ')
                                    print('#'*50)
                                    print('ENTER ROOM DETAIL ')
                                    print('#'*50)
                                    roomno=int(input('ENTER ROOM NUMBER :: '))
                                    roomc=input('ENTER ROOM TYPE :: ')
                                    cost=int(input('ENTER COST OF PERDAY :: '))
                                    create_cursor()
                                    a='insert into room values (%s,%s,%s)'
                                    values=[roomno,roomc,cost]
                                    cur.execute(a,values)
                                    x.commit()
                                    print('data added sucessfully')
                                    new()
                                    loading()
                                    new()                           
                                elif ch1==2:
                                    c=input('ENTER ROOM_TYPE TO VIEW ROOM  :: ')
                                    create_cursor()
                                    a='select * from room where room_type=\"'+c+'\"'
                                    try:
                                        cur.execute(a)
                                        data=cur.fetchall()
                                        h=[ 'room_number','room_type','feeperday']
                                        print(tabulate (data ,headers=h ,tablefmt='psql'))
                                    except:
                                        print('!!! ERROR IN PROCESSING THE DATA !!!')
                                        x.rollback()
                                elif ch1==3:
                                    new()
                                    loading()
                                    new()
                                    create_cursor()
                                    roomno=input('ENTER THE ROOM NUMBER ')
                                    cur.execute('select * from room where room_number ='+ roomno + ' ')
                                    data=cur.fetchall()
                                    h=[ 'room_number','room_type','feeperday']
                                    print(tabulate (data ,headers=h ,tablefmt='psql'))
                                    p=input('you really wanna update the room type this data? (y/n)::')
                                    if p=='y':
                                        print('press -1 FOR UPDATE ROOM TYPE')
                                        print('press -2 TO MOVE ON ')
                                        d=int(input('ENTER YOUR CHOICE : '))
                                        if d==1:
                                            room_type=input('ENTER UPDATED TYPE OF ROOM ')
                                            i="update room set room_type=%s where room_number=%s"
                                            j=(room_type,roomno )
                                            try:
                                                cur.execute(i,j)
                                                x.commit()
                                                new()
                                                loading()
                                                new()
                                                print('UPDATE SUCCESSFULLY COMPLETED')
                                            except:
                                                new()
                                                loading()
                                                new()
                                                print("ERROR OCCURED")
                                                x.rollback()
                                        print('press -1 TO UPDATE ROOM COST')
                                        print('press -2 TO MOVE ON')
                                        e=int(input('ENTER YOUR CHOICE :: '))
                                        if e==1:
                                            cost=int(input('ENTER  UPDATED ROOM COST/PERDAY :: '))
                                            k="update room set feeperday=%s where room_number=%s "
                                            l=(cost,roomno)

                                            try:
                                                cur.execute(k,l)
                                                x.commit()
                                                new()
                                                loading()
                                                new()
                                                print('VALUE UPDATED ')
                                            except:
                                                new()
                                                loading()
                                                new()
                                                print("ERROR OCCURED")
                                                x.rollback()
                                    else:
                                        new()
                                        loading()
                                        new()
                                        print('!!! NOT UPDATE !!!')
                                elif ch1==4:
                                    new()
                                    loading()
                                    new()
                                    roomno=input('ENTER ROOM NUMBER :: ')
                                    cur.execute('select * from room where room_number ='+ roomno + ' ')
                                    data=cur.fetchall()
                                    h=[ 'room_number','room_type','feeperday']
                                    print(tabulate (data ,headers=h ,tablefmt='psql'))
                                    p=input('you really wanna delete room number this data? (y/n)::')
                                    if p=='y'.lower():
                                        try:
                                            cur.execute('delete from room where room_number='+roomno+'')
                                            x.commit()
                                            new()
                                            print('loading..',end='')
                                            
                                            print('..',end='')
                                            
                                            print('..')
                                            new()
                                            print('')
                                            print("SUCCESSFULLY DELETED!!")
                                        except:
                                                new()
                                                loading()
                                                new()
                                                print('!!! NOT DELETED !!!')
                                    else:
                                        print('!!! NOT DELETED !!!')
                                elif ch1==5:
                                    new()
                                    loading()
                                    new()
                                    break
                                else:
                                    print('!!! INVALID INPUT !!! ')
                        elif s==3:
                            new()
                            loading()
                            new()
                            break
                        else:
                            print('!!! INVALID INPUT !!!')
                            new()
                            loading()
                            new()
                elif ch==2:
                    while True:
                        new()
                        print('_-'*20,'-WEL COME TO PATIENT MANAGEMENT','_-'*20)
                        time.sleep(0.3)
                        print('press-1 ADD NEW PATIENT')
                        time.sleep(0.3)
                        print('press-2 TO MODIFY PATIENT DETAIL ')
                        time.sleep(0.3)
                        print('press-3 VIEW PATIENT')
                        time.sleep(0.3)
                        print('press-4 BILL MANAGEMENT')
                        time.sleep(0.3)
                        print('press-5 APPOINTMENT MANAGEMENT')
                        time.sleep(0.3)
                        print('press-6 LABORATORY MANAGEMENT ') 
                        time.sleep(0.3)
                        print('press-7 DELETE PATIENT DETAIL ')
                        time.sleep(0.3)
                        print('press-8 GO TO BACK')
                        time.sleep(0.3)
                        ch1=int(input('ENTER YOUR CHOICE :: '))
                        current_time()
                        new() 
                        loading()                                                 
                        new()
                        if ch1==1:
                            create_cursor()
                            pid=random.randint(100,999)
                            p='p'+str(pid)
                            FName=input('ENTER THE FIRST NAME :: ')
                            LName=input('ENTER THE LAST NAME  :: ')
                            Age=int(input('ENTER THE AGE      :: '))
                            gender=input('ENTER THE GENDER OF PATIENT :: ')
                            ContactNumber=int(input('ENTER THE PATIENT CONTACT NUMBER :: '))
                            Address=input('ENTER THE ADDRESS OF PATIENT :: ')
                            print('     ROOM IS YOU IS ALOCATED    ')
                            r=input('ENTER Y/N ? :::')
                            if r.upper()=='Y':
                                RoomNo=input("Enter The Room Number ")
                                value=[p,FName,LName,Age,gender,ContactNumber,Address,RoomNo]
                                query='''
                                INSERT INTO patient VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
                                '''
                                cur.execute(query,value)
                                x.commit()
                                print('DATA ADDED SUCESSFULLY')
                                try:
                                    cur.execute(query,value)
                                    x.commit()
                                except:
                                    x.rollback()
                            else:
                                value=[p,FName,LName,Age,gender,ContactNumber,Address]
                                query='''
                                INSERT INTO patient(pid,fname,lname,age,gender,contactnumber,address) VALUES(%s,%s,%s,%s,%s,%s,%s)
                                '''
                                cur.execute(query,value)
                                x.commit()
                                print('DATA ADDED SUCESSFULLY')
                                try:
                                    cur.execute(query,value)
                                    x.commit()                                
                                except:
                                    x.rollback()  
                        elif ch1==2:
                            create_cursor()
                            Fname = input("ENTER THE PATIENT FIRST NAME :: ")
                            Lname = input("ENTER THE PATIENT LAST NAME :: ")
                            cur.execute("select * from patient where Fname=\'"+Fname+"\' AND Lname =\'"+Lname+"\'")
                            row = cur.fetchall()
                            h=[ 'Patient_id','first_name','last_name','age','gender','phonenumber',' address','current_room' ]
                            print(tabulate (row ,headers=h ,tablefmt='psql'))
                            create_cursor()
                            cur.execute("select exists (select * from patient where Fname=\'"+Fname+"\' AND Lname =\'"+Lname+"\')")  
                            data=cur.fetchone()
                            print(data)
                            if data[0]==1:
                                print('press-1 TO CHANGE AGE')
                                print('press-2 TO MOVE ON')
                                ch2=int(input('ENTER YOUR CHOICE :: '))
                                if ch2==1:
                                    create_cursor()
                                    Age=int(input('ENTER THE NEW AGE :: '))
                                    query="""
                                    UPDATE Patient SET Age=%s WHERE FName=%s AND LName=%s
                                    """
                                    value=[Age,Fname,Lname]
                                    try:
                                        cur.execute(query,value)
                                        x.commit()
                                    except:
                                        x.rollback()
                                        new()
                                elif ch2==2:
                                    pass
                                else:
                                    print('INVALID CHOICE')
                                    new()
                                print('press-1 TO CHANGE CONTACTNUMBER')
                                print('press-2 TO MOVE ON')
                                ch2=int(input('ENTER YOUR CHOICE :: '))
                                if ch2==1:
                                    ContactNumber=int(input('ENTER THE PATIENT CONTACT NUMBER :: '))
                                    query="""
                                    UPDATE Patient SET ContactNumber=%s WHERE FName=%s AND LName=%s
                                    """
                                    value=[ContactNumber,Fname,Lname]
                                    try:
                                        cur.execute(query,value)
                                        x.commit()
                                    except:
                                        x.rollback()
                                        new()
                                elif ch2==2:
                                    pass
                                else:
                                    print('INVALID CHOICE')
                                    new()
                                print('press-1 TO CHANGE ADDRESS')
                                print('press-2 TO MOVE ON')
                                ch2=int(input('ENTER YOUR CHOICE :: '))
                                if ch2==1:
                                    Address=input('ENTER THE NEW ADDRESS :: ')
                                    query="""
                                    UPDATE Patient SET Address=%s WHERE FName=%s AND LName=%s
                                    """
                                    value=[Address,Fname,Lname]
                                    try:
                                        cur.execute(query,value)
                                        x.commit()
                                    except:
                                        x.rollback()
                                        new()
                                elif ch2==2:
                                    pass
                                else:
                                    print('INVALID CHOICE')
                                    new()
                                print('press-1 TO CHANGE CURRENTROOM')
                                print('press-2 TO MOVE ON')
                                ch2=int(input('ENTER YOUR CHOICE :: '))
                                if ch2==1:
                                    CurrentRoom=input('ENTER THE NEW CURRENT ROOM ::')
                                    query="""
                                    UPDATE Patient SET CurrentRoom=%s WHERE FName=%s AND LName=%s
                                    """
                                    value=[CurrentRoom,Fname,Lname]
                                    try:
                                        cur.execute(query,value)
                                        x.commit()
                                    except:
                                        x.rollback()
                                        new()
                                elif ch2==2:
                                    pass
                                else:
                                    print('INVALID CHOICE')
                                    new()
                            else:
                                print('!!! NOT FOUND !!!') 
                            print('PATIENT  DETAIL UPDATED SUCESSFULLY')
                            create_cursor()
                            cur.execute("select * from patient where Fname=\'"+Fname+"\' AND Lname =\'"+Lname+"\'")
                            row = cur.fetchall()
                            h=[ 'Patient_id','first_name','last_name','age','gender','phonenumber',' address','current_room' ]
                            print(tabulate (row ,headers=h ,tablefmt='psql'))
                        elif ch1==7:        
                            Fname = input("ENTER THE PATIENT FIRST NAME :: ")
                            Lname = input("ENTER THE PATIENT LAST NAME :: ")
                            try:
                                create_cursor()
                                cur.execute("select * from patient where Fname=\'"+Fname+"\' AND Lname =\'"+Lname+"\'")
                                row = cur.fetchall()
                                h=[ 'Patient_id','first_name','last_name','age','gender','phonenumber',' address','current_room' ]
                                print(tabulate (row ,headers=h ,tablefmt='psql'))
                            except:
                                x.rollback()
                                new()
                            p = input("you really wanna delete this data? (y/n):")
                            if p == "y":
                                try:
                                    cur.execute("delete from patient where Fname=\'"+Fname+"\' AND Lname =\'"+Lname+"\'")
                                    x.commit()
                                    print("SUCCESSFULLY DELETED!!")
                                except:
                                    x.rollback()
                                    new()
                                else:
                                    new()
                            else:
                                print("NOT DELETED")                      
                        elif ch1==4:
                            while True:
                                print('press-1 TO ADD NEW PATIENT BILL')
                                time.sleep(0.3)
                                print('press-2 TO VIEW ALL PATIENTS BILLS')
                                time.sleep(0.3)
                                print('press-3 TO UPDATE PATIENT BILL STATUS')
                                time.sleep(0.3)
                                print('press-4 TO GO BACK')
                                time.sleep(0.3)
                                ch6=int(input('ENTER YOUR CHOICE :: ' ))
                                current_time()
                                new()
                                loading()
                                new()     
                                if ch6==1:
                                    create_cursor()
                                    bill=random.randint(100,999)
                                    BILLID='B'+str(bill)
                                    pname=input('ENTER THE PATIENT FIRST NAME  :: ')
                                    TotalAmount=int(input('ENTER TOTAL BILL AMOUNT :: '))
                                    PaymentStatus=input('ENTER THE PAYMENT STATUS (PAID/NOT) :: ')
                                    BILLLINGDATE=input('ENTER DATE OF BILL PAID :: ')
                                    try:
                                        cur.execute("Select pid from patient where FName = '{}'".format(pname))    
                                        p=cur.fetchone()
                                        for i in p:
                                            pid=i
                                            break
                                        if pid==' ':
                                            print('!!!PATIENT NOT ERROR!!!!!')
                                    except:
                                        x.rollback()
                                        print('!! error !!')
                                    create_cursor()
                                    query2='insert into billinfo values (%s,%s,%s,%s,%s)'
                                    value=(BILLID,pid,TotalAmount,PaymentStatus,BILLLINGDATE)
                                    cur.execute(query2,value)
                                    x.commit()      
                                    try:
                                        create_cursor()
                                        query2='insert into billinfo values (%s,%s,%s,%s,%s)'
                                        value=(BILLID,pid,TotalAmount,PaymentStatus,BILLLINGDATE)
                                        cur.execute(query2,value)
                                        x.commit()
                                        print('DATA ADDED SUCESSFULLY')
                                        new()
                                        loading()
                                        new()  
                                    except:
                                        x.rollback()
                                        new()
                                        loading()
                                        new()  
                                elif ch6==2:
                                    create_cursor()
                                    cur.execute('select * from billinfo')
                                    rows=cur.fetchall()
                                    if len(rows)!=0:
                                        h=[ 'bill_id','patient_id','total_amount','Payment_status','bill_date']
                                        print(tabulate(rows,headers=h ,tablefmt='psql'))
                                    new()
                                    print('loading..',end='')
                                    
                                    print('..',end='')
                                    
                                    print('...')
                                    
                                    new()  
                                elif ch6==3:
                                    create_cursor()
                                    pname=input('ENTER THE PATIENT NAME  :: ')
                                    cur.execute("Select pid from patient where FName = '{}'".format(pname))
                                    p=cur.fetchone()
                                    for i in p:
                                        pid=i
                                        break
                                    create_cursor()
                                    #cur.execute("select exists (select * from billinfo where PID ="+ pid +" OR paymentstatus = 'notpaid' )")
                                    cur.execute("select * from billinfo where paymentstatus = 'notpaid' ")
                                    data=cur.fetchall()
                                    for i in data:
                                        if pid == i[1]:
                                            data=1,
                                            break
                                    if data[0]==1:
                                        print('PATIENT BILL  FOUND AS NOT PAID')
                                        print('NOW PATIENT BILL IS UPDATE AS PAID')
                                        create_cursor()
                                        cur.execute('select bid,pid from billinfo')
                                        bd=cur.fetchall()
                                        for i in bd:
                                            if pid==i[1]:
                                                bid=i[0]
                                                break
                                        u="update billinfo set PaymentStatus='PAID' where  pid=\'"+pid+"\'"
                                        cur.execute(u)
                                        x.commit()
                                    else:
                                        print('PATIENT BILL ALREADY MARKED AS PAID')
                                    new()
                                    loading()
                                    new()
                                elif ch6==4:
                                    new()
                                    print('loading..',end='')
                                    
                                    print('..',end='')
                                    
                                    print('...')
                                    
                                    new()
                                    break
                                else:
                                    print('INVALID CHOICE ')
                                    new()
                                    loading()
                                    new()
                        elif ch1==5:
                            while True:
                                print('press-1 FOR NEW APPOINTMENT')
                                print('press-2 FOR CANCEL APPOINTMENT')
                                print('press-3 FOR CHECK APPOINTMENT')
                                print('press-4 GO BACK')
                                ch2=int(input('ENTER YOUR CHOICE :: '))
                                current_time()
                                new()
                                print('loading.....')
                                new()
                                if ch2==1:
                                    create_cursor()
                                    pname=input('ENTER THE PATIENT FIRSTNAME  :: ')
                                    dname=input('ENTER THE DOCTOR NAME :: ')
                                    date=input('ENTER THE APPOINTMENT DATE :: ')
                                    time=input('ENTER THE APPOINTMENT TIME :: ')
                                    app=random.randint(100,999)
                                    appid='A'+str(app)
                                    create_cursor()
                                    query='Select pid,fname from patient'
                                    query2='Select D_id,first_name from DOCTOR '
                                    query3="select d_id from doctor where FIRST_name = \'"+dname+"\'"
                                    try:
                                        cur.execute(query)
                                        data=cur.fetchall()
                                        for i in data:
                                            if i[1]==pname:
                                                pid=i[0]
                                    except:
                                        x.rollback()
                                        print('PATIENT NOT FOUND')
                                    cur.execute(query3)
                                    data=cur.fetchone()
                                    print(data)
                                    try:
                                        cur.execute(query3)
                                        data=cur.fetchone()
                                        did=data[0]
                                        '''for i in data:
                                            if i[1]==dname:
                                                did=i[0]
                                                print(did)'''
                                    except:
                                        x.rollback()
                                        print('not found')
                                    query3='insert into Appointments values (%s,%s,%s,%s,%s)'
                                    value=(appid,pid,did,date,time)
                                    try:
                                        cur.execute(query3,value)
                                        x.commit()
                                        print('Data added sucessfully...')
                                        new()
                                        print('loading....')
                                        new()
                                    except:
                                        x.rollback()
                                        new()
                                        loading()
                                        new()
                                elif ch2==2:
                                    create_cursor()
                                    appid=input('ENTER THE APPOINTMENT ID :: ')
                                    pname=input('ENTER THE PATIENT FIRSTNAME  :: ')
                                    query='Select pid,fname from patient'
                                    try:
                                        cur.execute(query)
                                        data=cur.fetchall()
                                        for i in data:
                                            if i[1]==pname:
                                                pid=i[0]
                                    except:
                                        x.rollback()
                                        print('PATIENT NOT FOUND')
                                    cur.execute('select * from appointments where AID=\"'+appid+'\"')
                                    data=cur.fetchall()
                                    h=[ 'bill_id','patient_id','total_amount','Payment_status','bill_date']
                                    print(tabulate(data,headers=h ,tablefmt='psql'))
                                    p = input("you really wanna delete this data? (y/n):")
                                    if p == "y":
                                        try:
                                            cur.execute('delete from appointments where AID=\"'+appid+'\"')
                                            x.commit()
                                            print('APPOINTMENT DELETE SUCESSFULLY')
                                        except:
                                            x.rollback()
                                            print('!!! Error in deleting the appointment !!!')
                                            new()
                                            loading()
                                            new()
                                    else:
                                        print('APOINTMENT IS NOT DELETED')
                                elif ch2==3:
                                    create_cursor()
                                    appid=input('ENTER THE APPOINTMENT ID :: ')
                                    pname=input('ENTER THE PATIENT FIRSTNAME  :: ')
                                    query='Select pid,fname from patient'
                                    try:
                                        cur.execute(query)
                                        data=cur.fetchall()
                                        for i in data:
                                            if i[1]==pname:
                                                pid=i[0]
                                    except:
                                        x.rollback()
                                        print('PATIENT NOT FOUND')
                                    cur.execute('select * from appointments where AID=\"'+appid+'\"')
                                    data=cur.fetchall()
                                    h=[ 'bill_id','patient_id','total_amount','Payment_status','bill_date']
                                    print(tabulate(data,headers=h ,tablefmt='psql'))
                                    new()
                                    loading()
                                    new()
                                elif ch2==4:
                                    new()
                                    loading()
                                    new()
                                    break 
                        elif ch1==6:
                            while True:
                                print('_-' * 20, '-WELCOME TO LABORATORY MANAGEMENT', '_-' * 20)
                                print('press-1 ADD NEW TEST')
                                time.sleep(0.3)
                                print('press-2 VIEW TEST RESULTS')
                                time.sleep(0.3)
                                print('press-3 GO TO BACK')
                                time.sleep(0.3)
                                ch1 = int(input('ENTER YOUR CHOICE :: '))
                                current_time()
                                if ch1 == 1:
                                    test_name = input('ENTER THE TEST NAME :: ')
                                    patient_fname = input('ENTER THE PATIENT FIRST NAME :: ')
                                    patient_lname = input('ENTER THE PATIENT LAST NAME :: ')
                                    result = input('ENTER THE TEST RESULT :: ')
                                    query='Select pid,fname from patient'
                                    try:
                                        cur.execute(query)
                                        data=cur.fetchall()
                                        for i in data:
                                            if i[1]==patient_fname:
                                                pid=i[0]
                                    except:
                                        x.rollback()
                                        print('PATIENT NOT FOUND')
                                    query = ''' INSERT INTO lab_tests VALUES(%s, %s, %s, %s, %s,%s) '''
                                    test=random.randint(1000,9999)
                                    t1 ='t'+str(test)
                                    print(t1)
                                    value = [t1,test_name,pid,patient_fname,patient_lname,result]
                                    cur.execute(query, value)
                                    x.commit()
                                    print('TEST ADDED SUCCESSFULLY')
                                    try:
                                        cur.execute(query, values)
                                        x.commit()
                                        print('TEST ADDED SUCCESSFULLY')
                                    except:
                                        x.rollback()
                                        print("SOMETHING WENT WRONG")
                                elif ch1 == 2:
                                    patient_name = input('ENTER THE PATIENT FIRST NAME :: ')
                                    cur.execute( 'SELECT * FROM lab_tests WHERE patient_Fname =\''+patient_name+'\'')
                                    results = cur.fetchall()
                                    for i in results:
                                        print('TEST RESULTS FOR :: ', patient_name+i[4])
                                        print('Test ID:', i[0])
                                        print('Test Name:', i[1])
                                        print('Result:', i[5])
                                        print('---------------------')
                                        break
                                    else:
                                            print('No test results found for', patient_name)

                                elif ch1 == 3:
                                    new()
                                    loading()
                                    new()
                                    break  
                                else:
                                    print('Invalid Choice')
                                    new()
                                    loading()
                                    new()  
                        elif ch1==3:
                            while True:
                                print('press-1 VIEW SPECIFIC PATIENT DETAIL')
                                time.sleep(0.3)
                                print('press-2 VIEW ALL PATIENT DETAIL')
                                time.sleep(0.3)
                                print('press-3 GO TO MAIN MENU')
                                time.sleep(0.3)
                                ch=int(input("Enter your choice : "))
                                new()
                                loading()
                                new()                    
                                if ch==1:
                                    create_cursor()
                                    Fname = input("ENTER THE PATIENT FIRST NAME :: ")
                                    Lname = input("ENTER THE PATIENT LAST NAME :: ")
                                    cur.execute("select exists (select * from patient where Fname=\'"+Fname+"\' AND Lname =\'"+Lname+"\')")
                                    data=cur.fetchone()
                                    if data[0]==1:
                                        create_cursor()
                                        cur.execute("select * from patient where Fname=\'"+Fname+"\' AND Lname =\'"+Lname+"\'")
                                        dta=cur.fetchall()
                                        h=[ 'Patient_id','first_name','last_name','age','gender','phonenumber',' address','current_room' ]
                                        print(tabulate (dta ,headers=h ,tablefmt='psql'))
                                    else:
                                        print('!!!PATIENT NOT FOUND!!!')
                                elif ch==2:
                                    create_cursor()
                                    q='select * from patient'
                                    d=cur.execute(q)
                                    r=cur.fetchall()
                                    count=0
                                    for i in r:
                                        count+=1
                                    print('TOTAL OF NUMBER PATIENT FOUND ARE :: ',count)
                                    h=[ 'Patient_id','first_name','last_name','age','gender','phonenumber',' address','current_room' ]
                                    print(tabulate (r,headers=h ,tablefmt='psql'))
                                    new()
                                elif ch==3:
                                    new()
                                    loading()
                                    new()
                                    break 
                                else:
                                    print('!!! INVALID INPUT !!!')
                                    new()
                                    loading()
                                    new()
                        elif ch1==8:
                            new()
                            loading()
                            new()
                            break 
                elif ch==3:
                    new()
                    loading()
                    new()
                    print('''
Welcome to XYZ Hospital, an exemplary healthcare institution committed to providing unparalleled medical services. 
Our hospital, equipped with advanced technology and led by a skilled medical team, stands as a beacon of health and compassion.  
With a patient-centric philosophy, XYZ Hospital ensures each individual receives comprehensive and personalized care. 
Our modern facilities create a healing environment, and our commitment to transparent communication fosters trust. 
We go beyond traditional healthcare by offering holistic wellness programs that prioritize mental, emotional, and physical well-being. 
XYZ Hospital is not just a medical facility; it's a community partner dedicated to outreach initiatives and health education. 
As you explore our website, you'll discover the depth of our medical expertise, patient testimonials, and our ongoing pursuit of the latest healthcare advancements. 
Join us in the journey to optimal health, where your well-being is our unwavering priority. 
At XYZ Hospital ,we redefine healthcare with empathy, innovation, and a commitment to your health and happiness.
                    ''')
                    current_time()
                    time.sleep(10.3)
                    new()
                elif ch==4:
                    new()
                    loading()
                    new()
                    break
    a='n'
else:
    print('')

