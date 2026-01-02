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

attempts = int(input('How many times you want to play? Give a attemps number:'))
counter = 0
best_score = 101
#new_score = 0
iteration = 0
for i in range(attempts):
    number_to_guess = random.randint(1, 100)
    print('Your number is ready! You can start now:')
    while True:
        counter += 1
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
    print(f'You guessed in {counter} attempts')
    #new_score = counter
    if counter < best_score:
        best_score = counter
        iteration = i+1
    counter = 0

print(f'Your Best scoured in guessing attempts are: {best_score} and the iteration of {iteration}')