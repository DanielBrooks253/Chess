import pygame as p

class Board:

    def __init__(self, white_pieces, black_pieces, height, width, dimension, y_dim=8, x_dim=8):
        '''
        Initializes the board

        :param white_pieces (list): list of all the white piece objects on the board
        :param black_pieces (list): list of all the black piece objects on the board
        :param height (int): height of the game board (pixels)
        :param width (int): width of the game board (pixels)
        :param dimension (int): number of squares

        :param y_dim (int): number of sqaures in the y direction (up and down)
            defalut value: 8
        :param x_dim (int): number of sqaures in the x direction (left and right)
            defalut value: 8

        :return Null (Nothing)
        '''
        # get all of the location of the white and black pieces
        self.black_piece_loc = set([i.pos for i in black_pieces])
        self.white_piece_loc = set([i.pos for i in white_pieces])

        # map the setup locations to their respective objects
        self.white_set_up_locs = {i.set_up_coord:i for i in white_pieces}
        self.black_set_up_locs = {i.set_up_coord:i for i in black_pieces}

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
        self.SQ_SIZE = (width-70) //dimension

        # Promotion squares for the ne (pawns)
        self.promotion_sq_white = ((0,0), (1,1), (2,2), (3,3), (0,7), (1,6), (2,5), (3,4))
        self.promotion_sq_black = ((4,4), (5,5), (6,6), (7,7), (4,3), (5,2), (6,1), (7,0))

        self.promotion_selection_white = None
        self.promotion_selection_black = None

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

    def drawGameState(self, screen, names_obj, game_over, text, num, high_squares, king_pos, turns, 
                      white_promote=False, black_promote=False):
        '''
        Draws the current game state of the board

        :param screen (object): Screen object
        :param names_obj (dict): Dictionary that maps the piece name to the object
        :param game_over (Bool): Flag to determine if the game is "over" no more available moves
            for a certain color
        :param text (str): Display text
        :param num (int): Size of the text to be displayed
        :param high_squares (set): The sqaures that need to be highlighted on the screen
        :param king_pos (tuple): Location of the king on the board
        :param turns (int): The number of turns that have passed

        :param white_param (Bool): Flag to see if the white pieces can promote or not
            defalut value: False
        :param black_param (Bool): Flag to see if the black pieces can promote or not
            defalut value: False

        :return Null (Nothing)
        '''
        if game_over:
            Board.drawBoard(self, screen, high_squares, king_pos) # Draw board first so pieces do not get overwritten
            Board.drawPieces(self, screen, names_obj, turns)
            Board.drawText(self, screen, text, num)

        elif white_promote or black_promote:
            Board.drawBoard(self, screen, high_squares, king_pos) # Draw board first so pieces do not get overwritten
            Board.drawPieces(self, screen, names_obj, turns)
            Board.drawMessgaeBox(self, screen, black_promote)
            
        else:
            Board.drawBoard(self, screen, high_squares, king_pos) # Draw board first so pieces do not get overwritten
            Board.drawPieces(self, screen, names_obj, turns)

            if turns > 1:
                Board.drawBoard(self, screen, high_squares, king_pos) # Draw board first so pieces do not get overwritten
                Board.drawPieces(self, screen, names_obj, turns)
            else:
                Board.drawBoard(self, screen, high_squares, king_pos) # Draw board first so pieces do not get overwritten
                Board.drawPieces(self, screen, names_obj,  turns)
                Board.Header_Text(self, screen,names_obj, turns)

    def drawBoard(self, screen, high_squares, king_pos):
        '''
        Draw the game board

        :param screen (object): Screen object
        :param high_squares (set): Set of sqaures that need to be highlighted
        :param king_pos (tuple): Location of the King

        :return Null (Nothing)
        '''
        # Red check; darkolivegreen moves
        # Draw the tiles on the board
        for r in range(self.x_dim):
            for c in range(self.y_dim):
                p.draw.rect(screen, p.Color('wheat1'), 
                   p.Rect(r*self.SQ_SIZE, c*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
                p.draw.rect(screen, p.Color('black'),
                   p.Rect((r*self.SQ_SIZE-1), (c*self.SQ_SIZE-1), 
                           (self.SQ_SIZE+1), (self.SQ_SIZE+1)),1)
        
        p.draw.line(screen, p.Color('black'), (0 ,0), (512, 512))
        p.draw.line(screen, p.Color('black'), (0, 512), (512, 0))

        p.draw.rect(screen, p.Color('wheat1'), p.Rect(512, 0, 68, 512))
        p.draw.rect(screen, p.Color('black'), p.Rect(512, 0, 68, 512),1)

        # Check to see if a place has been clicked 
        # Highlight the space and the pieces moves in grey
        if high_squares is not None:
            if type(high_squares) is tuple: 
                if high_squares in self.loc_names.keys() or high_squares in self.white_set_up_locs or high_squares in self.black_set_up_locs:
                    p.draw.rect(screen, p.Color('darkolivegreen'), 
                        p.Rect(high_squares[1]*self.SQ_SIZE, high_squares[0]*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
                    p.draw.rect(screen, p.Color('black'),
                        p.Rect((high_squares[1]*self.SQ_SIZE-1), (high_squares[0]*self.SQ_SIZE-1), 
                                (self.SQ_SIZE+1), (self.SQ_SIZE+1)),1)
                    p.draw.line(screen, p.Color('black'), (0 ,0), (512, 512))
                    p.draw.line(screen, p.Color('black'), (0, 512), (512, 0))
            else:
                for i in high_squares:
                    p.draw.rect(screen, p.Color('darkolivegreen'), 
                       p.Rect(i[1]*self.SQ_SIZE, i[0]*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
                    p.draw.rect(screen, p.Color('black'),
                       p.Rect((i[1]*self.SQ_SIZE-1), (i[0]*self.SQ_SIZE-1), 
                               (self.SQ_SIZE+1), (self.SQ_SIZE+1)),1)
                    p.draw.line(screen, p.Color('black'), (0 ,0), (512, 512))
                    p.draw.line(screen, p.Color('black'), (0, 512), (512, 0))

        if king_pos is not None:
            p.draw.rect(screen, p.Color('red'), 
                        p.Rect(king_pos[1]*self.SQ_SIZE, king_pos[0]*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
            p.draw.rect(screen, p.Color('black'),
                        p.Rect((king_pos[1]*self.SQ_SIZE-1), (king_pos[0]*self.SQ_SIZE-1), 
                           (self.SQ_SIZE+1), (self.SQ_SIZE+1)),1)
            p.draw.line(screen, p.Color('black'), (0 ,0), (512, 512))
            p.draw.line(screen, p.Color('black'), (0, 512), (512, 0))

    def drawPieces(self, screen, names_obj, turns):
        '''
        Draw the pieces on the board

        :param screen (object): Screen object
        :param names_obj (dict): Dictionary that maps piece names to objects
        :param turns (int): The number of turns that have gone by in the game

        :return Null (Nothing)
        '''
        # Draw the pieces on the board
        # x and y axis are flipped when drawing the pieces
        if turns == 1:
            p.draw.rect(screen, p.Color('wheat1'), p.Rect(0, 256, 512, 256))
        else:
            pass

        for piece in names_obj.values():
            if piece.pos is None:
                if turns == 0:
                    if piece.color == 'white':
                        screen.blit(piece.piece_image,
                            p.Rect(piece.set_up_loc[0], piece.set_up_loc[1], self.SQ_SIZE, self.SQ_SIZE))
                elif turns == 1:
                    if piece.color == 'black':
                        screen.blit(piece.piece_image,
                             p.Rect(piece.set_up_loc[0], piece.set_up_loc[1], self.SQ_SIZE, self.SQ_SIZE))
                else:
                    pass
            else:
                if turns == 1 and piece.color == 'white':
                    continue
                else:
                    screen.blit(piece.piece_image, 
                            p.Rect(piece.pos[1]*self.SQ_SIZE+8, piece.pos[0]*self.SQ_SIZE+8, 
                                self.SQ_SIZE, self.SQ_SIZE))

    def Header_Text(self, screen, names_obj, turns):
        '''
        Draw the names above the side bar when placing pieces

        :param scrren (objec): Screen object
        :param names_obj (dict): Dictionary that maps piece names to objects
        :param turns (int): The number of turns that have gone by in the game

        :return NULL (Nothing)
        '''
        count = 0
        if turns == 0:
            side_locs = [i.set_up_coord for i in names_obj.values() if i.color == 'white']
        else:
            side_locs = [i.set_up_coord for i in names_obj.values() if i.color == 'black']

        for piece, loc, set_up_loc in \
          zip(['Yahhta', 'Yahhta', 'Myin', 'Myin', 'Sin', 'Sin', 'Min-Gyi', 'Sit-Ke'],
              [530, 530, 535, 535,  535, 535, 530, 530],
              [(0,8), (1,8), (2,8), (3,8), (4,8), (5,8), (6,8), (7,8)]):

            if set_up_loc in side_locs:
                font = p.font.SysFont('Comic Sans MS', 10, True, False)
                textObject = font.render(piece, 0, p.Color('black'))
                textLocation = p.Rect(loc, 64*count, 68, 3)
                screen.blit(textObject, textLocation)  
                count += 1
            else:
                count += 1

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

    def drawMessgaeBox(self, screen, black_promote):
        '''
        Draw the promotion message box. Asking the player if they want to promote a pawn 
            or not

        :param screen (object): Screen object
        :param black_promote (Bool): Flag to determine if black can promote or not
            Determines where the message boax will be placed on the screen

        :return NULL (Nothing)
        '''
        font = p.font.SysFont('Comic Sans MS', 18, True, False)

        text_1 = 'Would You like to promote pawn?'
        text_2 = '(This counts as your turn)'
        
        textObject_1 = font.render(text_1, 0, p.Color('black'))
        textObject_2 = font.render(text_2, 0, p.Color('black'))

        textObject_3 = font.render('Yes!', 0, p.Color('black'))
        textObject_4 = font.render('No! ', 0, p.Color('black'))

        if black_promote:
            textLocation_1 = p.Rect(100, 30, 100, 18)
            textLocation_2 = p.Rect(125, 50, 100, 18)

            yesLocation = p.Rect(155, 90, 50, 30)
            noLocation = p.Rect(285, 90, 50, 30)

            p.draw.rect(screen, p.Color('wheat1'), p.Rect(90, 20, 310, 100))

            # Yes and No Buttons
            p.draw.rect(screen, p.Color('black'), p.Rect(150, 90, 50, 30), 1)
            p.draw.rect(screen, p.Color('black'), p.Rect(275, 90, 50, 30), 1)

            screen.blit(textObject_1, textLocation_1)
            screen.blit(textObject_2, textLocation_2)
            
            screen.blit(textObject_3, yesLocation)
            screen.blit(textObject_4, noLocation)
        else:
            textLocation_1 = p.Rect(100, 300, 100, 18)
            textLocation_2 = p.Rect(125, 320, 100, 18)

            yesLocation = p.Rect(155, 350, 50, 30)
            noLocation = p.Rect(285, 350, 50, 30)

            p.draw.rect(screen, p.Color('wheat1'), p.Rect(90, 290, 310, 100))

            # Yes and No Buttons
            p.draw.rect(screen, p.Color('black'), p.Rect(150, 350, 50, 30), 1)
            p.draw.rect(screen, p.Color('black'), p.Rect(275, 350, 50, 30), 1)

            screen.blit(textObject_1, textLocation_1)
            screen.blit(textObject_2, textLocation_2)

            screen.blit(textObject_3, yesLocation)
            screen.blit(textObject_4, noLocation)
        

        

