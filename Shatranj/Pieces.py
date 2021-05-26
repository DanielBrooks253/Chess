###### Shatranj (Persian Chess) ######
class Pieces:
    def __init__(self, start_pos, piece_name, color='white'):
        self.pos=start_pos
        self.piece_name=piece_name
        self.color = color.lower()

        self.has_moved=False
        self.captured=False
        self.giving_check=False   

class Shah(Pieces):
    '''
        Has the same movements as the modern day king

        1) Cannot Castle
    '''
    def __init__(self, start_pos, piece_name, color='white'):
        self.in_check = False
        super().__init__(start_pos, piece_name, color)

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in zip([0,1,1,1,0,-1,-1,-1], [1,1,0,-1,-1,-1,0,1])])

    def Available_Moves(self, y_dim, x_dim, same_color_locs, opp_color_locs):
        all_moves = Shah.Get_Moves(self)
        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color

class Rukh(Pieces):
    '''
        Has the same movement as the modern day rook
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in list(zip([1,2,3,4,5,6,7], [0,0,0,0,0,0,0])) + \
                                                                  list(zip([-1,-2,-3,-4,-5,-6,-7], [0,0,0,0,0,0,0])) + \
                                                                  list(zip([0,0,0,0,0,0,0], [1,2,3,4,5,6,7])) + \
                                                                  list(zip([0,0,0,0,0,0,0], [-1,-2,-3,-4,-5,-6,-7]))])
    
    def Available_Moves(self, y_dim, x_dim, same_color_locs, opp_color_locs):
        all_moves = Rukh.Get_Moves(self)
        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        Rukh.Get_Orthogonal_Pieces(self, rm_same_color, opp_color_locs)

        # if len(rm_same_color) == 0:
        #     return None
        # else:
        #     return rm_same_color

    def Get_Orthogonal_Pieces(self, same_color_locs, opp_color_locs):
        combine_locs = same_color_locs | opp_color_locs

        closest_up = list(filter(lambda x: x[1] == self.pos[1] and x[0] < self.pos[0], combine_locs))
        closest_down = list(filter(lambda x: x[1] == self.pos[1] and x[0] > self.pos[0], combine_locs))
        closest_left = list(filter(lambda x: x[0] == self.pos[0] and x[1] < self.pos[1], combine_locs))
        closest_right = list(filter(lambda x: x[0] == self.pos[0] and x[1] > self.pos[1], combine_locs))

        closest_up = {None if len(closest_up) == 0 else (sorted(closest_up, key=lambda y:y[0], reverse=True))[0]}
        closest_down = {None if len(closest_down) == 0 else (sorted(closest_down, key=lambda y:y[0]))[0]}
        closest_left = {None if len(closest_left) == 0 else (sorted(closest_left, key=lambda y:y[1], reverse=True))[0]}
        closest_right = {None if len(closest_right) == 0 else (sorted(closest_right, key=lambda y:y[1]))[0]}

        if len(closest_up & same_color_locs) != 0:
            closest_up_color = self.color
        elif len(closest_up & same_color_locs) == 0 and self.color == 'white':
            closest_up_color = 'black'
        elif len(closest_up & same_color_locs) == 0 and self.color == 'black':
            closest_up_color = 'white'
        else:
            closest_up_color = None

        if len(closest_right & same_color_locs) != 0:
            closest_right_color = self.color
        elif len(closest_right & same_color_locs) == 0 and self.color == 'white':
            closest_right_color = 'black'
        elif len(closest_right & same_color_locs) == 0 and self.color == 'black':
            closest_right_color = 'white'
        else:
            closest_right_color = None

        if len(closest_left & same_color_locs) != 0:
            closest_left_color = self.color
        elif len(closest_left & same_color_locs) == 0 and self.color == 'white':
            closest_left_color = 'black'
        elif len(closest_left & same_color_locs) == 0 and self.color == 'black':
            closest_left_color = 'white'
        else:
            closest_left_color = None

        if len(closest_down & same_color_locs) != 0:
            closest_down_color = self.color
        elif len(closest_down & same_color_locs) == 0 and self.color == 'white':
            closest_down_color = 'black'
        elif len(closest_down & same_color_locs) == 0 and self.color == 'black':
            closest_down_color = 'white'
        else:
            closest_down_color = None

        return (closest_up_color, closest_left_color, closest_right_color, closest_down_color)

class Asp(Pieces):
    '''
        Has the same movement as the modern day knight
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in zip([2,2,1,1,-2,-2,-1,-1], [1,-1,2,-2,1,-1,2,-2])])

    def Available_Moves(self, y_dim, x_dim, same_color_locs, opp_color_locs):
        all_moves = Asp.Get_Moves(self)
        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color
        
class Pujada(Pieces):
    '''
        Similar to modern day pawn.

        1) Can only move one space forward; regardless of the turn
        2) If promoted (moving to the end of the board); it will always promote to a counselor
        3) Captures diagonally
    '''

    def __init__(self, start_pos, piece_name, color='white', promoted=False):
        self.promoted = promoted
        super().__init__(start_pos, piece_name, color)

    def Get_Moves(self):
        if self.promoted:
            return Farzin.Get_Moves(self)
        else:
            if self.color =='black':
                return {(self.pos[0]+1, self.pos[1])}
            else:
                return {(self.pos[0]-1, self.pos[1])}

    def Available_Moves(self, y_dim, x_dim, same_color_locs, opp_color_locs):
        all_moves = Pujada.Get_Moves(self)
        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color

class Farzin(Pieces):
    '''
        Place of the modern day Queen

        1) Can only move one space diagonally
    '''

    def Get_Moves(self):
        return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,1,-1,-1], [1,-1,1,-1])])
    
    def Available_Moves(self, y_dim, x_dim, same_color_locs, opp_color_locs):
        all_moves = Farzin.Get_Moves(self)
        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color

class Pil(Pieces):
    '''
        In place of the modern day bishop

        1) Can move two spaces diagonally
        2) Can jump over pieces like a modern day knight
    '''

    def Get_Moves(self):
        return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([2,2,-2,-2], [2,-2,2,-2])]) 

    def Available_Moves(self, y_dim, x_dim, same_color_locs, opp_color_locs):
        all_moves = Pil.Get_Moves(self)
        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color 
