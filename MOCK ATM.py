name=input('what is your user name? \n')
allowedusers=('seyi,david,ife,timi')
allowedpassword=('passwordseyi','passworddavid','passwordife','passwordtimi')

if(name in allowedusers):
    password=input('what is your password? \n')
    userid=(allowedusers.index(name))


    if(password==allowedpassword[userid]):
        print('welcome')
    else:
        print('password incorrect try again')
else:
    print('name not found try again')
    


    
