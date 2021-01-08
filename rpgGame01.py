#!/usr/bin/python3

inventory = []
currentLocation = "WestOfMangrooveIsland"
points = 50

locations = {
    'WestOfMangrooveIsland': {
        'north' : 'Armada',
        'south' : 'TwinIslands',
        'west' : 'BigIsland',
        'east' : 'MangrooveIsland',
    },
    'Armada': {
        'south': 'WestOfMangrooveIsland',
    },
    'TwinIslands':{
        'north':'WestOfMangrooveIsland',
        'west': 'VolcanoIsland',
    },
    'BigIsland':{
        'east': 'WestOfMangrooveIsland',
        'south': 'VolcanoIsland',
    },
    'MangrooveIsland':{
        'west': 'WestOfMangrooveIsland',
    },
    'ThreeTreeIsland': {
        'north': 'VolcanoIsland',
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
  drink [item]
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

def showStatus():
    print('-----------------')
    print('You are currently at:  ', currentLocation)
    print('You inventory includes:  ', inventory)
    print('You have this many points: ', points)
    print('-----------------')




def begin():
    while True:
        showStatus()
        # get the player's next 'move'
        # .split() breaks it up into an list array
        # eg typing 'go east' would give the list:
        # ['go','east']
        move = ''
        while move == '':
            move = input('>')
            # split allows an items to have a space on them
            # get golden key is returned ["get", "golden key"]
            move = move.lower().split(" ", 1)

        if move[0] == 'sail':
            # check that they are allowed wherever they want to go
            if move[1] in locations[currentLocation]:
                # set the current location to the new location
                currentLocation= locations[currentLocation][move[1]]



def main():
    showInstructions()
    showInitStatus()
    begin()

if __name__ == '__main__':
    main()