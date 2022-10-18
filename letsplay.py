import four_main

ROWS = 6
COLS = 7

def play():
    game = four_main.Board()
    game_over = False
    while not game_over:
        game.display_board()
        valid_move = False
        while not valid_move:
            #ingreso una col
            user_move = input(f'Turn: {game.which_turn()}\nPick a column: ')

            try:
                valid_move = game.turn(int(user_move) - 1)
            except ValueError:
                print(f'{user_move} is not valid move')
                print(f'Please choose a number between 1 and {COLS}')
            except IndexError:
                print(f'Please choose a number between 1 and {COLS}')

        # false si no hay ganador
        game_over, player = game.check_winner()
        if game_over:
            game.display_board()
            print(f'\n{player} is the WINNER!!')


        if not any(' ' in x for x in game.board):
            print('TIE')
            return

        
if __name__ == '__main__':
    play()
