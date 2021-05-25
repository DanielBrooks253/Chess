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

###### English Chess ######

class Knight(Pieces):
    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in zip([2,2,1,1,-2,-2,-1,-1], [1,-1,2,-2,1,-1,2,-2])])

class King(Pieces):
    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in zip([0,1,1,1,0,-1,-1,-1], [1,1,0,-1,-1,-1,0,1])])
        
class Queen(Pieces):
    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in list(zip(range(1,8), range(1,8))) + \
                                                                  list(zip(range(7,0,-1), range(-7,0))) + \
                                                                  list(zip(range(-7,0), range(7,0,-1))) + \
                                                                  list(zip(range(-7,0), range(-7,0))) + \
                                                                  list(zip([1,2,3,4,5,6,7], [0,0,0,0,0,0,0])) + \
                                                                  list(zip([-1,-2,-3,-4,-5,-6,-7], [0,0,0,0,0,0,0])) + \
                                                                  list(zip([0,0,0,0,0,0,0], [1,2,3,4,5,6,7])) + \
                                                                  list(zip([0,0,0,0,0,0,0], [-1,-2,-3,-4,-5,-6,-7]))])

class Pawn(Pieces):
    def Get_Moves(self):
        if self.color =='black':
            if self.has_moved:
                return {(self.pos[0]+1, self.pos[1])}
            else:
                return set([(self.pos[0]+y, self.pos[1]) for y in [1,2]])
        else:
            if self.has_moved:
                return {(self.pos[0]-1, self.pos[1])}
            else:
                return set([(self.pos[0]-y, self.pos[1]) for y in [1,2]])

class Bishop(Pieces):
    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in list(zip(range(1,8), range(1,8))) + \
                                                                  list(zip(range(7,0,-1), range(-7,0))) + \
                                                                  list(zip(range(-7,0), range(7,0,-1))) + \
                                                                  list(zip(range(-7,0), range(-7,0)))])

class Rook(Pieces):
    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in list(zip([1,2,3,4,5,6,7], [0,0,0,0,0,0,0])) + \
                                                                  list(zip([-1,-2,-3,-4,-5,-6,-7], [0,0,0,0,0,0,0])) + \
                                                                  list(zip([0,0,0,0,0,0,0], [1,2,3,4,5,6,7])) + \
                                                                  list(zip([0,0,0,0,0,0,0], [-1,-2,-3,-4,-5,-6,-7]))])
