
'''
Aurthor : Tushar Verma.
Date : 29-Dec-20
'''
# Guess The Number Game.

import random

print("*"*5,'Welcome to the Guess The Number Game',"*"*5)

a = int(input('Enter the value of a : ')) # Inital Value 
 
b = int(input('Enter the value of b : ')) # Final Value

# This function genrate random number for game by given input range
def randomNumber(a,b):
    ran = random.randrange(a,b)
    return ran
    
ranG1 = randomNumber(a,b) # Return the genrated number to the variable

print("\nNow ,Let's Begin the Game")

over = True
count1 = 0
i = 1

print('Player 1 : ')
print(f'\nPlease Guess the number between {a} and {b} : \n')

while over: # Loop runs till over is True
    player1 = int(input(f'Guess {i} : '))
    # Comparing the player 1 int to random number and count how many trials takes
    if(player1 < ranG1):
        print('\nWrong guess a greater number again!')
        count1 += 1 
    elif(player1 > ranG1):
        print('\nWrong guess a smaller number again!')
        count1 +=1
    elif(player1 == ranG1):
        print(f'\nCorrect ,you took {count1} trials to guess the number!')
        over = False
    else:
        print('Oops ,Something went worng! Please check again.')
    i += 1

print('\n')
print("-"*5,"Now it's time for another player to play the game.","-"*5)

print('\nPlayer 2 :')
print(f'\nPlease Guess the number between {a} and {b} : \n')

over2 = True
count2 = 0
j = 1
ranG2 = randomNumber(a,b)

while over2:
    player2 = int(input(f'Guess {j} : '))
    if(player2 < ranG2):
        print('\nWrong guess a greater number again!')
        count2 += 1 
    elif(player2 > ranG2):
        print('\nWrong guess a smaller number again!')
        count2 +=1
    elif(player2 == ranG2):
        print(f'\nCorrect ,you took {count2} trials to guess the number!')
        over2 = False
    else:
        print('Oops ,Something went worng! Please check again.')
    j += 1

if (count1 > count2):
    print('\n')
    print('*'*20)
    print('The Winner is Player 2')
elif(count1 == count2):
    print("\nIt's a Draw!")
else:
    print('\n')
    print('*'*20)
    print('The Winner is Player 1')








