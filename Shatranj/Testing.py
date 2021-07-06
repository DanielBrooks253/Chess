import numpy as np
from Board import Board
from Pieces import Shah, Pil, Rukh, Asp, Pujada, Farzin

# Initialize all of the pieces on the board
wp0 = Pujada((6,0), piece_type='one', piece_name='wp0', color='white')
wp1 = Pujada((6,1), piece_type='one', piece_name='wp1', color='white')
wp2 = Pujada((6,2), piece_type='one', piece_name='wp2', color='white')
wp3 = Pujada((6,3), piece_type='one', piece_name='wp3', color='white')
wp4 = Pujada((6,4), piece_type='one', piece_name='wp4', color='white')
wp5 = Pujada((6,5), piece_type='one', piece_name='wp5', color='white')
wp6 = Pujada((6,6), piece_type='one', piece_name='wp6', color='white')
wp7 = Pujada((6,7), piece_type='one', piece_name='wp7', color='white')

bp0 = Pujada((1,0), piece_type='one', piece_name='bp0', color='black')
bp1 = Pujada((1,1), piece_type='one', piece_name='bp1', color='black')
bp2 = Pujada((1,2), piece_type='one', piece_name='bp2', color='black')
bp3 = Pujada((1,3), piece_type='one', piece_name='bp3', color='black')
bp4 = Pujada((1,4), piece_type='one', piece_name='bp4', color='black')
bp5 = Pujada((1,5), piece_type='one', piece_name='bp5', color='black')
bp6 = Pujada((1,6), piece_type='one', piece_name='bp6', color='black')
bp7 = Pujada((1,7), piece_type='one', piece_name='bp7', color='black')

# Rukh (Rooks)
wr0 = Rukh((7,0), piece_type='multi', piece_name='wr0', color='white')
wr1 = Rukh((7,7), piece_type='multi', piece_name='wr1', color='white')

br0 = Rukh((0,0), piece_type='multi', piece_name='br0', color='black')
br1 = Rukh((0,7), piece_type='multi', piece_name='br1', color='black')

# Asp (Horses)
wa0 = Asp((7,1), piece_type='one', piece_name='wa0', color='white')
wa1 = Asp((7,6), piece_type='one', piece_name='wa1', color='white')

ba0 = Asp((0,1), piece_type='one', piece_name='ba0', color='black')
ba1 = Asp((0,6), piece_type='one', piece_name='ba1', color='black')

# Pil (Elephants)
we0 = Pil((7,2), piece_type='one', piece_name='we0', color='white')
we1 = Pil((7,5), piece_type='one', piece_name='we1', color='white')

be0 = Pil((0,2), piece_type='one', piece_name='be0', color='black')
be1 = Pil((0,5), piece_type='one', piece_name='be1', color='black')

# Shah (King) and Farzin (Queen)
wS = Shah((7,3), piece_type='one', piece_name='wS0', color='white')
wF = Farzin((7,4), piece_type='one', piece_name='wF0', color='white')

bS = Shah((0,3), piece_type='one', piece_name='bS0', color='black')
bF = Farzin((0,4), piece_type='one', piece_name='bF0', color='black')

# Set the pieces on the board for the start of the match
board = Board([wp0, wp1, wp2, wp3,
                wp4, wp5, wp6, wp7,
                wr0, wr1, wa0, wa1,
                we0, we1, wS, wF], 
              [bp0, bp1, bp2, bp3,
                bp4, bp5, bp6, bp7,
                br0, br1, ba0, ba1,
                be0, be1, bS, bF])

# Print the board
board.print_board(board.name_obj_dict['wp0'],board.name_obj_dict['wp1'],
                  board.name_obj_dict['wp2'],board.name_obj_dict['wp3'],
                  board.name_obj_dict['wp4'],board.name_obj_dict['wp5'],
                  board.name_obj_dict['wp6'],board.name_obj_dict['wp7'],
                  board.name_obj_dict['wr0'],board.name_obj_dict['wr1'],
                  board.name_obj_dict['wa0'],board.name_obj_dict['wa1'],
                  board.name_obj_dict['we0'],board.name_obj_dict['we1'],
                  board.name_obj_dict['wS0'],board.name_obj_dict['wF0'],
                  board.name_obj_dict['bp0'],board.name_obj_dict['bp1'],
                  board.name_obj_dict['bp2'],board.name_obj_dict['bp3'],
                  board.name_obj_dict['bp4'],board.name_obj_dict['bp5'],
                  board.name_obj_dict['bp6'],board.name_obj_dict['bp7'],
                  board.name_obj_dict['br0'],board.name_obj_dict['br1'],
                  board.name_obj_dict['ba0'],board.name_obj_dict['ba1'],
                  board.name_obj_dict['be0'],board.name_obj_dict['be1'],
                  board.name_obj_dict['bS0'],board.name_obj_dict['bF0'])


# print(board.name_obj_dict['br0'].Available_Moves(board.y_dim, board.x_dim, 
#                           board.black_piece_loc, board.white_piece_loc))

# Make a move
piece_id = 'bp0'
old_loc = (1,0)
new_loc = (2,0)

# Step 1: Make the move
  # Update the position of the piece
# Step 2: Update the location of the pieces
  # Update the dictionaries within the board
# Step 3: Update The moves
  # Update all of the available moves for the pieces

board.name_obj_dict[piece_id].Make_Move(new_loc)
board.update_locs(board.name_obj_dict[piece_id].color,
                  old_loc,
                  new_loc)

print(board.name_obj_dict[piece_id].pos)


