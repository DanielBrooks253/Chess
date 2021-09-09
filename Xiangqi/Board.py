import pygame as p

class Board:
    '''
        Class to define the chess board
    '''
    def __init__(self, white_pieces, black_pieces, height, width, sq_size, y_dim, x_dim):
        '''
        Initializes the Board class

        :param white_pieces (list): list of objects that belong to the white pieces 
        :param black_pieces (list): list of objects that belong to the black pieces
        :param height (int): The height of the pygame window
        :param width (int): The width of the pygame window
        :param dimension (int): the size of the squares for the chess board

        :param y_dim (int): the number of squares in the y direction (up/down)
            :default value: 8
        :param x_dim (int): the number of squares in the x direction (left/right) 
            :default value: 8

        :return: Null (Nothing)
        '''
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

        self.HEIGHT = height
        self.WIDTH = width
        self.SQ_SIZE = sq_size

    def Convert_Pxl_To_Coord(self, y, x):
        '''
        Convert the click that revoles around cress to tiles 
        '''
        return ((y-32)//64, (x-32)//64)    
    
    def game_over_check(self, color_name_obj, num_turns):
        '''
        Checks to see if the game is over (No available moves)

        :param color_name_obj (dict): a dictionary containing the objects of the color pieces
            that did not make a move.
            ex) If white just moved, color_name_obj would be a dict of the black pieces. Checking
                to see if the white move resulted in a checkmate or stalemate for the black king.

            :key: piece name
            :value: the class associated with the piece
        :param num_turns (int): The number of turns that have been taken in the game. This is used
                to determine which moves to check 

            num_turns % 2 == 0: blacks moves
            num_turns % 2 != 0: whites moves

        :return Bool
            :True means there are no available moves to make
            :False means there are available moves for the king and other pieces
        '''
        for i in color_name_obj.values():
            if i.pos is None:
                continue
            else:
                if num_turns % 2 == 0: # White move
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
                        self.white_piece_loc,
                        self.black_piece_loc
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

    def update_locs(self, color, old_move, new_move, is_captured=False, captured_piece=None):
        '''
        Once a move is made, all of the dictionaries will update with the new locations and
        objects will updated their positions if there was a capture (Change pos to None if captured)

        :param color (str): The color of the piece that is being moved
        :param old_move (tuple): The location that the piece is currently on (y,x)
        :param new_move( tuple): The location to which the piece will mvoe to (y,x)
        
        :param is_catpured (Bool): Checks to see if the move resulted in a captured piece or not
            :default value: False
        :param captured_piece (str): The piece_name/id of of the piece that was captured
            :defalut value: None

        :return: Null (Nothing)
        '''
        self.loc_names[new_move] = self.loc_names[old_move]
        del self.loc_names[old_move]

        if is_captured: # Remove piece from opposing color and update sets
            # Change the captured pieces position to None
            self.name_obj_dict[captured_piece].pos = None
            
            if color == 'white':
                self.black_name_obj_dict[captured_piece].pos = None

                # Remove the captured piece location from the location dictionary
                self.black_piece_loc -= {new_move}

                # Switch the old and new locations ofr the piece that moved
                rm_old_move = self.white_piece_loc - {old_move}
                add_new_move = rm_old_move | {new_move}

                # Update the color locations
                self.white_piece_loc = add_new_move

            else:
                self.white_name_obj_dict[captured_piece].pos = None
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
                
    def drawGameState(self, screen, names_obj, game_over, text, num, high_squares, king_pos, piece_locs):
        '''
        Responsible for drawing the game board, pieces and end of game text

        :param screen (pygame obj): Pygame game object that houses all of the "drawings" and images
            rendered for the chess game (Basically the pygame window and board)
        :param name_obj (dict): all of the piece objects that are on the board
            :key piece_name
            :value class associated with the piece
        :param game_over (Bool): Flag to determine if the game is over or not
            :True draw the end if game text
            : False draw the game baord and pieces
        :param text (str): The text to display after the game is over
        :param num (int): The size of the font to display the text

        :param args (list): This is the catch all parameter. This is used to color the square for
            the king in red and highlight the available moves for the pieces. 
            :args[0]: 
                list of available moves for the piece
            :args[1]:
                None if king is not in check
                king pos if the king is in check

        return: Null (Nothing)
        '''
        if game_over:
            Board.DrawBoard(self, screen, high_squares, king_pos, piece_locs)
            Board.drawPieces(self, screen, names_obj)
            Board.drawText(self, screen, text, num)
        else:
            Board.DrawBoard(self, screen, high_squares, king_pos, piece_locs)
            Board.drawPieces(self, screen, names_obj)


    def DrawBoard(self, screen, high_squares, king_pos, piece_locs):
        for r in range(self.x_dim):
            for c in range(self.y_dim):
                # Add border around the playing field and for the river
                if c == 5 or r == 0 or c == 0 or r == 9 or c == 10:
                    p.draw.rect(screen, p.Color('wheat1'),
                            p.Rect((r*self.SQ_SIZE), (c*self.SQ_SIZE), 
                            (self.SQ_SIZE), (self.SQ_SIZE)))
                else:
                    p.draw.rect(screen, p.Color('wheat1'),
                            p.Rect((r*self.SQ_SIZE), (c*self.SQ_SIZE), 
                            (self.SQ_SIZE), (self.SQ_SIZE)))
                    p.draw.rect(screen, p.Color('black'),
                            p.Rect((r*self.SQ_SIZE-1), (c*self.SQ_SIZE-1), 
                            (self.SQ_SIZE+1), (self.SQ_SIZE+1)),1)


        if high_squares is not None:
            if type(high_squares) is tuple:
                p.draw.rect(screen, p.Color('darkolivegreen'),
                p.Rect(high_squares[1]*self.SQ_SIZE +32, high_squares[0]*self.SQ_SIZE+32, 
                                   self.SQ_SIZE, self.SQ_SIZE))
            else:
                for i in high_squares:
                    if i in piece_locs:
                        p.draw.rect(screen, p.Color('darkolivegreen'),
                            p.Rect(i[1]*self.SQ_SIZE+32, i[0]*self.SQ_SIZE+32, 
                                    self.SQ_SIZE, self.SQ_SIZE))
                        p.draw.rect(screen, p.Color('black'),
                            p.Rect(i[1]*self.SQ_SIZE+32, i[0]*self.SQ_SIZE+32, 
                                    self.SQ_SIZE, self.SQ_SIZE),1)
                    else:
                        p.draw.circle(screen, p.Color('red'), (i[1]*64+64,i[0]*64+64), 8)

        if king_pos is not None:
            p.draw.rect(screen, p.Color('red'), 
                        p.Rect(king_pos[1]*self.SQ_SIZE+32, king_pos[0]*self.SQ_SIZE+32, self.SQ_SIZE, self.SQ_SIZE))
            p.draw.rect(screen, p.Color('black'),
                        p.Rect((king_pos[1]*self.SQ_SIZE+32-1), (king_pos[0]*self.SQ_SIZE+32-1), 
                           (self.SQ_SIZE+1), (self.SQ_SIZE+1)),1)

        p.draw.line(screen, p.Color('black'), (63, 320), (63, 384))
        p.draw.line(screen, p.Color('black'), (575, 320), (575, 384))

        # Fortess Lines
        p.draw.line(screen, p.Color('black'), (256, 64), (384, 190))
        p.draw.line(screen, p.Color('black'), (384, 64), (256, 190))

        p.draw.line(screen, p.Color('black'), (256, 640), (384, 510))
        p.draw.line(screen, p.Color('black'), (384, 640), (256, 510))


    def drawPieces(self, screen, names_obj):
        '''
        Responsible for drawing the piece images of the board

        :param screen (pygame obj): Pygame game object that houses all of the "drawings" and images
            rendered for the chess game (Basically the pygame window and board)
        :param name_obj (dict): all of the piece objects that are on the board
            :key piece_name
            :value class associated with the piece

        :return Null (Nothing)
        '''
        y_adjust = 40
        x_adjust = 40

        # Draw the pieces on the board
        # x and y axis are flipped when drawing the pieces
        for piece in names_obj.values():
            if piece.pos is None:
                continue
            else:
                if piece.color == 'white':
                    pass
                screen.blit(piece.piece_image, 
                    p.Rect(piece.pos[1]*self.SQ_SIZE + y_adjust, piece.pos[0]*self.SQ_SIZE+ x_adjust, 
                           self.SQ_SIZE, self.SQ_SIZE))

                
    def drawText(self, screen, text, num):
        '''
        Responsible for drawing the end of the game text across the screen

        :param screen (pygame obj): Pygame game object that houses all of the "drawings" and images
            rendered for the chess game (Basically the pygame window and board)
        :param text (str): The text that will show once the game is over
        :param num (int): The size of the font to show on the screen

        :return Null (Nothing)
        '''
        # Draw the text at the end of the game
        p.font.init()

        if num == 1:
            size = 32
        else:
            size = 22


        font = p.font.SysFont('Comic Sans MS', size, True, False)
        textObject = font.render(text, 0, p.Color('white'))
        textLocation = p.Rect(0,0, self.WIDTH, self.HEIGHT) \
                        .move(self.WIDTH//2-textObject.get_width()//2, 
                              self.HEIGHT//2-textObject.get_height()//2)
        screen.blit(textObject, textLocation)

        textObject = font.render(text, 0, p.Color('gray2'))
        screen.blit(textObject, textLocation.move(2,2))


    