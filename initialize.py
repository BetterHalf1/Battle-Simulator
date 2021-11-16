class Pokemon:  # REQUIREMENT NATHAN

    def __init__(self, name, hp, thp, lvl, att, de, spAtt, spDe, sp, typ, moves):
        ''' initializes a type of pokemon with its stats and characteristics'''

        self.n = name  # name
        self.hp = hp  # current health
        self.thp = thp  # total health
        self.l = lvl  # level
        self.a = att  # attack
        self.d = de  # defense
        self.spa = spAtt  # special attack
        self.spd = spDe  # special defense
        self.s = sp  # speed
        self.t = typ  # type
        self.m = moves  # moves

    def __repr__(self):
        # ex. ['Charmander', '20', '20', '5', '11', '10', '60', 'Fire', 'Scratch']
        s = '[' + str(self.n) + ', HP: ' + str(self.hp) + '/' + str(self.thp) + ', LVL: ' + \
            str(self.l) + ', ATT: ' + str(self.a) + ', DEF: ' + str(self.d) + ', TYPE: ' \
            + str(self.t) + ', MOVES: ' + str(self.m) + ']'
        return s

class Player:  # REQUIREMENT KENNETH

    def __init__(self, player, activePokemon, partyPokemon1, partyPokemon2):
        ''' initializes the state of the player's active and party Pokemon'''

        self.p = player  # player name
        self.ap = activePokemon  # active pokemon
        self.pp1 = partyPokemon1  # party pokemon 1
        self.pp2 = partyPokemon2  # party pokemon 2

    def __repr__(self):
        # ex. ['Player1', 'Charmander', 'Pikachu', 'Squirtle']
        s = '[' + str(self.p) + ', *' + str(self.ap) + ', ' + str(self.pp1) + ', ' + \
            str(self.pp2) + ']'
        return s

    def switchToParty(self, ptynum):
        ''' switches out activePokemon with partyPokemon1'''
        buffer = ''
        if ptynum == 1:
            buffer = self.ap
            self.ap = self.pp1
            self.pp1 = buffer
        if ptynum == 2:
            buffer = self.ap
            self.ap = self.pp2
            self.pp2 = buffer

        return self

def PokeStats(filename):
    """Opens the file containing all the stats and returns a list of list with all the stats."""

    grid = []  # make the empty list
    file = open(filename, 'r')

    file.readline()  # read the header and throw away

    for line in file:

        if line[-1] == '\n':
            line = line[:-1]  # removes the '\n' from the end of each line

        line = line.split(',')  # splits the line up into list dividing by ','
        grid.append(line)  # add the pokemon and its stats list as another element of the list

    file.close()
    return (grid)


def Roster(stats):
    # player 1 active pokemon out in battle, within the Battle class
    p1active = Pokemon(str(stats[0][0]), int(stats[0][1]), int(stats[0][2]), int(stats[0][3]), int(stats[0][4]),
                       int(stats[0][5]), int(stats[0][6]), int(stats[0][7]), int(stats[0][8]), stats[0][9].split('/'),
                       (stats[0][10]).split('/'))
    # player 1 party pokemon
    p1party1 = Pokemon(str(stats[1][0]), int(stats[1][1]), int(stats[1][2]), int(stats[1][3]), int(stats[1][4]),
                       int(stats[1][5]), int(stats[1][6]), int(stats[1][7]), int(stats[1][8]), stats[1][9].split('/'),
                       (stats[1][10]).split('/'))
    p1party2 = Pokemon(str(stats[2][0]), int(stats[2][1]), int(stats[2][2]), int(stats[2][3]), int(stats[2][4]),
                       int(stats[2][5]), int(stats[2][6]), int(stats[2][7]), int(stats[2][8]), stats[2][9].split('/'),
                       (stats[2][10]).split('/'))

    # player 2 active pokemon out in battle, within the Battle class
    p2active = Pokemon(str(stats[3][0]), int(stats[3][1]), int(stats[3][2]), int(stats[3][3]), int(stats[3][4]),
                       int(stats[3][5]), int(stats[3][6]), int(stats[3][7]), int(stats[3][8]), stats[3][9].split('/'),
                       (stats[3][10]).split('/'))
    # player 2 party pokemon
    p2party1 = Pokemon(str(stats[4][0]), int(stats[4][1]), int(stats[4][2]), int(stats[4][3]), int(stats[4][4]),
                       int(stats[4][5]), int(stats[4][6]), int(stats[4][7]), int(stats[4][8]), stats[4][9].split('/'),
                       (stats[4][10]).split('/'))
    p2party2 = Pokemon(str(stats[5][0]), int(stats[5][1]), int(stats[5][2]), int(stats[5][3]), int(stats[5][4]),
                       int(stats[5][5]), int(stats[5][6]), int(stats[5][7]), int(stats[5][8]), stats[5][9].split('/'),
                       (stats[5][10]).split('/'))

    p1name = str(stats[6][1])
    p2name = str(stats[6][3])

    roster = [p1name, p1active, p1party1, p1party2, p2name, p2active, p2party1, p2party2]
    player1 = Player(roster[0], roster[1], roster[2], roster[3])
    player2 = Player(roster[4], roster[5], roster[6], roster[7])

    return [' ', player1, player2]