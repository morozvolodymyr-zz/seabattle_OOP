from random import randint
import sys

import datetime


class Game:
    def __init__(self, player1, player2):
        self.pl1 = player1
        self.pl2 = player2

    def start_game(self):
        self.pl1.set_ships()
        self.pl2.set_ships()
        self.pl1.field_enemy = self.pl2.field_own
        self.pl2.field_enemy = self.pl1.field_own
        while True:
            while True:
                x, y = self.pl1.input_coordinates()
                if self.pl1.no_shoot(x, y):
                    if self.pl1.wound(x, y):
                        print('wounded!')
                        self.pl1.print_fields()
                        if self.pl1.kill(x, y):
                            print('killed!')
                            self.pl1.print_fields()
                            if self.pl1.is_win():
                                print('player1 is win!')
                                sys.exit()
                    if self.pl1.no_ship(x, y):
                        break
                else:
                    print('shoot again!')
            self.pl1.print_fields()

            while True:
                x, y = self.pl2.input_coordinates()
                if self.pl2.no_shoot(x, y):
                    if self.pl2.wound(x, y):
                        print('wounded!')
                        self.pl1.print_fields()
                        if self.pl2.kill(x, y):
                            print('killed!')
                            self.pl1.print_fields()
                            if self.pl2.is_win():
                                print('player2 is win!')
                                sys.exit()
                    if self.pl2.no_ship(x, y):
                        break
                else:
                    print('shoot again!')
            self.pl1.print_fields()


class Player:
    def __init__(self):
        self.field_own = Field()
        self.field_enemy = Field()

    def set_ships(self):
        pass

    def input_coordinates(self):
        pass

    def no_shoot(self, x, y):
        return self.field_enemy.no_shoot(x, y)

    def wound(self, x, y):
        return self.field_enemy.wound(x, y)

    def print_fields(self):
        self.field_own.print_field()
        self.field_enemy.print_field()

    def kill(self, x, y):
        return self.field_enemy.kill(x, y)

    def no_ship(self, x, y):
        return self.field_enemy.no_ship(x, y)

    def is_win(self):
        return self.field_enemy.is_win()


class Human(Player):
    def __init__(self):
        Player.__init__(self)

    def set_ships(self):
        for i in range(1):
            print('set ship 4')
            s = Ship(4)
            print('set coordinates of ship 4')
            for j in range(0, s.num):
                x, y = self.input_coordinates()
                self.field_own.cells[x][y] = 'o'
                self.field_own.print_field()
        for i in range(2):
            print('set ship 3')
            s = Ship(3)
            print('set coordinates of ship 3')
            for j in range(0, s.num):
                x, y = self.input_coordinates()
                self.field_own.cells[x][y] = 'o'
                self.field_own.print_field()
        for i in range(3):
            print('set ship 2')
            s = Ship(2)
            print('set coordinates of ship 2')
            for j in range(0, s.num):
                x, y = self.input_coordinates()
                self.field_own.cells[x][y] = 'o'
                self.field_own.print_field()
        for i in range(4):
            print('set ship 1')
            s = Ship(1)
            print('set coordinates of ship 1')
            for j in range(0, s.num):
                x, y = self.input_coordinates()
                self.field_own.cells[x][y] = 'o'
                self.field_own.print_field()

    def input_coordinates(self):
        x = 0
        y = 0
        while True:
            print('enter coordinates x and y')
            x = int(input())
            y = int(input())
            if 0 <= x <= 9 and 0 <= y <= 9:
                break
        return x, y


class Computer(Player):
    def __init__(self):
        Player.__init__(self)

    def set_ships(self):
        ships = [Ship(4), Ship(3), Ship(3), Ship(2), Ship(2), Ship(2), Ship(1), Ship(1), Ship(1), Ship(1)]

        for s in ships:
            while True:
                x, y = self.input_coordinates()

                k = True
                if x - s.num + 1 >= 0 and self.check_around(x, y):
                    for j in range(s.num):
                        x_temp = x - j
                        if self.field_own.cells[x_temp][y] == 'o' or (
                                            0 <= x_temp - 1 <= 9 and self.field_own.cells[x_temp - 1][y] == 'o') or (
                                            0 <= y + 1 <= 9 and self.field_own.cells[x_temp][y + 1] == 'o') or (
                                            0 <= y - 1 <= 9 and self.field_own.cells[x_temp][y - 1] == 'o') or (
                                                0 <= x_temp + 1 <= 9 and 0 <= y + 1 <= 9 and
                                        self.field_own.cells[x_temp + 1][
                                                y + 1] == 'o') or (
                                                0 <= x_temp + 1 <= 9 and 0 <= y - 1 <= 9 and
                                        self.field_own.cells[x_temp + 1][
                                                y - 1] == 'o') or (
                                                0 <= x_temp - 1 <= 9 and 0 <= y + 1 <= 9 and
                                        self.field_own.cells[x_temp - 1][
                                                y + 1] == 'o') or (
                                                0 <= x_temp - 1 <= 9 and 0 <= y - 1 <= 9 and
                                        self.field_own.cells[x_temp - 1][
                                                y - 1] == 'o'):
                            k = False
                            break
                        else:
                            self.field_own.cells[x_temp][y] = 'o'
                else:
                    k = False
                if k is True:
                    break

                k = True
                if y - s.num + 1 >= 0 and self.check_around(x, y):
                    for j in range(s.num):
                        y_temp = y - j
                        if self.field_own.cells[x][y_temp] == 'o' or (
                                            0 <= x + 1 <= 9 and self.field_own.cells[x + 1][y_temp] == 'o') or (
                                            0 <= x - 1 <= 9 and self.field_own.cells[x - 1][y_temp] == 'o') or (
                                            0 <= y_temp - 1 <= 9 and self.field_own.cells[x][y_temp - 1] == 'o') or (
                                                0 <= x + 1 <= 9 and 0 <= y_temp + 1 <= 9 and
                                        self.field_own.cells[x + 1][
                                                y_temp + 1] == 'o') or (
                                                0 <= x + 1 <= 9 and 0 <= y_temp - 1 <= 9 and
                                        self.field_own.cells[x + 1][
                                                y_temp - 1] == 'o') or (
                                                0 <= x - 1 <= 9 and 0 <= y_temp + 1 <= 9 and
                                        self.field_own.cells[x - 1][
                                                y_temp + 1] == 'o') or (
                                                0 <= x - 1 <= 9 and 0 <= y_temp - 1 <= 9 and
                                        self.field_own.cells[x - 1][
                                                y_temp - 1] == 'o'):
                            k = False
                            break
                        else:
                            self.field_own.cells[x][y_temp] = 'o'
                else:
                    k = False
                if k is True:
                    break

                k = True
                if x + s.num - 1 <= 9 and self.check_around(x, y):
                    for j in range(s.num):
                        x_temp = x + j
                        if self.field_own.cells[x_temp][y] == 'o' or (
                                            0 <= x_temp + 1 <= 9 and self.field_own.cells[x_temp + 1][y] == 'o') or (
                                            0 <= y + 1 <= 9 and self.field_own.cells[x_temp][y + 1] == 'o') or (
                                            0 <= y - 1 <= 9 and self.field_own.cells[x_temp][y - 1] == 'o') or (
                                                0 <= x_temp + 1 <= 9 and 0 <= y + 1 <= 9 and
                                        self.field_own.cells[x_temp + 1][
                                                y + 1] == 'o') or (
                                                0 <= x_temp + 1 <= 9 and 0 <= y - 1 <= 9 and
                                        self.field_own.cells[x_temp + 1][
                                                y - 1] == 'o') or (
                                                0 <= x_temp - 1 <= 9 and 0 <= y + 1 <= 9 and
                                        self.field_own.cells[x_temp - 1][
                                                y + 1] == 'o') or (
                                                0 <= x_temp - 1 <= 9 and 0 <= y - 1 <= 9 and
                                        self.field_own.cells[x_temp - 1][
                                                y - 1] == 'o'):
                            k = False
                            break
                        else:
                            self.field_own.cells[x_temp][y] = 'o'
                else:
                    k = False
                if k is True:
                    break

                k = True
                if y + s.num - 1 <= 0 and self.check_around(x, y):
                    for j in range(s.num):
                        y_temp = y + j
                        if self.field_own.cells[x][y_temp] == 'o' or (
                                            0 <= x + 1 <= 9 and self.field_own.cells[x + 1][y_temp] == 'o') or (
                                            0 <= x - 1 <= 9 and self.field_own.cells[x - 1][y_temp] == 'o') or (
                                            0 <= y_temp + 1 <= 9 and self.field_own.cells[x][y_temp + 1] == 'o') or (
                                                0 <= x + 1 <= 9 and 0 <= y_temp + 1 <= 9 and
                                        self.field_own.cells[x + 1][
                                                y_temp + 1] == 'o') or (
                                                0 <= x + 1 <= 9 and 0 <= y_temp - 1 <= 9 and
                                        self.field_own.cells[x + 1][
                                                y_temp - 1] == 'o') or (
                                                0 <= x - 1 <= 9 and 0 <= y_temp + 1 <= 9 and
                                        self.field_own.cells[x - 1][
                                                y_temp + 1] == 'o') or (
                                                0 <= x - 1 <= 9 and 0 <= y_temp - 1 <= 9 and
                                        self.field_own.cells[x - 1][
                                                y_temp - 1] == 'o'):
                            k = False
                            break
                        else:
                            self.field_own.cells[x][y_temp] = 'o'
                else:
                    k = False
                if k is True:
                    break
        self.field_own.print_field()

    def check_around(self, x, y):
        if self.field_own.cells[x][y] == 'o' or (
                            0 <= x + 1 <= 9 and self.field_own.cells[x + 1][y] == 'o') or (
                            0 <= x - 1 <= 9 and self.field_own.cells[x - 1][y] == 'o') or (
                            0 <= y + 1 <= 9 and self.field_own.cells[x][y + 1] == 'o') or (
                            0 <= y - 1 <= 9 and self.field_own.cells[x][y - 1] == 'o') or (
                                0 <= x + 1 <= 9 and 0 <= y + 1 <= 9 and
                        self.field_own.cells[x + 1][
                                y + 1] == 'o') or (
                                0 <= x + 1 <= 9 and 0 <= y - 1 <= 9 and
                        self.field_own.cells[x + 1][
                                y - 1] == 'o') or (
                                0 <= x - 1 <= 9 and 0 <= y + 1 <= 9 and
                        self.field_own.cells[x - 1][
                                y + 1] == 'o') or (
                                0 <= x - 1 <= 9 and 0 <= y - 1 <= 9 and
                        self.field_own.cells[x - 1][
                                y - 1] == 'o'):
            return False
        else:
            return True

    def input_coordinates(self):
        x = randint(0, 9)
        y = randint(0, 9)
        return x, y


class Field:
    def __init__(self):
        self.cells = []
        for i in range(0, 10):
            temp = []
            for j in range(0, 10):
                temp.append(Cell().state)
            self.cells.append(temp)

    def no_shoot(self, x, y):
        if self.cells[x][y] != '-':
            return True
        return False

    def wound(self, x, y):
        if self.cells[x][y] == 'o':
            self.cells[x][y] = 'X'
            return True
        return False

    def kill(self, x, y):
        if (0 <= x + 1 <= 9 and self.cells[x + 1][y] == 'o') or (0 <= x - 1 <= 9 and self.cells[x - 1][y] == 'o') or (
                            0 <= y + 1 <= 9 and self.cells[x][y + 1] == 'o') or (
                            0 <= y - 1 <= 9 and self.cells[x][y - 1] == 'o'):
            return False
        x_temp = x
        if 0 <= x_temp + 1 <= 9 and self.cells[x_temp + 1][y] == 'X':
            while 0 <= x_temp + 1 <= 9 and self.cells[x_temp][y] == 'X':
                if self.cells[x_temp + 1][y] == 'o':
                    return False
                x_temp += 1
        x_temp = x
        if 0 <= x_temp - 1 <= 9 and self.cells[x_temp - 1][y] == 'X':
            while 0 <= x_temp - 1 <= 9 and self.cells[x_temp][y] == 'X':
                if self.cells[x_temp - 1][y] == 'o':
                    return False
                x_temp -= 1
        y_temp = y
        if 0 <= y_temp + 1 <= 9 and self.cells[x][y_temp + 1] == 'X':
            while 0 <= y_temp + 1 <= 9 and self.cells[x][y_temp] == 'X':
                if self.cells[x][y_temp + 1] == 'o':
                    return False
                y_temp += 1
        y_temp = y
        if 0 <= y_temp - 1 <= 9 and self.cells[x][y_temp - 1] == 'X':
            while 0 <= y_temp - 1 <= 9 and self.cells[x][y_temp] == 'X':
                if self.cells[x][y_temp - 1] == 'o':
                    return False
                y_temp -= 1

        self.change_to_x(x, y)
        while 0 <= x + 1 <= 9 and self.cells[x + 1][y] == 'X':
            self.change_to_x(x + 1, y)
            x += 1
        while 0 <= x - 1 <= 9 and self.cells[x - 1][y] == 'X':
            self.change_to_x(x - 1, y)
            x -= 1
        while 0 <= y + 1 <= 9 and self.cells[x][y + 1] == 'X':
            self.change_to_x(x, y + 1)
            y += 1
        while 0 <= y - 1 <= 9 and self.cells[x][y - 1] == 'X':
            self.change_to_x(x, y - 1)
            y -= 1

        return True

    def no_ship(self, x, y):
        if self.cells[x][y] == ' ':
            self.cells[x][y] = '-'
            return True
        return False

    def is_win(self):
        for x in range(10):
            for y in range(10):
                if self.cells[x][y] == 'o':
                    return False
        return True

    def print_field(self):
        for x in range(10):
            print(self.cells[x])
        print('\n')

    def change_to_x(self, x, y):
        if 0 <= x + 1 <= 9 and self.cells[x + 1][y] == ' ':
            self.cells[x + 1][y] = '-'
        if 0 <= x - 1 <= 9 and self.cells[x - 1][y] == ' ':
            self.cells[x - 1][y] = '-'
        if 0 <= y + 1 <= 9 and self.cells[x][y + 1] == ' ':
            self.cells[x][y + 1] = '-'
        if 0 <= y - 1 <= 9 and self.cells[x][y - 1] == ' ':
            self.cells[x][y - 1] = '-'
        if 0 <= x + 1 <= 9 and 0 <= y + 1 <= 9 and self.cells[x + 1][y + 1] == ' ':
            self.cells[x + 1][y + 1] = '-'
        if 0 <= x + 1 <= 9 and 0 <= y - 1 <= 9 and self.cells[x + 1][y - 1] == ' ':
            self.cells[x + 1][y - 1] = '-'
        if 0 <= x - 1 <= 9 and 0 <= y + 1 <= 9 and self.cells[x - 1][y + 1] == ' ':
            self.cells[x - 1][y + 1] = '-'
        if 0 <= x - 1 <= 9 and 0 <= y - 1 <= 9 and self.cells[x - 1][y - 1] == ' ':
            self.cells[x - 1][y - 1] = '-'


class Cell:
    def __init__(self):
        self.state = ' '
        return


class Ship:
    def __init__(self, number):
        self.num = number


def main():
    b = datetime.datetime.now()
    player1 = Computer()
    player2 = Computer()
    game = Game(player1, player2)
    game.start_game()
    e = datetime.datetime.now()
    print(e - b)


main()
