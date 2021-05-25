###### Xiangqi (Chinese Chess) ######

class Chuh(Pieces):
    '''
        Has the same movement as the modern day rooks
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in list(zip([1,2,3,4,5,6,7,8], [0,0,0,0,0,0,0,0])) + \
                                                                  list(zip([-1,-2,-3,-4,-5,-6,-7,-8], [0,0,0,0,0,0,0,0])) + \
                                                                  list(zip([0,0,0,0,0,0,0,0,0], [1,2,3,4,5,6,7,8,9])) + \
                                                                  list(zip([0,0,0,0,0,0,0,0,0], [-1,-2,-3,-4,-5,-6,-7,-8,-9]))])

class Ma(Pieces): # Xiangqi and Janggi Chess (Knight)
    '''
        Has the movement of the modern day knight

        1) Cannot jump over pieces
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in zip([2,2,1,1,-2,-2,-1,-1], [1,-1,2,-2,1,-1,2,-2])])

class JiangShuai(Pieces):
    '''
        Modern Day King

        1) Can move orthongonally
        2) Must stay within the fortress
        3) Cannot move into straight line of other general
    '''

    def Get_Moves(self):
        return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([0,0,1,-1], [1,-1,0,0])])

class Shi(Pieces):
    '''
        Modern Day Queen

        1) Can move one space diagonally
        2) Must stay within the fortress like the general
    '''

    def Get_Moves(self):
        return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,1,-1,-1], [1,-1,1,-1])])


class Shiang(Pieces):
    '''
        Modern Day Bishop

        1) Cannot cross the river (Center of the board)
        2) Can be blocked if an enemy piece is one space diagonal from piece
    '''

    def Get_Moves(self):
        return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([2,2,-2,-2], [2,-2,2,-2])]) 

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

class PingTsuh(Pieces):
    '''
        Modern day Pawn

        1) Moves one space forward
        2) Captures moving forward
        3) Once piece crosses the river; piece can move left and right
    '''

    def __init__(self, start_pos, piece_name, color='white', cross_river=False):
        self.cross_river = cross_river
        super().__init__(start_pos, piece_name, color)

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