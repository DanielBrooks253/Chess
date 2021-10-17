import pygame as p

from random import shuffle
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

wpawn0 = Pawn((6,0), piece_name = 'wp0', piece_image = IMAGES['wp'], color = 'white', piece_value = 1)
wpawn1 = Pawn((6,1), piece_name = 'wp1', piece_image = IMAGES['wp'], color = 'white', piece_value = 1)
wpawn2 = Pawn((6,2), piece_name = 'wp2', piece_image = IMAGES['wp'], color = 'white', piece_value = 1)
wpawn3 = Pawn((6,3), piece_name = 'wp3', piece_image = IMAGES['wp'], color = 'white', piece_value = 1)
wpawn4 = Pawn((6,4), piece_name = 'wp4', piece_image = IMAGES['wp'], color = 'white', piece_value = 1)
wpawn5 = Pawn((6,5), piece_name = 'wp5', piece_image = IMAGES['wp'], color = 'white', piece_value = 1)
wpawn6 = Pawn((6,6), piece_name = 'wp6', piece_image = IMAGES['wp'], color = 'white', piece_value = 1)
wpawn7 = Pawn((6,7), piece_name = 'wp7', piece_image = IMAGES['wp'], color = 'white', piece_value = 1)

bpawn0 = Pawn((1,0), piece_name = 'bp0', piece_image = IMAGES['bp'], color = 'black', piece_value = 1)
bpawn1 = Pawn((1,1), piece_name = 'bp1', piece_image = IMAGES['bp'], color = 'black', piece_value = 1)
bpawn2 = Pawn((1,2), piece_name = 'bp2', piece_image = IMAGES['bp'], color = 'black', piece_value = 1)
bpawn3 = Pawn((1,3), piece_name = 'bp3', piece_image = IMAGES['bp'], color = 'black', piece_value = 1)
bpawn4 = Pawn((1,4), piece_name = 'bp4', piece_image = IMAGES['bp'], color = 'black', piece_value = 1)
bpawn5 = Pawn((1,5), piece_name = 'bp5', piece_image = IMAGES['bp'], color = 'black', piece_value = 1)
bpawn6 = Pawn((1,6), piece_name = 'bp6', piece_image = IMAGES['bp'], color = 'black', piece_value = 1)
bpawn7 = Pawn((1,7), piece_name = 'bp7', piece_image = IMAGES['bp'], color = 'black', piece_value = 1)

wrook0 = Rook((7,0), piece_name = 'wr0', piece_image = IMAGES['wr'], color = 'white', piece_value = 5)
wrook1 = Rook((7,7), piece_name = 'wr1', piece_image = IMAGES['wr'], color = 'white', piece_value = 5)

brook0 = Rook((0,0), piece_name = 'br0', piece_image = IMAGES['br'], color = 'black', piece_value = 5)
brook1 = Rook((0,7), piece_name = 'br1', piece_image = IMAGES['br'], color = 'black', piece_value = 5)

wknight0 = Knight((7,1), piece_name = 'wk0', piece_image = IMAGES['wk'], color = 'white', piece_value = 3)
wknight1 = Knight((7,6), piece_name = 'wk1', piece_image = IMAGES['wk'], color = 'white', piece_value = 3)

bknight0 = Knight((0,1), piece_name = 'bk0', piece_image = IMAGES['bk'], color = 'black', piece_value = 3)
bknight1 = Knight((0,6), piece_name = 'bk1', piece_image = IMAGES['bk'], color = 'black', piece_value = 3)

wbishop0 = Bishop((7,2), piece_name = 'wb0', piece_image = IMAGES['wb'], color = 'white', piece_value = 3)
wbishop1 = Bishop((7,5), piece_name = 'wb1', piece_image = IMAGES['wb'], color = 'white', piece_value = 3)

bbishop0 = Bishop((0,2), piece_name = 'bb0', piece_image = IMAGES['bb'], color = 'black', piece_value = 3)
bbishop1 = Bishop((0,5), piece_name = 'bb1', piece_image = IMAGES['bb'], color = 'black', piece_value = 3)

wqueen = Queen((7,3), piece_name = 'wQ', piece_image = IMAGES['wQ'], color = 'white', piece_value = 8)
wking = King((7,4), piece_name = 'wK', piece_image = IMAGES['wK'], color = 'white', piece_value = 100)

bqueen = Queen((0,3), piece_name = 'bQ', piece_image = IMAGES['bQ'], color = 'black', piece_value = 8)
bking = King((0,4), piece_name = 'bK', piece_image = IMAGES['bK'], color = 'black', piece_value = 100)

board = Board([wpawn0, wpawn1, wpawn2, wpawn3,
               wpawn4, wpawn5, wpawn6, wpawn7,
               wbishop0, wbishop1, wrook0, wrook1,
               wknight0, wknight1, wqueen, wking],
               [bpawn0, bpawn1, bpawn2, bpawn3,
               bpawn4, bpawn5, bpawn6, bpawn7,
               bbishop0, bbishop1, brook0, brook1,
               bknight0, bknight1, bqueen, bking],
               HEIGHT, WIDTH, DIMENSION, 3)

high_squares = None
start_pos = ()

white_promotion = False
black_promotion = False

AI_Mode = False
AI_color = 'black'

while running:
    for e in p.event.get():
        if e.type == p.QUIT:
            running = False

        if not game_over: # Check to see if the game has endded in checkmate or stalemate
            if AI_Mode and num_turns % 2 != 0:
                # Shuffle the dictionaries
                # This will prevent the AI from moving the same piece
                #   multiple times during the beginning of the games
                white_keys = list(board.white_name_obj_dict.keys())
                black_keys = list(board.black_name_obj_dict.keys())

                shuffle(white_keys)
                shuffle(black_keys)

                board.white_name_obj_dict = {i:board.white_name_obj_dict[i] for i in white_keys}
                board.black_name_obj_dict = {i:board.black_name_obj_dict[i] for i in black_keys}

                AI_move = board.MinMax_Algorithm(board.depth, True)

                piece_name = AI_move[0]
                board.name_obj_dict[AI_move[0]].Make_Move(
                    AI_move[1],
                    board
                )

                if piece_name[1] in ['p', 'K', 'r']:
                    board.name_obj_dict[piece_name].has_moved = True

                board.name_obj_dict['bK'].in_check = board.name_obj_dict['bK'].check_check(
                                board.white_name_obj_dict,
                                board.white_piece_loc,
                                board.black_piece_loc
                            )

                board.name_obj_dict['wK'].in_check = board.name_obj_dict['wK'].check_check(
                    board.black_name_obj_dict,
                    board.black_piece_loc,
                    board.white_piece_loc
                )

                high_sqaures = None
                num_turns += 1
 
            else:
                if e.type == p.MOUSEBUTTONDOWN:
                    location = p.mouse.get_pos()
                    row = location[0]//SQ_SIZE
                    col = location[1]//SQ_SIZE

                    if len(player_clicks) == 0:
                        if white_promotion or black_promotion:
                            if white_promotion:
                                if col == 5 and 2 <= row <= 5:
                                    if row == 2:
                                        board.name_obj_dict[piece_name].promoted_name = 'wk'
                                        board.name_obj_dict[piece_name].piece_image = IMAGES['wk']
                                    elif row == 3:
                                        board.name_obj_dict[piece_name].promoted_name = 'wb'
                                        board.name_obj_dict[piece_name].piece_image = IMAGES['wb']
                                    elif row == 4:
                                        board.name_obj_dict[piece_name].promoted_name = 'wr'
                                        board.name_obj_dict[piece_name].piece_image = IMAGES['wr']
                                    else:
                                        board.name_obj_dict[piece_name].promoted_name = 'wQ'
                                        board.name_obj_dict[piece_name].piece_image = IMAGES['wQ']
                                    
                                    white_promotion = False
                                    player_clicks = []
                                    high_squares = None
                                    break

                                else:
                                    break
                            else:
                                if col == 2 and 2 <= row <= 5:
                                    if row == 2:
                                        board.name_obj_dict[piece_name].promoted_name = 'bk'
                                        board.name_obj_dict[piece_name].piece_image = IMAGES['bk']
                                    elif row == 3:
                                        board.name_obj_dict[piece_name].promoted_name = 'bb'
                                        board.name_obj_dict[piece_name].piece_image = IMAGES['bb']
                                    elif row == 4:
                                        board.name_obj_dict[piece_name].promoted_name = 'br'
                                        board.name_obj_dict[piece_name].piece_image = IMAGES['br']
                                    else:
                                        board.name_obj_dict[piece_name].promoted_name = 'bQ'
                                        board.name_obj_dict[piece_name].piece_image = IMAGES['bQ']
                                    
                                    black_promotion = False
                                    player_clicks = []
                                    high_squares = None
                                    break

                                else:
                                    break

                        if (col, row) not in board.loc_names.keys():
                            break
                        else:
                            piece_name = board.loc_names[(col, row)]
                            start_pos = (col, row)

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
                            
                            # Castling
                            # Check to see if neight rook or king have moved
                            # Check to see if all of the pieces are out of the way
                            # Check tos ee if the kins is not in check
                            if piece_name[1] == 'K':
                                if num_turns % 2 == 0:
                                    if not board.name_obj_dict['wr0'].has_moved and \
                                        (7,1) not in board.loc_names.keys() and \
                                        (7,2) not in board.loc_names.keys() and \
                                        (7,3) not in board.loc_names.keys() and \
                                        not board.name_obj_dict['wK'].has_moved and \
                                        not board.name_obj_dict['wK'].in_check:

                                        valid_moves |= {(7,2)}
                                    else:
                                        pass

                                    if not board.name_obj_dict['wr1'].has_moved and \
                                        (7,5) not in board.loc_names.keys() and \
                                        (7,6) not in board.loc_names.keys() and \
                                        not board.name_obj_dict['wK'].has_moved and \
                                        not board.name_obj_dict['wK'].in_check:

                                        valid_moves |= {(7,6)}
                                    else:
                                        pass
                                else:
                                    if not board.name_obj_dict['br0'].has_moved and \
                                        (0,1) not in board.loc_names.keys() and \
                                        (0,2) not in board.loc_names.keys() and \
                                        (0,3) not in board.loc_names.keys() and \
                                        not board.name_obj_dict['bK'].has_moved and \
                                        not board.name_obj_dict['bK'].in_check:

                                        valid_moves |= {(0,2)}
                                    else:
                                        pass

                                    if not board.name_obj_dict['br1'].has_moved and \
                                        (0,5) not in board.loc_names.keys() and \
                                        (0,6) not in board.loc_names.keys() and \
                                        not board.name_obj_dict['bK'].has_moved and \
                                        not board.name_obj_dict['bK'].in_check:

                                        valid_moves |= {(0,6)}
                                    else:
                                        pass
                            # En Passant
                            elif piece_name[1] == 'p':
                                en_passant_moves = board.name_obj_dict[piece_name].En_Passant(
                                    board.loc_names, board.name_obj_dict
                                )
                                valid_moves |= en_passant_moves
                            else:
                                pass

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

                                if piece_name[1] in ['p', 'K', 'r'] and not board.name_obj_dict[piece_name].has_moved:
                                    board.name_obj_dict[piece_name].has_moved = True
                                    if piece_name[1] == 'p':
                                        board.name_obj_dict[piece_name].move_count += 1
                                else:
                                    pass

                                if piece_name[1] == 'p' and not board.name_obj_dict[piece_name].moved_two_spaces:
                                    if abs(board.name_obj_dict[piece_name].pos[0] - start_pos[0]) == 2:
                                        board.name_obj_dict[piece_name].moved_two_spaces = True
                                        board.name_obj_dict[piece_name].en_passant_flag = True
                                    else:
                                        pass
                                else:
                                    pass

                                # En Passant Capture clean up and promotion prep
                                if piece_name[1] == 'p':
                                    if board.name_obj_dict[piece_name].color == 'white':
                                        if col == 0 and not board.name_obj_dict[piece_name].promoted:
                                            board.name_obj_dict[piece_name].promoted = True
                                            white_promotion = True

                                        if abs(start_pos[0]-col) + abs(start_pos[1]-row) == 2 and \
                                            (col, row) not in board.black_piece_loc and \
                                            start_pos[0] == 3:
                                            
                                            if start_pos[1] > row:
                                                board.black_piece_loc.remove((start_pos[0],start_pos[1]-1))
                                                board.name_obj_dict[board.loc_names[(start_pos[0], start_pos[1]-1)]].pos = None
                                                board.black_name_obj_dict[board.loc_names[(start_pos[0], start_pos[1]-1)]].pos = None
                                                del board.loc_names[(start_pos[0], start_pos[1]-1)]
                                            else:
                                                board.black_piece_loc.remove((start_pos[0],start_pos[1]+1))
                                                board.name_obj_dict[board.loc_names[(start_pos[0], start_pos[1]+1)]].pos = None
                                                board.black_name_obj_dict[board.loc_names[(start_pos[0], start_pos[1]+1)]].pos = None
                                                del board.loc_names[(start_pos[0], start_pos[1]+1)]
                                    else:
                                        if col == 7 and not board.name_obj_dict[piece_name].promoted:
                                            board.name_obj_dict[piece_name].promoted = True
                                            black_promotion = True

                                        if abs(start_pos[0]-col) + abs(start_pos[1]-row) == 2 and \
                                        (col, row) not in board.white_piece_loc and \
                                        start_pos[0] == 4:
                                            
                                            if start_pos[1] > row:
                                                board.white_piece_loc.remove((start_pos[0],start_pos[1]-1))
                                                board.name_obj_dict[board.loc_names[(start_pos[0], start_pos[1]-1)]].pos = None
                                                board.white_name_obj_dict[board.loc_names[(start_pos[0], start_pos[1]-1)]].pos = None
                                                del board.loc_names[(start_pos[0], start_pos[1]-1)]
                                            else:
                                                board.white_piece_loc.remove((start_pos[0],start_pos[1]+1))
                                                board.name_obj_dict[board.loc_names[(start_pos[0], start_pos[1]+1)]].pos = None
                                                board.white_name_obj_dict[board.loc_names[(start_pos[0], start_pos[1]+1)]].pos = None
                                                del board.loc_names[(start_pos[0], start_pos[1]+1)]
                                        else:
                                            pass
                                else:
                                    pass

                                # If the king moves two spaces in the left or the right direction,
                                # Move the rook next to it. (Castling)
                                if piece_name[1] == 'K' and abs(start_pos[1] - board.name_obj_dict[piece_name].pos[1]) > 1:
                                    if board.name_obj_dict[piece_name].color == 'white':
                                        if board.name_obj_dict[piece_name].pos[1] < start_pos[1]:
                                            board.name_obj_dict['wr0'].Make_Move(
                                                (7,3), board)
                                        else:
                                            board.name_obj_dict['wr1'].Make_Move(
                                                (7,5), board)
                                    else:
                                        if board.name_obj_dict[piece_name].pos[1] < start_pos[1]:
                                            board.name_obj_dict['br0'].Make_Move(
                                                (0,3), board)
                                        else:
                                            board.name_obj_dict['br1'].Make_Move(
                                                (0,5), board)
                                
                                if white_promotion or black_promotion:
                                    high_squares = (col, row)
                                else:
                                    high_squares = None

                                player_clicks = []

                                board.name_obj_dict['bK'].in_check = board.name_obj_dict['bK'].check_check(
                                    board.white_name_obj_dict,
                                    board.white_piece_loc,
                                    board.black_piece_loc
                                )

                                board.name_obj_dict['wK'].in_check = board.name_obj_dict['wK'].check_check(
                                    board.black_name_obj_dict,
                                    board.black_piece_loc,
                                    board.white_piece_loc
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

                                for i in board.name_obj_dict.values():
                                    if i.piece_name[:2] == 'bp' and num_turns % 2 == 0:
                                        i.en_passant_flag = False
                                    elif i.piece_name[:2] == 'wp' and num_turns % 2 != 0:
                                        i.en_passant_flag = False
                                    else:
                                        continue
                                num_turns += 1
                            else:
                                break
    
    if board.name_obj_dict['wK'].in_check:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares, 
                                board.name_obj_dict['wK'].pos, white_promotion, black_promotion, {'White': [IMAGES['wk'], IMAGES['wb'], IMAGES['wr'], IMAGES['wQ']],
                                                                                                  'Black': [IMAGES['bk'], IMAGES['bb'], IMAGES['br'], IMAGES['bQ']]})
        clock.tick(MAX_FPS)
        p.display.flip()

    elif board.name_obj_dict['bK'].in_check:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares,
                                board.name_obj_dict['bK'].pos, white_promotion, black_promotion, {'White': [IMAGES['wk'], IMAGES['wb'], IMAGES['wr'], IMAGES['wQ']],
                                                                                                  'Black': [IMAGES['bk'], IMAGES['bb'], IMAGES['br'], IMAGES['bQ']]})
        clock.tick(MAX_FPS)
        p.display.flip()

    else:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares, None, white_promotion, black_promotion, 
        {'White': [IMAGES['wk'], IMAGES['wb'], IMAGES['wr'], IMAGES['wQ']],                                                                       
        'Black': [IMAGES['bk'], IMAGES['bb'], IMAGES['br'], IMAGES['bQ']]})

        clock.tick(MAX_FPS)
        p.display.flip()