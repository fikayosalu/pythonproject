
import random
database={}
def init():
    isvalidoptionselected=False

    print('Welcome to SaluBank')

    while isvalidoptionselected==False:

        haveaccount=int(input('Do you have an account with us 1 (yes) or 2 (no) \n '))


        if haveaccount==1:
            isvalidoptionselected=True
            login()


        elif haveaccount==2:
            isvalidoptionselected=True
            print(register())

        else:
            print('Invalid option selected please try again')




def login():
    print('******Login******')

    accountnumberforuser=int(input('What is your account number \n'))
    password=input('What is your password \n')
    print('Login successful')

    bankoperations()



def register():
    print('****Register****')
    firstname=input('What is your first name \n')
    lastname=input('What is your last name \n')
    email=input('What is your email address \n')
    password=input('create a strong password \n')
    accountnumber=generateaccountnumber()
    database[accountnumber] = [ firstname, lastname, email, password]
    print('Account has been created')
    print('Your Account Has been created')
    print('Your account number is %d'%accountnumber)
    login()



def generateaccountnumber():


    return random.randrange(1111111111,9999999999)

def withdarawal():
    int(input('How much would you like to withdraw \n'))
    print('Take cash')

def deposit():
    int(input('How much would like to deposit \n'))
    print('Current balance')
def transfer():
    int(input('How much would like to transfer \n'))
    input('Account number to transfer \n')
    input('Name of bank \n')
    print('Transfer successful')

def complaint():
    input('What issue would you like to report \n')
    print('Thank you for contacting us')



def bankoperations():
    print('Available Options')
    print('1.cash withdrawal')
    print('2.cash deposit')
    print('3.cash transfer')
    print('4.Lodge a complaint')
    selectoption = int(input('Please select an option \n'))

    if selectoption==1:
        withdarawal()
    if selectoption==2:
        deposit()
    elif selectoption==3:
        transfer()
    elif selectoption==4:
        complaint()

    else:
        print('Invalid option selected')
        bankoperations()


init()
