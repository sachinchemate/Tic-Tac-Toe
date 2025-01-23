from IPython.display import clear_output
import random


class Helper:

    def display_board(self, board):
        clear_output()  # Remember, this only works in jupyter!

        # print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        #print('   |   |')
        print('-----------')
        # print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        #print('   |   |')
        print('-----------')
        # print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        #print('   |   |')

    def player_input(self):
        marker = ''

        while not (marker == 'X' or marker == 'O'):
            marker = input('Player 1: Do you want to be X or O? ').upper()

        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')

    def place_marker(self, board, marker, position):
        board[position] = marker

    def win_check(self, board, mark):
        return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
                (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
                (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
                (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
                (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
                (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
                (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
                (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

    def choose_first(self):
        if random.randint(0, 1) == 0:
            return 'Player 2'
        else:
            return 'Player 1'

    def space_check(self, board, position):
        return board[position] == ' '

    def full_board_check(self, board):
        for i in range(1, 10):
            if self.space_check(self, board, i):
                return False
        return True

    def player_choice(self, board, player_name):
        position = 0

        while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not self.space_check(self, board, position):
            print('Whose Turn: ', player_name)
            position = int(input('Choose your next position: (1-9) '))

        return position

    @staticmethod
    def replay():
        return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
