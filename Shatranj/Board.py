import numpy as np
import pygame as p

class Board:
    '''
        Class to define the chess board
    '''
    def __init__(self, white_pieces, black_pieces, height, dimension, y_dim=8, x_dim=8):
        # get all of the location of the white and black pieces
        self.black_piece_loc = set([i.pos for i in black_pieces])
        self.white_piece_loc = set([i.pos for i in white_pieces])

        # Dictionary that takes the piece name and maps it to the object
        # One for each color and an overall dictionary
        self.white_name_obj_dict = {i.piece_name:i for i in white_pieces}
        self.black_name_obj_dict = {i.piece_name:i for i in black_pieces}

        self.loc_names = {i.pos:i.piece_name for i in white_pieces + black_pieces}
        self.name_obj_dict = {i.piece_name:i for i in white_pieces + black_pieces}

        # Dimensions of the chess board
        self.y_dim=y_dim
        self.x_dim=x_dim

        self.SQ_SIZE = height //dimension
        
    def update_locs(self, color, old_move, new_move, is_captured=False, caputed_piece=None):
        self.loc_names[new_move] = self.loc_names[old_move]
        del self.loc_names[old_move]

        if is_captured: # Remove piece from opposing color and update sets
            # Change the captured pieces position to None
            self.name_obj_dict[caputed_piece].pos = None
            
            if color == 'white':
                self.black_name_obj_dict[caputed_piece].pos = None

                # Remove the captured piece location from the location dictionary
                self.black_piece_loc -= {new_move}

                # Switch the old and new locations ofr the piece that moved
                rm_old_move = self.white_piece_loc - {old_move}
                add_new_move = rm_old_move | {new_move}

                # Update the color locations
                self.white_piece_loc = add_new_move

            else:
                self.white_name_obj_dict[caputed_piece].pos = None
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

    def print_board(self, args):
        # Print a character array  for the board
        board = np.chararray((self.x_dim, self.y_dim), itemsize=3)
        board[:] = "  "

        for _, values in args.items():
            if values.pos is None:
                continue
            else:
                board[values.pos[0], values.pos[1]] = values.piece_name

        print(board)

    def drawGameState(self, screen, names_obj):
        Board.drawBoard(self, screen) # Draw board first so pieces do not get overwritten
        Board.drawPieces(self, screen, names_obj)

    def drawBoard(self, screen):
        # Red check; gray moves
        colors = [p.Color("wheat1"), p.Color("darkkhaki")]
        for r in range(self.x_dim):
            for c in range(self.y_dim):
                p.draw.rect(screen, colors[(r+c)%2], 
                   p.Rect(r*self.SQ_SIZE, c*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))

    def drawPieces(self, screen, names_obj):
        # x and y axis are flipped when drawing the pieces
        for piece in names_obj.values():
            screen.blit(piece.piece_image, 
                 p.Rect(piece.pos[1]*self.SQ_SIZE+8, piece.pos[0]*self.SQ_SIZE+8, 
                        self.SQ_SIZE, self.SQ_SIZE))
                


