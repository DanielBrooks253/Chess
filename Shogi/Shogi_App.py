import pygame as p

from Board import Board
from Pieces import OSho, GinSho, Kyosha, KeiMa, Fuhyo, KinSho, Hisha, Kaku

p.init()

WIDTH = HEIGHT = 522
DIMENSION = 9
MAX_FPS = 15
SQ_SIZE = HEIGHT//DIMENSION
PCT_SHRINK = .75

IMAGES = {} 

num_turns = 0
num = 1
game_over = False
text = ''
player_clicks = []

# Get all of the images loaded for the given pieces
for pieces in [('Pawn', 'Pawn'), ('Bishop', 'Bishop'), ('Gold_General', 'Gold_General'),
               ('King', 'King'), ('Lance', 'Lance'), ('Knight', 'Knight'),
               ('Silver_General', 'Silver_General'), ('Rook', 'Rook'), ('prom_pawn', 'Promoted_Pawn_Red'),
               ('prom_bishop', 'Promoted_Bishop_Red'), ('prom_knight', 'Promoted_Knight_Red'),
               ('prom_lance', 'Promoted_Lance_Red'), ('prom_rook', 'Promoted_Rook_Red'),
               ('prom_silver', 'Promoted_Silver_Red')]:
            IMAGES[pieces[0]] = p.transform.scale(p.image.load("Images/" + pieces[1] + ".jpg"), (int(SQ_SIZE*PCT_SHRINK), int(SQ_SIZE*PCT_SHRINK)))

# Pygame initializations
screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Shogi')

clock = p.time.Clock()
screen.fill(p.Color('white'))
running = True

# sq_selected = () # no sqaure that is selected (row, col)
player_Clicks = [] # keep track of the number of clicks the user does

# Initialize all of the pieces on the board
# Fuhyo (Pawns)
wfuhyo0 = Fuhyo((6,0), piece_name='wf0', piece_image = IMAGES['Pawn'], promoted_image = IMAGES['prom_pawn'], color='white', capture_name = 'fuhyo')
wfuhyo1 = Fuhyo((6,1), piece_name='wf1', piece_image = IMAGES['Pawn'], promoted_image = IMAGES['prom_pawn'], color='white', capture_name = 'fuhyo')
wfuhyo2 = Fuhyo((6,2), piece_name='wf2', piece_image = IMAGES['Pawn'], promoted_image = IMAGES['prom_pawn'], color='white', capture_name = 'fuhyo')
wfuhyo3 = Fuhyo((6,3), piece_name='wf3', piece_image = IMAGES['Pawn'], promoted_image = IMAGES['prom_pawn'], color='white', capture_name = 'fuhyo')
wfuhyo4 = Fuhyo((6,4), piece_name='wf4', piece_image = IMAGES['Pawn'], promoted_image = IMAGES['prom_pawn'], color='white', capture_name = 'fuhyo')
wfuhyo5 = Fuhyo((6,5), piece_name='wf5', piece_image = IMAGES['Pawn'], promoted_image = IMAGES['prom_pawn'], color='white', capture_name = 'fuhyo')
wfuhyo6 = Fuhyo((6,6), piece_name='wf6', piece_image = IMAGES['Pawn'], promoted_image = IMAGES['prom_pawn'], color='white', capture_name = 'fuhyo')
wfuhyo7 = Fuhyo((6,7), piece_name='wf7', piece_image = IMAGES['Pawn'], promoted_image = IMAGES['prom_pawn'], color='white', capture_name = 'fuhyo')
wfuhyo8 = Fuhyo((6,8), piece_name='wf8', piece_image = IMAGES['Pawn'], promoted_image = IMAGES['prom_pawn'], color='white', capture_name = 'fuhyo')

bfuhyo0 = Fuhyo((2,0), piece_name='bp0', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black', capture_name = 'fuhyo')
bfuhyo1 = Fuhyo((2,1), piece_name='bp1', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black', capture_name = 'fuhyo')
bfuhyo2 = Fuhyo((2,2), piece_name='bp2', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black', capture_name = 'fuhyo')
bfuhyo3 = Fuhyo((2,3), piece_name='bp3', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black', capture_name = 'fuhyo')
bfuhyo4 = Fuhyo((2,4), piece_name='bp4', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black', capture_name = 'fuhyo')
bfuhyo5 = Fuhyo((2,5), piece_name='bp5', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black', capture_name = 'fuhyo')
bfuhyo6 = Fuhyo((2,6), piece_name='bp6', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black', capture_name = 'fuhyo')
bfuhyo7 = Fuhyo((2,7), piece_name='bp7', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black', capture_name = 'fuhyo')
bfuhyo8 = Fuhyo((2,8), piece_name='bp8', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black', capture_name = 'fuhyo')

# Kyosha (Lances)
wkyosha0 = Kyosha((8,0), piece_name='wl0', piece_image = IMAGES['Lance'], promoted_image = IMAGES['prom_lance'], color='white', capture_name = 'kyosha')
wkyosha1 = Kyosha((8,8), piece_name='wl1', piece_image = IMAGES['Lance'], promoted_image = IMAGES['prom_lance'], color='white', capture_name = 'kyosha')

bkyosha0 = Kyosha((0,0), piece_name='bl0', piece_image = p.transform.rotate(IMAGES['Lance'], 180), promoted_image = p.transform.rotate(IMAGES['prom_lance'], 180), color='black', capture_name = 'kyosha')
bkyosha1 = Kyosha((0,8), piece_name='bl1', piece_image = p.transform.rotate(IMAGES['Lance'], 180), promoted_image = p.transform.rotate(IMAGES['prom_lance'], 180), color='black', capture_name = 'kyosha')

# Kei-Ma (Knights)
wkeima0 = KeiMa((8,1), piece_name='wk0', piece_image = IMAGES['Knight'], promoted_image = IMAGES['prom_knight'], color='white', capture_name = 'keima')
wkeima1 = KeiMa((8,7), piece_name='wk1', piece_image = IMAGES['Knight'], promoted_image = IMAGES['prom_knight'], color='white', capture_name = 'keima')

bkeima0 = KeiMa((0,1), piece_name='bk0', piece_image = p.transform.rotate(IMAGES['Knight'], 180), promoted_image = p.transform.rotate(IMAGES['prom_knight'], 180), color='black', capture_name = 'keima')
bkeima1 = KeiMa((0,7), piece_name='bk1', piece_image = p.transform.rotate(IMAGES['Knight'], 180), promoted_image = p.transform.rotate(IMAGES['prom_knight'], 180), color='black', capture_name = 'keima')

# Gin-Sho (Silver Generals)
wginsho0 = GinSho((8,2), piece_name='wg0', piece_image = IMAGES['Silver_General'], promoted_image = IMAGES['prom_silver'], color='white', capture_name = 'ginsho')
wginsho1 = GinSho((8,6), piece_name='wg1', piece_image = IMAGES['Silver_General'], promoted_image = IMAGES['prom_silver'], color='white', capture_name = 'ginsho')

bginsho0 = GinSho((0,2), piece_name='bg0', piece_image = p.transform.rotate(IMAGES['Silver_General'], 180), promoted_image = p.transform.rotate(IMAGES['prom_silver'], 180), color='black', capture_name = 'ginsho')
bginsho1 = GinSho((0,6), piece_name='bg1', piece_image = p.transform.rotate(IMAGES['Silver_General'], 180), promoted_image = p.transform.rotate(IMAGES['prom_silver'], 180), color='black', capture_name = 'ginsho')

# Kin-Sho (Gold Generals)
wkinsho0 = KinSho((8,3), piece_name='wks0', piece_image = IMAGES['Gold_General'], promoted_image = None, color='white', capture_name = 'kinsho')
wkinsho1 = KinSho((8,5), piece_name='wks1', piece_image = IMAGES['Gold_General'], promoted_image = None, color='white', capture_name = 'kinsho')

bkinsho0 = KinSho((0,3), piece_name='bks0', piece_image = p.transform.rotate(IMAGES['Gold_General'], 180), promoted_image = None, color='black', capture_name = 'kinsho')
bkinsho1 = KinSho((0,5), piece_name='bks1', piece_image = p.transform.rotate(IMAGES['Gold_General'], 180), promoted_image = None, color='black', capture_name = 'kinsho')

# Kaku (Bishop)
wkaku = Kaku((7,1), piece_name = 'wk', piece_image = IMAGES['Bishop'], promoted_image = IMAGES['prom_bishop'], color='white', capture_name = 'kaku')
bkaku = Kaku((1,1), piece_name = 'bk', piece_image = p.transform.rotate(IMAGES['Bishop'], 180), promoted_image = p.transform.rotate(IMAGES['prom_bishop'], 180), color='black', capture_name = 'kaku')

# Hisha (Rook)
whisha = Hisha((7,7), piece_name = 'wh', piece_image = IMAGES['Rook'], promoted_image = IMAGES['prom_rook'], color='white', capture_name = 'hisha')
bhisha = Hisha((1,7), piece_name = 'bh', piece_image = p.transform.rotate(IMAGES['Rook'], 180), promoted_image = p.transform.rotate(IMAGES['prom_rook'], 180), color='black', capture_name = 'hisha')

# O-Sho/Gyuk (King)
wosho = OSho((8,4), piece_name = 'wO', piece_image = IMAGES['King'], promoted_image = None, color='white', capture_name = 'osho')
bosho = OSho((0,4), piece_name = 'bO', piece_image = p.transform.rotate(IMAGES['King'], 180), promoted_image = None, color='black', capture_name = 'osho')

# Set the pieces on the board for the start of the match
board = Board([wfuhyo0, wfuhyo1, wfuhyo2, wfuhyo3,
                wfuhyo4, wfuhyo5, wfuhyo6, wfuhyo7, wfuhyo8,
                wkyosha0, wkyosha1, wkeima0, wkeima1, wginsho0, wginsho1,
                wkinsho0, wkinsho1, wkaku, whisha, wosho], 
              [bfuhyo0, bfuhyo1, bfuhyo2, bfuhyo3,
                bfuhyo4, bfuhyo5, bfuhyo6, bfuhyo7, bfuhyo8,
                bkyosha0, bkyosha1, bkeima0, bkeima1, bginsho0, bginsho1,
                bkinsho0, bkinsho1, bkaku, bhisha, bosho], HEIGHT, WIDTH, DIMENSION)

high_squares = None

while running:
    for e in p.event.get():
        if e.type == p.QUIT:
            running = False

        if e.type == p.MOUSEBUTTONDOWN:
          location = p.mouse.get_pos()

          row = location[0]//SQ_SIZE
          col = location[1]//SQ_SIZE     

          if not game_over:
            # First Click
            if len(player_clicks) == 0:
              # Check to make sure that is is a valid move (piece is on square)
              # Get available moves
              # Highlight moves
              if (col, row) not in board.loc_names.keys():
                break
              else:
                piece_name = board.loc_names[(col, row)]

                if board.name_obj_dict[piece_name].color == 'white' and  \
                      num_turns % 2 == 0:
                  moves = board.name_obj_dict[piece_name].Available_Moves(
                      board.x_dim,
                      board.y_dim,
                      board.white_piece_loc,
                      board.black_piece_loc
                  )
                elif board.name_obj_dict[piece_name].color == 'black' and  \
                    num_turns % 2 != 0:
                  moves = board.name_obj_dict[piece_name].Available_Moves(
                      board.x_dim,
                      board.y_dim,
                      board.black_piece_loc,
                      board.white_piece_loc)
                else:
                  # Do not highlight anything if the place they click 
                  # doesn't have any piece or a piece of their color 
                  break
              
              if moves is None:
                player_clicks.append((col, row))
                high_squares = ((col, row))
              else:
                invalid_moves = board.name_obj_dict[piece_name].avail_move_check_check(
                  moves, board)

                # Removes all the moves that will not get you out
                # of check
                valid_moves = moves - invalid_moves

                # If there are no valid moves, return none
                if len(valid_moves) == 0:
                  moves = None
                  player_clicks.append((row, col))
                else:
                  moves = valid_moves.copy()
                  player_clicks.append((col, row))

                high_squares = {(col, row)} | valid_moves

            # second click
            else:
              if (col, row) in player_clicks:
                # If the player selects the same square that was previouslly
                # selected, deselect the piece
                high_squares = None
                player_clicks = []
              else:
                # If the piece has no available moves,
                # ignore the click

                if moves is None:
                  break
                # If the second click is in the pieces available moves,
                # make the move and update everything
                elif (col, row) in moves:
                  board.name_obj_dict[piece_name].Make_Move(
                    (col, row),
                    board
                  )

                  high_squares = None
                  player_clicks = []

                  # Check to see if the move as resulted in the king being in 
                  # check or not
                  board.name_obj_dict['bO'].in_check = board.name_obj_dict['bO'].check_check(
                      board.white_name_obj_dict,
                      board.white_piece_loc,
                      board.black_piece_loc
                  )

                  board.name_obj_dict['wO'].in_check = board.name_obj_dict['wO'].check_check(
                      board.black_name_obj_dict,
                      board.black_piece_loc,
                      board.white_piece_loc
                  )

                  if num_turns % 2 == 0:
                      if board.game_over_check(
                          board.black_name_obj_dict,
                          num_turns
                      ) and bosho.in_check:

                          text = 'Checkmate!! White Wins'
                          game_over = True
                          break

                      elif board.game_over_check(
                          board.black_name_obj_dict,
                          num_turns
                      ) and not bosho.in_check:

                          text = 'Stalemate!! Draw Game'
                          game_over = True
                          break
                      else:
                          pass
                  else:
                      if board.game_over_check(
                          board.white_name_obj_dict,
                          num_turns
                      ) and wosho.in_check:

                          text = 'Checkmate!! Black Wins'
                          game_over = True
                          break

                      elif board.game_over_check(
                          board.white_name_obj_dict,
                          num_turns
                      ) and not wosho.in_check:

                          text = 'Stalemate!! Draw Game'
                          game_over = True
                          break
                      else:
                          pass

                  num_turns += 1

    board.drawGameState(screen, board.name_obj_dict, False, '', 0, high_squares, None)

    clock.tick(MAX_FPS)
    p.display.flip()