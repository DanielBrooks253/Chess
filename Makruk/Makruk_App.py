import pygame as p

from Board import Board
from Pieces import Khun, Khon, Bia, Met, Ma, Rua

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

for pieces in [('wb', 'piondames-w1'), ('wm', 'knight-w1'), ('wr', 'boat-w1'), 
               ('wk', 'noble-w1'),  ('wK', 'grandferz2-w1'), ('wM', 'queen-w1'), 
               ('bb', 'piondames-b1'), ('bm', 'knight-b1'), ('br', 'boat-b1'), 
               ('bK', 'grandferz2-b1'), ('bM', 'queen-b1'), ('bk', 'noble-b1')]:
            IMAGES[pieces[0]] = p.transform.scale(p.image.load("Images/" + pieces[1] + ".jpg"), (int(SQ_SIZE*PCT_SHRINK), int(SQ_SIZE*PCT_SHRINK)))

screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Makruk')

clock = p.time.Clock()
screen.fill(p.Color('white'))
running = True

player_clicks = []

wbia0 = Bia((5,0), piece_name = 'wb0', piece_image = IMAGES['wb'], color = 'white')
wbia1 = Bia((5,1), piece_name = 'wb1', piece_image = IMAGES['wb'], color = 'white')
wbia2 = Bia((5,2), piece_name = 'wb2', piece_image = IMAGES['wb'], color = 'white')
wbia3 = Bia((5,3), piece_name = 'wb3', piece_image = IMAGES['wb'], color = 'white')
wbia4 = Bia((5,4), piece_name = 'wb4', piece_image = IMAGES['wb'], color = 'white')
wbia5 = Bia((5,5), piece_name = 'wb5', piece_image = IMAGES['wb'], color = 'white')
wbia6 = Bia((5,6), piece_name = 'wb6', piece_image = IMAGES['wb'], color = 'white')
wbia7 = Bia((5,7), piece_name = 'wb7', piece_image = IMAGES['wb'], color = 'white')

bbia0 = Bia((2,0), piece_name = 'bb0', piece_image = IMAGES['bb'], color = 'black')
bbia1 = Bia((2,1), piece_name = 'bb1', piece_image = IMAGES['bb'], color = 'black')
bbia2 = Bia((2,2), piece_name = 'bb2', piece_image = IMAGES['bb'], color = 'black')
bbia3 = Bia((2,3), piece_name = 'bb3', piece_image = IMAGES['bb'], color = 'black')
bbia4 = Bia((2,4), piece_name = 'bb4', piece_image = IMAGES['bb'], color = 'black')
bbia5 = Bia((2,5), piece_name = 'bb5', piece_image = IMAGES['bb'], color = 'black')
bbia6 = Bia((2,6), piece_name = 'bb6', piece_image = IMAGES['bb'], color = 'black')
bbia7 = Bia((2,7), piece_name = 'bb7', piece_image = IMAGES['bb'], color = 'black')

wrua0 = Rua((7,0), piece_name = 'wr0', piece_image = IMAGES['wr'], color = 'white')
wrua1 = Rua((7,7), piece_name = 'wr1', piece_image = IMAGES['wr'], color = 'white')

brua0 = Rua((0,0), piece_name = 'br0', piece_image = IMAGES['br'], color = 'black')
brua1 = Rua((0,7), piece_name = 'br1', piece_image = IMAGES['br'], color = 'black')

wma0 = Ma((7,1), piece_name = 'wm0', piece_image = IMAGES['wm'], color = 'white')
wma1 = Ma((7,6), piece_name = 'wm1', piece_image = IMAGES['wm'], color = 'white')

bma0 = Ma((0,1), piece_name = 'bm0', piece_image = IMAGES['bm'], color = 'black')
bma1 = Ma((0,6), piece_name = 'bm1', piece_image = IMAGES['bm'], color = 'black')

wkhon0 = Khon((7,2), piece_name = 'wk0', piece_image = IMAGES['wk'], color = 'white')
wkhon1 = Khon((7,5), piece_name = 'wk1', piece_image = IMAGES['wk'], color = 'white')

bkhon0 = Khon((0,2), piece_name = 'bk0', piece_image = IMAGES['bk'], color = 'black')
bkhon1 = Khon((0,5), piece_name = 'bk1', piece_image = IMAGES['bk'], color = 'black')

wmet = Met((7,3), piece_name = 'wM', piece_image = IMAGES['wM'], color = 'white')
wkhun = Khun((7,4), piece_name = 'wK', piece_image = IMAGES['wK'], color = 'white')

bmet = Met((0,3), piece_name = 'bM', piece_image = IMAGES['bM'], color = 'black')
bkhun = Khun((0,4), piece_name = 'bK', piece_image = IMAGES['bK'], color = 'black')

board = Board([wbia0,wbia1,wbia2,wbia3,wbia4,wbia5,wbia6,wbia7,
               wrua0, wrua1, wma0, wma1,wkhon0,wkhon1,wmet,wkhun],
              [bbia0,bbia1,bbia2,bbia3,bbia4,bbia5,bbia6,bbia7,
               brua0, brua1, bma0, bma1,bkhon0,bkhon1,bmet,bkhun],
               HEIGHT,WIDTH,DIMENSION)

high_squares = None
stalemate_move_count = 0
stalemate_moves = 0

while running:
    for e in p.event.get():
        if e.type == p.QUIT:
            running = False

        if not game_over:
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
                        player_clicks.append((col,row))
                        high_squares = ((col,row))
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
                                (col,row),
                                board)

                            if piece_name[1] == 'b' and \
                               board.name_obj_dict[piece_name].color == 'white' and \
                               col == 2 and not board.name_obj_dict[piece_name].promoted:

                               board.name_obj_dict[piece_name].Promote_pawn()
                               board.name_obj_dict[piece_name].piece_image = IMAGES['wM']
                            
                            elif piece_name[1] == 'b' and \
                               board.name_obj_dict[piece_name].color == 'black' and \
                               col == 5 and not board.name_obj_dict[piece_name].promoted:

                               board.name_obj_dict[piece_name].Promote_pawn()
                               board.name_obj_dict[piece_name].piece_image = IMAGES['bM']
                            else:
                                pass

                            player_clicks = []
                            high_squares = None

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

                            total_pieces = len([i for i in board.name_obj_dict.values() if i.pos is not None])

                            unpromoted_pawns = len([1 for name, obj in board.name_obj_dict.items()
                                                          if name[1] == 'b' and 
                                                            (obj.pos is None or not obj.promoted)])

                            print(total_pieces, unpromoted_pawns)

                            if unpromoted_pawns == 0:
                                if num_turns % 2 == 0: # White Made move:
                                    if len(board.black_piece_loc) == 1:
                                        stalemate_moves = board.Stalemate_Moves(board.white_name_obj_dict) # Lone black king
                                    else:
                                        stalemate_moves = 64
                                else:
                                    if len(board.white_piece_loc) == 1:
                                        stalemate_moves = board.Stalemate_Moves(board.black_name_obj_dict) # Lone white king
                                    else:
                                        stalemate_moves = 64

                            # Check to see if placing the piece cause checkmate or not
                            elif board.game_over_check(
                            board.black_name_obj_dict,
                            num_turns
                            ) and bkhun.in_check:

                                text = 'Checkmate!! White Wins'
                                game_over = True
                                break

                            elif (board.game_over_check(
                                board.black_name_obj_dict,
                                num_turns
                            ) or  board.game_over_check(
                                board.white_name_obj_dict,
                                num_turns)) and (not bkhun.in_check or not wkhun.in_check):

                                text = 'Stalemate!! Draw Game'
                                game_over = True
                                break

                            elif board.game_over_check(
                                board.white_name_obj_dict,
                                num_turns
                            ) and wkhun.in_check:
                                text = 'Checkmate!! Black Wins'
                                game_over = True
                                break
                            else:
                                pass
                            
                            if stalemate_moves != 0:
                                screen = p.display.set_mode((WIDTH+128, HEIGHT))
                                stalemate_move_count = total_pieces
                                num_turns += 1
                            else:
                                num_turns += 1

    if board.name_obj_dict['wK'].in_check:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares, 
                                board.name_obj_dict['wK'].pos, stalemate_move_count, stalemate_moves)
        clock.tick(MAX_FPS)
        p.display.flip()

    elif board.name_obj_dict['bK'].in_check:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares,
                                board.name_obj_dict['bK'].pos, stalemate_move_count, stalemate_moves)
        clock.tick(MAX_FPS)
        p.display.flip()

    else:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares,
         None, stalemate_move_count, stalemate_moves)

        clock.tick(MAX_FPS)
        p.display.flip()

