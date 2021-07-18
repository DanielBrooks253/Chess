## \/\/ Pregame Loading \/\/
from Board import Board
from Pieces import Shah, Pil, Rukh, Asp, Pujada, Farzin

num_turns = 0
checkmate = False

# Initialize all of the pieces on the board
wp0 = Pujada((6,0), piece_name='wp0', piece_image = None, color='white')
wp1 = Pujada((6,1), piece_name='wp1', piece_image = None, color='white')
wp2 = Pujada((6,2), piece_name='wp2', piece_image = None, color='white')
wp3 = Pujada((6,3), piece_name='wp3', piece_image = None, color='white')
wp4 = Pujada((6,4), piece_name='wp4', piece_image = None, color='white')
wp5 = Pujada((6,5), piece_name='wp5', piece_image = None, color='white')
wp6 = Pujada((6,6), piece_name='wp6', piece_image = None, color='white')
wp7 = Pujada((6,7), piece_name='wp7', piece_image = None, color='white')

bp0 = Pujada((1,0), piece_name='bp0', piece_image = None, color='black')
bp1 = Pujada((1,1), piece_name='bp1', piece_image = None, color='black')
bp2 = Pujada((1,2), piece_name='bp2', piece_image = None, color='black')
bp3 = Pujada((1,3), piece_name='bp3', piece_image = None, color='black')
bp4 = Pujada((1,4), piece_name='bp4', piece_image = None, color='black')
bp5 = Pujada((1,5), piece_name='bp5', piece_image = None, color='black')
bp6 = Pujada((1,6), piece_name='bp6', piece_image = None, color='black')
bp7 = Pujada((1,7), piece_name='bp7', piece_image = None, color='black')

# Rukh (Rooks)
wr0 = Rukh((7,0), piece_name='wr0', piece_image = None, color='white')
wr1 = Rukh((7,7), piece_name='wr1', piece_image = None, color='white')

br0 = Rukh((0,0), piece_name='br0', piece_image = None, color='black')
br1 = Rukh((0,7), piece_name='br1', piece_image = None, color='black')

# Asp (Horses)
wa0 = Asp((7,1), piece_name='wa0', piece_image = None, color='white')
wa1 = Asp((7,6), piece_name='wa1', piece_image = None, color='white')

ba0 = Asp((0,1), piece_name='ba0', piece_image = None, color='black')
ba1 = Asp((0,6), piece_name='ba1', piece_image = None, color='black')

# Pil (Elephants)
we0 = Pil((7,2), piece_name='we0', piece_image = None, color='white')
we1 = Pil((7,5), piece_name='we1', piece_image = None, color='white')

be0 = Pil((0,2), piece_name='be0', piece_image = None, color='black')
be1 = Pil((0,5), piece_name='be1', piece_image = None, color='black')

# Shah (King) and Farzin (Queen)
wS = Shah((7,3), piece_name='wS0', piece_image = None, color='white')
wF = Farzin((7,4), piece_name='wF0', piece_image = None, color='white')

bS = Shah((0,3), piece_name='bS0', piece_image = None, color='black')
bF = Farzin((0,4), piece_name='bF0', piece_image = None, color='black')

# Set the pieces on the board for the start of the match
board = Board([wp0, wp1, wp2, wp3,
                wp4, wp5, wp6, wp7,
                wr0, wr1, wa0, wa1,
                we0, we1, wS, wF], 
              [bp0, bp1, bp2, bp3,
                bp4, bp5, bp6, bp7,
                br0, br1, ba0, ba1,
                be0, be1, bS, bF], 512, 8)


# Print the board
board.print_board(board.name_obj_dict)

## /\/\ Pregame Loading /\/\

#=====================================================================#
#=====================================================================#

## \/\/ Game Play \/\/

while not checkmate:
  turn = 'white' if num_turns % 2 == 0 else 'black'
  legal_move = False

  name = input("What piece should I move? ")

  # ---- White Pieces ----
  if turn == 'white':
    moves = board.name_obj_dict[name].Available_Moves(
                      board.x_dim,
                      board.y_dim,
                      board.white_piece_loc,
                      board.black_piece_loc
    )
  
    if board.name_obj_dict['wS0'].in_check:
      print(board.name_obj_dict[name].avail_move_check_check(
        moves, board
      ))

    while not legal_move:
      if board.name_obj_dict['wS0'].in_check:
        invalid_moves = board.name_obj_dict[name].avail_move_check_check(
                             moves, board)
        valid_moves = moves - invalid_moves

        if len(valid_moves) == 0: 
          break
        else:
          moves = valid_moves.copy()

      print(moves)

      new_loc_str = input('Where should I move the piece to? ')
      new_loc = (int(new_loc_str[1]), int(new_loc_str[3]))

      if new_loc not in moves:
        continue
      else:
        legale_move = True

        board.name_obj_dict[name].Make_Move(new_loc, board)
        board.print_board(board.name_obj_dict)

        board.name_obj_dict['bS0'].in_check = board.name_obj_dict['bS0'].check_check(
                                            board.white_name_obj_dict, # color for available moves
                                            board.white_piece_loc,
                                            board.black_piece_loc)
        num_turns+=1
        break
  else:
    # ---- Black Pieces ----
    moves = board.name_obj_dict[name].Available_Moves(
                      board.x_dim,
                      board.y_dim,
                      board.black_piece_loc,
                      board.white_piece_loc
    )

    while not legal_move:
      if board.name_obj_dict['bS0'].in_check:
        invalid_moves = board.name_obj_dict[name].avail_move_check_check(
                             moves, board)
        valid_moves = moves - invalid_moves

        if len(valid_moves) == 0: 
          break
        else:
          moves = valid_moves.copy()
          
      print(moves)

      new_loc_str = input('Where should I move the piece to? ')
      new_loc = (int(new_loc_str[1]), int(new_loc_str[3]))

      if new_loc not in moves:
        continue
      else:
        legale_move = True

        board.name_obj_dict[name].Make_Move(new_loc, board)
        board.print_board(board.name_obj_dict)

        board.name_obj_dict['wS0'].in_check = board.name_obj_dict['wS0'].check_check(
                                              board.black_name_obj_dict, # color for available moves
                                              board.black_piece_loc,
                                              board.white_piece_loc)
        num_turns+=1
        break

## /\/\ Game Play /\/\
