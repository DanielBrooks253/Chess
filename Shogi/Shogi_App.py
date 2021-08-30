import pygame as p

from Board import Board
from Pieces import OSho, GinSho, Kyosha, KeiMa, Fuhyo, KinSho, Hisha, Kaku

p.init()

WIDTH = 586 # 3 pixels available on each side (6 in total)
HEIGHT = 522
DIMENSION = 9
MAX_FPS = 15
SQ_SIZE = HEIGHT//DIMENSION # 58 pixels 
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

bfuhyo0 = Fuhyo((2,0), piece_name='bf0', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black', capture_name = 'fuhyo')
bfuhyo1 = Fuhyo((2,1), piece_name='bf1', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black', capture_name = 'fuhyo')
bfuhyo2 = Fuhyo((2,2), piece_name='bf2', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black', capture_name = 'fuhyo')
bfuhyo3 = Fuhyo((2,3), piece_name='bf3', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black', capture_name = 'fuhyo')
bfuhyo4 = Fuhyo((2,4), piece_name='bf4', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black', capture_name = 'fuhyo')
bfuhyo5 = Fuhyo((2,5), piece_name='bf5', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black', capture_name = 'fuhyo')
bfuhyo6 = Fuhyo((2,6), piece_name='bf6', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black', capture_name = 'fuhyo')
bfuhyo7 = Fuhyo((2,7), piece_name='bf7', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black', capture_name = 'fuhyo')
bfuhyo8 = Fuhyo((2,8), piece_name='bf8', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black', capture_name = 'fuhyo')

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
wkaku = Kaku((7,1), piece_name = 'wka', piece_image = IMAGES['Bishop'], promoted_image = IMAGES['prom_bishop'], color='white', capture_name = 'kaku')
bkaku = Kaku((1,7), piece_name = 'bka', piece_image = p.transform.rotate(IMAGES['Bishop'], 180), promoted_image = p.transform.rotate(IMAGES['prom_bishop'], 180), color='black', capture_name = 'kaku')

# Hisha (Rook)
whisha = Hisha((7,7), piece_name = 'wh', piece_image = IMAGES['Rook'], promoted_image = IMAGES['prom_rook'], color='white', capture_name = 'hisha')
bhisha = Hisha((1,1), piece_name = 'bh', piece_image = p.transform.rotate(IMAGES['Rook'], 180), promoted_image = p.transform.rotate(IMAGES['prom_rook'], 180), color='black', capture_name = 'hisha')

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
                bkinsho0, bkinsho1, bkaku, bhisha, bosho], 
                HEIGHT, WIDTH, DIMENSION, IMAGES)

high_squares = None
# Highlighted squares that show where the captured pieces could be placed
# on the board.
capture_high_squares = None
piece_name_numbers = {'fuhyo': ['f', list(range(9, 100))],
                      'kyosha': ['l', list(range(2, 50))],
                      'ginsho': ['g', list(range(2, 50))],
                      'kingsho': ['ks', list(range(2, 50))],
                      'keima': ['k', list(range(2, 50))],
                      'kaku': ['ka', list(range(20))],
                      'hisha': ['h', list(range(20))]}
black_promotion = False
white_promotion = False

while running:
  for e in p.event.get():
    if e.type == p.QUIT:
        running = False

    if e.type == p.MOUSEBUTTONDOWN:
      location = p.mouse.get_pos()

      row = location[0]//SQ_SIZE
      col = location[1]//SQ_SIZE     

      raw_row = location[0]
      raw_col = location[1]

      if not game_over:
        # First Click
        if len(player_clicks) == 0:
          # Check to make sure that is is a valid move (piece is on square)
          # Get available moves
          # Highlight moves
          if row == 9 and col < 7: # Click on the side bar
            moves = None

            # Highlight the sqaures of the captured piece that is selected
            # If the king in in check, show only the squares that would result
            # in not being in check.
            if num_turns % 2 == 0:
              captured_item_selected = list(board.white_capture_counts_dict.keys())[col]
              if board.white_capture_counts_dict[captured_item_selected][0] == 0:
                capture_high_squares = None
              else:
                if board.name_obj_dict['wO'].in_check:
                  avail_places = board.Placement_Check_Check(num_turns)
                  all_high_squares = board.capture_name_obj_dict[captured_item_selected] \
                                  .Place_Pieces(board.name_obj_dict, board.y_dim, num_turns)
                  legal_places = avail_places & all_high_squares

                  if len(legal_places) == 0:
                    capture_high_squares = None
                  else:
                    capture_high_squares = legal_places
                else:
                  capture_high_squares = board.capture_name_obj_dict[captured_item_selected] \
                                  .Place_Pieces(board.name_obj_dict, board.y_dim, num_turns)
            else:
              captured_item_selected = list(board.black_capture_counts_dict.keys())[col]
              if board.black_capture_counts_dict[captured_item_selected][0] == 0:
                captured_item_selected = None
              else:
                if board.name_obj_dict['bO'].in_check:
                  avail_places = board.Placement_Check_Check(num_turns)
                  all_high_squares = board.capture_name_obj_dict[captured_item_selected] \
                                  .Place_Pieces(board.name_obj_dict, board.y_dim, num_turns)
                  legal_places = avail_places & all_high_squares

                  if len(legal_places) == 0:
                    capture_high_squares = None
                  else:
                    capture_high_squares = legal_places
                else:
                  capture_high_squares = board.capture_name_obj_dict[captured_item_selected] \
                                  .Place_Pieces(board.name_obj_dict, board.y_dim, num_turns)

          elif (col, row) not in board.loc_names.keys():
            break
          else:
            piece_name = board.loc_names[(col, row)]

            # If you start off in the promotion zone, increase the promotion
            # counter. You can promote as long as you start/end in the promotion
            # zone.
            if num_turns % 2 == 0 and col <= 2 and not board.name_obj_dict[piece_name].promoted and \
              board.name_obj_dict[piece_name].color == 'white':
              board.name_obj_dict[piece_name].promotion_count += 1
              high_squares = board.name_obj_dict[piece_name].pos

            elif num_turns % 2 != 0 and col >= 6 and not board.name_obj_dict[piece_name].promoted and \
              board.name_obj_dict[piece_name].color == 'black': 
              board.name_obj_dict[piece_name].promotion_count += 1
            else:
              pass

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
            if capture_high_squares is not None:
              player_clicks.append((col, row))
              high_squares = capture_high_squares | {(col, row)}
            else:
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
              player_clicks.append((col, row))
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
            capture_high_squares = None
            player_clicks = []
          else:
            # If the piece has no available moves,
            # ignore the click
            if moves is None:
              if capture_high_squares is not None:
                if (col, row) in capture_high_squares:
                  if num_turns % 2 == 0:
                    # Create the new piece name for the placed piece
                    new_name = 'w' + \
                               piece_name_numbers[captured_item_selected][0] + \
                               str(piece_name_numbers[captured_item_selected][1][0])

                    # Choose the proper object depending pn which piece is selected
                    temp = {'fuhyo': Fuhyo((col, row), piece_name = new_name, piece_image = IMAGES['Pawn'], promoted_image = IMAGES['prom_pawn'], color='white', capture_name = 'fuhyo'),
                            'keima': KeiMa((col, row), piece_name = new_name, piece_image = IMAGES['Knight'], promoted_image = IMAGES['prom_knight'], color='white', capture_name = 'keima'),
                            'ginsho': GinSho((col, row), piece_name = new_name, piece_image = IMAGES['Silver_General'], promoted_image = IMAGES['prom_silver'], color='white', capture_name = 'ginsho'),
                            'kinsho': KinSho((col, row), piece_name = new_name, piece_image = IMAGES['Gold_General'], promoted_image = None, color='white', capture_name = 'kinsho'),
                            'kaku': Kaku((col, row), piece_name = new_name, piece_image = IMAGES['Bishop'], promoted_image = IMAGES['prom_bishop'], color='white', capture_name = 'kaku'),
                            'hisha': Hisha((col, row), piece_name = new_name, piece_image = IMAGES['Rook'], promoted_image = IMAGES['prom_rook'], color='white', capture_name = 'hisha'),
                            'kyosha': Kyosha((col, row), piece_name = new_name, piece_image = IMAGES['Lance'], promoted_image = IMAGES['prom_lance'], color='white', capture_name = 'kyosha')}

                    # Update all of the white dictionaries on the board
                    board.white_piece_loc |= {(col, row)}
                    board.white_name_obj_dict[temp[captured_item_selected].piece_name] = temp[captured_item_selected]
                    board.white_capture_counts_dict[captured_item_selected][0] -= 1

                    # Check to see if the resulting placement ends up in check
                    # For the opposing side
                    board.name_obj_dict['bO'].in_check = board.name_obj_dict['bO'].check_check(
                                          board.white_name_obj_dict,
                                          board.white_piece_loc,
                                          board.black_piece_loc,
                                          board.y_dim,
                                          board.x_dim
                                      )

                  else:
                    new_name = 'b' + \
                               piece_name_numbers[captured_item_selected][0] + \
                               str(piece_name_numbers[captured_item_selected][1][0])

                    temp = {'fuhyo': Fuhyo((col, row), piece_name = new_name, piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black', capture_name = 'fuhyo'),
                            'keima': KeiMa((col, row), piece_name = new_name, piece_image = p.transform.rotate(IMAGES['Knight'], 180), promoted_image = p.transform.rotate(IMAGES['prom_knight'], 180), color='black', capture_name = 'keima'),
                            'ginsho': GinSho((col, row), piece_name = new_name, piece_image = p.transform.rotate(IMAGES['Silver_General'], 180), promoted_image = p.transform.rotate(IMAGES['prom_silver'], 180), color='black', capture_name = 'ginsho'),
                            'kinsho': KinSho((col, row), piece_name = new_name, piece_image = p.transform.rotate(IMAGES['Gold_General'], 180), promoted_image = None, color='black', capture_name = 'kinsho'),
                            'kaku': Kaku((col, row), piece_name = new_name, piece_image = p.transform.rotate(IMAGES['Bishop'], 180), promoted_image = p.transform.rotate(IMAGES['prom_bishop'], 180), color='black', capture_name = 'kaku'),
                            'hisha': Hisha((col, row), piece_name = new_name, piece_image = p.transform.rotate(IMAGES['Rook'], 180), promoted_image = p.transform.rotate(IMAGES['prom_rook'], 180), color='black', capture_name = 'hisha'),
                            'kyosha': Kyosha((col, row), piece_name = new_name, piece_image = p.transform.rotate(IMAGES['Lance'], 180), promoted_image = p.transform.rotate(IMAGES['prom_lance'], 180), color='black', capture_name = 'kyosha')}
 
                    # Update all the black dictuinaries on the board
                    board.black_piece_loc |= {(col, row)}
                    board.black_name_obj_dict[temp[captured_item_selected].piece_name] = temp[captured_item_selected]
                    board.black_capture_counts_dict[captured_item_selected][0] -= 1

                    # Check to see if the resulting placement ends up in check
                    # For the opposing side
                    board.name_obj_dict['wO'].in_check = board.name_obj_dict['wO'].check_check(
                                          board.black_name_obj_dict,
                                          board.black_piece_loc,
                                          board.white_piece_loc,
                                          board.y_dim,
                                          board.x_dim
                                      )

                  # Update all the general dictionaries on the board
                  board.loc_names[(col, row)] = new_name
                  board.name_obj_dict[new_name] = temp[captured_item_selected]
            
                  # End of the turn clean up
                  high_squares = None
                  capture_high_squares = None
                  
                  player_clicks = []

                  # Delete the used number, that is being used for the name
                  # of the pieces.
                  piece_name_numbers[captured_item_selected][1].pop(0)
                  num_turns += 1 
                  break

                else:
                  break
              else:
                break
            # If the second click is in the pieces available moves,
            # make the move and update everything
            elif (col, row) in moves or white_promotion or black_promotion:
              if white_promotion:
                if 150 <= raw_row <= 200 and 350 <= raw_col <= 380:
                  board.name_obj_dict[piece_name].promoted = True
                  board.name_obj_dict[piece_name].promotion_count = 0
                  white_promotion = False
                elif 275 <= raw_row <= 325 and 350 <= raw_col <= 380:
                  white_promotion = False
                else:
                  pass
              elif black_promotion:
                if 150 <= raw_row <= 200 and 90 <= raw_col <= 120:
                  board.name_obj_dict[piece_name].promoted = True
                  board.name_obj_dict[piece_name].promotion_count = 0
                  black_promotion = False
                elif 275 <= raw_row <= 325 and 90 <= raw_col <= 120:
                  black_promotion = False
                else:
                  pass
              else:
                board.name_obj_dict[piece_name].Make_Move(
                  (col, row),
                  board
                )

                if board.name_obj_dict[piece_name].promotion_count > 0 and num_turns % 2 == 0:
                  white_promotion = True
                  board.name_obj_dict[piece_name].promotion_count = 0
                elif board.name_obj_dict[piece_name].promotion_count > 0 and num_turns % 2 != 0:
                  black_promotion = True
                  board.name_obj_dict[piece_name].promotion_count = 0
                else:
                  pass

              # Check to see if a pawn, knight or lance are at the end of the board.
              # If they are, then they must promote.
              # Checks to see if a piece is able to promote by being in the promotion
              # zone at the start or end of their turn
              if num_turns % 2 == 0 and col == 0 and board.name_obj_dict[piece_name].capture_name in ['fuhyo', 'kyosha']: 
                board.name_obj_dict[piece_name].promoted = True
                high_squares = None
                player_clicks = []
              elif num_turns % 2 == 0 and board.name_obj_dict[piece_name].capture_name == 'keima' and col <= 1:
                board.name_obj_dict[piece_name].promoted = True
                high_squares = None
                player_clicks = []
              elif num_turns % 2 != 0 and col == 8 and board.name_obj_dict[piece_name].capture_name in ['fuhyo', 'kyosha']:
                board.name_obj_dict[piece_name].promoted = True
                high_squares = None
                player_clicks = []
              elif num_turns % 2 != 0 and col <= 7 and board.name_obj_dict[piece_name].capture_name == 'keima':
                board.name_obj_dict[piece_name].promoted = True
                high_squares = None
                player_clicks = []

              elif num_turns % 2 == 0 and col <= 2 and not board.name_obj_dict[piece_name].promoted and \
              board.name_obj_dict[piece_name].color == 'white':
                board.name_obj_dict[piece_name].promotion_count += 1
                white_promotion = True
                high_squares = board.name_obj_dict[piece_name].pos

              elif num_turns % 2 != 0 and col >= 6 and not board.name_obj_dict[piece_name].promoted and \
              board.name_obj_dict[piece_name].color == 'black':
                board.name_obj_dict[piece_name].promotion_count += 1
                black_promotion = True
                high_squares = board.name_obj_dict[piece_name].pos
              else:
                pass

              # Check to see if the move as resulted in the king being in 
              # check or not

              board.name_obj_dict['bO'].in_check = board.name_obj_dict['bO'].check_check(
                  board.white_name_obj_dict,
                  board.white_piece_loc,
                  board.black_piece_loc,
                  board.y_dim,
                  board.x_dim
              )

              board.name_obj_dict['wO'].in_check = board.name_obj_dict['wO'].check_check(
                  board.black_name_obj_dict,
                  board.black_piece_loc,
                  board.white_piece_loc,
                  board.y_dim,
                  board.x_dim
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

              if white_promotion or black_promotion:
                continue
              else:
                high_squares = None
                player_clicks = []
                num_turns += 1

            else:
              break

  if board.name_obj_dict['wO'].in_check:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares,
                                board.name_obj_dict['wO'].pos, num_turns, black_promotion, white_promotion)
        clock.tick(MAX_FPS)
        p.display.flip()

  elif board.name_obj_dict['bO'].in_check:
      board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares,
                              board.name_obj_dict['bO'].pos, num_turns, black_promotion, white_promotion)
      clock.tick(MAX_FPS)
      p.display.flip()

  else:
      board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares, None, num_turns, black_promotion, white_promotion)
      clock.tick(MAX_FPS)
      p.display.flip()