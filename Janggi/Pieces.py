###### Janggi (Korean Chess) ######
# Ma (Horse) Moves exactly like the chinese counter part

class Tcha(Pieces):
    '''
        Has the same movement as the modern day rook
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in list(zip([1,2,3,4,5,6,7,8], [0,0,0,0,0,0,0,0])) + \
                                                                  list(zip([-1,-2,-3,-4,-5,-6,-7,-8], [0,0,0,0,0,0,0,0])) + \
                                                                  list(zip([0,0,0,0,0,0,0,0,0], [1,2,3,4,5,6,7,8,9])) + \
                                                                  list(zip([0,0,0,0,0,0,0,0,0], [-1,-2,-3,-4,-5,-6,-7,-8,-9]))])

class Ma(Pieces):
    '''
        Has the movement of the modern day knight

        1) Cannot jump over pieces
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in zip([2,2,1,1,-2,-2,-1,-1], [1,-1,2,-2,1,-1,2,-2])])

class Koung(Pieces):
    '''
        Has the movement of the modern day king

        1) Must stay within fortress
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in zip([2,2,1,1,-2,-2,-1,-1], [1,-1,2,-2,1,-1,2,-2])])


class Sa(Pieces):
    '''
        Has the movement of the modern day king

        1) Must stay within the fortress
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in zip([2,2,1,1,-2,-2,-1,-1], [1,-1,2,-2,1,-1,2,-2])])


class Syang(Pieces):
    '''
        Place of the modern day bishop

        1) Moves one space forward and two spaces diagonally
        2) Cannot jump over any pieces along the movement path
    '''

    def Get_Moves(self):
        return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([2,2,-2,-2,3,-3,3,-3], [3,-3,3,-3,2,2,-2,-2])])

class PyengTjol(Pieces):
    '''
        Place of the modern day pawn

        1) Can move forward and left/right
        2) Captures on movement paths
        3) If the pawn is in the fortress, the pawn can move diagonally
    '''

    def __init__(self, start_pos, piece_name, color='white', in_fortress=False):
        self.in_fortress = in_fortress
        super().__init__(start_pos, piece_name, color)

    def Get_Moves(self, in_fortress=False):
        if self.color=='black':
            if self.in_fortress:
                return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([0,1,-1,1,-1], [1,0,0,1,1])])
            else:
                return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([0,1,-1], [1,0,0])])

        else:
            if self.in_fortress:
                return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([0,1,-1,1,-1], [-1,0,0,-1,-1])])
            else:
                return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([0,1,-1], [-1,0,0])])

class Hpo(Pieces):
    '''
        1) Moves like a modern day rook
        2) Must jump over a piece in order to move/capture
        3) Cannot jump over another Hpo
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in list(zip([1,2,3,4,5,6,7,8], [0,0,0,0,0,0,0,0])) + \
                                                                  list(zip([-1,-2,-3,-4,-5,-6,-7,-8], [0,0,0,0,0,0,0,0])) + \
                                                                  list(zip([0,0,0,0,0,0,0,0,0], [1,2,3,4,5,6,7,8,9])) + \
                                                                  list(zip([0,0,0,0,0,0,0,0,0], [-1,-2,-3,-4,-5,-6,-7,-8,-9]))])
        
