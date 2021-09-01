import pygame as p

from Board import Board
from Pieces import Queen, King, Bishop, Rook, Pawn, Knight

p.init()

WIDTH = 512
HEIGHT = 512
DIMENSION = 8
MAX_FPS = 15
SQ_SIZE = HEIGHT//DIMENSION
PCT_SHRINK = .75

IMAGES = {}

num_turns = 0
game_over = False
text = ''
num = 1

for pieces in [('wp', 'pawn-w1'), ('wb', 'bishop-w1'), ('wK', 'king-w1'),
               ('wQ', 'queen-w1'), ('wk', 'knight-w1'), ('wr', 'rook-w1'),
               ('bp', 'pawn-b1'), ('bb', 'bishop-b1'), ('bK', 'king-b1'),
               ('bQ', 'queen-b1'), ('bk', 'knight-b1'), ('br', 'rook-b1')]:
            IMAGES[pieces[0]] = p.transform.scale(p.image.load("Images/" + pieces[1] + ".jpg"), (int(SQ_SIZE*PCT_SHRINK), int(SQ_SIZE*PCT_SHRINK)))

screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('English Chess')

clock = p.time.Clock()
screen.fill(p.Color('white'))
running = True

player_clicks = []

wpawn0 = Pawn((6,0), piece_name = 'wp0', piece_image = IMAGES['wp'], color = 'white')
wpawn1 = Pawn((6,1), piece_name = 'wp1', piece_image = IMAGES['wp'], color = 'white')
wpawn2 = Pawn((6,2), piece_name = 'wp2', piece_image = IMAGES['wp'], color = 'white')
wpawn3 = Pawn((6,3), piece_name = 'wp3', piece_image = IMAGES['wp'], color = 'white')
wpawn4 = Pawn((6,4), piece_name = 'wp4', piece_image = IMAGES['wp'], color = 'white')
wpawn5 = Pawn((6,5), piece_name = 'wp5', piece_image = IMAGES['wp'], color = 'white')
wpawn6 = Pawn((6,6), piece_name = 'wp6', piece_image = IMAGES['wp'], color = 'white')
wpawn7 = Pawn((6,7), piece_name = 'wp7', piece_image = IMAGES['wp'], color = 'white')

bpawn0 = Pawn((1,0), piece_name = 'bp0', piece_image = IMAGES['bp'], color = 'black')
bpawn1 = Pawn((1,1), piece_name = 'bp1', piece_image = IMAGES['bp'], color = 'black')
bpawn2 = Pawn((1,2), piece_name = 'bp2', piece_image = IMAGES['bp'], color = 'black')
bpawn3 = Pawn((1,3), piece_name = 'bp3', piece_image = IMAGES['bp'], color = 'black')
bpawn4 = Pawn((1,4), piece_name = 'bp4', piece_image = IMAGES['bp'], color = 'black')
bpawn5 = Pawn((1,5), piece_name = 'bp5', piece_image = IMAGES['bp'], color = 'black')
bpawn6 = Pawn((1,6), piece_name = 'bp6', piece_image = IMAGES['bp'], color = 'black')
bpawn7 = Pawn((1,7), piece_name = 'bp7', piece_image = IMAGES['bp'], color = 'black')

wrook0 = Rook((7,0), piece_name = 'wr0', piece_image = IMAGES['wr'], color = 'white')
wrook1 = Rook((7,7), piece_name = 'wr1', piece_image = IMAGES['wr'], color = 'white')

brook0 = Rook((0,0), piece_name = 'br0', piece_image = IMAGES['br'], color = 'black')
brook1 = Rook((0,7), piece_name = 'br1', piece_image = IMAGES['br'], color = 'black')

wknight0 = Knight((7,1), piece_name = 'wk0', piece_image = IMAGES['wk'], color = 'white')
wknight1 = Knight((7,6), piece_name = 'wk1', piece_image = IMAGES['wk'], color = 'white')

bknight0 = Knight((0,1), piece_name = 'bk0', piece_image = IMAGES['bk'], color = 'black')
bknight1 = Knight((0,6), piece_name = 'bk1', piece_image = IMAGES['bk'], color = 'black')

wbishop0 = Bishop((7,2), piece_name = 'wb0', piece_image = IMAGES['wb'], color = 'white')
wbishop1 = Bishop((7,5), piece_name = 'wb1', piece_image = IMAGES['wb'], color = 'white')

bbishop0 = Bishop((0,2), piece_name = 'bb0', piece_image = IMAGES['bb'], color = 'black')
bbishop1 = Bishop((0,5), piece_name = 'bb1', piece_image = IMAGES['bb'], color = 'black')

wqueen = Queen((7,3), piece_name = 'wQ', piece_image = IMAGES['wQ'], color = 'white')
wking = King((7,4), piece_name = 'wK', piece_image = IMAGES['wK'], color = 'white')

bqueen = Queen((0,3), piece_name = 'bQ', piece_image = IMAGES['bQ'], color = 'black')
bking = King((0,4), piece_name = 'bK', piece_image = IMAGES['bK'], color = 'black')

board = Board([wpawn0, wpawn1, wpawn2, wpawn3,
               wpawn4, wpawn5, wpawn6, wpawn7,
               wbishop0, wbishop1, wrook0, wrook1,
               wknight0, wknight1, wqueen, wking],
               [bpawn0, bpawn1, bpawn2, bpawn3,
               bpawn4, bpawn5, bpawn6, bpawn7,
               bbishop0, bbishop1, brook0, brook1,
               bknight0, bknight1, bqueen, bking],
               HEIGHT, WIDTH, DIMENSION)

high_squares = None
while running:
    for e in p.event.get():
        if e.type == p.QUIT:
            running = False

        if not game_over: # Check to see if the game has endded in checkmate or stalemate
            if e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                row = location[0]//SQ_SIZE
                col = location[1]//SQ_SIZE

                if len(player_clicks) == 0:

                    if (col, row) not in board.loc_names.keys():
                        break
                    else:
                        piece_name = board.loc_names[(col, row)]

                        if board.name_obj_dict[piece_name].color == 'white' and \
                            num_turns % 2 == 0:
                             moves = board.name_obj_dict[piece_name].Available_Moves(
                                 board.x_dim,
                                 board.y_dim, 
                                 board.white_piece_loc,
                                 board.black_piece_loc)

                        elif board.name_obj_dict[piece_name].color == 'black' and \
                            num_turns % 2 != 0:
                            moves = board.name_obj_dict[piece_name].Available_Moves(
                                board.x_dim,
                                board.y_dim,
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
                        high_squares = None
                        player_clicks = []
                    else:
                        if moves is None:
                            break
                        elif (col, row) in moves:
                            board.name_obj_dict[piece_name].Make_Move(
                                (col, row),
                                board
                            )

                            high_squares = None
                            player_clicks = []

                            board.name_obj_dict['wK'].in_check = board.name_obj_dict['wK'].check_check(
                                board.white_name_obj_dict,
                                board.white_piece_loc,
                                board.black_piece_loc
                            )

                            board.name_obj_dict['bK'].in_check = board.name_obj_dict['bK'].check_check(
                                board.white_name_obj_dict,
                                board.white_piece_loc,
                                board.black_piece_loc
                            )

                            if board.game_over_check(
                                board.black_name_obj_dict,
                                num_turns
                            ) and bking.in_check:
                                text = 'Checkmate!! White Wins'
                                game_over = True
                                break

                            elif board.game_over_check(
                                board.white_name_obj_dict,
                                num_turns
                            ) and wking.in_check:
                                text = 'Checkmate!! Black Wins'
                                game_over = True
                                break

                            elif (board.game_over_check(
                                board.black_name_obj_dict,
                                num_turns
                            ) or board.game_over_check(
                                board.white_name_obj_dict,
                                num_turns
                            )) and (not bking.in_check or not wking.in_check):
                                text = 'Stalemate!! Draw Game'
                                game_over = True
                                break
                            else:
                                pass

                            num_turns += 1
                        else:
                            break
    
    if board.name_obj_dict['wK'].in_check:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares,
                                board.name_obj_dict['wK'].pos)
        clock.tick(MAX_FPS)
        p.display.flip()

    elif board.name_obj_dict['bK'].in_check:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares,
                                board.name_obj_dict['bK'].pos)
        clock.tick(MAX_FPS)
        p.display.flip()

    else:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares, None)
        clock.tick(MAX_FPS)
        p.display.flip()