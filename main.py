# This is a sample Python script.

from com.hello.game.utility.helper import Helper

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def play(self):
    while True:
        # Reset the board
        theBoard = [' '] * 10
        player1_marker, player2_marker = Helper.player_input(self)
        turn = Helper.choose_first(self)
        print(turn + ' will go first.')

        play_game = input('Are you ready to play? Enter Yes or No.')

        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                # Player1's turn.

                Helper.display_board(self,theBoard)
                position = Helper.player_choice(self,theBoard,turn)
                Helper.place_marker(self,theBoard, player1_marker, position)

                if Helper.win_check(self,theBoard, player1_marker):
                    Helper.display_board(self,theBoard)
                    print('Congratulations! You have won the game!')
                    game_on = False
                else:
                    if Helper.full_board_check(self,theBoard):
                        Helper.display_board(self,theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:
                # Player2's turn.

                Helper.display_board(self,theBoard)
                position = Helper.player_choice(self,theBoard,turn)
                Helper.place_marker(self,theBoard, player2_marker, position)

                if Helper.win_check(self,theBoard, player2_marker):
                    Helper.display_board(self,theBoard)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if Helper.full_board_check(self,theBoard):
                        Helper.display_board(self,theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1'

        if not Helper.replay():
            break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Welcome to Tic Tac Toe!')
    play(self=Helper)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
