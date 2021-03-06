import pygame as p

from Board import Board
from Pieces import Tcha, Ma, Kuong, Syang, Pyeng, Sa, Hpo

p.init()

WIDTH = 640
HEIGHT = 704
X_DIM = 10
Y_DIM = 11
Y_BOARD_DIM = 9
X_BOARD_DIM = 8
MAX_FPS = 15
SQ_SIZE = 64
PCT_SHRINK = .75 # Images 48 x 48

IMAGES = {}

num_turns = 0
game_over = False
text = ''
num = 1

for pieces in [('wp', 'White_Solider'), ('wt', 'White_Chariot'), ('wm', 'White_Knight'), ('wK', 'White_King'),
               ('wS', 'White_Advisor'), ('ws', 'White_Elephant'), ('wh', 'White_Cannon'), ('bp', 'Black_Solider'), 
               ('bt', 'Black_Chariot'), ('bm', 'Black_Knight'), ('bK', 'Black_King'),
               ('bS', 'Black_Advisor'), ('bs', 'Black_Elephant'), ('bh', 'Black_Cannon')]:
   IMAGES[pieces[0]] = p.transform.scale(p.image.load("Images/" + pieces[1] + ".jpg"), (int(SQ_SIZE*PCT_SHRINK), int(SQ_SIZE*PCT_SHRINK))) 

screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Janggi')

clock = p.time.Clock()
screen.fill(p.Color('wheat1'))
running = True
player_clicks = []

wpyeng0 = Pyeng((6,0), location_y = (416,480), location_x = (32,96), piece_name = 'wp0', piece_image = IMAGES['wp'], color = 'white')
wpyeng1 = Pyeng((6,2), location_y = (416,480), location_x = (160,224), piece_name = 'wp1', piece_image = IMAGES['wp'], color = 'white')
wpyeng2 = Pyeng((6,4), location_y = (416,480), location_x = (288,352), piece_name = 'wp2', piece_image = IMAGES['wp'], color = 'white')
wpyeng3 = Pyeng((6,6), location_y = (416,480), location_x = (416,480), piece_name = 'wp3', piece_image = IMAGES['wp'], color = 'white')
wpyeng4 = Pyeng((6,8), location_y = (416,480), location_x = (544,608), piece_name = 'wp4', piece_image = IMAGES['wp'], color = 'white')

bpyeng0 = Pyeng((3,0), location_y = (224,288), location_x = (32,96), piece_name = 'bp0', piece_image = IMAGES['bp'], color = 'black')
bpyeng1 = Pyeng((3,2), location_y = (224,288), location_x = (160,224), piece_name = 'bp1', piece_image = IMAGES['bp'], color = 'black')
bpyeng2 = Pyeng((3,4), location_y = (224,288), location_x = (288,352), piece_name = 'bp2', piece_image = IMAGES['bp'], color = 'black')
bpyeng3 = Pyeng((3,6), location_y = (224,288), location_x = (416,480), piece_name = 'bp3', piece_image = IMAGES['bp'], color = 'black')
bpyeng4 = Pyeng((3,8), location_y = (224,288), location_x = (544,608), piece_name = 'bp4', piece_image = IMAGES['bp'], color = 'black')

whpo0 = Hpo((7,1), location_y = (480,544), location_x = (96,160), piece_name = 'wh0', piece_image = IMAGES['wh'], color = 'white')
whpo1 = Hpo((7,7), location_y = (480,544), location_x = (480,544), piece_name = 'wh1', piece_image = IMAGES['wh'], color = 'white')

bhpo0 = Hpo((2,1), location_y = (160,224), location_x = (96,160), piece_name = 'bh0', piece_image = IMAGES['bh'], color = 'black')
bhpo1 = Hpo((2,7), location_y = (160,224), location_x = (480,544), piece_name = 'bh1', piece_image = IMAGES['bh'], color = 'black')

wtcha0 = Tcha((9,0), location_y = (608,672), location_x = (32,96), piece_name = 'wt0', piece_image = IMAGES['wt'], color = 'white')
wtcha1 = Tcha((9,8), location_y = (608,672), location_x = (544,608), piece_name = 'wt1', piece_image = IMAGES['wt'], color = 'white')

btcha0 = Tcha((0,0), location_y = (32,96), location_x = (32,96), piece_name = 'bt0', piece_image = IMAGES['bt'], color = 'black')
btcha1 = Tcha((0,8), location_y = (32,96), location_x = (544,608), piece_name = 'bt1', piece_image = IMAGES['bt'], color = 'black')

wma0 = Ma((9,1), location_y = (608,672), location_x = (96,160), piece_name = 'wm0', piece_image = IMAGES['wm'], color = 'white')
wma1 = Ma((9,7), location_y = (608,672), location_x = (480,544), piece_name = 'wm1', piece_image = IMAGES['wm'], color = 'white')

bma0 = Ma((0,1), location_y = (32,96), location_x = (96,160), piece_name = 'bm0', piece_image = IMAGES['bm'], color = 'black')
bma1 = Ma((0,7), location_y = (32,96), location_x = (480,544), piece_name = 'bm1', piece_image = IMAGES['bm'], color = 'black')

wsyang0 = Syang((9,2), location_y = (608,672), location_x = (160,224), piece_name = 'ws0', piece_image = IMAGES['ws'], color = 'white')
wsyang1 = Syang((9,6), location_y = (608,672), location_x = (416,480), piece_name = 'ws1', piece_image = IMAGES['ws'], color = 'white')

bsyang0 = Syang((0,2), location_y = (32,96), location_x = (160,224), piece_name = 'bs0', piece_image = IMAGES['bs'], color = 'black')
bsyang1 = Syang((0,6), location_y = (32,96), location_x = (416,480), piece_name = 'bs1', piece_image = IMAGES['bs'], color = 'black')

wsa0 = Sa((9,3), location_y = (608,672), location_x = (224,288), piece_name = 'wS0', piece_image = IMAGES['wS'], color = "white")
wsa1 = Sa((9,5), location_y = (608,672), location_x = (352,416), piece_name = 'wS1', piece_image = IMAGES['wS'], color = "white")

bsa0 = Sa((0,3), location_y = (32,96), location_x = (224,288), piece_name = 'bS0', piece_image = IMAGES['bS'], color = "black")
bsa1 = Sa((0,5), location_y = (32,96), location_x = (352,416), piece_name = 'bS1', piece_image = IMAGES['bS'], color = "black")

wkuong = Kuong((8,4), location_y = (608,672), location_x = (288,352), piece_name = 'wK', piece_image = IMAGES['wK'], color = 'white')
bkuong = Kuong((1,4), location_y = (32,96), location_x = (288,352), piece_name = 'bK', piece_image = IMAGES['bK'], color = 'black')

board = Board([wpyeng0, wpyeng1, wpyeng2, wpyeng3, wpyeng4,
               wtcha0,wtcha1,wma0,wma1,wsyang0,wsyang1,
               wsa0,wsa1,wkuong,whpo0,whpo1],
               [bpyeng0, bpyeng1, bpyeng2, bpyeng3, bpyeng4,
               btcha0,btcha1,bma0,bma1,bsyang0,bsyang1,
               bsa0,bsa1,bkuong,bhpo0,bhpo1],
               HEIGHT,WIDTH,SQ_SIZE,Y_DIM,X_DIM)

high_squares = None
piece_name = None

start_flag_white = True
start_flag_black = True

start_flag_white_count = 0
start_flag_black_count = 0

while running:
    for e in p.event.get():
        if e.type == p.QUIT:
            running = False                

        if start_flag_white or start_flag_black:
            if num_turns % 2 == 0:
                if start_flag_white_count == 0:
                    high_squares = {wma0.pos, wsyang0.pos}
                else:
                    high_squares = {wma1.pos, wsyang1.pos}
            else:
                if start_flag_black_count == 0:
                    high_squares = {bma0.pos, bsyang0.pos}
                else:
                    high_squares = {bma1.pos, bsyang1.pos}

        if e.type == p.MOUSEBUTTONDOWN:
            location = p.mouse.get_pos()
            raw_row = location[0]
            raw_col = location[1]

            col, row = board.Convert_Pxl_To_Coord(raw_col, raw_row)
            cannon_locs = {whpo1.pos, whpo0.pos, bhpo1.pos, bhpo0.pos}

            if (start_flag_white or start_flag_black) and 235 <= raw_row <= 285 and 350 <= raw_col <= 380:
                if num_turns % 2 == 0:
                    if start_flag_white_count == 0:
                        start_flag_white_count += 1
                        wma0.pos, wsyang0.pos = wsyang0.pos, wma0.pos
                    else:
                        num_turns += 1
                        wma1.pos, wsyang1.pos = wsyang1.pos, wma1.pos
                        start_flag_white = False
                        high_squares = None
                else:
                    if start_flag_black_count == 0:
                        start_flag_black_count += 1
                        bma0.pos, bsyang0.pos = bsyang0.pos, bma0.pos
                    else:
                        num_turns += 1
                        bma1.pos, bsyang1.pos = bsyang1.pos, bma1.pos
                        start_flag_black = False
                        high_squares = None

            elif (start_flag_white or start_flag_black) and 365 <= raw_row <= 415 and 350 <= raw_col <= 380:
                if num_turns % 2 == 0:
                    if start_flag_white_count == 0:
                        start_flag_white_count += 1
                    else:
                        num_turns += 1
                        start_flag_white = False
                        high_squares = None
                else:
                    if start_flag_black_count == 0:
                        start_flag_black_count += 1
                    else:
                        num_turns += 1
                        start_flag_black = False
                        high_squares = None

            elif not(start_flag_white or start_flag_black):
                pass
            else:
                continue

            if len(player_clicks) == 0:
                if (col, row) not in board.loc_names.keys():
                    break
                else:
                    piece_name = board.loc_names[(col, row)]
                    
                    if board.name_obj_dict[piece_name].color == 'white' and \
                        num_turns % 2 == 0:
                        moves = board.name_obj_dict[piece_name].Available_Moves(
                            Y_BOARD_DIM,
                            X_BOARD_DIM,
                            board.white_piece_loc,
                            board.black_piece_loc,
                            cannon_locs
                        )
                    elif board.name_obj_dict[piece_name].color == 'black' and \
                        num_turns % 2 != 0:
                        moves = board.name_obj_dict[piece_name].Available_Moves(
                            Y_BOARD_DIM,
                            X_BOARD_DIM,
                            board.black_piece_loc,
                            board.white_piece_loc,
                            cannon_locs
                        )
                    else:
                        break
                
                if moves is None:
                    player_clicks.append((col, row))
                    high_squares = ((col, row))
                else:
                    invalid_moves = board.name_obj_dict[piece_name].avail_move_check_check(
                            moves, board, cannon_locs
                        )

                    if piece_name[1] == 'h':
                        rm_cannon = moves - cannon_locs
                        valid_moves = rm_cannon - invalid_moves
                    else:
                        valid_moves = moves - invalid_moves

                    if len(valid_moves) == 0:
                        moves = None
                        player_clicks.append((col, row))
                    else:
                        moves = valid_moves.copy()
                        player_clicks.append((col, row))
                    
                    high_squares = {(col, row)} | valid_moves

            else:
                if (col, row) in player_clicks:
                    player_clicks = []
                    high_squares = None
                else:
                    if moves is None:
                        break
                    elif (col, row) in moves:
                        board.name_obj_dict[piece_name].Make_Move(
                            (col, row),
                            board
                        )

                        player_clicks = []
                        high_squares = None

                        board.name_obj_dict['bK'].in_check = board.name_obj_dict['bK'].check_check(
                                board.white_name_obj_dict,
                                board.white_piece_loc,
                                board.black_piece_loc, 
                                cannon_locs
                            )

                        board.name_obj_dict['wK'].in_check = board.name_obj_dict['wK'].check_check(
                            board.black_name_obj_dict,
                            board.black_piece_loc,
                            board.white_piece_loc,
                            cannon_locs
                        )

                        # Check to see if placing the piece cause checkmate or not
                        if board.game_over_check(
                        board.black_name_obj_dict,
                        num_turns, cannon_locs

                        ) and bkuong.in_check:

                            text = 'Checkmate!! White Wins'
                            game_over = True
                            break

                        elif (board.game_over_check(
                            board.black_name_obj_dict,
                            num_turns, cannon_locs
                        ) or  board.game_over_check(
                            board.white_name_obj_dict,
                            num_turns, cannon_locs)) and (not bkuong.in_check or not wkuong.in_check):

                            text = 'Stalemate!! Draw Game'
                            game_over = True
                            break

                        elif board.game_over_check(
                            board.white_name_obj_dict,
                            num_turns, cannon_locs
                        ) and wkuong.in_check:
                            text = 'Checkmate!! Black Wins'
                            game_over = True
                            break
                        else:
                            pass
                        
                        num_turns += 1




    if board.name_obj_dict['wK'].in_check:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares, 
                                board.name_obj_dict['wK'].pos, board.loc_names.keys())
        clock.tick(MAX_FPS)
        p.display.flip()

    elif board.name_obj_dict['bK'].in_check:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares,
                                board.name_obj_dict['bK'].pos, board.loc_names.keys())
        clock.tick(MAX_FPS)
        p.display.flip()

    else:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares, 
                            None, board.loc_names.keys(), start_flag_white,
                            start_flag_black)

        clock.tick(MAX_FPS)
        p.display.flip()

    
