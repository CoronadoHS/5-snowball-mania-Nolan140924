''' 
    Name: Snowball-Mania
    Author: Nolan
    Date: 12/5/2025
    Class: AP Computer Science Principles
    Python: Python 3.13
'''

import random
import time
import colorama

colorama.init(True)

def printIntro():
    '''
    ' Param: none
    ' 
    ' Print a welcome message to the user
    ' 
    ' Return: none
    '''
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")
    print("❄️  Welcome to Snowball Mania!❄️")
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")


def getNames():
    '''
    ' Param: none
    ' 
    ' Create a list to hold player names.
    ' Ask the user for their name.  Store it in a variable and add it to the player list.
    ' Print instructions for the user to add more players and to type "DONE" when finished.
    ' Read in the first additional player name.
    ' While the user hasn't typed "DONE", add the new name to the player list and prompt for the next name
    ' After the user is finished entering names, print a "Time to play!" message
    '
    ' Return: the list of player names
    ' 
    '''
    print("\n")
    Players = [input("What is your name?: ")]
    while True:
        player = input("Give a player name(Leave blank if finished): ")
        if player == "":
            break
        else:
            Players.append(player)
    print("\n")
    return Players
        


def getThrower(players):
    '''
    ' Param: players (list of player names)
    '
    ' Return a randomly chosen player name to be the next thrower.
    '
    ' Return: player name
    '''
    return random.choice(players)

    
def getVictim(players, t):
    '''
    ' Param: players (list of player names), t (the thrower for this round)
    ' 
    ' Select a random player to be the next victim.  
    ' While the victim is the same player as the thrower, randomly select a new victim from the list.
    ' Return the victim's name.
    '
    ' Return: victim's name
    '''
    Victim = random.choice(players)
    return Victim != t and Victim or getVictim(players, t)


def getHitResult():
    '''
    ' Param: none
    ' 
    ' Generate a random number between 1 and 10
    ' If the number is greater than ___, return True
    ' Else, return False
    '
    ' Return: Boolean representing whether or not the snowball hit
    '''
    return random.randint(1, 10) > 6


def playSnowballFight(players):
    '''
    ' Param: players (a list of players still in the game)
    '
    ' While there are still multiple players in the game...
    '   - Get the next thrower
    '   - Get the next victim
    '   - Get the next hit result
    '   - If a hit occurred, flip a coin to see if it is a knockout or not.
    '     - If knockout, print a knockout message and remove the victim from the list
    '     - Else, print a hit message but do not remove victim
    '   - Else, print a miss message
    '   - time.sleep(3) - delay execution for three seconds
    ' 
    ' Return: none
    '''
    while len(players) > 1:
        Thrower = getThrower(players)
        Victim = getVictim(players, Thrower)
        Hit = getHitResult()
        if Hit:
            if random.randint(0, 1) == 1:
                Endings = (" Will they get up..? probably not..", " HOW!?", " They're done for the day.", " No more snowballs for them..")
                print(colorama.Fore.RED + f"{Thrower} knocked out {Victim}!" + random.choice(Endings))
                players.remove(Victim)
            else:
                Endings = (" They don't look so good anymore.", " And they just dusted it off..", " Ow!")
                print(colorama.Fore.GREEN + f"{Victim} was hit by {Thrower}!" + colorama.Fore.YELLOW + random.choice(Endings))
        else:
            Endings = (" just barely.", " horribly!", ", were they even aiming?", ", but hit that person's window, ouch..")
            print(colorama.Fore.YELLOW + f"{Thrower} missed {Victim}" + random.choice(Endings))

        time.sleep(3)


    
def printOutro(winner):
    '''
    ' Param: name of the winner
    ' 
    ' Print a congratulatory message naming the winner
    '
    ' Return: none
    '''
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")
    print("All hail " + winner + ", the Ultimate Student/Snowball Wizard!")
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")


def runProgram():
    '''
    ' Param: none
    ' 
    ' Call the method that will print the intro messages
    ' Call the method that will return a list of player names.  Save the list in a variable.
    ' Call the method that will simulate the snowball fight
    ' Call the method that will print the outro messagees
    '
    ' Return: none
    '''
    printIntro()
    players = getNames()
    playSnowballFight(players)
    printOutro(players[0])

runProgram()