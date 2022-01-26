import pickle
def menu():
    print('\tHostel Management System')
    print()
    print('1. New Admission')
    print('2. Fee Payment')
    print('3. Modify Student Detail')
    print('4. Search Student')
    print('5. Display All Students')
    print('9. Exit')
def newStudent(students):
    try:
        vroll=int(input('Enter the roll number:- '))
        if vroll not in students.keys():
            vname=input("Enter the name:- ")
            vaddress=input('Enter the address:- ')
            vphone=int(input('Enter the phone number:- '))
            vroom=int(input('Enter the room number:- '))
            fees=[]
            students[vroll]=[vname, vaddress, vphone, vroom, fees]
        else:
            print('Student with',vroll,'ID has been already added!')
    except:
        print('Please Enter Proper Values')
    return students
def fee(students,months):
    try:
        vroll=int(input('Enter the roll number:- '))
        if vroll in students.keys():
            stu=students[vroll]
            fees=stu[4]
            month=int(input('Enter the month for the fee to be paid(in MM format):- '))
            year=int(input('Enter the year for the fee to be paid(in YYYY format):- '))
            month=months[month]
            date=str(month)+str(year)
            if date not in fees:
                fees.append(date)
                print('Pls pay Rs 8000 at the counter.')
            else:
                print('Already paid!')
        else:
            print('Student with',vroll,'ID not found!')
    except:
        print('Please Enter Proper Values')
    return students
def modify(students):
    try:
        vroll=int(input('Enter the roll number:- '))
        if vroll in students.keys():
            vname=students[vroll][0]
            vaddress=input('Enter the address:- ')
            vphone=int(input('Enter the phone number:- '))
            vroom=int(input('Enter the room number:- '))
            fees=students[vroll][4]
            students[vroll]=[vname, vaddress, vphone, vroom, fees]
        else:
            print('Student with',vroll,'ID not found!')
    except:
        print('Please Enter Proper Values')
    return students
def search(students):
    try:
        vroll=int(input('Enter the roll number:- '))
        if vroll in students.keys():
            print()
            print('Roll No:- ',vroll)
            print('Name:-    ',students[vroll][0])
            print('Address:- ',students[vroll][1])
            print('Phone No:-',students[vroll][2])
            print('Room No:- ',students[vroll][3])
            if len(students[vroll][4])>0:
                for i in students[vroll][4]:
                    print('Paid For The Year', i[-1:-5:-1], 'Month',i[3])
                else:
                    print('No fees paid till now!')
        else:
            print('Student with',vroll,'ID not found!')
    except:
        print('Please Enter Proper Values')
def show(students):
    if len(students.keys())>0:
        for i in students.keys():
            print('Roll No:',i,"Name:",students[i][0])
    else:
        print('No Data Found')
def db_creation():
    f1=open('students.dat','wb')
    students={}
    pickle.dump(students,f1)
    f1.close()
def db_load():
    f2=open('students.dat','rb')
    a=pickle.load(f2)
    f2.close()
    return a
def db_save(a):
    f3=open('students.dat','wb')
    pickle.dump(a,f3)
    f3.close()
months=['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', "Jul", 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
students={}#roll:name,address, phone, room, fees

while True:
    print('\nStartup\n')
    b=input("Is this the first time running this program?(Y/N):- ")
    if b=='y'or b=='Y':
        db_creation()
        break
    elif b=='n'or b=='N':
        students=db_load()
        break
    else:
        print('Enter a valid input')
    print('\n')

while True:
    print('\n\n')
    menu()
    a=(input('Enter Your Choice:- '))
    if a=='1':
        students=newStudent(students)
    elif a=='2':
        students=fee(students,months)
    elif a=='3':
        students=modify(students)
    elif a=='4':
        search(students)
    elif a=='5':
        show(students)
    elif a=='9':
        break
    db_save(students)