import re


class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.player_turn = None
        self.status = 'Game in progress.'
        self.print_board = '\n  -------------\n' +\
            '3 |   |   |   |\n' +\
            '  -------------\n' +\
            '2 |   |   |   |\n' +\
            '  -------------\n' +\
            '1 |   |   |   |\n' +\
            '  -------------\n' +\
            '    A   B   C  \n'

    def __setitem__(self, index_string, value):
        if not re.match(r'^[ABC][123]$', index_string):
            raise InvalidKey('Invalid key.')

        elif not re.match(r'^[XO]$', value):
            raise InvalidValue('Invalid value. Valid values are X and O.')

        index = self.string_into_digits(index_string)
        if self.player_turn is None:
            self.player_turn = value
            self.change_turn()

        if self.board[index[0]][index[1]] != ' ':
            raise InvalidMove('This place is already taken.')

        if value == self.player_turn:
            raise NotYourTurn("It's not your turn!")

        self.board[index[0]][index[1]] = value
        self.change_turn()
        if self.status != 'Game in progress.':
            return
        self.change_status(index[0], index[1], value)

    def __getitem__(self, index_string):
        if re.match(r'^[ABC][123]$', index_string):
            index = self.string_into_digits(index_string)
            return self.board[index[0]][index[1]]
        raise InvalidKey('Invalid key.')

    def game_status(self):
        return self.status

    def string_into_digits(self, index):
        result = []
        if index[0] == 'A':
            result.append(0)
        elif index[0] == 'B':
            result.append(1)
        elif index[0] == 'C':
            result.append(2)
        result.append(int(index[1]) - 1)
        return result

    def change_turn(self):
        if self.player_turn == 'O':
            self.player_turn = 'X'
        else:
            self.player_turn = 'O'

    def change_status(self, row, column, value):
        if (self.board[0][column] == value and
            self.board[1][column] == value and
            self.board[2][column] == value) or (self.board[row][0] == value and
                                                self.board[row][1] == value and
                                                self.board[row][2] == value):
            self.status = '{} wins!'.format(value)

        if (row != 2 or column == 2) and (row == 2 or column != 2):
            if (self.board[0][0] == value and self.board[1][1] == value and
                self.board[2][2] == value) or (self.board[0][2] == value and
                                               self.board[1][1] == value and
                                               self.board[2][0] == value):
                self.status = '{} wins!'.format(value)

        if self.board_is_full():
            self.status = 'Draw!'

    def board_is_full(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == ' ':
                    return False
        return True

    def __str__(self):
        self.print_board = '\n  -------------\n' +\
            '3 | {} | {} | {} |\n'.format(self.board[0][2], self.board[1][2],
                                          self.board[2][2]) +\
            '  -------------\n' +\
            '2 | {} | {} | {} |\n'.format(self.board[0][1], self.board[1][1],
                                          self.board[2][1]) +\
            '  -------------\n' +\
            '1 | {} | {} | {} |\n'.format(self.board[0][0], self.board[1][0],
                                          self.board[2][0]) +\
            '  -------------\n' +\
            '    A   B   C  \n'
        return self.print_board
