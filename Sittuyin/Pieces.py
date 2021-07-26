###### Sittuyin (Burmese Chess) ######
class Pieces:
    def __init__(self, start_pos, piece_name, piece_image, color='white'):
        self.pos=start_pos
        self.piece_name=piece_name
        self.color = color.lower()
        self.piece_image = piece_image

class MinGyi(Pieces):
    '''
        Has the movement of the modern day king

        1) Cannot Castle
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in zip([0,1,1,1,0,-1,-1,-1], [1,1,0,-1,-1,-1,0,1])])

class Yahhta(Pieces):
    '''
        Has the movement of the modern day rook
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in list(zip([1,2,3,4,5,6,7], [0,0,0,0,0,0,0])) + \
                                                                  list(zip([-1,-2,-3,-4,-5,-6,-7], [0,0,0,0,0,0,0])) + \
                                                                  list(zip([0,0,0,0,0,0,0], [1,2,3,4,5,6,7])) + \
                                                                  list(zip([0,0,0,0,0,0,0], [-1,-2,-3,-4,-5,-6,-7]))])

class Myin(Pieces):
    '''
        Has the movement of the modern day knight
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in zip([2,2,1,1,-2,-2,-1,-1], [1,-1,2,-2,1,-1,2,-2])])

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
