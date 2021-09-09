import pygame as p

from Board import Board
from Pieces import Chuh, Ma, Jiang, Shi, Shiang, Pao, Tsuh

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

for pieces in [('wt', 'White-Solider'), ('wc', 'White-Chariot'), ('wm', 'White-Horse'), ('wJ', 'White-King'),
               ('wS', 'White-Advisor'), ('ws', 'White-Elephant'), ('wp', 'White-Cannon'), ('bt', 'Black-Solider'), 
               ('bc', 'Black-Chariot'), ('bm', 'Black-Horse'), ('bJ', 'Black-King'),
               ('bS', 'Black-Advisor'), ('bs', 'Black-Elephant'), ('bp', 'Black-Cannon')]:
   IMAGES[pieces[0]] = p.transform.scale(p.image.load("Images/" + pieces[1] + ".jpg"), (int(SQ_SIZE*PCT_SHRINK), int(SQ_SIZE*PCT_SHRINK))) 

screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Xiangqi')

clock = p.time.Clock()
screen.fill(p.Color('wheat1'))
running = True
player_clicks = []

wtsuh0 = Tsuh((6,0), location_y = (416,480), location_x = (32,96), piece_name = 'wt0', piece_image = IMAGES['wt'], color = 'white')
wtsuh1 = Tsuh((6,2), location_y = (416,480), location_x = (160,224), piece_name = 'wt1', piece_image = IMAGES['wt'], color = 'white')
wtsuh2 = Tsuh((6,4), location_y = (416,480), location_x = (288,352), piece_name = 'wt2', piece_image = IMAGES['wt'], color = 'white')
wtsuh3 = Tsuh((6,6), location_y = (416,480), location_x = (416,480), piece_name = 'wt3', piece_image = IMAGES['wt'], color = 'white')
wtsuh4 = Tsuh((6,8), location_y = (416,480), location_x = (544,608), piece_name = 'wt4', piece_image = IMAGES['wt'], color = 'white')

btsuh0 = Tsuh((3,0), location_y = (224,288), location_x = (32,96), piece_name = 'bt0', piece_image = IMAGES['bt'], color = 'black')
btsuh1 = Tsuh((3,2), location_y = (224,288), location_x = (160,224), piece_name = 'bt1', piece_image = IMAGES['bt'], color = 'black')
btsuh2 = Tsuh((3,4), location_y = (224,288), location_x = (288,352), piece_name = 'bt2', piece_image = IMAGES['bt'], color = 'black')
btsuh3 = Tsuh((3,6), location_y = (224,288), location_x = (416,480), piece_name = 'bt3', piece_image = IMAGES['bt'], color = 'black')
btsuh4 = Tsuh((3,8), location_y = (224,288), location_x = (544,608), piece_name = 'bt4', piece_image = IMAGES['bt'], color = 'black')

wpao0 = Pao((7,1), location_y = (480,544), location_x = (96,160), piece_name = 'wp0', piece_image = IMAGES['wp'], color = 'white')
wpao1 = Pao((7,7), location_y = (480,544), location_x = (480,544), piece_name = 'wp1', piece_image = IMAGES['wp'], color = 'white')

bpao0 = Pao((2,1), location_y = (160,224), location_x = (96,160), piece_name = 'bp0', piece_image = IMAGES['bp'], color = 'black')
bpao1 = Pao((2,7), location_y = (160,224), location_x = (480,544), piece_name = 'bp1', piece_image = IMAGES['bp'], color = 'black')

wchuh0 = Chuh((9,0), location_y = (608,672), location_x = (32,96), piece_name = 'wc0', piece_image = IMAGES['wc'], color = 'white')
wchuh1 = Chuh((9,8), location_y = (608,672), location_x = (544,608), piece_name = 'wc1', piece_image = IMAGES['wc'], color = 'white')

bchuh0 = Chuh((0,0), location_y = (32,96), location_x = (32,96), piece_name = 'bc0', piece_image = IMAGES['bc'], color = 'black')
bchuh1 = Chuh((0,8), location_y = (32,96), location_x = (544,608), piece_name = 'bc1', piece_image = IMAGES['bc'], color = 'black')

wma0 = Ma((9,1), location_y = (608,672), location_x = (96,160), piece_name = 'wm0', piece_image = IMAGES['wm'], color = 'white')
wma1 = Ma((9,7), location_y = (608,672), location_x = (480,544), piece_name = 'wm1', piece_image = IMAGES['wm'], color = 'white')

bma0 = Ma((0,1), location_y = (32,96), location_x = (96,160), piece_name = 'bm0', piece_image = IMAGES['bm'], color = 'black')
bma1 = Ma((0,7), location_y = (32,96), location_x = (480,544), piece_name = 'bm1', piece_image = IMAGES['bm'], color = 'black')

wshiang0 = Shiang((9,2), location_y = (608,672), location_x = (160,224), piece_name = 'ws0', piece_image = IMAGES['ws'], color = 'white')
wshiang1 = Shiang((9,6), location_y = (608,672), location_x = (416,480), piece_name = 'ws1', piece_image = IMAGES['ws'], color = 'white')

bshiang0 = Shiang((0,2), location_y = (32,96), location_x = (160,224), piece_name = 'bs0', piece_image = IMAGES['bs'], color = 'black')
bshiang1 = Shiang((0,6), location_y = (32,96), location_x = (416,480), piece_name = 'bs1', piece_image = IMAGES['bs'], color = 'black')

wshi0 = Shi((9,3), location_y = (608,672), location_x = (224,288), piece_name = 'wS0', piece_image = IMAGES['wS'], color = "white")
wshi1 = Shi((9,5), location_y = (608,672), location_x = (352,416), piece_name = 'wS1', piece_image = IMAGES['wS'], color = "white")

bshi0 = Shi((0,3), location_y = (32,96), location_x = (224,288), piece_name = 'bS0', piece_image = IMAGES['bS'], color = "black")
bshi1 = Shi((0,5), location_y = (32,96), location_x = (352,416), piece_name = 'bS1', piece_image = IMAGES['bS'], color = "black")

wjiang = Jiang((9,4), location_y = (608,672), location_x = (288,352), piece_name = 'wJ', piece_image = IMAGES['wJ'], color = 'white')
bjiang = Jiang((0,4), location_y = (32,96), location_x = (288,352), piece_name = 'bJ', piece_image = IMAGES['bJ'], color = 'black')

board = Board([wtsuh0, wtsuh1, wtsuh2, wtsuh3, wtsuh4,
               wchuh0,wchuh1,wma0,wma1,wshiang0,wshiang1,
               wshi0,wshi1,wjiang,wpao0,wpao1],
               [btsuh0, btsuh1, btsuh2, btsuh3, btsuh4,
               bchuh0,bchuh1,bma0,bma1,bshiang0,bshiang1,
               bshi0,bshi1,bjiang,bpao0,bpao1],
               HEIGHT,WIDTH,SQ_SIZE,Y_DIM,X_DIM)

high_squares = None
piece_name = None

while running:
    for e in p.event.get():
        if e.type == p.QUIT:
            running = False                
                    
        if e.type == p.MOUSEBUTTONDOWN:
            location = p.mouse.get_pos()
            raw_row = location[0]
            raw_col = location[1]

            col, row = board.Convert_Pxl_To_Coord(raw_col, raw_row)

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
                            board.black_piece_loc
                        )
                    elif board.name_obj_dict[piece_name].color == 'black' and \
                        num_turns % 2 != 0:
                        moves = board.name_obj_dict[piece_name].Available_Moves(
                            Y_BOARD_DIM,
                            X_BOARD_DIM,
                            board.black_piece_loc,
                            board.white_piece_loc
                        )
                    else:
                        break
                
                if moves is None:
                    player_clicks.append((col, row))
                    high_squares = ((col, row))
                else:
                    invalid_moves = board.name_obj_dict[piece_name].avail_move_check_check(
                            moves, board
                        )

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

                        if piece_name[1] == 't':
                            if (num_turns % 2 == 0 and col == 4) or (num_turns % 2 != 0 and col == 5):
                                board.name_obj_dict[piece_name].Promote_Pawn()
                            else:
                                pass
                        else:
                            pass

                        player_clicks = []
                        high_squares = None

                        board.name_obj_dict['bJ'].in_check = board.name_obj_dict['bJ'].check_check(
                                board.white_name_obj_dict,
                                board.white_piece_loc,
                                board.black_piece_loc
                            )

                        board.name_obj_dict['wJ'].in_check = board.name_obj_dict['wJ'].check_check(
                            board.black_name_obj_dict,
                            board.black_piece_loc,
                            board.white_piece_loc
                        )

                        # Check to see if placing the piece cause checkmate or not
                        if board.game_over_check(
                        board.black_name_obj_dict,
                        num_turns
                        ) and bjiang.in_check:

                            text = 'Checkmate!! White Wins'
                            game_over = True
                            break

                        elif (board.game_over_check(
                            board.black_name_obj_dict,
                            num_turns
                        ) or  board.game_over_check(
                            board.white_name_obj_dict,
                            num_turns)) and (not bjiang.in_check or not wjiang.in_check):

                            text = 'Stalemate!! Draw Game'
                            game_over = True
                            break

                        elif board.game_over_check(
                            board.white_name_obj_dict,
                            num_turns
                        ) and wjiang.in_check:
                            text = 'Checkmate!! Black Wins'
                            game_over = True
                            break
                        else:
                            pass
                        
                        num_turns += 1




    if board.name_obj_dict['wJ'].in_check:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares, 
                                board.name_obj_dict['wJ'].pos)
        clock.tick(MAX_FPS)
        p.display.flip()

    elif board.name_obj_dict['bJ'].in_check:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares,
                                board.name_obj_dict['bJ'].pos)
        clock.tick(MAX_FPS)
        p.display.flip()

    else:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares, None)

        clock.tick(MAX_FPS)
        p.display.flip()

    
