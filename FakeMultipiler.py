# Fake Multiplier Checker

'''
Aurthor : Tushar verma
Date : 05-Jan-21
'''

import random as rn


# Genrate Fake Multiplication Table
def FakeMultiplier(number):
    fakenum = rn.randrange(1, 10)
    fakeTable = []
    randomNumber = rn.randrange(1, 10)
    for i in range(1, 11):
        if i == randomNumber:
            mul = number * fakenum
        else:
            mul = number * i
        fakeTable.append(mul)
    return fakeTable


# Check if the table is correct or not
def Checker(table, number):
    correctTable = []
    for i in range(1, 11):
        multi = number * i
        correctTable.append(multi)

    for i in range(len(table)):
        if table[i] != correctTable[i]:
            print(
                f'Multiplication Table of {number} is incorrect at index {i} and the number is {table[i]}')
            print(f'\n Incorrect Table : {table}')

    print('\n Correct Table : ', correctTable)


if __name__ == "__main__":
    num = int(input('Enter Any Number to get Multiplication Table : '))

    Tabel = FakeMultiplier(num)

    Checker(Tabel, num)
