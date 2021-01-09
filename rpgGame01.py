#!/usr/bin/python3
import os

#INVENTORY = []
#CURRENTLOCATION = "WestOfMangrooveIsland"
#POINTS = 50

locations = {
    'WestOfMangrooveIsland': {
        'north' : 'Armada',
        'south' : 'TwinIslands',
        'west' : 'BigIsland',
        'east' : 'MangrooveIsland',
        'item' : 'pump'
    },
    'Armada': {
        'south': 'WestOfMangrooveIsland',
        'item' : 'mermaid',
    },
    'TwinIslands':{
        'north':'WestOfMangrooveIsland',
        'west': 'VolcanoIsland',
        'item': 'compass',
    },
    'BigIsland':{
        'east': 'WestOfMangrooveIsland',
        'south': 'VolcanoIsland',
        'item': 'binos'
    },
    'MangrooveIsland':{
        'west': 'WestOfMangrooveIsland',
        'item': 'rum'
    },
    'VolcanoIsland': {
        'north' : 'BigIsland',
        'east' : 'TwinIslands',
        'south' : 'ThreeTreeIsland',
        'item' : 'water',
    },
    'ThreeTreeIsland': {
        'north': 'VolcanoIsland',
        'item': 'rowboat'
    }
}

def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  see [direction]
  get [item]
  sail [direction]
''')
    print('''
    Use the listed commands to navigate your way around the islands
    Looking for Pirates Treasure and trying not to get your ass kicked
    or fall upon too many mis-adventures.
    If too many bad things happen to you: YOU LOOSE because you lost too many points
    If you find the treasure before too much mis-adventures, YOU WIN
    ''')

def showInitStatus():
    # print the player's initial status
    print('''
    ---------------------------
    You wake up from a night of hard drinking, on a leaking scowl of a boat 
    it looks like some place in the Caribbean Islands
    you stumble to the deck and find a note. 
    It says "good luck" and has what looks like a map written by a child
    probably written by one of your drinking mates.
    The map shows an amoeba shape and 3 palm trees with an "X" in the middle
    of them.
    You look around and find yourself in a empty harbor with a bunch of mangroove
    trees and the stench like somebody pumped shit in the harbor
    It appears you are on the west side of the island
    You take inventory and realize you ain't got shit, just this old scowl and a gallon
    of water.
    Time to set sail and get out of this place and look for treasure
    ---------------------------
    ''')
    return

#def showStatus():
   # print('-----------------')
   # print('You are currently at:  ', CURRENTLOCATION)
   # print('You inventory includes:  ', INVENTORY)
   # print('You have this many points: ', POINTS)
   # print('-----------------')
   # return


def youLoose():
    print("you lost too many points doing dumb moves and LOST")
    print("Try again by restarting")
    exit(0)

def begin():
    INVENTORY = []
    CURRENTLOCATION = "WestOfMangrooveIsland"
    POINTS = 50

    while True:
        print('-----------------')
        print('You are currently at:  ', CURRENTLOCATION)
        print('You inventory includes:  ', INVENTORY)
        print('You have this many points: ', POINTS)
        if 'item' in locations[CURRENTLOCATION]:
            print('You find : ', locations[CURRENTLOCATION]["item"])
        print('-----------------')
        #print('test  --  ', CURRENTLOCATION)
   # while True:
        #showStatus()
        # get the player's next 'move'
        # .split() breaks it up into an list array
        # eg typing 'go east' would give the list:
        # ['go','east']
        move = ''
        while move == '':
            move = input('> ')

            # split allows an items to have a space on them
            # get golden key is returned ["get", "golden key"]
        move = move.lower().split(" ", 1)

        if move[0] == 'sail':
            # check that they are allowed wherever they want to go
            if move[1] in locations[CURRENTLOCATION]:
                # set the current location to the new location
                POINTS = POINTS + 10
                CURRENTLOCATION = locations[CURRENTLOCATION][move[1]]
            else:
                print("You sail in that direction for a while and find nothing.. ")
                print("You loose 10 points for wasteing time and taking on water to your leaky scowl")
                POINTS = POINTS - 10
                if POINTS <= 0:
                    youLoose()

        if move[0] == 'see':
            # let them see in that direction
            if move[1] in locations[CURRENTLOCATION]:
                POINTS = POINTS - 5
                print("In that direction you see:  ", locations[CURRENTLOCATION][move[1]])
            else:
                print("You only see open ocean and mares-tails clouds ")
                print("gotta take some points before the storm")
                POINTS = POINTS -5
                if POINTS <= 0:
                    youLoose()
        if move[0] == 'get':
            # see if there is anything to get to add points
            if 'item' in locations[CURRENTLOCATION] and move[1] in locations[CURRENTLOCATION]['item']:
                # add item to inventory
                INVENTORY += [move[1]]
                # display what they got
                print(move[1], ' aquired')
                item = move[1]
                if item == "rowboat":
                    POINTS = POINTS + 25
                    # print('You might consider going ashore and looking for treasure')
                    # break
                elif item == "binos":
                    POINTS = POINTS + 10
                    # break
                elif item == "compass":
                    POINTS = POINTS + 10
                elif item == 'water':
                    POINTS = POINTS + 15
                elif item == 'pump':
                    POINTS = POINTS - 5
                    print("you needed the pump because you won't fix your leaky boat")
                elif item == 'rum':
                    POINTS = POINTS - 10
                    print('Should not have gone ashore and gotten the bad rum')
                elif item == 'mermaid':
                    POINTS = POINTS - 15
                    print("there are no such thing as mermaids, you loose points")


                #adjustPoints(POINTS, item)
                print('Points returned?  ', POINTS)
                del locations[CURRENTLOCATION]['item']


            else:
                # notify there is nothing to get
                print("Not able to get ", move[1])

# temp holder

        # remove item from island

        if CURRENTLOCATION == 'ThreeTreeIsland' and POINTS >= 100:
            print('You are either one lucky misfit, or else King Neptune Likes you')
            print("You have WON")


def main():
    os.system('clear')
    showInstructions()
    #showInitStatus()
    begin()

if __name__ == '__main__':
    main()