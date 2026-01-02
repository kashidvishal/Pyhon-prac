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

number_to_guess = random.randint(1, 100)
print('Your number is ready! You can start now:')
while True:
    try:
        guess = int(input('Guess the number between 1 to 100: '))
        if guess < number_to_guess:
            print('Too low!')
        elif guess > number_to_guess:
            print('Too high!')
        else:
            print('Congratulation! You guessed the number.')
            break
    except ValueError:
        print('Please enter a valid number.')

