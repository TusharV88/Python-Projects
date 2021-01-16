# Age Teller
'''
Author : Tushar Verma
Date : 24-Dec-2020
'''

print('-'*10,'Age Teller','-'*10)

age = input(print('\n Enter your Age or Year Of Birth to find out that on which year you will be 100 years old :'))

at = int(age)
x = len(age) # length of age
y = 2020 # current year


if (x == 1 or x == 2 or x == 3):
    if (at < 10 and at > 0 ):
        print(f'\nThis {y-at+100} year your age will be 100.')
    elif (at < 0):
        print("Don't be oversmart.You are not born yet.")            
    elif (at < 100 and at > 9):
        print(f'\nThis {y-at+100} year your age will be 100.')
    elif (at >= 100 and at <= 150):
        print(f'\nThis {y-at+100} year your age was 100.')
    elif (at > 150 and at <= 200):    
        print('\n Awesome you are that old.')
        print(f'\n This {y-at+100} years your age was 100.')
    else:
        print('\n Sorry ,no one alive at that age.')
elif (x == 4):
    if (at > y):
        print('You are not born yet.')
    elif (at == y):
        print('\n This year you are 100 years old.')
    else:
        print(f'This {at+100} year you was 100 year old.')
else:
    print('Please Enter Your Age or Year Of Birth Properly.')


z =  input(print('Do you want see your age at particular year ? (y/n)'))

if (z == 'y' or z == 'Y'):
    yb = input(print('Year of Birth : '))
    year = len(yb)
    if (year < 4):
        print('This is not a year of birth!')
    elif (year == 4):
        c = int(input(print('Enter Any year to want to see your age : ')))
        ssd = int(yb)
        if ssd > y:
            print('Oops,You are not born yet!')
        else:
            print(f'Your age at {c} is {c-ssd}.')
    else:    
        print('This is not a year of birth!')
elif (z == 'n' or z == 'N'):
        print('\nThank You 😉,Have a Good Day !')
else:        
    print('Something Went worng!,Please check input.')
        
    
        
