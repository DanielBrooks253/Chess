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

###### Shatranj (Persian Chess) ######

class Shah(Pieces):
    '''
        Has the same movements as the modern day king

        1) Cannot Castle
    '''

    def Get_Moves(self):
        return King.Get_Moves(self)

class Rukh(Pieces):
    '''
        Has the same movement as the modern day rook
    '''

    def Get_Moves(self):
        return Rook.Get_Moves(self)

class Asp(Pieces):
    '''
        Has the same movement as the modern day knight
    '''

    def Get_Moves(self):
        return Knight.Get_Moves(self)

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

class Farzin(Pieces):
    '''
        Place of the modern day Queen

        1) Can only move one space diagonally
    '''

    def Get_Moves(self):
        return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,1,-1,-1], [1,-1,1,-1])])

class Pil(Pieces):
    '''
        In place of the modern day bishop

        1) Can move two spaces diagonally
        2) Can jump over pieces like a modern day knight
    '''

    def Get_Moves(self):
        return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([2,2,-2,-2], [2,-2,2,-2])])   

###### Shatar (Mongolian Chess) ######

class Noyon(Pieces):
    '''
        Has the same movements as the modern day king

        1) Cannot Castle
    '''

    def Get_Moves(self):
        return King.Get_Moves(self)

class Tereg(Pieces):
    '''
        Has the same movement as the modern day rook
    '''

    def Get_Moves(self):
        return Rook.Get_Moves(self)

class Teme(Pieces):
    '''
        Has the same movement as teh modern day bishop
    '''

    def Get_Moves(self):
        return Bishop.Get_Moves(self)

class Mori(Pieces):
    '''
        Has the same movement as the modern day knight
    '''

    def Get_Moves(self):
        return Knight.Get_Moves(self)

class Fu(Pieces):
    '''
        Mongolain Pawn

        1) Can only move one space 
        2) Captures diagonally

        ** First move of the game, both players must move their pawn in front of their queen two spaces forward. **
    '''

    def Get_Moves(self):
        if self.color =='black':
            return {(self.pos[0]+1, self.pos[1])}
        else:
            return {(self.pos[0]-1, self.pos[1])}

    def Queens_Pawn_First_Move(self):
        if self.color =='black':
            return {(self.pos[0]+2, self.pos[1])}
        else:
            return {(self.pos[0]-2, self.pos[1])}

class Bers(Pieces):
    '''
        Takes place of modern day Queen

        1) Can move one space diagonally 
        2) Any number of spaces orthognally
    '''

    def Get_Moves(self):
       return Rook.Get_Moves(self) | set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,1,-1,-1], [1,-1,1,-1])])

###### Sittuyin (Burmese Chess) ######

class MinGyi(Pieces):
    '''
        Has the movement of the modern day king

        1) Cannot Castle
    '''

    def Get_Moves(self):
        return King.Get_Moves(self)

class Yahhta(Pieces):
    '''
        Has the movement of the modern day rook
    '''

    def Get_Moves(self):
        return Rook.Get_Moves(self)

class Myin(Pieces):
    '''
        Has the movement of the modern day knight
    '''

    def Get_Moves(self):
        return Knight.Get_Moves(self)

class Ne(Pieces):
    '''
        Burmese Pawn

        1) Can only move one space 
        2) Captures diagonally
    '''

    def Get_Moves(self):
        if self.color =='black':
            return {(self.pos[0]+1, self.pos[1])}
        else:
            return {(self.pos[0]-1, self.pos[1])}

class SitKe(Pieces):
    '''
        Takes place of modern day Queen

        1) Can move one space diagonally 
    '''

    def Get_Moves(self):
        return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,1,-1,-1], [1,-1,1,-1])])

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

###### Xiangqi (Chinese Chess) ######

class Chuh(Pieces):
    '''
        Has the same movement as the modern day rooks
    '''

    def Get_Moves(self):
        return Rook.Get_Moves(self) | set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([0,0,8,-8], [9,-9,0,0])])

class Ma(Pieces): # Xiangqi and Janggi Chess (Knight)
    '''
        Has the movement of the modern day knight

        1) Cannot jump over pieces
    '''

    def Get_Moves(self):
        return Knight.Get_Moves(self)

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
        return Rook.Get_Moves(self) | set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([0,0,8,-8], [9,-9,0,0])])

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
                return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,-1,0], [0,0,1])])
            else:
                return {(self.pos[0]+1, self.pos[1])}
        else:
            if cross_river:
                return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([-1,1,0], [0,0,-1])])
            else:
                return {(self.pos[0]-1, self.pos[1])}

###### Janggi (Korean Chess) ######
# Ma (Horse) Moves exactly like the chinese counter part

class Tcha(Pieces):
    '''
        Has the same movement as the modern day rook
    '''

    def Get_Moves(self):
        return Rook.Get_Moves(self) | set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([0,0,8,-8], [9,-9,0,0])])

class Koung(Pieces):
    '''
        Has the movement of the modern day king

        1) Must stay within fortress
    '''

    def Get_Moves(self):
        return King.Get_Moves(self)

class Sa(Pieces):
    '''
        Has the movement of the modern day king

        1) Must stay within the fortress
    '''

    def Get_Moves(self):
        return King.Get_Moves(self)

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
    def Get_Moves(self, in_fortress=False):
        if self.color=='black':
            if in_fortress:
                return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([0,1,-1,1,-1], [1,0,0,1,1])])
            else:
                return set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([0,1,-1], [1,0,0])])

        else:
            if in_fortress:
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
        return Rook.Get_Moves(self) | set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([0,0,8,-8], [9,-9,0,0])])

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
            return Bishop.Get_Moves(self) | set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,-1,0,0, 8,8,-8,-8], [0,0,1,-1,8,-8,8,-8])])
        else:
            return Bishop.Get_Moves(self) | set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([8,-8,8,-8], [8,8,-8,-8])])

class OSho(Pieces):
    '''
        Has the same movement as the modern day king
    '''

    def Get_Moves(self):
        return King.Get_Moves(self)

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
            return Rook.Get_Moves(self) | set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,1,-1,-1,0,0,8,-8], [1,-1,1,-1,8,-8,0,0])])
        else:
            return Rook.Get_Moves(self) | set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([0,0,8,-8], [8,-8,0,0])])

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
                return set([(self.pos[0]+y, self.pos[1]+y) for x,y in zip([1,-1], [-2,-2])])

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