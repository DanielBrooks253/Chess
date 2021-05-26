###### Shatar (Mongolian Chess) ######

class Noyon(Pieces):
    '''
        Has the same movements as the modern day king

        1) Cannot Castle
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in zip([0,1,1,1,0,-1,-1,-1], [1,1,0,-1,-1,-1,0,1])])

class Tereg(Pieces):
    '''
        Has the same movement as the modern day rook
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in list(zip([1,2,3,4,5,6,7], [0,0,0,0,0,0,0])) + \
                                                                  list(zip([-1,-2,-3,-4,-5,-6,-7], [0,0,0,0,0,0,0])) + \
                                                                  list(zip([0,0,0,0,0,0,0], [1,2,3,4,5,6,7])) + \
                                                                  list(zip([0,0,0,0,0,0,0], [-1,-2,-3,-4,-5,-6,-7]))])

class Teme(Pieces):
    '''
        Has the same movement as the modern day bishop
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in list(zip(range(1,8), range(1,8))) + \
                                                                  list(zip(range(7,0,-1), range(-7,0))) + \
                                                                  list(zip(range(-7,0), range(7,0,-1))) + \
                                                                  list(zip(range(-7,0), range(-7,0)))])

class Mori(Pieces):
    '''
        Has the same movement as the modern day knight
    '''

    def Get_Moves(self):
        return set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in zip([2,2,1,1,-2,-2,-1,-1], [1,-1,2,-2,1,-1,2,-2])])

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
       return  set([(self.pos[0]+y, self.pos[1]+x) for x,y in zip([1,1,-1,-1], [1,-1,1,-1])]) | set([((self.pos[0]+y), (self.pos[1]+x)) for x,y in list(zip([1,2,3,4,5,6,7], [0,0,0,0,0,0,0])) + \
                                                                                                                                                   list(zip([-1,-2,-3,-4,-5,-6,-7], [0,0,0,0,0,0,0])) + \
                                                                                                                                                   list(zip([0,0,0,0,0,0,0], [1,2,3,4,5,6,7])) + \
                                                                                                                                                   list(zip([0,0,0,0,0,0,0], [-1,-2,-3,-4,-5,-6,-7]))]) 
