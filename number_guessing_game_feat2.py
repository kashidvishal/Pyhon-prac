#Generate a random number
#Loop
    #Ask the user for make a random guess
    #If not valid number
        #Print error message
    #If number < guess
        #too low
    #If number > guess
        #too high
    #else
        # print well done message

import random

min_num = int(input('Enter the minimum number: '))
max_num = int(input('Enter the maximum number: '))

number_to_guess = random.randint(min_num, max_num)
#print(number_to_guess)
print('Your number is ready! You can start now')
for i in range(5):
    try:
        guess = int(input(f'Guess the number between {min_num} to {max_num}: '))
        if guess < number_to_guess:
            print('Too low!')
        elif guess > number_to_guess:
            print('Too high!')
        else:
            print('Congratulation! You guessed the number.')
            #guessed = True
            break
    except ValueError:
        print('Please enter a valid number.')
else:
    print('Sorry! You did not guess the number.')

#if guessed = False:
    #print('Sorry! You did not guess the number.')