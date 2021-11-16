# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 10:35:11 2019

Final Project II - Pocket Monsters

Authors@author: Kenneth Tang and Nathan Tran
@email: ketang@clarku.edu / natran@clarku.edu

"""
import random
import dictionaries
import initialize


# from playsound import playsound


class Battle:

    def __init__(self, p1, p2):
        ''' initializes state of the battle with the active pokemon p1 and p2
            being from the Pokemon class.
        '''
        # Active Pokemon for player 1 and player 2
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):

        # display to the console the health of rival and player. displayed in form of current / total
        s1 = f"{self.p2.p}: {self.p2.ap.n} (LVL: {self.p2.ap.l}) (HP: {self.p2.ap.hp}/{self.p2.ap.thp})\n"  # Rival's Active pokemon health
        s2 = f"{self.p1.p}(You): {self.p1.ap.n} (LVL: {self.p1.ap.l}) (HP: {self.p1.ap.hp}/{self.p1.ap.thp})"  # Player's Active pokemon health
        return '\n' + s1 + '\n' + s2

    def p1action(self, move):
        """" processes the move that player 1 inputted"""

        x = dictionaries.getDamageDictionary()
        for i in x:
            if move in x[i]:  # looks for the move in each power catergory
                power = i

        # damage done to rival's active pokemon
        ps = dictionaries.getMovePSDictionary(move)
        if ps == 'Physical':

            damage = (((2 * self.p1.ap.l / 5 + 2) * power * self.p1.ap.a / self.p2.ap.d) / 50) + 2  # damage calculator
        elif ps == 'Special':
            damage = (((
                               2 * self.p1.ap.l / 5 + 2) * power * self.p1.ap.spa / self.p2.ap.spd) / 50) + 2  # damage calculator
        else:
            damage = 0
        # tests if critical strike occurs (1/16 chance), if yes, damage * 1.5
        critchance = random.randint(84, 100)
        if critchance == 100:
            damage *= 1.5
            critchance = True

        # tests if move type matches active pokemon's type, if yes, damage * 1.5
        x = dictionaries.getMoveType(move)
        if x in self.p1.ap.t:  # checks if the type of the move is type of the pokemon
            damage *= 1.5

        # tests type dictionaries.effectiveness
        numTypes = dictionaries.countNumTypes(self.p2.ap.t)
        y = 1
        for k in range(numTypes):
            y *= dictionaries.effectiveness(self.p2.ap.t[k], x)
        damage *= y

        damage = round(damage)  # rounded to nearest integer
        self.p2.ap.hp -= damage  # subtracts damage from health of player 2's active pokemon
        if self.p2.ap.hp < 0:
            self.p2.ap.hp = 0
        print('\n--You used ' + move + '!')

        if damage == 0 and move == 'Splash':
            print('\n--But it did nothing!')

        if y == 0:
            print('\n--It had no effect!')

        if y > 0 and y < 1:
            print("\n--It wasn't very effective.")

        if y > 1:
            print('\n--It was super effective!')

        if critchance == True:
            print('\n--A critical hit!')

    def p2action(self, move):
        """ processes the move that player 1 inputted """

        x = dictionaries.getDamageDictionary()
        for i in x:
            if move in x[i]:  # looks for the move in each power catergory
                power = i

        # damage done to rival's active pokemon
        ps = dictionaries.getMovePSDictionary(move)
        if ps == 'Physical':

            damage = (((2 * self.p1.ap.l / 5 + 2) * power * self.p2.ap.a / self.p1.ap.d) / 50) + 2  # damage calculator
        elif ps == 'Special':
            damage = (((
                               2 * self.p1.ap.l / 5 + 2) * power * self.p2.ap.spa / self.p1.ap.spd) / 50) + 2  # damage calculator
        else:
            damage = 0
        # tests if critical strike occurs (1/16 chance), if yes, damage * 1.5
        critchance = random.randint(84, 100)
        if critchance == 100:
            damage *= 1.5
            critchance = True

        # tests if move type matches active pokemon's type, if yes, damage * 1.5
        x = dictionaries.getMoveType(move)
        if x in self.p2.ap.t:  # checks to see if move type is the same as pokemon type
            damage *= 1.5

        # tests type dictionaries.effectiveness
        numTypes = dictionaries.countNumTypes(self.p1.ap.t)
        y = 1
        for k in range(numTypes):
            y *= dictionaries.effectiveness(self.p1.ap.t[k], x)

        damage *= y
        damage = round(damage)  # rounded to nearest integer
        self.p1.ap.hp -= damage  # subtracts damage from health of player 1's active pokemon
        if self.p1.ap.hp < 0:
            self.p1.ap.hp = 0
        print('\n--Your rival used ' + move + '!')

        if damage == 0 and move == 'Splash':
            print('\n--But it did nothing!')

        if y == 0:
            print('\n--It had no effect!')

        if y > 0 and y < 1:
            print("\n--It wasn't very effective.")

        if y > 1:
            print('\n--It was super effective!')

        if critchance == True:
            print('\n--A critical hit!')


def main():
    """ user interface to interact with program"""

    print('\nHello. Welcome to the development beta of our final project for CS 120 at Clark University. '
          + 'Our project is a Pokemon Battle Simulation using what we"ve learned in CS120. '
          + 'Press "q" anytime to quit or go back.')
    print("-----------------------------------------------------------------------------------------")

    # reads from spreadsheet and initializes pokemon
    stats = initialize.PokeStats('PokemonRoster0.csv')

    players = initialize.Roster(stats)

    # initializes Battle class that interacts with active pokemon
    c = Battle(players[1], players[2])
    print(c)
    # playsound('Rival Theme.mp3', 0)

    while True:  # REQUIREMENT

        # prevents players from wrong inputs to switch Pokemon when active Pokemon is dead
        if c.p1.ap.hp < 1:

            choice2 = input(
                '*Party:\n[' + str(c.p1.pp1.n) + ' (LVL: ' + str(c.p1.pp1.l) + ') (HP: ' + str(c.p1.pp1.hp) + '/' + str(
                    c.p1.pp1.thp) + ') = "1"] [' \
                + str(c.p1.pp2.n) + ' (LVL: ' + str(c.p1.pp2.l) + ') (HP: ' + str(c.p1.pp2.hp) + '/' + str(
                    c.p1.pp2.thp) + ') = "2"] \n')

            if choice2 == '1':  # switches to party Pokemon 1
                p1SwitchToPP1(c)

            elif choice2 == '2':  # switches to party Pokemon 2
                p1SwitchToPP2(c)
            else:
                print('\nPlease choose a Pokemon.')

        # where the code really starts
        else:

            choice = input('*Please choose your input: \n[Attack = "a"] [Party = "p"] [Quit = "q"] \n')

            if choice == 'q':  # quits the game
                print('\nThis simulation was made by Kenneth Tang and Nathan Tran. ' \
                      'Thanks for playing!')
                break

            elif choice == 'a':

                choice2 = input('*Please choose your move: \n[' + str(c.p1.ap.m[0]) + ' = "1"] [' + str(
                    c.p1.ap.m[1]) + ' = "2"] [' + str(c.p1.ap.m[2]) + ' = "3"] [' + str(c.p1.ap.m[3]) + ' = "4"] \n')

                if choice2 in ['1', '2', '3', '4']:

                    # player 1 uses 1a move. Currently each Pokemon can also use one move
                    if str(c.p1.ap.m[int(choice2) - 1]) == 'Quick Attack':
                        if not p1FirstProcessTurn(c, str(c.p1.ap.m[int(choice2) - 1])):
                            print('\nThis simulation was made by Kenneth Tang and Nathan Tran. ' \
                                  'Thanks for playing!')
                            break

                    elif str(c.p2.ap.m[int(choice2) - 1]) == 'Quick Attack':
                        if not p2FirstProcessTurn(c, str(c.p1.ap.m[int(choice2) - 1])):
                            print('\nThis simulation was made by Kenneth Tang and Nathan Tran. ' \
                                  'Thanks for playing!')
                            break

                    elif c.p1.ap.s >= c.p2.ap.s:  # if the speed of player's pokemon is faster

                        if not p1FirstProcessTurn(c, str(c.p1.ap.m[int(choice2) - 1])):
                            print('\nThis simulation was made by Kenneth Tang and Nathan Tran. ' \
                                  'Thanks for playing!')
                            break

                    else:  # if rival pokemon is faster
                        if not p2FirstProcessTurn(c, str(c.p1.ap.m[int(choice2) - 1])):
                            print('\nThis simulation was made by Kenneth Tang and Nathan Tran. ' \
                                  'Thanks for playing!')
                            break

                else:
                    print("\n" + "That's not a valid choice yet. Try again.")

            elif choice == 'p':
                # menu, pulls up the Pokemon currently in your party
                choice2 = input('*Party:\n[' + str(c.p1.pp1.n) + ' (LVL: ' + str(c.p1.pp1.l) + ') (HP: ' + \
                                str(c.p1.pp1.hp) + '/' + str(c.p1.pp1.thp) + ') = "1"] [' + str(c.p1.pp2.n) + \
                                ' (LVL: ' + str(c.p1.pp2.l) + ') (HP: ' + str(c.p1.pp2.hp) + '/' + str(
                    c.p1.pp2.thp) + ') = "2"] \n')

                if choice2 == '1':
                    p1SwitchToPP1(c)  # switches to party Pokemon 1
                    c.p2action(c.p2.ap.m[random.randint(0, 3)])  # takes damage for switching
                    print(c)

                elif choice2 == '2':
                    p1SwitchToPP2(c)  # switches to party Pokemon 2
                    c.p2action(c.p2.ap.m[random.randint(0, 3)])  # takes damage for switching
                    print(c)
            else:
                print("\n" + "That's not a valid choice. Try again.")


def p1SwitchToPP1(c):
    """ Switches to party Pokemon 1 by calling a method in Player"""

    # check hp of party Pokemon 1
    if c.p1.pp1.hp < 1:
        print('\n' + '--This Pokemon fainted already!')

    # executes switch
    else:
        c.p1.switchToParty(1)
        print('\n' + '--Switch! You can do it ' + str(c.p1.ap.n) + '!')
        print(c)


def p1SwitchToPP2(c):
    """ Switches to party Pokemon 2 by calling a method in Player"""

    # checks hp of party Pokemon 2
    if c.p1.pp2.hp < 1:
        print('\n' + '--This Pokemon fainted already!')

    # executes switch
    else:
        c.p1.switchToParty(2)
        print('\n' + "--Switch! I'm counting on you " + str(c.p1.ap.n) + "!")
        print(c)


def p2PartyRandomSwitch(c):
    switchChance = random.randint(0, 1)

    if switchChance == 0:

        c.p2.switchToParty(1)
        p2FaintedChoice(c)
        print('\n' + "--Your opponent sent out " + str(c.p2.ap.n) + "!")
        print(c)
        return True
    else:

        c.p2.switchToParty(2)
        p2FaintedChoice(c)
        print('\n' + "--Your opponent sent out " + str(c.p2.ap.n) + "!")
        print(c)
        return True


def apFaintedChoice1(c):
    if c.p1.pp1.hp >= 1:  # if the party pokemon 1 is alive then switch.

        c.p1.switchToParty(1)  # make party pokemon 1 the active pokemon.

        print('\n' + '--You got this ' + str(c.p1.ap.n) + '!')
        print(c)
        return True

    else:  # if the party pokemon 1 is fainted
        print('This Pokemon already fainted!')
        return True


def apFaintedChoice2(c):
    if c.p1.pp2.hp >= 1:  # if the party pokemon 2 is alive then switch

        c.p1.switchToParty(2)  # make party pokemon 2 the active pokemon

        print('\n' + '--I believe in you, ' + str(c.p1.ap.n) + '!')
        print(c)
        return True

    else:  # if the party pokemon 2 fainted
        print('This Pokemon already fainted!')
        return True


def p2FaintedChoice(c):
    print('\n' + "Your opponent's Pokemon fainted!")
    choice = input('Your opponent is about to send out ' + str(c.p2.ap.n) + \
                   '. Would you like to switch Pokemon?' + '\n' + \
                   '[Yes = "y"] [No = "n"]' + '\n')
    if choice == 'y':  # provide the prompt of which pokemon to choose.
        choice2 = input('*Party:\n[' + str(c.p1.pp1.n) + ' (LVL: ' + str(c.p1.pp1.l) + \
                        ') (HP: ' + str(c.p1.pp1.hp) + '/' + str(c.p1.pp1.thp) + ') = "1"] [' \
                        + str(c.p1.pp2.n) + ' (LVL: ' + str(c.p1.pp2.l) + ') (HP: ' + \
                        str(c.p1.pp2.hp) + '/' + str(c.p1.pp2.thp) + ') = "2"] [Back = "q"]\n')

        if choice2 == '1':
            p1SwitchToPP1(c)  # switches to party Pokemon 1


        elif choice2 == '2':
            p1SwitchToPP2(c)  # switches to party Pokemon 2


def p1FirstProcessTurn(c, p1Move):
    """ Executes if player inputs a move from Attack choice, and their active
        Pokemon's speed is higher than opponent
    """

    # method processes move for damage
    c.p1action(p1Move)
    print(c)
    if c.p2.ap.hp < 1:  # if player 2's active pokemon's hp is less than 1, or fainted

        if c.p2.pp1.hp < 1 and c.p2.pp2.hp < 1:  # if both of the rival's party pokemon is fainted, then player 1 wins
            print('\n' + 'You won!')
            return False
        # if both party Pokemon are still alive, send one out randomly
        elif c.p2.pp1.hp >= 1 and c.p2.pp2.hp >= 1:

            return p2PartyRandomSwitch(c)

        elif c.p2.pp1.hp >= 1:  # if the rival's first party Pokemon fainted, send out the second Pokemon

            # swapping active pokemon slot with party pokemon slot
            c.p2.switchToParty(1)
            # initializes Battle once active pokemon is updated
            p2FaintedChoice(c)

            print('\n' + "--Your opponent sent out " + str(c.p2.ap.n) + "!")
            print(c)
            return True

        elif c.p2.pp2.hp >= 1:  # if the rival's second party Pokemon fainted, send out the first Pokemon

            # swapping active pokemon slot with party pokemon slot
            c.p2.switchToParty(2)

            # initializes Battle once active pokemon is updated
            p2FaintedChoice(c)
            print('\n' + "--Your opponent sent out " + str(c.p2.ap.n) + "!" + '\n')
            print(c)
            return True

    else:
        # if player 2's pokemon does not faint, their move goes through

        c.p2action(c.p2.ap.m[random.randint(0, 3)])
        print(c)
        if c.p1.ap.hp < 1:  # when player 1's active pokemon faints
            print('\n--Your Pokemon fainted!')

            if c.p1.pp1.hp < 1 and c.p1.pp2.hp < 1:
                print('\n' + 'You lost!')
                return False

            # player decides what Pokemon to send out
            choice = input('*Party:\n[' + str(c.p1.pp1.n) + ' (LVL: ' + str(c.p1.pp1.l) + \
                           ') (HP: ' + str(c.p1.pp1.hp) + '/' + str(c.p1.pp1.thp) + ') = "1"] [' \
                           + str(c.p1.pp2.n) + ' (LVL: ' + str(c.p1.pp2.l) + ') (HP: ' + \
                           str(c.p1.pp2.hp) + '/' + str(c.p1.pp2.thp) + ') = "2"] \n')

            if choice == '1':  # switch to party Pokemon 1

                return apFaintedChoice1(c)

            elif choice == '2':  # switch to party Pokemon 2

                return apFaintedChoice2(c)

            else:
                print('\nPlease choose a Pokemon.')
                return True

        else:

            return True


def p2FirstProcessTurn(c, p1Move):
    '''
    Executes if player inputs a move from Attack choice, and their active
    Pokemon's speed is lower than opponent
    '''
    # method processes move for damage
    c.p2action(c.p2.ap.m[random.randint(0, 3)])
    print(c)
    if c.p1.ap.hp < 1:  # when player 1's active pokemon faints, similar behavior to player 2 above
        print('\n--Your Pokemon fainted!')

        if c.p1.pp1.hp < 1 and c.p1.pp2.hp < 1:
            print('\n' + 'You lost!')
            return False

        choice = input('*Party:\n[' + str(c.p1.pp1.n) + ' (LVL: ' + str(c.p1.pp1.l) + \
                       ') (HP: ' + str(c.p1.pp1.hp) + '/' + str(c.p1.pp1.thp) + ') = "1"] [' \
                       + str(c.p1.pp2.n) + ' (LVL: ' + str(c.p1.pp2.l) + ') (HP: ' + \
                       str(c.p1.pp2.hp) + '/' + str(c.p1.pp2.thp) + ') = "2"] \n')

        # player decides which Pokemon to send out
        if choice == '1':

            return apFaintedChoice1(c)

        elif choice == '2':

            return apFaintedChoice2(c)

        else:
            print('\nPlease choose a Pokemon.')
            return True


    else:
        # if player's active pokemon does not faint, their move goes through
        c.p1action(p1Move)
        print(c)
        if c.p2.ap.hp < 1:  # when rival's active pokemon faints, similar behavior to player above

            if c.p2.pp1.hp < 1 and c.p2.pp2.hp < 1:
                print('\n' + 'You Won!')
                return False

            # if both party Pokemon are still alive, send one out randomly
            elif c.p2.pp1.hp >= 1 and c.p2.pp2.hp >= 1:

                return p2PartyRandomSwitch(c)

            elif c.p2.pp1.hp >= 1:

                c.p2.switchToParty(1)
                p2FaintedChoice(c)
                print('\n' + "--Your opponent sent out " + str(c.p2.ap.n) + "!")
                print(c)
                return True

            elif c.p2.pp2.hp >= 1:

                c.p2.switchToParty(2)

                print('\n' + "--Your opponent sent out " + str(c.p2.ap.n) + "!")
                print(c)
                return True
        else:

            return True


if __name__ == "__main__":
    main()
