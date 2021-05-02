name=input('what is your is your name? \n')
password=input('please login your password \n')
print('Login successful')
import datetime
now=datetime.datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
print('These are available options')
print('1.cash withdrawal')
print('2.cash deposit')
print('3.Lodge a complaint')
print('4.cash transfer')
print('5.Get a loan')
selectoption=int(input('Please select an option \n'))
if(selectoption==1):
   withdrawal=input('How much would you like to withdraw\n')
   print('Take cash')
elif(selectoption==2):
   deposit=input('How much would you like to deposit \n')
   print('Current balance')
elif(selectoption==3):
   complaint=input('What issue will you like report \n')
   print('Thank you for contacting us')
else:
   print('Invalid option selected, please try again')




     
     
     
   
    
      
   

   
   
    
    
       
   
   
   







         

