def effectiveness(pokemonType, moveType):
    ''' returns mulitplier for damage based on type effectiveness'''

    # dictionary that has every pokemon type and corresponding number
    d = {'Normal': 0, 'Fire': 1, 'Water': 2, 'Grass': 3, 'Electric': 4, 'Ice': 5, \
         'Fighting': 6, 'Poison': 7, 'Ground': 8, 'Flying': 9, 'Psychic': 10, 'Bug': 11, \
         'Rock': 12, 'Ghost': 13, 'Dragon': 14, 'Dark': 15, 'Steel': 16, 'Fairy': 17}

    # matrix that has the effectiveness of every pokemon typing. REQUIREMENT
    matrix = [[1,1,1,1,1,1,1,1,1,1,1,1,0.5,0,1,1,0.5,1],
              [0,0.5,0.5,2,1,2,1,1,1,1,1,2,0.5,1,0.5,1,2,1],
              [1,2,0.5,0.5,1,1,1,1,2,1,1,1,2,1,0.5,1,1,1],
              [1,0.5,2,0.5,1,1,1,0.5,2,0.5,1,0.5,2,1,0.5,1,0.5,1],
              [1,1,2,0.5,0.5,1,1,1,0,2,1,1,1,1,0.5,1,1,1],
              [1,0.5,0.5,2,1,0.5,1,1,2,2,1,1,1,1,2,1,0.5,1],
              [2,1,1,1,1,2,1,0.5,1,0.5,0.5,0.5,2,0,1,2,2,0.5],
              [1,1,1,2,1,1,1,0.5,0.5,1,1,1,0.5,0.5,1,1,0,2],
              [1,2,1,0.5,2,1,1,2,1,0,1,0.5,2,1,1,1,2,1],
              [1,1,1,2,0.5,1,2,1,1,1,1,2,0.5,1,1,1,0.5,1],
              [1,1,1,1,1,1,2,2,1,1,0.5,1,1,1,1,0,0.5,1],
              [1,0.5,1,2,1,1,0.5,0.5,1,0.5,2,1,1,0.5,1,2,0.5,0.5],
              [1,2,1,1,1,2,0.5,1,0.5,2,1,2,1,1,1,1,0.5,1],
              [0,1,1,1,1,1,1,1,1,1,2,1,1,2,1,0.5,0.5,1],
              [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,0.5,0],
              [1,1,1,1,1,1,0.5,1,1,1,2,1,1,2,1,0.5,0.5,0.5],
              [1,0.5,0.5,1,1,2,1,1,1,1,1,1,2,1,1,1,0.5,2],
              [1,0.5,1,1,1,1,2,0.5,1,1,1,1,1,1,2,2,0.5,1]]

    moveType = d[moveType]  # find the type of the move
    pokemonType = d[pokemonType]    # find the pokemon users type

    m = matrix[moveType][pokemonType]

    return m


def getMovePSDictionary(move):
    # dictionary that has all attacks in there respective typing attacks
    d = {'Physical': ['Aerial Ace', 'Bite', 'Brick Break', 'Bug Bite', 'Close Combat', 'Dragon Claw', 'Dragon Pulse', \
                      'Earthquake', 'Fire Fang', 'Ice Punch', 'Karate Chop', 'Metal Claw', 'Nuzzle', \
                      'Quick Attack', 'Razor Leaf', 'Scratch', 'Seed Bomb', 'Slash', 'Spark', 'Stone Edge', \
                      'Tackle', 'Take Down', 'Thrash', 'Vine Whip'], \
         'Special': ['Aura Sphere', 'Confusion', 'Dark Pulse', 'Dragon Breath', 'Ember', 'Flamethrower', \
                     'Gust', 'Ice Beam', 'Thunderbolt', 'Thunder Shock', 'Water Gun', 'Water Pulse'], \
         'Other': ['Splash']}

    for i in d:  # REQUIRMENT
        if move in d[i]:  # returns key
            return i


def getDamageDictionary():
    # dictionary that has all power totals and what moves have that amount of power.
    d = {0: ['Splash'], \
         20: ['Nuzzle'], \
         40: ['Acid', 'Brick Break', 'Ember', 'Gust', 'Quick Attack', 'Scratch', 'Tackle', 'Thunder Shock', 'Vine Whip',
              'Water Gun'], \
         50: ['Confusion', 'Dragon Claw', 'Ice Punch', 'Karate Chop', 'Metal Claw'], \
         55: ['Aerial Ace', 'Razor Leaf'], \
         60: ['Bite', 'Bug Bite', 'Dragon Breath', 'Water Pulse'], \
         65: ['Fire Fang', 'Spark'], \
         70: ['Slash'], \
         80: ['Aura Sphere', 'Dark Pulse', 'Thunderbolt', 'Seed Bomb'], \
         85: ['Dragon Pulse'], \
         90: ['Flamethrower', 'Ice Beam', 'Take Down'], \
         100: ['Earthquake', 'Stone Edge'], \
         120: ['Close Combat', 'Thrash']}

    return d


def getMoveDictionary():
    ''' Move dictionary for types'''

    # dictionary of all pokemon types and moves that correspond REQUIREMENT
    d = {'Bug': ['Bug Bite'], \
         'Dark': ['Bite', 'Dark Pulse'], \
         'Fighting': ['Aura Sphere', 'Brick Break', 'Close Combat', 'Karate Chop'], \
         'Fire': ['Ember', 'Fire Fang', 'Flamethrower'], \
         'Grass': ['Razor Leaf', 'Seed Bomb', 'Vine Whip'], \
         'Ground': ['Earthquake'], \
         'Water': ['Aqua Jet', 'Splash', 'Water Gun', 'Water Pulse'], \
         'Normal': ['Tackle', 'Take Down', 'Thrash', 'Scratch', 'Slash', 'Quick Attack'], \
         'Poison': ['Acid'], \
         'Flying': ['Aerial Ace', 'Gust'], \
         'Rock': ['Stone Edge'], \
         'Electric': ['Thunderbolt', 'Thunder Shock', 'Spark'], \
         'Dragon': ['Dragon Breath', 'Dragon Claw', 'Dragon Pulse'], \
         'Ice': ['Ice Beam', 'Ice Punch'], \
         'Steel': ['Metal Claw'], \
         'Psychic': ['Confusion']}

    return d

def getMoveType(move):
    ''' Used in damage calculating function. Returns the type of the move used'''

    d = getMoveDictionary()  # contains a dictionary of the types corresponding moves

    for i in d:
        if move in d[i]:  # checks if move is in the values of key
            return i  # return key (type)



def countNumTypes(listOfTypes):     # REQUIREMENT

    if len(listOfTypes) == 0:
        return 0
    if listOfTypes[0] == 'None':
        return 0 + countNumTypes(listOfTypes[1:])
    else:
        return 1 + countNumTypes(listOfTypes[1:])