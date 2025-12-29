#-----------------Basic Idea-------------------
#Loop
    #ask to roll the dice
    #if user enters y
    #    generate 2 random numbers
    #    print them
    #else if user enters n
    #    print thank you message
    #    program terminate
    #else 
    #    print envalid choice
    #    program terminate
#loop End
import random

iter = int(input('How many iteration? '))
for i in range(iter)
    choice = input('Roll the dice? (y/n): ')
    #choice = input('Roll the dice? (y/n): ').lower()

    if choice == 'y' or choice == 'Y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'{die1}, {die2}') #f-sting 
        # The f tells Python: “This string contains variables that should be replaced with their values.”
        #print(die1, die2)
        #print(str(die1) + ', ' + str(die2))
        #print('{}, {}'.format(die1, die2))
        #print('%d, %d' % (die1, die2))
    elif choice == 'n' or choice == 'N':
        print('Thanks for playing!!!')
        break
    else:
        print('Invalid choice')