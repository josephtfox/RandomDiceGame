# Name: Tanner Fox
# Section: 02
# Email: jtfo234@g.uky.edu

# Reference: Sung il Kang

'''
Purpose: to play multiple dice games with a user.  
  The game rules are: one die is rolled,
  the user can roll as many more times as they like and accumulate the 
  points (dollars).  They can stop at any time they want and leave 
  with that total, but if they roll a die that matches the first one rolled, 
   they lose all their total and leave the game.

Pre-conditions:  User enters y/n choices for rolling again, and for playing
  another game.  Any other input values are rejected and the user asked for 
  another.

Post-conditions:  Rolls of the die are displayed, prompts for user's decisions,
   total accumulated points, final results of the games
'''

# need random library for number between 1 and 6 for die roll
from random import *

'''
Function one
Purpose: prints a die with a one on its face
Pre-conditions: none
Post-conditions: a die with a one on its face on the shell window
   returns nothing
'''

def one():
    print('+---+')
    print('|   |')
    print('| * |')
    print('|   |')
    print('+---+')    
    
'''
Function two
Purpose: prints a die with a two on its face
Pre-conditions: none
Post-conditions: a die with a two on its face on the shell window
   returns nothing
'''

def two():
    print('+---+')
    print('|*  |')
    print('|   |')
    print('|  *|')
    print('+---+')       
    
'''
Function three
Purpose: prints a die with a three on its face
Pre-conditions: none
Post-conditions: a die with a three on its face on the shell window
   returns nothing
'''

def three():
    print('+---+')
    print('|*  |')
    print('| * |')
    print('|  *|')
    print('+---+')  
    
'''
Function four
Purpose: prints a die with a four on its face
Pre-conditions: none
Post-conditions: a die with a four on its face on the shell window
   returns nothing
'''

def four():
    print('+---+')
    print('|* *|')
    print('|   |')
    print('|* *|')
    print('+---+')    

'''
Function five
Purpose: prints a die with a five on its face
Pre-conditions: none
Post-conditions: a die with a five on its face on the shell window
   returns nothing
'''

def five():
    print('+---+')
    print('|* *|')
    print('| * |')
    print('|* *|')
    print('+---+')    
    
'''
Function six
Purpose: prints a die with a six on its face
Pre-conditions: none
Post-conditions: a die with a six on its face on the shell window
   returns nothing
'''

def six():
    print('+---+')
    print('|* *|')
    print('|* *|')
    print('|* *|')
    print('+---+') 
    
'''
Function display_die
Purpose: to print to screen one die with specified number of spots
Pre-conditions:  one parameter, integer, number of spots on die to print
Post-conditions:  one die with number of spots specified on screen
   returns nothing
'''

def display_die(dice):
    # uses if/elif/elif to check the number of spots, 1-6, to see which 
    # function, one() - six(), to call
    if dice == 1:
        one()
    elif dice == 2:
        two()
    elif dice == 3:
        three()
    elif dice == 4:
        four()
    elif dice == 5:
        five()
    elif dice == 6:
        six()
    
'''
Function validate_input
Purpose: to present a prompt to the user, allow them to input an answer,
    validate the input - only y and n allowed, and return validated answer
Pre-conditions:  one string, which is the prompt
     allows user to input answers until valid answer is given
Post-conditions: returns the validated answer, string that is y or n
'''

def validate_input(user_input):
    
    # allows user to input string, showing parameter as prompt
    # uses while loop to validate the input, allowing only y or n as valid
    while user_input != 'y' and user_input != 'n':
        # outputs error message if not valid 
        print('please answer y or n')
        # gets another input
        user_input = input('Do you want to roll again? (y/n) ')
    # returns valid input
    return user_input


# Function main 
def main():
    # seed the random number generator
    seed(0)
    # display the title of the game
    print("The game of 'Don't Match'")
    print()    
    # set play flag to True
    play_flag = True 
    
    # while they want to play a game
    while play_flag == True: 
        # these steps are getting ready to play a game
        # initialize point accumulator to zero
        total_points = 0
        # get first roll - random number 1-6, and inform user what it is
        first_roll = randint(1,6)
        print('Your first roll is ',first_roll)
        # display a die with that many spots on it
        display_die(first_roll)
        # show them instructions - don't match this number!
        print("You can roll as long as you don't roll another", first_roll)
        # add first roll to point accumulator
        total_points += first_roll
        print()
        # tell them how many points they have
        print(' You have ${:.0f}'.format(total_points))
        print()
        # ask (validated input) if they want to roll again
        user_input = input('Do you want to roll again? (y/n) ')
        user_input = validate_input(user_input)
        # if they say no, set roll flag to False, otherwise True
        if user_input == 'n':
            roll_flag = False
        elif user_input == 'y':
            roll_flag = True 
        # get another roll - random number 1-6
        roll = randint(1,6)
        # while they want to roll and number rolled has not matched first roll
        while user_input == 'y' and roll != first_roll:
            # show them the number rolled - die with that many spots
            print('You rolled a', roll)
            display_die(roll)
            # add number rolled to point accumulator
            total_points += roll
            # tell them how much they won and their total
            print('You won $', roll, sep = '')
            print(' You have ${:.0f}'.format(total_points))
            print()
            # ask (validated input) if they want to roll again
            user_input = input('Do you want to roll again? (y/n) ')
            user_input = validate_input(user_input)
            # set play flag to False if they don't want to roll again
            if user_input == 'n':
                roll_flag = False
            # get another roll - random number 1-6
            roll = randint(1,6)
        # now the game is over
        # if they said they didn't want to roll again
        if user_input == 'n':
            # tell them how many points they left with
            print()
            print('You left with ${:.2f}'.format(total_points))
            print()
        # otherwise
        elif roll == first_roll:
            # tell them they lost all their money
            print('Sorry, you rolled', first_roll, 'and lost all your money!')
            print()
        # ask (validated input) if they want to play another game 
        input_game = input('Do you want to play another game? (y/n) ')
        input_game = validate_input(input_game)
        # if they say no, set play flag to False
        if input_game == 'n':
            play_flag = False

    # after all games have been played, say goodbye
    print('Goodbye!')
main()
