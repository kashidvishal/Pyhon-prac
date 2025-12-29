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

rolls = 0
invalid = 0
valid = 0
while True:
    choice = input('Roll the dice? (y/n): ')
    #choice = input('Roll the dice? (y/n): ').lower()
    rolls += 1
    if choice in ('Y', 'y', 'N', 'n'):
        valid += 1

    if choice == 'y' or choice == 'Y':
        #valid += 1
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
        #counter = counter + 1
        #valid += 1
        break
    else:
        print('Invalid choice')
        invalid += 1
    #counter = counter + 1
print("Total rolls :", rolls)
print("Total valid tries :", valid)
print("Total Invalid tries :", invalid)