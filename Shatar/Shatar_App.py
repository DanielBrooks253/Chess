import pygame as p

from Board import Board
from Pieces import Noyon, Tereg, Teme, Mori, Fu, Bers

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

for pieces in [('wf', 'citizen-w1'), ('wm', 'knight-w1'), ('wr', 'dabbaba-w1'), 
               ('wt', 'camel-w1'),  ('wN', 'shah-w1'), ('wB', 'queen-w1'), 
               ('bf', 'citizen-b1'), ('bm', 'knight-b1'), ('br', 'dabbaba-b1'), 
               ('bN', 'shah-b1'), ('bB', 'queen-b1'), ('bt', 'camel-b1')]:
            IMAGES[pieces[0]] = p.transform.scale(p.image.load("Images/" + pieces[1] + ".jpg"), (int(SQ_SIZE*PCT_SHRINK), int(SQ_SIZE*PCT_SHRINK)))

screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Shatar')

clock = p.time.Clock()
screen.fill(p.Color('white'))
running = True

player_clicks = []

wfu0 = Fu((6,0), piece_name = 'wf0', piece_image = IMAGES['wf'], color = 'white')
wfu1 = Fu((6,1), piece_name = 'wf1', piece_image = IMAGES['wf'], color = 'white')
wfu2 = Fu((6,2), piece_name = 'wf2', piece_image = IMAGES['wf'], color = 'white')
wfu3 = Fu((6,3), piece_name = 'wf3', piece_image = IMAGES['wf'], color = 'white')
wfu4 = Fu((6,4), piece_name = 'wf4', piece_image = IMAGES['wf'], color = 'white')
wfu5 = Fu((6,5), piece_name = 'wf5', piece_image = IMAGES['wf'], color = 'white')
wfu6 = Fu((6,6), piece_name = 'wf6', piece_image = IMAGES['wf'], color = 'white')
wfu7 = Fu((6,7), piece_name = 'wf7', piece_image = IMAGES['wf'], color = 'white')

bfu0 = Fu((1,0), piece_name = 'bf0', piece_image = IMAGES['bf'], color = 'black')
bfu1 = Fu((1,1), piece_name = 'bf1', piece_image = IMAGES['bf'], color = 'black')
bfu2 = Fu((1,2), piece_name = 'bf2', piece_image = IMAGES['bf'], color = 'black')
bfu3 = Fu((1,3), piece_name = 'bf3', piece_image = IMAGES['bf'], color = 'black')
bfu4 = Fu((1,4), piece_name = 'bf4', piece_image = IMAGES['bf'], color = 'black')
bfu5 = Fu((1,5), piece_name = 'bf5', piece_image = IMAGES['bf'], color = 'black')
bfu6 = Fu((1,6), piece_name = 'bf6', piece_image = IMAGES['bf'], color = 'black')
bfu7 = Fu((1,7), piece_name = 'bf7', piece_image = IMAGES['bf'], color = 'black')

wtereg0 = Tereg((7,0), piece_name = 'wr0', piece_image = IMAGES['wr'], color = 'white')
wtereg1 = Tereg((7,7), piece_name = 'wr1', piece_image = IMAGES['wr'], color = 'white')

btereg0 = Tereg((0,0), piece_name = 'br0', piece_image = IMAGES['br'], color = 'black')
btereg1 = Tereg((0,7), piece_name = 'br1', piece_image = IMAGES['br'], color = 'black')

wmori0 = Mori((7,1), piece_name = 'wm0', piece_image = IMAGES['wm'], color = 'white')
wmori1 = Mori((7,6), piece_name = 'wm1', piece_image = IMAGES['wm'], color = 'white')

bmori0 = Mori((0,1), piece_name = 'bk0', piece_image = IMAGES['bm'], color = 'black')
bmori1 = Mori((0,6), piece_name = 'bk1', piece_image = IMAGES['bm'], color = 'black')

wteme0 = Teme((7,2), piece_name = 'wt0', piece_image = IMAGES['wt'], color = 'white')
wteme1 = Teme((7,5), piece_name = 'wt1', piece_image = IMAGES['wt'], color = 'white')

bteme0 = Teme((0,2), piece_name = 'bt0', piece_image = IMAGES['bt'], color = 'black')
bteme1 = Teme((0,5), piece_name = 'bt1', piece_image = IMAGES['bt'], color = 'black')

wbers = Bers((7,3), piece_name = 'wB', piece_image = IMAGES['wB'], color = 'white')
wnoyon = Noyon((7,4), piece_name = 'wN', piece_image = IMAGES['wN'], color = 'white')

bbers = Bers((0,3), piece_name = 'bB', piece_image = IMAGES['bB'], color = 'black')
bnoyon = Noyon((0,4), piece_name = 'bN', piece_image = IMAGES['bN'], color = 'black')

board = Board([wfu0,wfu1,wfu2,wfu3,wfu4,wfu5,wfu6,wfu7,
              wtereg0,wtereg1,wmori0,wmori1,wteme0,wteme1,wbers,wnoyon],
              [bfu0,bfu1,bfu2,bfu3,bfu4,bfu5,bfu6,bfu7,
              btereg0,btereg1,bmori0,bmori1,bteme0,bteme1,bbers,bnoyon],
              HEIGHT,WIDTH,DIMENSION)

high_squares = None

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

                            if piece_name[1] == 'f' and \
                               board.name_obj_dict[piece_name].color == 'white' and \
                               col == 0 and not board.name_obj_dict[piece_name].promoted:

                               board.name_obj_dict[piece_name].Promote_pawn()
                               board.name_obj_dict[piece_name].piece_image = IMAGES['wB']
                            
                            elif piece_name[1] == 'f' and \
                               board.name_obj_dict[piece_name].color == 'black' and \
                               col == 7 and not board.name_obj_dict[piece_name].promoted:

                               board.name_obj_dict[piece_name].Promote_pawn()
                               board.name_obj_dict[piece_name].piece_image = IMAGES['bB']
                            else:
                                pass

                            player_clicks = []
                            high_squares = None

                            board.name_obj_dict['bN'].in_check = board.name_obj_dict['bN'].check_check(
                                board.white_name_obj_dict,
                                board.white_piece_loc,
                                board.black_piece_loc
                            )

                            board.name_obj_dict['wN'].in_check = board.name_obj_dict['wN'].check_check(
                                board.black_name_obj_dict,
                                board.black_piece_loc,
                                board.white_piece_loc
                            )

                            # Number of pieces left 
                            if len(board.white_piece_loc) == 1 or len(board.black_piece_loc) == 1:
                                text = 'Stalemate!! Draw Game'
                                game_over = True
                                break

                            elif board.game_over_check(
                                board.black_name_obj_dict,
                                num_turns
                            ) and bnoyon.in_check:
                                text = 'Checkmate!! White Wins'
                                game_over = True
                                break

                            elif board.game_over_check(
                                board.white_name_obj_dict,
                                num_turns
                            ) and wnoyon.in_check:
                                text = 'Checkmate!! Black Wins'
                                game_over = True
                                break

                            elif (board.game_over_check(
                                board.black_name_obj_dict,
                                num_turns
                            ) or board.game_over_check(
                                board.white_name_obj_dict,
                                num_turns
                            )) and (not bnoyon.in_check or not wnoyon.in_check):
                                text = 'Stalemate!! Draw Game'
                                game_over = True
                                break
                            else:
                                pass

                            num_turns += 1

    if board.name_obj_dict['wN'].in_check:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares, 
                                board.name_obj_dict['wN'].pos)
        clock.tick(MAX_FPS)
        p.display.flip()

    elif board.name_obj_dict['bN'].in_check:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares,
                                board.name_obj_dict['bN'].pos)
        clock.tick(MAX_FPS)
        p.display.flip()

    else:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares, None)

        clock.tick(MAX_FPS)
        p.display.flip()

