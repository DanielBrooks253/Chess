###### Shogi (Japanese Chess) ######
class Pieces:
    def __init__(self, start_pos, piece_name, piece_image, promoted_image, color, capture_name, promotion_count = 0):
        '''
        Initalize the pieces class

        :param start_pos (tuple): The position of the piece on the board (y,x)
        :param piece_name (str): The name given to the piece
        :param piece_image (array pixels): The image to be displayed for the piece

        :param color (str): The color of the piece
            :default value: white

        :return Null (Nothing)
        '''
        self.promoted_image = promoted_image
        self.piece_image = piece_image

        self.pos=start_pos
        self.piece_name=piece_name
        self.color = color.lower()
        
        self.promoted = False
        self.promotion_count = promotion_count
        self.capture_name = capture_name

    def Place_Pieces(self, name_obj_dict, y_dim, turns):
        '''
        Place the piieces back on the board after they have been captured

        :param name_obj_dict (dict): Maps the piece name to the object
        :param y_dim (int): Number of squares in the y direction (up and down)
        :param turns (int): The number of turns that happend in the game

        :return set: Returns a set of coordinates that indicate where the particular piece
            is allowed to be placed
        '''
        all_piece_locations = set([i.pos for i in name_obj_dict.values()])

        # Locate the file of all the pawns on the board
        if turns % 2 == 0:
            pawn_on_board_locations = set([i.pos[1] for i in name_obj_dict.values() \
                                               if i.color == 'white' and \
                                                  i.capture_name == 'fuhyo' and \
                                                  i.pos is not None and \
                                                  i.promoted == False])
        else:
            pawn_on_board_locations = set([i.pos[1] for i in name_obj_dict.values() \
                                               if i.color == 'black' and \
                                                  i.capture_name == 'fuhyo' and \
                                                  i.pos is not None and \
                                                  i.promoted == False])

        # Kyosha cannot be placed on the last row of the game board
        if self.capture_name == 'kyosha':
            if turns % 2 == 0:
                return set(sum([[(i,j) for j in range(y_dim)] for i in range(1, 9)], [])) - \
                           all_piece_locations
            else:
                return set(sum([[(i,j) for j in range(y_dim)] for i in range(0, 8)], [])) - \
                           all_piece_locations

        # Kei-Ma cannot be placed on the last two rows of the game board.
        # It would not have any available moves once placed, which is illegal
        elif self.capture_name == 'keima':
            if turns % 2 == 0:
                return set(sum([[(i,j) for j in range(y_dim)] for i in range(2, 9)], [])) - \
                           all_piece_locations
            else:
                return set(sum([[(i,j) for j in range(y_dim)] for i in range(0, 7)], [])) - \
                           all_piece_locations

        # Pawns cannot be placed on the same file as another pawn of the same color.
        elif self.capture_name == 'fuhyo':
            if turns % 2 == 0:
                # Filter out the locations of all the other pieces on the board
                filter_pieces_on_board = set(sum([[(i,j) for j in range(y_dim)] for i in range(1,9)], [])) - \
                                             all_piece_locations
                # Filter out any files that share the same file as another pawn
                filter_pawn_file = set(list(filter(lambda x: x[1] not in pawn_on_board_locations, 
                                               filter_pieces_on_board)))

                if len(filter_pawn_file) == 0:
                    return None
                else:
                    return filter_pawn_file
            else:
                filter_pieces_on_board = set(sum([[(i,j) for j in range(y_dim)] for i in range(0,8)], [])) - \
                                             all_piece_locations
                filter_pawn_file = set(list(filter(lambda x: x[1] not in pawn_on_board_locations, 
                                               filter_pieces_on_board)))

                if len(filter_pawn_file) == 0:
                    return None
                else:
                    return filter_pawn_file
        else:
            return set(sum([[(i,j) for j in range(y_dim)] for i in range(y_dim)], [])) - \
                      all_piece_locations
        
    def Make_Move(self, new_loc, board_obj):
        '''
        Makes a move on the chess board

        :param new_loc (tuple): The location that the piece will move to
        :param board_obj (object Class Board): Houses all of the piece locations and 
            positions that need to be updated when something is moved

        :return Null (Nothing)
        '''
        # Check if the move results in a capture
        if self.color == 'white':
            piece_insct = [key for key, values in board_obj.black_name_obj_dict.items()
                            if new_loc == values.pos]

            if len(piece_insct) != 0:
                capture_check = (True, piece_insct[0])
                board_obj.white_capture_counts_dict[ # Add counts to the catpure counts
                    board_obj.black_name_obj_dict[piece_insct[0]].capture_name][0] += 1
            else:
                capture_check = (False, None)
        else:
            piece_insct = [key for key, values in board_obj.white_name_obj_dict.items()
                             if new_loc == values.pos]

            if len(piece_insct) != 0:
                capture_check = (True, piece_insct[0])
                board_obj.black_capture_counts_dict[ \
                    board_obj.white_name_obj_dict[piece_insct[0]].capture_name][0] += 1
            else:
                capture_check = (False, None) 
                        
            # Update the dictionaries within the board
        board_obj.update_locs(self.color,
                          self.pos,
                          new_loc,
                          capture_check[0],
                          capture_check[1])

        # Change the position to the new location
        self.pos = new_loc
    
    def avail_move_check_check(self, available_moves, board_obj):
        '''
        This is used to filter out any moves that would result in a check for your king

        :param avaiable_moves (set): Contains the coordinates of all the possible moves the 
            selected piece can take
        :param board_obj (Oblject of Class board): Contains all of the locations of every piece
            on the board.

        :return checks (set): All of the "illegal" moves that a piece can make. These moves would
            result in the king being in check after they are taken.
        '''
        rm = False
        checks = set()

        # Copy the locations so the "fake" moves do not change the actual objects
        black_loc_copy = board_obj.black_piece_loc.copy()
        white_loc_copy = board_obj.white_piece_loc.copy()

        name_obj_copy = board_obj.name_obj_dict.copy()
        white_name_obj_copy = board_obj.white_name_obj_dict.copy()
        black_name_obj_copy = board_obj.black_name_obj_dict.copy()

        # This logic temporarily changes the position for the given piece
        # to check if any of the available moves result in the king not
        # being in check

        if self.color == 'white':
            for i in available_moves:
                # If the piece being moved is a king
                # Need to move the position of the king along with
                # the different moves
                if self.piece_name == 'wO':
                    old_move = self.pos
                    self.pos = i

                    white_loc_copy -= {old_move}
                    white_loc_copy |= {i}
                    # Check to see if the movement of the king will capture a piece
                    if i in black_loc_copy:
                        rm =True
                        opp_piece = board_obj.loc_names[i]

                        black_loc_copy -= {i}
                        black_name_obj_copy[opp_piece].pos = None
                    else:
                        pass
                # Check to see if the move will capture a piece
                # Change the captured pieces pos to None and
                # remove it from the locations
                elif i in black_loc_copy:
                    rm = True
                    opp_piece = board_obj.loc_names[i]

                    white_loc_copy -= {self.pos}
                    white_loc_copy |= {i}
                    
                    black_loc_copy -= {i}
                    black_name_obj_copy[opp_piece].pos = None
                else:
                # Simply moving a piece in the way of the checking piece
                    white_loc_copy -= {self.pos}
                    white_loc_copy |= {i}

                # Check to see if the resulting move would get you out
                # of check or not
                if name_obj_copy['wO'].check_check(
                    black_name_obj_copy,
                    black_loc_copy,
                    white_loc_copy,
                    board_obj.y_dim,
                    board_obj.x_dim):

                    checks |= {i}
                else:
                    pass

                # Reset all of the original positions for the different 
                # scenarios
                if self.piece_name == 'wO':
                    self.pos = old_move

                    white_loc_copy -= {i}
                    white_loc_copy |= {self.pos}

                    if rm:
                        black_loc_copy |= {i}
                        black_name_obj_copy[opp_piece].pos = i
                        rm = False
                    else:
                        pass
                elif rm:
                    rm = False

                    white_loc_copy -= {i}
                    white_loc_copy |= {self.pos}
                    
                    black_loc_copy |= {i}
                    black_name_obj_copy[opp_piece].pos = i
                else:
                    white_loc_copy -= {i}
                    white_loc_copy |= {self.pos}
            return checks
        # Repeat the same process for the black moves
        else:
            for i in available_moves:
                # If the piece being moved is a king
                if self.piece_name == 'bO':
                    old_move = self.pos
                    self.pos = i

                    black_loc_copy -= {old_move}
                    black_loc_copy |= {i}

                    if i in white_loc_copy:
                        rm =True
                        opp_piece = board_obj.loc_names[i]

                        white_loc_copy -= {i}
                        white_name_obj_copy[opp_piece].pos = None
                    else:
                        pass

                elif i in white_loc_copy:
                    rm = True
                    opp_piece = board_obj.loc_names[i]

                    black_loc_copy -= {self.pos}
                    black_loc_copy |= {i}
                    
                    white_loc_copy -= {i}
                    white_name_obj_copy[opp_piece].pos = None
                else:
                # Simply moving a piece in the way of the checking piece
                    black_loc_copy -= {self.pos}
                    black_loc_copy |= {i}

                if name_obj_copy['bO'].check_check(
                    white_name_obj_copy,
                    white_loc_copy,
                    black_loc_copy,
                    board_obj.y_dim,
                    board_obj.x_dim):

                    checks |= {i}
                else:
                    pass

                if self.piece_name == 'bO':
                    self.pos = old_move

                    black_loc_copy -= {i}
                    black_loc_copy |= {self.pos}

                    if rm:
                        white_loc_copy |= {i}
                        white_name_obj_copy[opp_piece].pos = i
                        rm = False
                    else:
                        pass
                elif rm:
                    rm = False

                    black_loc_copy -= {i}
                    black_loc_copy |= {self.pos}
                    
                    white_loc_copy |= {i}
                    white_name_obj_copy[opp_piece].pos = i
                else:
                    black_loc_copy -= {i}
                    black_loc_copy |= {self.pos}

            return checks

class Kaku(Pieces):
    '''
        Has the movement of the modern day bishop

        1) When promoted, can move one space orthogonally
    '''

    def Available_Moves(self, y_dim, x_dim, same_color_locs, opp_color_locs):
        '''
        Filter out all of the moves that are off of the board and on a space occupied by
            the same color
        
        :param y_dim (int): number of squares in the y direction (up/down)
        :param x_dim (int): number of squares in the x direction (right/left)
        :param same_color_locs (list): a list of tuples that house the location of the piece
            of the same color as the select piece
        :param args (list): used for extra parameters

        :return rm_checks (set): All possible moves a piece can make (Does not take into account
            checks)
        '''
        all_moves = Kaku.Get_Moves(self, same_color_locs, opp_color_locs)
        if self.promoted:
            all_moves |= Kaku.Get_Promoted_Moves(self)
        else:
            pass

        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color
    
    def Get_Promoted_Moves(self):
        '''
        Returns the promoted moves when the piece is promoted
        '''
        return  set(((self.pos[0]+1, self.pos[1]),
                    (self.pos[0]-1, self.pos[1]),
                    (self.pos[0], self.pos[1]+1),
                    (self.pos[0], self.pos[1]-1)))

    def Get_Moves(self, same_color_locs, opp_color_locs):
        '''
        Get all the moves for the bishop. Looks at the closest pieces in each direction diagonally
        and determines if the bishop can move onto the square (capture) or right befor it.

        :param same_color_locs (list): List of positions of all the pieces that have the same color
            as the selected piece
        :param opp_color_locs (list): List of positions of all the pieces that have a different color
            as the selected piece

        :return set: Returns all the available moves in each of the four diagonal directions
        '''
        combine_locs = same_color_locs | opp_color_locs

        combine_locs = set(filter(None, combine_locs))

        same_color_up_left = False
        same_color_up_right = False
        same_color_down_left = False
        same_color_down_right = False

        all_down_right = set()
        all_down_left = set()
        all_up_left = set()
        all_up_right = set()

        # Calculate all of the diagonal squares in the 4 directions
        for i in range(1,9):
            all_down_right |= {((self.pos[0]+i), (self.pos[1]+i))}
            all_up_left |= {((self.pos[0]-i), (self.pos[1]-i))}

            all_down_left |= {((self.pos[0]+i), (self.pos[1]-i))}
            all_up_right |= {((self.pos[0]-i), (self.pos[1]+i))}

        # Locate any pieces that are on the diagonal paths
        pieces_down_right = combine_locs & all_down_right
        pieces_down_left = combine_locs & all_down_left
        pieces_up_right = combine_locs & all_up_right
        pieces_up_left = combine_locs & all_up_left

        # Find the closest piece (Regardless of color) to current piece
        closest_down_right = None if len(pieces_down_right) == 0 else (sorted(pieces_down_right, key=lambda y:y[0], reverse=False))[0]
        closest_down_left = None if len(pieces_down_left) == 0 else (sorted(pieces_down_left, key=lambda y:y[0], reverse=False))[0]
        closest_up_right = None if len(pieces_up_right) == 0 else (sorted(pieces_up_right, key=lambda y:y[0], reverse=True))[0]
        closest_up_left = None if len(pieces_up_left) == 0 else (sorted(pieces_up_left, key=lambda y:y[0], reverse=True))[0]

        # Check to see if the closest piece is of the same color or not
        if len({closest_down_right} & same_color_locs) != 0: same_color_down_right = True
        if len({closest_down_left} & same_color_locs) != 0: same_color_down_left = True
        if len({closest_up_right} & same_color_locs) != 0: same_color_up_right = True
        if len({closest_up_left} & same_color_locs) != 0: same_color_up_left = True

        # Places where the piece is allowed to move
        if same_color_down_right and closest_down_right is not None:
            distance = abs(closest_down_right[0] - self.pos[0])
            down_right = set([((self.pos[0]+i), (self.pos[1]+i)) for i in range(1,distance)])
        elif not same_color_down_right and closest_down_right is not None:
            distance = abs(closest_down_right[0] - self.pos[0])
            down_right = set([((self.pos[0]+i), (self.pos[1]+i)) for i in range(1,(distance+1))])
        else:
            down_right = all_down_right

        if same_color_down_left and closest_down_left is not None:
            distance = abs(closest_down_left[0] - self.pos[0])
            down_left = set([((self.pos[0]+i), (self.pos[1]-i)) for i in range(1,distance)])
        elif not same_color_down_left and closest_down_left is not None:
            distance = abs(closest_down_left[0] - self.pos[0])
            down_left = set([((self.pos[0]+i), (self.pos[1]-i)) for i in range(1,(distance+1))])
        else:
            down_left = all_down_left

        if same_color_up_right and closest_up_right is not None:
            distance = abs(closest_up_right[0] - self.pos[0])
            up_right = set([((self.pos[0]-i), (self.pos[1]+i)) for i in range(1,distance)])
        elif not same_color_up_right and closest_up_right is not None:
            distance = abs(closest_up_right[0] - self.pos[0])
            up_right = set([((self.pos[0]-i), (self.pos[1]+i)) for i in range(1,(distance+1))])
        else:
            up_right = all_up_right

        if same_color_up_left and closest_up_left is not None:
            distance = abs(closest_up_left[0] - self.pos[0])
            up_left = set([((self.pos[0]-i), (self.pos[1]-i)) for i in range(1,distance)])
        elif not same_color_up_left and closest_up_left is not None:
            distance = abs(closest_up_left[0] - self.pos[0])
            up_left = set([((self.pos[0]-i), (self.pos[1]-i)) for i in range(1,(distance+1))])
        else:
            up_left = all_up_left

        return down_right|down_left|up_right|up_left

class OSho(Pieces):
    '''
        Has the same movement as the modern day king
    '''

    def __init__(self, start_pos, piece_name, piece_image, promoted_image, color, capture_name):
        self.in_check = False
        super().__init__(start_pos, piece_name, piece_image, promoted_image, color, capture_name)

    def Available_Moves(self, y_dim, x_dim, same_color_locs, *args):
        '''
        Filter out all of the moves that are off of the board and on a space occupied by
            the same color
        
        :param y_dim (int): number of squares in the y direction (up/down)
        :param x_dim (int): number of squares in the x direction (right/left)
        :param same_color_locs (list): a list of tuples that house the location of the piece
            of the same color as the select piece
        :param args (list): used for extra parameters

        :return rm_checks (set): All possible moves a piece can make (Does not take into account
            checks)
        '''
        all_moves = OSho.Get_Moves(self)
        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in zip([0,1,1,1,0,-1,-1,-1], [1,1,0,-1,-1,-1,0,1])])
        
    def check_check(self, opp_objs, same_locs, opp_locs, y_dim, x_dim):
        '''
            See if the king is in check or not

            :param opp_objs (dict): Dictionary containing all the opponents pieces
                opponents means the color opposite the king whom the check_check is
                being made
            :param same_locs (list): Location of all the pieces that are on the same color
                as the king being checked
            :param opp_locs (list): Location of all the pieces that are on the opposite color
                as the king being checked

            :return (Bool)
                True: King is in check
                False: King is not in check
        '''
        opp_moves = list(filter(None, [None if i.pos is None else i.Available_Moves(y_dim, x_dim, same_locs, opp_locs) 
                     for i in opp_objs.values()]))

        if self.pos in set().union(*opp_moves):
            return True
        else:
            return False

class Hisha(Pieces):
    '''
        Has the same movement as the modern day rook

        1) When promoted, can move one space diagonally
    '''

    def Available_Moves(self, y_dim, x_dim, same_color_locs, opp_color_locs):
        '''
        Filter out all of the moves that are off of the board and on a space occupied by
            the same color
        
        :param y_dim (int): number of squares in the y direction (up/down)
        :param x_dim (int): number of squares in the x direction (right/left)
        :param same_color_locs (list): a list of tuples that house the location of the piece
            of the same color as the select piece
        :param args (list): used for extra parameters

        :return rm_checks (set): All possible moves a piece can make (Does not take into account
            checks)
        '''
        all_moves = Hisha.Get_Moves(self)

        if self.promoted:
            all_moves |= Hisha.Get_Promoted_Moves(self)
        else:
            pass

        orth_moves_beyon_pieces = Hisha.Get_Orthogonal_Pieces(self, same_color_locs, opp_color_locs, y_dim, x_dim)
        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        rm_over_pieces = rm_same_color - orth_moves_beyon_pieces
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_over_pieces

    def Get_Moves(self):
        if self.promoted:
            return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in list(zip([1,2,3,4,5,6,7,8], [0,0,0,0,0,0,0,0])) + \
                                                                      list(zip([-1,-2,-3,-4,-5,-6,-7,-8], [0,0,0,0,0,0,0,0])) + \
                                                                      list(zip([0,0,0,0,0,0,0,0], [1,2,3,4,5,6,7,8])) + \
                                                                      list(zip([0,0,0,0,0,0,0,0], [-1,-2,-3,-4,-5,-6,-7,-8]))]) | set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,1,-1,-1], [1,-1,1,-1])])
        else:
            return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in list(zip([1,2,3,4,5,6,7,8], [0,0,0,0,0,0,0,0])) + \
                                                                      list(zip([-1,-2,-3,-4,-5,-6,-7,-8], [0,0,0,0,0,0,0,0])) + \
                                                                      list(zip([0,0,0,0,0,0,0,0], [1,2,3,4,5,6,7,8])) + \
                                                                      list(zip([0,0,0,0,0,0,0,0], [-1,-2,-3,-4,-5,-6,-7,-8]))])

    def Get_Promoted_Moves(self):
        '''
        Returns the promoted moves when the piece is promoted
        '''
        return  set(((self.pos[0]+1, self.pos[1]+1),
                    (self.pos[0]+1, self.pos[1]-1),
                    (self.pos[0]-1, self.pos[1]+1),
                    (self.pos[0]-1, self.pos[1]-1)))

    def Get_Orthogonal_Pieces(self, same_color_locs, opp_color_locs, y_dim, x_dim):
        '''
        Rooks cannot jump over other pieces, therefore the moves the rook can make is limited
        by the closest piece in each direction orthogonally.

        This function finds the closest orthogonal pieces (If there are any) and creates a set of
        unavailable moves accordingly

        :param same_color_locs (list): locations of all the pieces that share the same color
            as the selected piece
        :param opp_color_locs (list):locations of all the pieces that have a differnet color
            as the selected piece
        :param y_dim (int): number of squares in the y direction (up/down)
        :param x_dim (int): number of squares in the x direction (right/left)

        :return (set): all of the moves the rook cannot take due to there being a 
            piece in the way. Used to filter all of the available moves.
        '''
        # Get the locations pf all the pieces on the board
        combine_locs = same_color_locs | opp_color_locs

        combine_locs = list(filter(None, combine_locs))

        # Set flags for the orthogonal locations to see if the same color
        # piece is closest in any of the four directions
        same_color_up = False
        same_color_down = False
        same_color_left = False
        same_color_right = False

        # Get a list of pieces that are ont he same file as the current piece
        closest_up = list(filter(lambda x: x[1] == self.pos[1] and x[0] < self.pos[0], combine_locs))
        closest_down = list(filter(lambda x: x[1] == self.pos[1] and x[0] > self.pos[0], combine_locs))
        closest_left = list(filter(lambda x: x[0] == self.pos[0] and x[1] < self.pos[1], combine_locs))
        closest_right = list(filter(lambda x: x[0] == self.pos[0] and x[1] > self.pos[1], combine_locs))

        # Find the closest piece out of the list of same file candidates
        closest_up = None if len(closest_up) == 0 else (sorted(closest_up, key=lambda y:y[0], reverse=True))[0]
        closest_down = None if len(closest_down) == 0 else (sorted(closest_down, key=lambda y:y[0]))[0]
        closest_left = None if len(closest_left) == 0 else (sorted(closest_left, key=lambda y:y[1], reverse=True))[0]
        closest_right = None if len(closest_right) == 0 else (sorted(closest_right, key=lambda y:y[1]))[0]

        # Check to see if the closest piece is the same color or not as the current peice
        if len({closest_up} & same_color_locs) != 0: same_color_up = True
        if len({closest_down} & same_color_locs) != 0: same_color_down = True
        if len({closest_left} & same_color_locs) != 0: same_color_left = True
        if len({closest_right} & same_color_locs) != 0: same_color_right = True

        # If the closest piece is of the same color, you can move to the 
        # space one unit before. If it is of a different color, you can move
        # onto the same piece and capture.
        if same_color_up and closest_up is not None:
            up_no = set(zip(range(closest_up[0], -1, -1), [closest_up[1]]*(closest_up[0]+1)))
        elif not same_color_up and closest_up is not None:
            up_no = set(zip(range(closest_up[0]-1, -1, -1), [closest_up[1]]*(closest_up[0]+1)))
        else:
            up_no = set()

        if same_color_down and closest_down is not None:
            down_no = set(zip(range((closest_down[0]), y_dim), [closest_down[1]] * (((y_dim-1) - closest_down[0]) + closest_down[0]+1)))
        elif not same_color_down and closest_down is not None:
            down_no = set(zip(range((closest_down[0]+1), y_dim), [closest_down[1]] * ((y_dim - closest_down[0]) + closest_down[0]+1)))
        else:
            down_no = set()

        if same_color_left and closest_left is not None:
            left_no = set(zip([closest_left[0]]*(closest_left[1]+1), range((closest_left[1]), -1, -1)))
        elif not same_color_left and closest_left is not None:
            left_no = set(zip([closest_left[0]]*(closest_left[1]+1), range((closest_left[1]-1), -1, -1)))
        else:
            left_no = set()

        if same_color_right and closest_right is not None:
            right_no = set(zip([closest_right[0]] * (((x_dim-1)-closest_right[1]+1) + closest_right[1]), range((closest_right[1]), x_dim)))
        elif not same_color_right and closest_right is not None:
            right_no = set(zip([closest_right[0]] * ((x_dim-closest_right[1]+1) + closest_right[1]), range((closest_right[1]+1), x_dim)))
        else:
            right_no = set()

        # Return the union of the four directions
        return up_no|down_no|left_no|right_no

class KinSho(Pieces):
    '''
        Gold General

        1) Can move one space orthogonally and 1 space diagonally up to the right or left
        2) Cannot be promoted
    '''
    def Available_Moves(self, y_dim, x_dim, same_color_locs, *args):
        '''
        Filter out all of the moves that are off of the board and on a space occupied by
            the same color
        
        :param y_dim (int): number of squares in the y direction (up/down)
        :param x_dim (int): number of squares in the x direction (right/left)
        :param same_color_locs (list): a list of tuples that house the location of the piece
            of the same color as the select piece
        :param args (list): used for extra parameters

        :return rm_checks (set): All possible moves a piece can make (Does not take into account
            checks)
        '''
        all_moves = KinSho.Get_Moves(self)
        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color

    def Get_Moves(self):
        if self.color=='black':
            return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,-1,0,0,1,-1], [0,0,1,-1,1,1])])
        else:
            return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,-1,0,0,1,-1], [0,0,1,-1,-1,-1])])

class GinSho(Pieces):
    '''
        Silver General

        1) Can move one space diagonally and one space forward
        2) Promotes to a gold general
    '''

    def Available_Moves(self, y_dim, x_dim, same_color_locs, *args):
        '''
        Filter out all of the moves that are off of the board and on a space occupied by
            the same color
        
        :param y_dim (int): number of squares in the y direction (up/down)
        :param x_dim (int): number of squares in the x direction (right/left)
        :param same_color_locs (list): a list of tuples that house the location of the piece
            of the same color as the select piece
        :param args (list): used for extra parameters

        :return rm_checks (set): All possible moves a piece can make (Does not take into account
            checks)
        '''
        if self.promoted: # promotes to a gold general move set
            all_moves = KinSho.Get_Moves(self)
        else:
            all_moves = GinSho.Get_Moves(self)

        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color

    def Get_Moves(self):
        if self.promoted:
            return KinSho.Get_Moves(self)
        else:
            if self.color=='black':
                return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,1,-1,-1,0], [1,-1,1,-1,1])])
            else:
                return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,1,-1,-1,0], [1,-1,1,-1,-1])])

class KeiMa(Pieces):
    '''
        Horse

        1) Can move two spaces forward and one space diagonally
        2) Can only move forward
        3) Promotes to a gold general
    '''

    def Available_Moves(self, y_dim, x_dim, same_color_locs, *args):
        '''
        Filter out all of the moves that are off of the board and on a space occupied by
            the same color
        
        :param y_dim (int): number of squares in the y direction (up/down)
        :param x_dim (int): number of squares in the x direction (right/left)
        :param same_color_locs (list): a list of tuples that house the location of the piece
            of the same color as the select piece
        :param args (list): used for extra parameters

        :return rm_checks (set): All possible moves a piece can make (Does not take into account
            checks)
        '''
        # An unpromoted knight cannot mvoe to the end of the board.
        # This is because it would have no available moves once it gets there.
        # The pawn must promote or not move at all

        if self.promoted: # promotes to gold general move set
            all_moves = KinSho.Get_Moves(self)
            on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))
        else:
            all_moves = KeiMa.Get_Moves(self)
            on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color

    def Get_Moves(self):
        if self.promoted:
            return KinSho.Get_Moves(self)
        else:
            if self.color=='black':
                return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,-1], [2,2])])
            else:
                return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,-1], [-2,-2])])

class Kyosha(Pieces):
    '''
        Lance

        1) Can move as many spaces as it wants straight forward
        2) Promotes to a gold general
    '''

    def Available_Moves(self, y_dim, x_dim, same_color_locs, opp_color_locs):
        '''
        Filter out all of the moves that are off of the board and on a space occupied by
            the same color
        
        :param y_dim (int): number of squares in the y direction (up/down)
        :param x_dim (int): number of squares in the x direction (right/left)
        :param same_color_locs (list): a list of tuples that house the location of the piece
            of the same color as the select piece
        :param args (list): used for extra parameters

        :return rm_checks (set): All possible moves a piece can make (Does not take into account
            checks)
        '''
        if self.promoted:
            all_moves = KinSho.Get_Moves(self)
            on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

            rm_same_color = on_board - same_color_locs
            if len(rm_same_color) == 0:
                return None
            else:
                return rm_same_color
        else:
            # An unpromoted lance cannot move to the end of the board.
            # This is because it would have no available moves once it gets there.
            # The pawn must promote or not move at all

            all_moves = Kyosha.Get_Moves(self)
            on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))
            orth_moves_beyong_pieces = Kyosha.Get_Orthogonal_Pieces(self, same_color_locs, opp_color_locs, y_dim)

            rm_same_color = on_board - same_color_locs
            rm_over_pieces = rm_same_color - orth_moves_beyong_pieces
            
            if len(rm_same_color) == 0:
                return None
            else:
                return rm_over_pieces

    def Get_Moves(self):
        if self.promoted:
            return KinSho.Get_Moves(self)
        else:
            if self.color=='black':
                return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([0,0,0,0,0,0,0,0], range(1,9))])
            else:
                return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([0,0,0,0,0,0,0,0], range(-8,0))])

    def Get_Orthogonal_Pieces(self, same_color_locs, opp_color_locs, y_dim):
        '''
        Rooks cannot jump over other pieces, therefore the moves the rook can make is limited
        by the closest piece in each direction orthogonally.

        This function finds the closest orthogonal pieces (If there are any) and creates a set of
        unavailable moves accordingly

        :param same_color_locs (list): locations of all the pieces that share the same color
            as the selected piece
        :param opp_color_locs (list):locations of all the pieces that have a differnet color
            as the selected piece
        :param y_dim (int): number of squares in the y direction (up/down)
        :param x_dim (int): number of squares in the x direction (right/left)

        :return (set): all of the moves the rook cannot take due to there being a 
            piece in the way. Used to filter all of the available moves.
        '''
         # Get the locations pf all the pieces on the board
        combine_locs = same_color_locs | opp_color_locs

        combine_locs = list(filter(None, combine_locs))

        # Set flags for the orthogonal locations to see if the same color
        # piece is closest in any of the four directions
        same_color_up = False
        same_color_down = False

        # Get a list of pieces that are ont he same file as the current piece
        closest_up = list(filter(lambda x: x[1] == self.pos[1] and x[0] < self.pos[0], combine_locs))
        closest_down = list(filter(lambda x: x[1] == self.pos[1] and x[0] > self.pos[0], combine_locs))
        
        # Find the closest piece out of the list of same file candidates
        closest_up = None if len(closest_up) == 0 else (sorted(closest_up, key=lambda y:y[0], reverse=True))[0]
        closest_down = None if len(closest_down) == 0 else (sorted(closest_down, key=lambda y:y[0]))[0]
        
        # Check to see if the closest piece is the same color or not as the current peice
        if len({closest_up} & same_color_locs) != 0: same_color_up = True
        if len({closest_down} & same_color_locs) != 0: same_color_down = True

        # If the closest piece is of the same color, you can move to the 
        # space one unit before. If it is of a different color, you can move
        # onto the same piece and capture.
        if same_color_up and closest_up is not None:
            up_no = set(zip(range(closest_up[0], -1, -1), [closest_up[1]]*(closest_up[0]+1)))
        elif not same_color_up and closest_up is not None:
            up_no = set(zip(range(closest_up[0]-1, -1, -1), [closest_up[1]]*(closest_up[0]+1)))
        else:
            up_no = set()

        if same_color_down and closest_down is not None:
            down_no = set(zip(range((closest_down[0]), y_dim), [closest_down[1]] * (((y_dim-1) - closest_down[0]) + closest_down[0]+1)))
        elif not same_color_down and closest_down is not None:
            down_no = set(zip(range((closest_down[0]+1), y_dim), [closest_down[1]] * ((y_dim - closest_down[0]) + closest_down[0]+1)))
        else:
            down_no = set()

        # Return the union of the four directions
        return up_no|down_no

class Fuhyo(Pieces):
    '''
        Foot Solider

        1) Move one space forward
        2) Promotes to gold general
    '''

    def Available_Moves(self, y_dim, x_dim, same_color_locs, *args):
        '''
        Filter out all of the moves that are off of the board and on a space occupied by
            the same color
        
        :param y_dim (int): number of squares in the y direction (up/down)
        :param x_dim (int): number of squares in the x direction (right/left)
        :param same_color_locs (list): a list of tuples that house the location of the piece
            of the same color as the select piece
        :param args (list): used for extra parameters

        :return rm_checks (set): All possible moves a piece can make (Does not take into account
            checks)
        '''

        # An unpromoted pawn cannot move to the end of the board.
        # This is because it would have no available moves once it gets there.
        # The pawn must promote or not move at all

        if self.promoted:
            all_moves = KinSho.Get_Moves(self)
            on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))
        else:
            all_moves = Fuhyo.Get_Moves(self)
            on_board = set(filter(lambda x: x[0]< y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color

    def Get_Moves(self):
        if self.promoted:
            return KinSho.Get_Moves(self)
        else:
            if self.color =='black':
                return {(self.pos[0]+1, self.pos[1])}
            else:
                return {(self.pos[0]-1, self.pos[1])}        