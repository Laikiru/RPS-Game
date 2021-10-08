# Rock Paper Scissors Game // 07/19/2021 - 10/07/2021
# by Laika!!

# Input options Rock, Paper, Scissors
# Bot chooses from random selection- Rock Paper Scissors
# Compare; win or lose
###############################

def end_game(): # Function to end game if the player wants to.
    print("Would you like to end the game? Y/N")
    endchoice = str(input('Y/N: '))
    if (endchoice == 'Y') or (endchoice == 'y'):
        invalid = False
        option = False
        print('Thanks for playing!')
        exit()
    elif (endchoice == 'N') or (endchoice == 'n'):
        invalid = False
        option = True
    else:
        invalid = True
        print('Please enter Y or N.')
        endchoice = str(input('Y/N: '))
        if (endchoice == 'Y') or (endchoice == 'y'):
            invalid = False
            option = False
            print('Thanks for playing!')
            exit()
        elif (endchoice == 'N') or (endchoice == 'n'):
            invalid = False
            option = True
            
import random
import time
invalid = True # Used when input is invalid; prompts user to enter a correct input.
option = True # Runs the program; when False the program stops.

while option == True:
    print('Enter "Rock", "Paper", or "Scissors"! Otherwise, enter "E" at anytime to end the game.')
    playerchoice = str(input('Selection: ')) # Input is not case sensitive.
    if (playerchoice == 'Rock') or (playerchoice == 'Paper') or (playerchoice == 'Scissors'):
        invalid = False
        choicelist = ['Rock', 'Paper', 'Scissors']
        botchoice = random.choice(choicelist)
        print('The opponent chose', botchoice, "!")
    elif (playerchoice == 'E') or (playerchoice == 'e'):
        invalid = False
        end_game()
    else:
        invalid = True
    while invalid == True: # Did not input one of the 6 options.
        print('Invalid entry; please try again!')
        playerchoice = str(input('Selection: '))
        if (playerchoice == 'Rock') or (playerchoice == 'Paper') or (playerchoice == 'Scissors'):
            invalid = False
            choicelist = ['Rock', 'Paper', 'Scissors']
            botchoice = random.choice(choicelist)
            print('The opponent chose', botchoice, "!")
        elif (playerchoice == 'E') or (playerchoice == 'e'):
            invalid = False
            end_game()
        else:
            invalid = True

    if playerchoice == botchoice:
        print('Tie!')
    elif playerchoice == 'Rock':
        if botchoice == 'Scissors':
            print('You win! Rock beats Scissors!')
        elif botchoice == 'Paper':
            print('You lose! Paper beats Rock')
    elif playerchoice == 'Paper':
        if botchoice == 'Rock':
            print('You win! Paper beats Rock!')
        elif botchoice == 'Scissors':
            print('You lose! Scissors beats Paper!')
    elif playerchoice == 'Scissors':
        if botchoice == 'Paper':
            print('You win! Scissors beats Paper!')
        elif botchoice == 'Rock':
            print('You lose! Rock beats Scissors!')

    time.sleep(3) # Wait 3 seconds before playing again.
    print('\n')
