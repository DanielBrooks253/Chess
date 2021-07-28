###### Sittuyin (Burmese Chess) ######
class Pieces:
    def __init__(self, start_pos, set_up_coord, piece_name, piece_image, set_up_loc, color='white'):
        self.pos=start_pos
        self.piece_name=piece_name
        self.color = color.lower()
        self.piece_image = piece_image

        self.set_up_loc = set_up_loc
        self.set_up_coord = set_up_coord

    def place_piece(self, same_color_locs, *args):
        # all other pieces can be placed on the 2nd or third rows
        # There are no special restrictions
        if self.color == 'white':
            all_spots = set([(6,i) for i in range(0, 8)])|set([(5,i)for i in range(0, 8)])
        else:
            all_spots = set([(1,i) for i in range(0, 8)])|set([(2,i)for i in range(0, 8)])

        return all_spots - same_color_locs

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
    
    def place_piece(self, same_color_locs, opp_color_locs, opp_king_obj):
        # Rooks must be placed on back rank
        # cannot be placed opposite king on same file 
        # if there are no other pieces between (besides pawn) between them

        # All locations the rook can be placed
        if self.color == 'white':
            all_spots = set([(7, i) for i in range(0, 8)])
        else:
            all_spots = set([(0, i) for i in range(0, 8)])

        if opp_king_obj.set_up_loc is None:
            filter_nones = set(filter(None, same_color_locs|opp_color_locs))
            king_file = opp_king_obj.pos[0] # File the king is on
            piece_on_file = list(filter(lambda x: x[1] == king_file and 
                                                  x[0] < opp_king_obj.pos[0], filter_nones))

            if len(piece_on_file) < 3:
                rm_file = all_spots - set(filter(lambda x: x[1] == king_file, all_spots))
                rm_same_piece_loc = rm_file - same_color_locs

                return rm_same_piece_loc
            else:
                return all_spots - same_color_locs
        else:
            return all_spots - same_color_locs

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
