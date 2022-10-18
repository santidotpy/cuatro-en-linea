




ROWS = 6
COLS = 7

class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
        self.turns = 0 # turnos hasta el momento
        self.last_move = [-1, -1] #row col

    
    def display_board(self):
        print(f"{'= ' * 20}")
        # display col number
        for col in range(COLS):
            print(f' ({col + 1}) ', end='')
        print('\n')

        for row in range(ROWS):
            print('|', end='')
            for col in range(COLS):
                print(f'  {self.board[row][col]} |', end='')
            print('\n')
        
        print(f"{'= ' * 20}\n")

    
    def which_turn(self):
        # 2 players
        player = ['🍏', '🍎']
        return player[self.turns % 2]

    def turn(self, col):
        
        if not type(col) is int:
            raise ValueError
        if col > COLS:
            raise IndexError
        

        # busco de abajo para arriba
        for row in range(ROWS - 1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.which_turn()
                self.last_move = [row, col]

                self.turns += 1
                return True

        return False

    # me fijo los limites para ver si gana de manera ok
    def check_limits(self, row, col):
        return (row >= 0 and row < ROWS and col >= 0 and col < COLS)

    def check_winner(self):
        last_row = self.last_move[0]
        last_col = self.last_move[1]
        last_player = self.board[last_row][last_col]

        # d[1] es la cantidad de fichas juntas que lleva
        directions = [
            [[-1, 0], 0, True],     # arriba
            [[1, 0], 0, True],      # abajo
            [[0, -1], 0, True],     # izquierza
            [[0, 1], 0, True],      # derecha
            [[-1, -1], 0, True],    # diagonal ...
            [[1, 1], 0, True],
            [[-1, 1], 0, True],
            [[1,-1], 0, True]
        ]

        # busco si coicide el player
        for a in range(4):
            for d in directions:
                r = last_row + (d[0][0] * (a+1)) # a+1 es cuantas piezas nos vamos a buscar
                c = last_col + (d[0][1] * (a+1))

                if d[2] and self.check_limits(r, c) and self.board[r][c] == last_player:
                    d[1] += 1 #si llego a 4 winner winner chicken dinner
                else:
                    # cambio de dirreccion
                    d[2] = False

        for i in range(0, 7, 2):
            if (directions[i][1] + directions[i+1][1] >= 3):
                #self.display_board()
                #print(f'{last_player} is the WINNER!!')
                return True, last_player

        #si no hay ganador
        return False, None

        
if __name__ == '__main__':
    #play()
    pass