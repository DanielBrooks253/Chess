import numpy as np

class Board:
    def __init__(self, white_loc, black_loc, y_dim=8, x_dim=8):
        self.black_piece_loc = black_loc # All black piece locations (Generally)
        self.white_piece_loc = white_loc # All white piece locations (Generally)

        #self.black_piece_dict = dict() # Key location, value piece name
        #self.white_piece_dict = dict() # Key location, value piece name

        self.y_dim=y_dim
        self.x_dim=x_dim

    def update_locs(self, color, old_move, new_move, is_captured=False):
        if is_captured:
            if color == 'white':
                self.black_piece_loc -= {new_move}

                rm_old_move = self.white_piece_loc - {old_move}
                add_new_move = rm_old_move | {new_move}

                self.white_piece_loc = add_new_move
            else:
                self.white_piece_loc -= {new_move}

                rm_old_move = self.black_piece_loc - {old_move}
                add_new_move = rm_old_move | {new_move}

                self.black_piece_loc = add_new_move
        else:
            if color =='white':
                rm_old_move = self.white_piece_loc - {old_move}
                add_new_move = rm_old_move | {new_move}

                self.white_piece_loc = add_new_move
            else:
                rm_old_move = self.black_piece_loc - {old_move}
                add_new_move = rm_old_move | {new_move}

                self.black_piece_loc = add_new_move

    def print_board(self, *args):
        board = np.chararray((self.x_dim, self.y_dim), itemsize=3)
        board[:] = "  "

        for items in args:
            if items.pos is None:
                continue
            else:
                board[items.pos[0], items.pos[1]] = items.piece_name

        print(board)

