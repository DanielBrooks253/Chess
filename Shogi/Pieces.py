###### Shogi (Japanese Chess) ######

class Kaku(Pieces):
    '''
        Has the movement of the modern day bishop

        1) When promoted, can move one space orthogonally
    '''

    def __init__(self, start_pos, piece_name, color='white', promoted=False):
        self.promoted=promoted
        super().__init__(start_pos, piece_name, color)

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

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in zip([0,1,1,1,0,-1,-1,-1], [1,1,0,-1,-1,-1,0,1])])
        
class Hisha(Pieces):
    '''
        Has the same movement as the modern day rook

        1) When promoted, can move one space diagonally
    '''

    def __init__(self, start_pos, piece_name, color='white', promoted=False):
        self.promoted=promoted
        super().__init__(start_pos, piece_name, color)

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

    def __init__(self, start_pos, piece_name, color='white', promoted=False):
        self.promoted=promoted
        super().__init__(start_pos, piece_name, color)

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

    def __init__(self, start_pos, piece_name, color='white', promoted=False):
        self.promoted=promoted
        super().__init__(start_pos, piece_name, color)

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
    def __init__(self, start_pos, piece_name, color='white', promoted=False):
        self.promoted=promoted
        super().__init__(start_pos, piece_name, color)

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

    def __init__(self, start_pos, piece_name, color='white', promoted=False):
        self.promoted=promoted
        super().__init__(start_pos, piece_name, color)

    def Get_Moves(self):
        if self.promoted:
            return KinSho.Get_Moves(self)
        else:
            if self.color =='black':
                return {(self.pos[0]+1, self.pos[1])}
            else:
                return {(self.pos[0]-1, self.pos[1])}        