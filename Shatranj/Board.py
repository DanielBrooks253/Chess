import numpy as np

class Board:
    def __init__(self, white_pieces, black_pieces, y_dim=8, x_dim=8):
        self.black_piece_loc = set([i.pos for i in black_pieces])
        self.white_piece_loc = set([i.pos for i in white_pieces])

        self.white_name_obj_dict = {i.piece_name:i for i in white_pieces}
        self.black_name_obj_dict = {i.piece_name:i for i in black_pieces}
        self.name_obj_dict = {i.piece_name:i for i in white_pieces + black_pieces}

        self.y_dim=y_dim
        self.x_dim=x_dim

        # self.white_available_moves = set().union(*list(filter(None, [i.Available_Moves(y_dim, x_dim, self.white_piece_loc, self.black_piece_loc) for i in white_pieces])))
        # self.black_available_moves = set().union(*list(filter(None, [i.Available_Moves(y_dim, x_dim, self.black_piece_loc, self.white_piece_loc) for i in black_pieces])))

        # self.pos_obj_dict = {i.pos:i for i in white_pieces + black_pieces if i.pos is not None}
        
    def update_locs(self, color, old_move, new_move, is_captured=False, caputed_piece=None):
        if is_captured: # Remove piece from opposing color and update sets
            self.name_obj_dict[caputed_piece].pos = None
            if color == 'white':
                self.name_obj_dict_black[caputed_piece].pos = None

                self.black_piece_loc -= {new_move}

                rm_old_move = self.white_piece_loc - {old_move}
                add_new_move = rm_old_move | {new_move}

                self.white_piece_loc = add_new_move

            else:
                self.name_obj_dict_white[caputed_piece].pos = None
                self.white_piece_loc -= {new_move}

                rm_old_move = self.black_piece_loc - {old_move}
                add_new_move = rm_old_move | {new_move}

                self.black_piece_loc = add_new_move
        else: # Update sets
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

