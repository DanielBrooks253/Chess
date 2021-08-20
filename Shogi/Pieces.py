###### Shogi (Japanese Chess) ######
class Pieces:
    def __init__(self, start_pos, piece_name, piece_image, promoted_image, color, capture_name):
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
        self.capture_name = capture_name
        
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
                    white_loc_copy):

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
                if self.piece_name == 'O':
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
                    black_loc_copy):

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
        all_moves = Kaku.Get_Moves(self)
        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color

    def Get_Moves(self):
        if self.promoted:
            return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in list(zip(range(1,9), range(1,9))) + \
                                                                      list(zip(range(8,0,-1), range(-8,0))) + \
                                                                      list(zip(range(-8,0), range(8,0,-1))) + \
                                                                      list(zip(range(-8,0), range(-8,0)))]) | set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,-1,0,0], [0,0,1,-1])])
        else:
            return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in list(zip(range(1,9), range(1,9))) + \
                                                                      list(zip(range(8,0,-1), range(-8,0))) + \
                                                                      list(zip(range(-8,0), range(8,0,-1))) + \
                                                                      list(zip(range(-8,0), range(-8,0)))])

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
        
    def check_check(self, opp_objs, same_locs, opp_locs):
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
        opp_moves = list(filter(None, [None if i.pos is None else i.Available_Moves(8, 8, same_locs, opp_locs) 
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
        all_moves = Hisha.Get_Moves(self)
        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color

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
        all_moves = Kyosha.Get_Moves(self)
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
                return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([0,0,0,0,0,0,0,0], range(1,9))])
            else:
                return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([0,0,0,0,0,0,0,0], range(-8,0))])

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
        all_moves = Fuhyo.Get_Moves(self)
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
            if self.color =='black':
                return {(self.pos[0]+1, self.pos[1])}
            else:
                return {(self.pos[0]-1, self.pos[1])}        