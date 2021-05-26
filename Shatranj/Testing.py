import numpy as np
from Board import Board
from Pieces import Shah, Pil, Rukh, Asp, Pujada, Farzin

wp0 = Pujada((6,0), piece_name='wp0', color='white')
wp1 = Pujada((6,1), piece_name='wp1', color='white')
wp2 = Pujada((6,2), piece_name='wp2', color='white')
wp3 = Pujada((6,3), piece_name='wp3', color='white')
wp4 = Pujada((6,4), piece_name='wp4', color='white')
wp5 = Pujada((6,5), piece_name='wp5', color='white')
wp6 = Pujada((6,6), piece_name='wp6', color='white')
wp7 = Pujada((6,7), piece_name='wp7', color='white')

bp0 = Pujada((1,0), piece_name='bp0', color='black')
bp1 = Pujada((1,1), piece_name='bp1', color='black')
bp2 = Pujada((1,2), piece_name='bp2', color='black')
bp3 = Pujada((1,3), piece_name='bp3', color='black')
bp4 = Pujada((1,4), piece_name='bp4', color='black')
bp5 = Pujada((1,5), piece_name='bp5', color='black')
bp6 = Pujada((1,6), piece_name='bp6', color='black')
bp7 = Pujada((1,7), piece_name='bp7', color='black')

# Rukh (Rooks)
wr0 = Rukh((7,0), piece_name='wr0', color='white')
wr1 = Rukh((7,7), piece_name='wr1', color='white')

br0 = Rukh((0,0), piece_name='br0', color='black')
br1 = Rukh((0,7), piece_name='br1', color='black')

# Asp (Horses)
wa0 = Asp((7,1), piece_name='wa0', color='white')
wa1 = Asp((7,6), piece_name='wa1', color='white')

ba0 = Asp((0,1), piece_name='ba0', color='black')
ba1 = Asp((0,6), piece_name='ba1', color='black')

# Pil (Elephants)
we0 = Pil((7,2), piece_name='we0', color='white')
we1 = Pil((7,5), piece_name='we1', color='white')

be0 = Pil((0,2), piece_name='be0', color='black')
be1 = Pil((0,5), piece_name='be1', color='black')

# Shah (King) and Farzin (Queen)
wS = Shah((7,3), piece_name='wK ', color='white')
wF = Farzin((7,4), piece_name='wF ', color='white')

bS = Shah((0,3), piece_name='bS ', color='black')
bF = Farzin((0,4), piece_name='bF ', color='black')

board = Board(set([wp0.pos, wp1.pos, wp2.pos, wp3.pos,
                wp4.pos, wp5.pos, wp6.pos, wp7.pos,
                wr0.pos, wr1.pos, wa0.pos, wa1.pos,
                we0.pos, we1.pos, wS.pos, wF.pos]), 
              set([bp0.pos, bp1.pos, bp2.pos, bp3.pos,
                bp4.pos, bp5.pos, bp6.pos, bp7.pos,
                br0.pos, br1.pos, ba0.pos, ba1.pos,
                be0.pos, be1.pos, bS.pos, bF.pos]))

board.print_board(wp0,wp1,wp2,wp3,wp4,wp5,wp6,wp7,
                   wr0,wr1,wa0,wa1,we0,we1,wS,wF,
                   bp0,bp1,bp2,bp3,bp4,bp5,bp6,bp7,
                   br0,br1,ba0,ba1,be0,be1,bS,bF)

print(be0.Available_Moves(board.y_dim, board.x_dim, board.white_piece_loc))
# print(board.white_piece_loc)

# board.update_locs('white', (6,4), (0,0), is_captured=True)
# print(board.white_piece_loc)
# print(board.black_piece_loc)

