###### Xiangqi (Chinese Chess) ######
class Pieces:
    def __init__(self, start_pos, location_y, location_x, piece_name, piece_image, color):
        '''
        Initalize the pieces class

        :param start_pos (tuple): The position of the piece on the board (y,x)
        :param piece_name (str): The name given to the piece
        :param piece_image (array pixels): The image to be displayed for the piece

        :param color (str): The color of the piece
            :default value: white

        :return Null (Nothing)
        '''
        self.piece_image = piece_image

        self.pos=start_pos
        self.piece_name=piece_name
        self.color = color.lower()

        self.location_x = location_x
        self.location_y = location_y
    
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
        self.location_y = (self.pos[0]*64+32, self.pos[0]*64+64)
        self.location_x = (self.pos[1]*64+32, self.pos[1]*64+64)
    
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
                if self.piece_name == 'wJ':
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
                if name_obj_copy['wJ'].check_check(
                    black_name_obj_copy,
                    black_loc_copy,
                    white_loc_copy):

                    checks |= {i}
                else:
                    pass

                # Reset all of the original positions for the different 
                # scenarios
                if self.piece_name == 'wJ':
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
                if self.piece_name == 'bJ':
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

                
                if name_obj_copy['bJ'].check_check(
                    white_name_obj_copy,
                    white_loc_copy,
                    black_loc_copy):

                    checks |= {i}
                else:
                    pass

                if self.piece_name == 'bJ':
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

class Chuh(Pieces):
    '''
        Has the same movement as the modern day rooks
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in list(zip([1,2,3,4,5,6,7,8], [0,0,0,0,0,0,0,0])) + \
                                                                  list(zip([-1,-2,-3,-4,-5,-6,-7,-8], [0,0,0,0,0,0,0,0])) + \
                                                                  list(zip([0,0,0,0,0,0,0,0,0], [1,2,3,4,5,6,7,8,9])) + \
                                                                  list(zip([0,0,0,0,0,0,0,0,0], [-1,-2,-3,-4,-5,-6,-7,-8,-9]))])

    def Available_Moves(self, y_dim, x_dim, same_color_locs, opp_color_locs):
        all_moves = Chuh.Get_Moves(self)
        orth_moves_beyond_pieces = Chuh.Get_Orthogonal_Pieces(self, same_color_locs, opp_color_locs, y_dim, x_dim)

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

class Ma(Pieces): # Xiangqi and Janggi Chess (Knight)
    '''
        Has the movement of the modern day knight

        1) Cannot jump over pieces
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in zip([2,2,1,1,-2,-2,-1,-1], [1,-1,2,-2,1,-1,2,-2])])

    def Available_Moves(self, y_dim, x_dim, same_color_locs, opp_color_locs):
        all_moves = Ma.Get_Moves(self)
        on_board = set(filter(lambda x: x[0] >= 0 and x[0] <= y_dim and x[1] >= 0 and x[1] <= x_dim, all_moves))

        rm_same_color = on_board - same_color_locs

        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color

class Jiang(Pieces):
    '''
        Modern Day King

        1) Can move orthongonally
        2) Must stay within the fortress
        3) Cannot move into straight line of other general
    '''

    def __init__(self, start_pos, location_y, location_x, piece_name, piece_image, color='white'):
        self.in_check = False
        super().__init__(start_pos, location_y, location_x, piece_name, piece_image, color)

    def Get_Moves(self):
        return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([0,0,1,-1], [1,-1,0,0])])

    def Available_Moves(self, y_dim, x_dim, same_color_locs, opp_color_locs):
        if self.color == 'white':
            y_dim_1 = 7
            y_dim_2 = 9
            x_dim_1 = 3
            x_dim_2 = 5
        else:
            y_dim_1 = 0
            y_dim_2 = 2
            x_dim_1 = 3
            x_dim_2 = 5

        all_moves = Jiang.Get_Moves(self)
        on_board = set(filter(lambda x: x[0] >= y_dim_1 and x[0] <= y_dim_2 and x[1] >= x_dim_1 and x[1] <= x_dim_2, all_moves))

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

class Shi(Pieces):
    '''
        Modern Day Queen

        1) Can move one space diagonally
        2) Must stay within the fortress like the general
    '''

    def Get_Moves(self):
        return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,1,-1,-1], [1,-1,1,-1])])

    def Available_Moves(self, y_dim, x_dim, same_color_locs, opp_color_locs):
        if self.color == 'white':
            y_dim_1 = 7
            y_dim_2 = 9
            x_dim_1 = 3
            x_dim_2 = 5
        else:
            y_dim_1 = 0
            y_dim_2 = 2
            x_dim_1 = 3
            x_dim_2 = 5

        all_moves = Shi.Get_Moves(self)
        on_board = set(filter(lambda x: x[0] >= y_dim_1 and x[0] <= y_dim_2 and x[1] >= x_dim_1 and x[1] <= x_dim_2, all_moves))

        rm_same_color = on_board - same_color_locs

        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color

class Shiang(Pieces):
    '''
        Modern Day Bishop

        1) Cannot cross the river (Center of the board)
        2) Can be blocked if an enemy piece is one space diagonal from piece
    '''

    def Get_Moves(self):
        return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([2,2,-2,-2], [2,-2,2,-2])]) 

    def Available_Moves(self, y_dim, x_dim, same_color_locs, opp_color_locs):
        all_moves = Shiang.Get_Moves(self)
        on_board = set(filter(lambda x: x[0] >= 0 and x[0] <= y_dim and x[1] >= 0 and x[1] <= x_dim, all_moves))

        rm_same_color = on_board - same_color_locs

        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color

class Pao(Pieces):
    '''
        1) Moves like a modern day rook
        2) Captures by jumping over a piece (enemy or friendly)
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in list(zip([1,2,3,4,5,6,7,8], [0,0,0,0,0,0,0,0])) + \
                                                                  list(zip([-1,-2,-3,-4,-5,-6,-7,-8], [0,0,0,0,0,0,0,0])) + \
                                                                  list(zip([0,0,0,0,0,0,0,0,0], [1,2,3,4,5,6,7,8,9])) + \
                                                                  list(zip([0,0,0,0,0,0,0,0,0], [-1,-2,-3,-4,-5,-6,-7,-8,-9]))])

    def Available_Moves(self, y_dim, x_dim, same_color_locs, opp_color_locs):
        all_moves = Pao.Get_Moves(self)
        orth_moves_beyond_pieces = Pao.Get_Orthogonal_Pieces(self, same_color_locs, opp_color_locs, y_dim, x_dim)

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

class Tsuh(Pieces):
    '''
        Modern day Pawn

        1) Moves one space forward
        2) Captures moving forward
        3) Once piece crosses the river; piece can move left and right
    '''

    def __init__(self, start_pos, location_y, location_x, piece_name, piece_image, color='white', cross_river=False):
        self.cross_river = cross_river
        super().__init__(start_pos, location_y, location_x, piece_name, piece_image, color)

    def Get_Moves(self):

        if self.color=='black':
            if self.cross_river:
                return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,-1,0], [0,0,1])])
            else:
                return {(self.pos[0]+1, self.pos[1])}
        else:
            if self.cross_river:
                return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([-1,1,0], [0,0,-1])])
            else:
                return {(self.pos[0]-1, self.pos[1])}

    def Promote_Pawn(self):
        self.cross_river = True
        
    def Available_Moves(self, y_dim, x_dim, same_color_locs, opp_color_locs):
        all_moves = Tsuh.Get_Moves(self)
        on_board = set(filter(lambda x: x[0] >= 0 and x[0] <= y_dim and x[1] >= 0 and x[1] <= x_dim, all_moves))

        rm_same_color = on_board - same_color_locs

        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color

