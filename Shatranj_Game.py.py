import numpy as np
import Pieces

board = np.chararray((8,8), itemsize=3)
board[:] = ""

# Pujada (Pawns)
wp0 = Pieces.Pujada((6,0), piece_name='wp0', color='white')
wp1 = Pieces.Pujada((6,1), piece_name='wp1', color='white')
wp2 = Pieces.Pujada((6,2), piece_name='wp2', color='white')
wp3 = Pieces.Pujada((6,3), piece_name='wp3', color='white')
wp4 = Pieces.Pujada((6,4), piece_name='wp4', color='white')
wp5 = Pieces.Pujada((6,5), piece_name='wp5', color='white')
wp6 = Pieces.Pujada((6,6), piece_name='wp6', color='white')
wp7 = Pieces.Pujada((6,7), piece_name='wp7', color='white')

bp0 = Pieces.Pujada((1,0), piece_name='bp0', color='black')
bp1 = Pieces.Pujada((1,1), piece_name='bp1', color='black')
bp2 = Pieces.Pujada((1,2), piece_name='bp2', color='black')
bp3 = Pieces.Pujada((1,3), piece_name='bp3', color='black')
bp4 = Pieces.Pujada((1,4), piece_name='bp4', color='black')
bp5 = Pieces.Pujada((1,5), piece_name='bp5', color='black')
bp6 = Pieces.Pujada((1,6), piece_name='bp6', color='black')
bp7 = Pieces.Pujada((1,7), piece_name='bp7', color='black')

# Rukh (Rooks)
wr0 = Pieces.Rukh((7,0), piece_name='wr0', color='white')
wr1 = Pieces.Rukh((7,7), piece_name='wr1', color='white')

br0 = Pieces.Rukh((0,0), piece_name='br0', color='black')
br1 = Pieces.Rukh((0,7), piece_name='br1', color='black')

# Asp (Horses)
wa0 = Pieces.Asp((7,1), piece_name='wa0', color='white')
wa1 = Pieces.Asp((7,6), piece_name='wa2', color='white')

ba0 = Pieces.Asp((0,1), piece_name='ba0', color='black')
ba1 = Pieces.Asp((0,6), piece_name='ba2', color='black')

# Pil (Elephants)
we0 = Pieces.Pil((7,2), piece_name='we0', color='white')
we1 = Pieces.Pil((7,5), piece_name='we2', color='white')

be0 = Pieces.Pil((0,2), piece_name='be0', color='black')
be1 = Pieces.Pil((0,5), piece_name='be2', color='black')

# Shah (King) and Farzin (Queen)
wS = Pieces.Shah((7,3), piece_name='wK ', color='white')
wF = Pieces.Farzin((7,4), piece_name='wF ', color='white')

bS = Pieces.Shah((0,3), piece_name='bS ', color='black')
bF = Pieces.Farzin((0,4), piece_name='bF ', color='black')

##### Show Board #####
board[wp0.pos[0], wp0.pos[1]] = wp0.piece_name
board[wp1.pos[0], wp1.pos[1]] = wp1.piece_name 
board[wp2.pos[0], wp2.pos[1]] = wp2.piece_name 
board[wp3.pos[0], wp3.pos[1]] = wp3.piece_name 
board[wp4.pos[0], wp4.pos[1]] = wp4.piece_name 
board[wp5.pos[0], wp5.pos[1]] = wp5.piece_name 
board[wp6.pos[0], wp6.pos[1]] = wp6.piece_name 
board[wp7.pos[0], wp7.pos[1]] = wp7.piece_name 

board[bp0.pos[0], bp0.pos[1]] = bp0.piece_name
board[bp1.pos[0], bp1.pos[1]] = bp1.piece_name 
board[bp2.pos[0], bp2.pos[1]] = bp2.piece_name 
board[bp3.pos[0], bp3.pos[1]] = bp3.piece_name 
board[bp4.pos[0], bp4.pos[1]] = bp4.piece_name 
board[bp5.pos[0], bp5.pos[1]] = bp5.piece_name 
board[bp6.pos[0], bp6.pos[1]] = bp6.piece_name 
board[bp7.pos[0], bp7.pos[1]] = bp7.piece_name  

board[wr0.pos[0], wr0.pos[1]] = wr0.piece_name 
board[wr1.pos[0], wr1.pos[1]] = wr1.piece_name  
board[br0.pos[0], br0.pos[1]] = br0.piece_name 
board[br1.pos[0], br1.pos[1]] = br1.piece_name  

board[wa0.pos[0], wa0.pos[1]] = wa0.piece_name 
board[wa1.pos[0], wa1.pos[1]] = wa1.piece_name  
board[ba0.pos[0], ba0.pos[1]] = ba0.piece_name 
board[ba1.pos[0], ba1.pos[1]] = ba1.piece_name  

board[we0.pos[0], we0.pos[1]] = we0.piece_name 
board[we1.pos[0], we1.pos[1]] = we1.piece_name  
board[be0.pos[0], be0.pos[1]] = be0.piece_name 
board[be1.pos[0], be1.pos[1]] = be1.piece_name  

board[wS.pos[0], wS.pos[1]] = wS.piece_name 
board[wF.pos[0], wF.pos[1]] = wF.piece_name  
board[bS.pos[0], bS.pos[1]] = bS.piece_name 
board[bF.pos[0], bF.pos[1]] = bF.piece_name  

print(board)