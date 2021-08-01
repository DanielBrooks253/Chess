###### Sittuyin (Burmese Chess) ######
class Pieces:
    def __init__(self, start_pos, set_up_coord, piece_name, piece_image, set_up_loc, color='white'):
        self.pos=start_pos
        self.piece_name=piece_name
        self.color = color.lower()
        self.piece_image = piece_image

        self.set_up_loc = set_up_loc
        self.set_up_coord = set_up_coord

    def place_piece(self, same_color_locs, *args):
        # all other pieces can be placed on the 2nd or third rows
        # There are no special restrictions
        if self.color == 'white':
            all_spots = set([(6,i) for i in range(0, 8)])|set([(5,i)for i in range(0, 8)])
        else:
            all_spots = set([(1,i) for i in range(0, 8)])|set([(2,i)for i in range(0, 8)])

        return all_spots - same_color_locs
    
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
            capture_check= (True, piece_insct[0]) if len(piece_insct) != 0 \
                            else (False, None)
        else:
            piece_insct = [key for key, values in board_obj.white_name_obj_dict.items()
                             if new_loc == values.pos]
            capture_check = (True, piece_insct[0]) if len(piece_insct) != 0 \
                        else (False, None)
                        
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
                if self.piece_name == 'wM0':
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
                if name_obj_copy['wM0'].check_check(
                    black_name_obj_copy,
                    black_loc_copy,
                    white_loc_copy):

                    checks |= {i}
                else:
                    pass

                # Reset all of the original positions for the different 
                # scenarios
                if self.piece_name == 'wM0':
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
                if self.piece_name == 'bM0':
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

                
                if name_obj_copy['bM0'].check_check(
                    white_name_obj_copy,
                    white_loc_copy,
                    black_loc_copy):

                    checks |= {i}
                else:
                    pass


                if self.piece_name == 'bM0':
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

class MinGyi(Pieces):
    '''
        Has the movement of the modern day king

        Cannot Castle
    '''
    def __init__(self, start_pos, set_up_coord, piece_name, piece_image, set_up_loc, color='white'):
        self.in_check = False
        super().__init__(start_pos, set_up_coord, piece_name, piece_image, set_up_loc, color)

    def Get_Moves(self):           
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in zip([0,1,1,1,0,-1,-1,-1], [1,1,0,-1,-1,-1,0,1])])

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
        all_moves = MinGyi.Get_Moves(self)
        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color
    
    def check_check(self, opp_objs, same_locs, opp_locs):
        '''
            See if the king is in check or not
        '''
        opp_moves = list(filter(None, [None if i.pos is None else i.Available_Moves(8, 8, same_locs, opp_locs) 
                     for i in opp_objs.values()]))

        if self.pos in set().union(*opp_moves):
            return True
        else:
            return False

class Yahhta(Pieces):
    '''
        Has the movement of the modern day rook
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in list(zip([1,2,3,4,5,6,7], [0,0,0,0,0,0,0])) + \
                                                                  list(zip([-1,-2,-3,-4,-5,-6,-7], [0,0,0,0,0,0,0])) + \
                                                                  list(zip([0,0,0,0,0,0,0], [1,2,3,4,5,6,7])) + \
                                                                  list(zip([0,0,0,0,0,0,0], [-1,-2,-3,-4,-5,-6,-7]))])
    
    def place_piece(self, same_color_locs, opp_color_locs, opp_king_obj):
        # Rooks must be placed on back rank
        # cannot be placed opposite king on same file 
        # if there are no other pieces between (besides pawn) between them

        # All locations the rook can be placed
        if self.color == 'white':
            all_spots = set([(7, i) for i in range(0, 8)])
        else:
            all_spots = set([(0, i) for i in range(0, 8)])

        if opp_king_obj.set_up_loc is None:
            filter_nones = set(filter(None, same_color_locs|opp_color_locs))
            king_file = opp_king_obj.pos[1] # File the king is on

            # Only have to check for less than, because there is not restriction on
            # the white rook placement. THey place first so there is no black kine
            # to worry about
            piece_on_file = list(filter(lambda x: x[1] == king_file and 
                                                  x[0] < opp_king_obj.pos[0], filter_nones))

            # Check to make sure there is a piece, besides the two pawns
            # between the "placed" rook and the opposing king
            if len(piece_on_file) < 3:
                rm_file = all_spots - set(filter(lambda x: x[1] == king_file, all_spots))
                rm_same_piece_loc = rm_file - same_color_locs

                return rm_same_piece_loc
            else:
                return all_spots - same_color_locs
        else:
            return all_spots - same_color_locs

    def Available_Moves(self, y_dim, x_dim, same_color_locs, opp_color_locs):
        all_moves = Yahhta.Get_Moves(self)
        orth_moves_beyond_pieces = Yahhta.Get_Orthogonal_Pieces(self, same_color_locs, opp_color_locs, y_dim, x_dim)

        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        rm_over_pieces = rm_same_color - orth_moves_beyond_pieces

        if len(rm_over_pieces) == 0:
            return None
        else:
            return rm_over_pieces

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

class Myin(Pieces):
    '''
        Has the movement of the modern day knight
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in zip([2,2,1,1,-2,-2,-1,-1], [1,-1,2,-2,1,-1,2,-2])])

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
        all_moves = Myin.Get_Moves(self)
        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color

class Ne(Pieces):
    '''
        Burmese Pawn

        1) Can only move one space 
        2) Captures diagonally
    '''

    def __init__(self, start_pos, set_up_coord, piece_name, piece_image, set_up_loc, color='white'):
        '''
        Initalize the Ne class

        :param start_pos (tuple): The position of the piece on the board (y,x)
        :param piece_name (str): The name given to the piece
        :param piece_image (array pixels): The image to be displayed for the piece

        :param color (str): The color of the piece
            :default value: white

        :return Null (Nothing)
        '''
        self.promoted = False
        super().__init__(start_pos, set_up_coord, piece_name, piece_image, set_up_loc, color)

    def Get_Moves(self, same_color_locs, args):
        ''' 
        Gets all available moves based off of the pieces position
        '''
        move = set()
        if self.color == 'black':
            if self.pos[0] == 7:
                self.promoted = True
                # self.piece_image = self.IMAGES['bF']
            else:
                pass
        else:
            if self.pos[0] == 0:
                self.promoted = True 
                # self.piece_image = self.IMAGES['wF']
            else:
                pass

        if self.promoted:
            return SitKe.Get_Moves(self)
        else:
            if self.color =='black':

                if (self.pos[0]+1, self.pos[1]) not in same_color_locs|args[0]:
                    move |= {(self.pos[0]+1, self.pos[1])}
                else:
                    pass

                if (self.pos[0]+1, self.pos[1]+1) in args[0]:
                    move |= {(self.pos[0]+1, self.pos[1]+1)}    
                else:
                    pass

                if (self.pos[0]+1, self.pos[1]-1) in args[0]:
                    move |= {(self.pos[0]+1, self.pos[1]-1)}      
                else:
                    pass
            else:
                if (self.pos[0]-1, self.pos[1]) not in same_color_locs|args[0]:
                    move |= {(self.pos[0]-1, self.pos[1])}
                else:
                    pass

                if (self.pos[0]-1, self.pos[1]-1) in args[0]:
                    move |= {(self.pos[0]-1, self.pos[1]-1)}      
                else:
                    pass

                if (self.pos[0]-1, self.pos[1]+1) in args[0]:
                    move |= {(self.pos[0]-1, self.pos[1]+1)}      
                else:
                    pass
        return move
    
    def Promote_pawn(self):
        '''
            Promote pawn to a queen
        '''
        self.promoted = True

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
        all_moves = Ne.Get_Moves(self, same_color_locs, args)
        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color

class SitKe(Pieces):
    '''
        Takes place of modern day Queen

        1) Can move one space diagonally 
    '''

    def Get_Moves(self):
        return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,1,-1,-1], [1,-1,1,-1])])

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
        all_moves = SitKe.Get_Moves(self)
        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color

class Sin(Pieces):
    '''
        Takes the place of a modern day bishop

        1) Can move one space diagonally and one space forward

        ** Move for each appendage (Diagonally for each leg and forward for the trunk)
    '''
    def Get_Moves(self):
        if self.color =='black':
            return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,1,-1,-1,0], [1,-1,1,-1,1])])
        else:
            return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,1,-1,-1,0], [1,-1,1,-1,-1])])

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
        all_moves = Sin.Get_Moves(self)
        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color