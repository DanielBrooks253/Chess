import pygame as p

class Board:
    '''
        Class to define the chess board
    '''
    def __init__(self, white_pieces, black_pieces, height, width, dimension, images, y_dim=9, x_dim=9):
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
        self.capture_name_obj_dict = {i.capture_name: i for i in white_pieces}

        # Dimensions of the chess board
        self.y_dim=y_dim
        self.x_dim=x_dim

        self.HEIGHT = height
        self.WIDTH = width
        self.SQ_SIZE = (width-64) //dimension

        # House the number of each piece type that has been captured.
        self.white_capture_counts_dict = {'fuhyo':[0, images['Pawn']], 'kaku': [0, images['Bishop']], 
                                          'hisha':[0, images['Rook']], 'kyosha':[0, images['Lance']],
                                          'keima':[0, images['Knight']], 'ginsho':[0, images['Silver_General']], 
                                          'kinsho':[0, images['Gold_General']]}
        self.black_capture_counts_dict = {'fuhyo':[0, images['Pawn']], 'kaku': [0, images['Bishop']], 
                                          'hisha':[0, images['Rook']], 'kyosha':[0, images['Lance']],
                                          'keima':[0, images['Knight']], 'ginsho':[0, images['Silver_General']], 
                                          'kinsho':[0, images['Gold_General']]}
    
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

        # See if there are any placements that can get the player out of check
        placement_check = self.Placement_Check_Check(num_turns+1)

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

        if len(placement_check) == 0:
            print('No More Placements')
            return True
        else:
            print('Placements')
            return False
        # return True
    
    def Placement_Check_Check(self, turns):
        '''
        Checks to see if a piece can be placed from the captured zone to stop a player from being in
        check.

        :param turns (int): The number of turns in the game

        :returns set: Return all of the places that will get the player out of check. If the player is
            not in check, then the function will return all of the pieces available places. If the player
            is in check, it will only return a subset of moves to get the player out of check, If there are
            no available places to get the player out of check, it will return an empty set.
        '''
        white_piece_loc_copy = self.white_piece_loc.copy()
        black_piece_loc_copy = self.black_piece_loc.copy()

        output = set()

        if turns % 2 == 0:
            # Grab all of the captured piece counts that have one piece in them
            for key, value in self.white_capture_counts_dict.items():
                if value[0] == 0:
                    continue
                else:
                    # Get all of the places the piece can be placed
                    placement_squares = self.capture_name_obj_dict[key].Place_Pieces(
                        self.name_obj_dict, self.y_dim, turns
                    )

                    if placement_squares is None:
                        return set()
                    else:
                        # Check all the possible places and see which ones get the player out of check
                        for i in placement_squares:
                            white_piece_loc_copy |= {i}
                            
                            if self.name_obj_dict['wO'].check_check(
                                self.black_name_obj_dict,
                                self.black_piece_loc,
                                white_piece_loc_copy,
                                self.y_dim, 
                                self.x_dim
                            ):
                                white_piece_loc_copy.remove(i)
                                continue
                            else:
                                white_piece_loc_copy.remove(i)
                                output |= {i}
            if len(output) == 0:
                return set()
            else:
                return output
        else:
            for key, value in self.black_capture_counts_dict.items():
                if value[0] == 0:
                    continue
                else:
                    placement_squares = self.capture_name_obj_dict[key].Place_Pieces(
                        self.name_obj_dict, self.y_dim, turns
                    )

                    if placement_squares is None:
                        return set()
                    else:
                        for i in placement_squares:
                            black_piece_loc_copy |= {i}
                            
                            if self.name_obj_dict['bO'].check_check(
                                self.white_name_obj_dict,
                                self.white_piece_loc,
                                black_piece_loc_copy,
                                self.y_dim, 
                                self.x_dim
                            ):
                                black_piece_loc_copy.remove(i)
                                continue
                            else:
                                black_piece_loc_copy.remove(i)
                                output |= {i}
            if len(output) == 0:
                return set()
            else:
                return output

    def update_locs(self, color, old_move, new_move, is_captured=False, captured_piece=None):
        '''
        Once a move is made, all of the dictionaries will update with the new locations and
        objects will updated their positions if there was a capture (Change pos to None if captured)

        :param color (str): The color of the piece that is being moved
        :param old_move (tuple): The location that the piece is currently on (y,x)
        :param new_move( tuple): The location to which the piece will move to (y,x)
        
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

    def drawGameState(self, screen, names_obj, game_over, text, num, high_squares, king_pos, num_turns, 
    black_promotion, white_promotion):
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
            Board.drawBoard(self, screen, high_squares, king_pos) # Draw board first so pieces do not get overwritten
            Board.drawPieces(self, screen, names_obj)
            Board.drawText(self, screen, text, num)
        else:
            if num_turns % 2 == 0:
                if white_promotion:
                    Board.drawBoard(self, screen, high_squares, king_pos) # Draw board first so pieces do not get overwritten
                    Board.drawPieces(self, screen, names_obj)
                    Board.drawCapturedPieces(self, screen, self.white_capture_counts_dict)
                    Board.drawMessgaeBox(self, screen, black_promotion)
                else:
                    Board.drawBoard(self, screen, high_squares, king_pos) # Draw board first so pieces do not get overwritten
                    Board.drawPieces(self, screen, names_obj)
                    Board.drawCapturedPieces(self, screen, self.white_capture_counts_dict)
            else:
                if black_promotion:
                    Board.drawBoard(self, screen, high_squares, king_pos) # Draw board first so pieces do not get overwritten
                    Board.drawPieces(self, screen, names_obj)
                    Board.drawCapturedPieces(self, screen, self.black_capture_counts_dict)
                    Board.drawMessgaeBox(self, screen, black_promotion)
                else:
                    Board.drawBoard(self, screen, high_squares, king_pos) # Draw board first so pieces do not get overwritten
                    Board.drawPieces(self, screen, names_obj)
                    Board.drawCapturedPieces(self, screen, self.black_capture_counts_dict)

    def drawBoard(self, screen, high_squares, king_pos):
        # Red check; darkolivegreen moves
        # Draw the tiles on the board

        for r in range(self.x_dim):
            for c in range(self.y_dim):
                p.draw.rect(screen, p.Color('wheat1'), 
                   p.Rect(r*self.SQ_SIZE, c*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
                p.draw.rect(screen, p.Color('black'),
                   p.Rect((r*self.SQ_SIZE-1), (c*self.SQ_SIZE-1), 
                           (self.SQ_SIZE+1), (self.SQ_SIZE+1)),1)

        # Promotion dots on the board
        p.draw.circle(screen, p.Color('black'), (174, 174), 3, width=0)
        p.draw.circle(screen, p.Color('black'), (348, 174), 3, width=0)
        p.draw.circle(screen, p.Color('black'), (174, 348), 3, width=0)
        p.draw.circle(screen, p.Color('black'), (348, 348), 3, width=0)

        p.draw.rect(screen, p.Color('wheat1'), p.Rect(522, 0, 64, 522))
        p.draw.rect(screen, p.Color('black'), p.Rect(522, 0, 64, 522), 1)

        # Check to see if a place has been clicked 
        # Highlight the space and the pieces moves in grey
        if high_squares is not None:
            if type(high_squares) is tuple: 
                if high_squares in self.loc_names.keys() or high_squares[1] == 9 or high_squares[0] < 7:
                    p.draw.rect(screen, p.Color('darkolivegreen'), 
                        p.Rect(high_squares[1]*self.SQ_SIZE, high_squares[0]*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
                    p.draw.rect(screen, p.Color('black'),
                        p.Rect((high_squares[1]*self.SQ_SIZE-1), (high_squares[0]*self.SQ_SIZE-1), 
                                (self.SQ_SIZE+1), (self.SQ_SIZE+1)),1)
            else:
                for i in high_squares:
                    p.draw.rect(screen, p.Color('darkolivegreen'), 
                       p.Rect(i[1]*self.SQ_SIZE, i[0]*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
                    p.draw.rect(screen, p.Color('black'),
                       p.Rect((i[1]*self.SQ_SIZE-1), (i[0]*self.SQ_SIZE-1), 
                               (self.SQ_SIZE+1), (self.SQ_SIZE+1)),1)
        if king_pos is not None:
            p.draw.rect(screen, p.Color('red'), 
                        p.Rect(king_pos[1]*self.SQ_SIZE, king_pos[0]*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
            p.draw.rect(screen, p.Color('black'),
                        p.Rect((king_pos[1]*self.SQ_SIZE-1), (king_pos[0]*self.SQ_SIZE-1), 
                           (self.SQ_SIZE+1), (self.SQ_SIZE+1)),1)

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
        # Draw the pieces on the board
        # x and y axis are flipped when drawing the pieces
        for piece in names_obj.values():
            if piece.pos is None:
                continue
            else:
                if piece.promoted and piece.promoted_image is not None:
                    screen.blit(piece.promoted_image, 
                        p.Rect(piece.pos[1]*self.SQ_SIZE+8, piece.pos[0]*self.SQ_SIZE+8, 
                                self.SQ_SIZE, self.SQ_SIZE))
                else:
                    screen.blit(piece.piece_image, 
                        p.Rect(piece.pos[1]*self.SQ_SIZE+8, piece.pos[0]*self.SQ_SIZE+8, 
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

    def drawCapturedPieces(self, screen, captured_dict):
        '''
        Draw the side bar that will show all of the captured pieces and their counts on the 
        side of the game board

        :param screen (object): Screen object
        :param captured_dict (dict): Counts of the different pieces that have been captured

        :return NULL (Nothing)
        '''

        font = p.font.SysFont('Comic Sans MS', 11, True, False)

        # Draw the pieces on the side of the board
        for idx, pieces in enumerate(captured_dict.values()):
            screen.blit(pieces[1],
                p.Rect(self.HEIGHT+8, idx*self.SQ_SIZE+10, self.SQ_SIZE, self.SQ_SIZE))

            textLocation = p.Rect(self.WIDTH-10, (idx+1)*self.SQ_SIZE-10, 8, 8)
            textObject = font.render(str(pieces[0]), 0, p.Color('black'))
            screen.blit(textObject, textLocation)
    
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

        text_1 = 'Would You like to promote piece?'
        
        textObject_1 = font.render(text_1, 0, p.Color('black'))

        textObject_3 = font.render('Yes!', 0, p.Color('black'))
        textObject_4 = font.render('No! ', 0, p.Color('black'))

        if black_promote:
            textLocation_1 = p.Rect(100, 30, 100, 18)

            yesLocation = p.Rect(155, 90, 50, 30)
            noLocation = p.Rect(285, 90, 50, 30)

            p.draw.rect(screen, p.Color('wheat1'), p.Rect(90, 20, 310, 100))

            # Yes and No Buttons
            p.draw.rect(screen, p.Color('black'), p.Rect(150, 90, 50, 30), 1)
            p.draw.rect(screen, p.Color('black'), p.Rect(275, 90, 50, 30), 1)

            screen.blit(textObject_1, textLocation_1)
            
            screen.blit(textObject_3, yesLocation)
            screen.blit(textObject_4, noLocation)
        else:
            textLocation_1 = p.Rect(100, 300, 100, 18)

            yesLocation = p.Rect(155, 350, 50, 30)
            noLocation = p.Rect(285, 350, 50, 30)

            p.draw.rect(screen, p.Color('wheat1'), p.Rect(90, 290, 310, 100))

            # Yes and No Buttons
            p.draw.rect(screen, p.Color('black'), p.Rect(150, 350, 50, 30), 1)
            p.draw.rect(screen, p.Color('black'), p.Rect(275, 350, 50, 30), 1)

            screen.blit(textObject_1, textLocation_1)

            screen.blit(textObject_3, yesLocation)
            screen.blit(textObject_4, noLocation)