#!/usr/bin/python3

inventory = []
currentLocation = "WestOfMangrooveIsland"

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
    },
    'BigIsland':{
        'east': 'WestOfMangrooveIsland',
    },
    'MangrooveIsland':{
        'west': 'WestOfMangrooveIsland',
    },
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
    If too many bad things happen to you: YOU LOOSE
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





def begin():
    while True:
        showStatus()

def main():
    showInstructions()
    showInitStatus()
    begin()

if __name__ == '__main__':
    main()