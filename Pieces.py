class Pieces:
    def __init__(self, start_pos, piece_name, color='white'):
        self.pos=start_pos
        self.piece_name=piece_name
        self.color = color.lower()

        self.has_moved=False
        self.captured=False
        self.promoted=False

###### English Chess ######

class Knight(Pieces):
    def Get_Moves(self):
        return set([((self.pos[0]+x), (self.pos[1]+y)) for x,y in zip([-2,-2,-1,1,2,2,1,-1], [-1,1,2,2,1,-2,-2,-2])])

class King(Pieces):
    def Get_Moves(self):
        return set([((self.pos[0]+x), (self.pos[1]+y)) for x,y in zip([0,1,1,1,0,-1,-1,-1], [1,1,0,-1,-1,-1,0,1])])
        
class Queen(Pieces):
    def Get_Moves(self):
        return set([((self.pos[0]+x), (self.pos[1]+y)) for x,y in list(zip(range(1,8), range(1,8))) + \
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
                return {(self.pos[0], self.pos[1]+1)}
            else:
                return set([(self.pos[0], self.pos[1]+y) for y in [1,2]])
        else:
            if self.has_moved:
                return {(self.pos[0], self.pos[1]-1)}
            else:
                return set([(self.pos[0], self.pos[1]-y) for y in [1,2]])

class Bishop(Pieces):
    def Get_Moves(self):
        return set([((self.pos[0]+x), (self.pos[1]+y)) for x,y in list(zip(range(1,8), range(1,8))) + \
                                                                  list(zip(range(7,0,-1), range(-7,0))) + \
                                                                  list(zip(range(-7,0), range(7,0,-1))) + \
                                                                  list(zip(range(-7,0), range(-7,0)))])

class Rook(Pieces):
    def Get_Moves(self):
        return set([((self.pos[0]+x), (self.pos[1]+y)) for x,y in list(zip([1,2,3,4,5,6,7], [0,0,0,0,0,0,0])) + \
                                                                  list(zip([-1,-2,-3,-4,-5,-6,-7], [0,0,0,0,0,0,0])) + \
                                                                  list(zip([0,0,0,0,0,0,0], [1,2,3,4,5,6,7])) + \
                                                                  list(zip([0,0,0,0,0,0,0], [-1,-2,-3,-4,-5,-6,-7]))])

###### Shatranj (Persian Chess) ######

# King has the same movement as the modern day King; Cannot Castle!!!
# Chariot has the same movement as the modern day Rook
# Horse has the same movement as the modern day Knight

class Foot_Solider(Pieces):
    '''
        Similar to modern day pawn.

        1) Can only move one space forward; regardless of the turn
        2) If promoted (movign to the end of the board); it will always promote to a counselor
        3) Captures diagonally
    '''
    def Get_Moves(self):
        if self.promoted:
            return Counselor.Get_Moves(self)
        else:
            if self.color =='black':
                return {(self.pos[0], self.pos[1]+1)}
            else:
                return {(self.pos[0], self.pos[1]-1)}

class Counselor(Pieces):
    '''
        Place of the modern day Queen

        1) Can only move one space diagonally
    '''

    def Get_Moves(self):
        return set([(self.pos[0]+x, self.pos[1]+y) for x,y in zip([1,1,-1,-1], [1,-1,1,-1])])

class Elephant(Pieces):
    '''
        In place of the modern day bishop

        1) Can move two spaces diagonally
        2) Can jump over pieces like a modern day knight
    '''

    def Get_Moves(self):
        return set([(self.pos[0]+x, self.pos[1]+y) for x,y in zip([2,2,-2,-2], [2,-2,2,-2])])   

###### Shatar (Mongolian Chess) ######

# Noyon (King) has the same movement as the modern day King; Cannot Castle!!!
# Tereg (Rook) has the same movement as the modern day Rook
# Teme (Bishop) has the same movement as the modern day Bishop
# Mori (Knight) has the same movement as the modern day Knight

class Fu(Pieces):
    '''
        Mongolain Pawn

        1) Can only move one space 
        2) Captures diagonally

        ** First move of the game, both players must move their pawn in front of their queen two spaces forward. **
    '''

    def Get_Moves(self):
        if self.color =='black':
            return {(self.pos[0], self.pos[1]+1)}
        else:
            return {(self.pos[0], self.pos[1]-1)}

    def Queens_Pawn_First_Move(self):
        if self.color =='black':
            return {(self.pos[0], self.pos[1]+2)}
        else:
            return {(self.pos[0], self.pos[1]-2)}

class Bers(Pieces):
    '''
        Takes place of modern day Queen

        1) Can move one space diagonally 
        2) Any number of spaces orthognally
    '''

    def Get_Moves(self):
       return set([((self.pos[0]+x), (self.pos[1]+y)) for x,y in list(zip([1,2,3,4,5,6,7], [0,0,0,0,0,0,0])) + \
                                                                 list(zip([-1,-2,-3,-4,-5,-6,-7], [0,0,0,0,0,0,0])) + \
                                                                 list(zip([0,0,0,0,0,0,0], [1,2,3,4,5,6,7])) + \
                                                                 list(zip([0,0,0,0,0,0,0], [-1,-2,-3,-4,-5,-6,-7])) + \
                                                                 list(zip([0,1,1,1,0,-1,-1,-1], [1,1,0,-1,-1,-1,0,1]))]) 

###### Sittuyin (Burmese Chess) ######

# Min-gyi (King) has the same movement as the modern day King; Cannot Castle!!!
# Yahhta (Rook) has the same movement as the modern day Rook
# Myin (Knight) has the same movement as the modern day Knight

class Ne(Pieces):
    '''
        Burmese Pawn

        1) Can only move one space 
        2) Captures diagonally
    '''

    def Get_Moves(self):
        if self.color =='black':
            return {(self.pos[0], self.pos[1]+1)}
        else:
            return {(self.pos[0], self.pos[1]-1)}

class SitKe(Pieces):
    '''
        Takes place of modern day Queen

        1) Can move one space diagonally 
    '''

    def Get_Moves(self):
        return set([(self.pos[0]+x, self.pos[1]+y) for x,y in zip([1,1,-1,-1], [1,-1,1,-1])])

class Sin(Pieces):
    '''
        Takes the place of a modern day bishop

        1) Can move one space diagonally and one space forward

        ** Move for each appendage (Diagonally for each leg and forward for the trunk)
    '''
    def Get_Moves(self):

        if self.color =='black':
            return set([(self.pos[0]+x, self.pos[1]+y) for x,y in zip([1,1,-1,-1,0], [1,-1,1,-1,-1])])
        else:
            return set([(self.pos[0]+x, self.pos[1]+y) for x,y in zip([1,1,-1,-1,0], [1,-1,1,-1,1])])

###### Xiangqi (Chinese Chess) ######
# Chuh (Rook) has the same movement as the modern day Rook
# Ma (Knight) Has the same movement as the modern day Knight
    # Cannot jump over pieces

class JiangShuai(Pieces):
    '''
        Modern Day King

        1) Can move orthongonally
        2) Must stay within the fortress
        3) Cannot move into straight line of other general
    '''

    def Get_Moves(self):
        return set([(self.pos[0]+x, self.pos[1]+y) for x,y in zip([1,-1,0,0], [0,0,1,-1])])

class Shi(Pieces):
    '''
        Modern Day Queen

        1) Can move one space diagonally
        2) Must stay within the fortress like the general
    '''

    def Get_Moves(self):
        return set([(self.pos[0]+x, self.pos[1]+y) for x,y in zip([1,1,-1,-1], [1,-1,1,-1])])


class Shiang(Pieces):
    '''
        Modern Day Bishop

        1) Cannot cross the river (Center of the board)
        2) Can be blocked if an enemy piece is one space diagonal from piece
    '''

    def Get_Moves(self):
        return set([(self.pos[0]+x, self.pos[1]+y) for x,y in zip([2,2,-2,-2], [2,-2,2,-2])]) 

class Pao(Pieces):
    '''
        1) Moves like a modern day rook
        2) Captures by jumping over a piece (enemy or friendly)
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+x), (self.pos[1]+y)) for x,y in list(zip([1,2,3,4,5,6,7], [0,0,0,0,0,0,0])) + \
                                                                  list(zip([-1,-2,-3,-4,-5,-6,-7], [0,0,0,0,0,0,0])) + \
                                                                  list(zip([0,0,0,0,0,0,0], [1,2,3,4,5,6,7])) + \
                                                                  list(zip([0,0,0,0,0,0,0], [-1,-2,-3,-4,-5,-6,-7]))])

class PingTsuh(Pieces):
    '''
        Modern day Pawn

        1) Moves one space forward
        2) Captures moving forward
        3) Once piece crosses the river; piece can move left and right
    '''

    def Get_Moves(self, cross_river=False):

        if self.color=='black':
            if cross_river:
                return set([(self.pos[0]+x, self.pos[1]+y) for x,y in zip([1,0,0], [0,1,-1])])
            else:
                return {(self.pos[0], self.pos[1]+1)}
        else:
            if cross_river:
                return set([(self.pos[0]+x, self.pos[1]+y) for x,y in zip([-1,0,0], [0,1,-1])])
            else:
                return {(self.pos[0], self.pos[1]-1)}

###### Janggi (Korean Chess) ######
# Koung (King) has the same movement as the modern day King
    # Must stay within the fortress
# Sa (Queen) has the same movement as the modern day King
    # Must stay within the fortress
# Ma (Knight) has the same movement as the modern day Knight
    # Cannot jump over a piece
# Tcha (Rook) has the same movement as the modern say Rook

class Syang(Pieces):
    '''
        Place of the modern day bishop

        1) Moves one space forward and two spaces diagonally
        2) Cannot jump over any pieces along the movement path
    '''

    def Get_Moves(self):
        return set([(self.pos[0]+x, self.pos[1]+y) for x,y in zip([3,3,-3-3], [2,-2,2,-2])])

class PyengTjol(Pieces):
    '''
        Place of the modern day pawn

        1) Can move forward and left/right
        2) Captures on movement paths
        3) If the pawn is in the fortress, the pawn can move diagonally
    '''
    def Get_Moves(self, in_fortress=False):
        if self.color=='black':
            if in_fortress:
                return set([(self.pos[0]+x, self.pos[1]+y) for x,y in zip([0,1,-1,1,-1], [1,0,0,1,1])])
            else:
                return set([(self.pos[0]+x, self.pos[1]+y) for x,y in zip([0,1,-1], [1,0,0])])

        else:
            if in_fortress:
                return set([(self.pos[0]+x, self.pos[1]+y) for x,y in zip([0,1,-1,1,-1], [-1,0,0,-1,-1])])
            else:
                return set([(self.pos[0]+x, self.pos[1]+y) for x,y in zip([0,1,-1], [-1,0,0])])

class Hpo(Pieces):
    '''
        1) Moves like a modern day rook
        2) Must jump over a piece in order to move/capture
        3) Cannot jump over another Hpo
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+x), (self.pos[1]+y)) for x,y in list(zip([1,2,3,4,5,6,7], [0,0,0,0,0,0,0])) + \
                                                                  list(zip([-1,-2,-3,-4,-5,-6,-7], [0,0,0,0,0,0,0])) + \
                                                                  list(zip([0,0,0,0,0,0,0], [1,2,3,4,5,6,7])) + \
                                                                  list(zip([0,0,0,0,0,0,0], [-1,-2,-3,-4,-5,-6,-7]))])

###### Shogi (Japanese Chess) ######
# OSho (King) has the same movement as the modern day King
# Hisha (Rook) has the same movement as the modern day Rook
    # Promotes to being able to move one space diagonally
# Kaku (Bishop) has the same movement as the modern day Bishop
    # Promotes to being able to move one space Orthogonally

class KinSho(Pieces):
    '''
        Gold General

        1) Can move one space orthogonally and 1 space diagonally up to teh right or left
        2) Cannot be promoted
    '''
    
    def Get_Moves(self):
        if self.color=='black':
            return set([(self.pos[0]+x, self.pos[1]+y) for x,y in zip([1,-1,0,0,1,-1], [0,0,1,-1,1,1])])
        else:
            return set([(self.pos[0]+x, self.pos[1]+y) for x,y in zip([1,-1,0,0,1,-1], [0,0,1,-1,-1,-1])])

class GinSho(Pieces):
    '''
        Silver General

        1) Can move one space diagonally and one space forward
        2) Promotes to a gold general
    '''

    def Get_Moves(self):
        if self.promoted:
            return KinSho.Get_Moves(self)
        else:
            if self.color=='black':
                return set([(self.pos[0]+x, self.pos[1]+y) for x,y in zip([1,1,-1,-1,0], [1,-1,1,-1,1])])
            else:
                return set([(self.pos[0]+x, self.pos[1]+y) for x,y in zip([1,1,-1,-1,0], [1,-1,1,-1,-1])])

class KeiMa(Pieces):
    '''
        Horse

        1) Can move two spaces forward and one space diagonally
        2) Can only move forward
        30 Promotes to a gold general
    '''

    def Get_Moves(self):
        if self.promoted:
            return KinSho.Get_Moves(self)
        else:
            if self.color=='black':
                return set([(self.pos[0]+x, self.pos[y]) for x,y in zip([1,-1], [2,2])])
            else:
                return set([(self.pos[0]+x, self.pos[y]) for x,y in zip([1,-1], [-2,-2])])

class Kyosha(Pieces):
    '''
        Lance

        1) Can move as many spaces as it wants straight forward
        2) Promotes to a gold general
    '''

    def Get_Moves(self):
        if self.promoted:
            return KinSho.Get_Moves(self)
        else:
            if self.color=='black':
                return set([(self.pos[0]+x, self.pox[1]+y) for x,y in zip([0,0,0,0,0,0,0], range(1,8))])
            else:
                return set([(self.pos[0]+x, self.pox[1]+y) for x,y in zip([0,0,0,0,0,0,0], range(-7,0))])

class Fuhyo(Pieces):
    '''
        Foot Solider

        1) Move one space forward
        2) Promotes to gold general
    '''

    def Get_Moves(self):
        if self.promoted:
            return KinSho.Get_Moves(self)
        else:
            if self.color =='black':
                return {(self.pos[0], self.pos[1]+1)}
            else:
                return {(self.pos[0], self.pos[1]-1)}        