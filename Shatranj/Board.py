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

    def game_over_chkmt_stlmt_check(self, color_name_obj, num_turns):
        for i in color_name_obj.values():
            if i.pos is None:
                continue
            else:
                if num_turns % 2 == 0: # White move
                    moves = i.Available_Moves(
                        self.x_dim,
                        self.y_dim,
                        self.white_piece_loc,
                        self.black_piece_loc
                    )
                    
                    if moves is None:
                        continue
                    else:
                        invalid_moves = i.avail_move_check_check(moves, self)

                    # Check if the pieces have any available moves to get out
                    # of check. If there are you are not in checkmate; break
                    # out of the loop.
                    if len(moves - invalid_moves) != 0:
                        return False
                    else:
                        continue

                else: # Black Move
                    moves = i.Available_Moves(
                        self.x_dim,
                        self.y_dim,
                        self.black_piece_loc,
                        self.white_piece_loc
                    )
                    
                    if moves is None:
                        continue
                    else:
                        invalid_moves = i.avail_move_check_check(moves, self)

                    if len(moves - invalid_moves) != 0:
                        return False
                    else:
                        continue
        return True


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

    def drawGameState(self, screen, names_obj, *args):
        Board.drawBoard(self, screen, args) # Draw board first so pieces do not get overwritten
        Board.drawPieces(self, screen, names_obj)

    def drawBoard(self, screen, args):
        # Red check; gray moves
        # Draw the tiles on the board
        colors = [p.Color("wheat1"), p.Color("darkkhaki")]

        for r in range(self.x_dim):
            for c in range(self.y_dim):
                p.draw.rect(screen, colors[(r+c)%2], 
                   p.Rect(r*self.SQ_SIZE, c*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))

        # Check to see if a place has been clicked 
        # Highlight the space and the pieces moves in grey
        if args[0] is not None:
            if type(args[0]) is tuple: 
                if args[0] in self.loc_names.keys():
                    p.draw.rect(screen, p.Color('darkolivegreen'), 
                        p.Rect(args[0][1]*self.SQ_SIZE, args[0][0]*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
            else:
                for i in args[0]:
                    p.draw.rect(screen, p.Color('darkolivegreen'), 
                       p.Rect(i[1]*self.SQ_SIZE, i[0]*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
        if args[1] is not None:
            p.draw.rect(screen, p.Color('red'), 
                        p.Rect(args[1][1]*self.SQ_SIZE, args[1][0]*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))

    def drawPieces(self, screen, names_obj):
        # Draw the pieces on the board
        # x and y axis are flipped when drawing the pieces
        for piece in names_obj.values():
            if piece.pos is None:
                continue
            else:
                screen.blit(piece.piece_image, 
                    p.Rect(piece.pos[1]*self.SQ_SIZE+8, piece.pos[0]*self.SQ_SIZE+8, 
                            self.SQ_SIZE, self.SQ_SIZE))
                


