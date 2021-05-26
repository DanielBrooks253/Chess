###### Shatranj (Persian Chess) ######
class Pieces:
    def __init__(self, start_pos, piece_name, color='white'):
        self.pos=start_pos
        self.piece_name=piece_name
        self.color = color.lower()

        self.has_moved=False
        self.captured=False
        self.giving_check=False

    def check_check(self):
        pass

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

    def Available_Moves(self, y_dim, x_dim, same_color_locs):
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
    
    def Available_Moves(self, y_dim, x_dim, same_color_locs):
        all_moves = Rukh.Get_Moves(self)
        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color


class Asp(Pieces):
    '''
        Has the same movement as the modern day knight
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in zip([2,2,1,1,-2,-2,-1,-1], [1,-1,2,-2,1,-1,2,-2])])

    def Available_Moves(self, y_dim, x_dim, same_color_locs):
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

    def Available_Moves(self, y_dim, x_dim, same_color_locs):
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
    
    def Available_Moves(self, y_dim, x_dim, same_color_locs):
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

    def Available_Moves(self, y_dim, x_dim, same_color_locs):
        all_moves = Pil.Get_Moves(self)
        on_board = set(filter(lambda x: x[0]<y_dim and x[1]<x_dim and x[1]>=0 and x[0]>=0, all_moves))

        rm_same_color = on_board - same_color_locs
        
        if len(rm_same_color) == 0:
            return None
        else:
            return rm_same_color  
