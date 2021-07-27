import pygame as p

from Pieces import MinGyi, Yahhta, Myin, Ne, SitKe, Sin
from Board_Test import Board

p.init()

WIDTH = 582
HEIGHT = 512

DIMENSION = 8
MAX_FPS = 15
SQ_SIZE = HEIGHT//DIMENSION
PCT_SHRINK = .75

IMAGES = {}

num_turns = 0
num = 1
game_over = False
text = ''
player_clicks = []
num_placed_pieces = 0

for pieces in [('wn', 'hh-lance-w1'), ('bn', 'hh-lance-b1'),
               ('wy', 'talia-w1'), ('by', 'talia-b1'),
               ('wm', 'knight-w1'), ('bm', 'knight-b1'),
               ('ws', 'elephant-w1'), ('bs', 'elephant-b1'),
               ('wM', 'wazir-w1'), ('bM', 'wazir-b1'),
               ('wS', 'general-w1'), ('bS', 'general-b1')]:
    IMAGES[pieces[0]] = p.transform.scale(p.image.load("Images/" + pieces[1] + ".jpg"), (int(SQ_SIZE*PCT_SHRINK), int(SQ_SIZE*PCT_SHRINK)))

screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Sittuyin')

clock = p.time.Clock()
screen.fill(p.Color('white'))
running = True

# Instantiate all the pieces
# Ne (Pawns or soliders)
wn0 = Ne((5,0), set_up_coord = None, piece_name = 'wn0', piece_image=IMAGES['wn'], set_up_loc = None, color='white')
wn1 = Ne((5,1), set_up_coord = None, piece_name = 'wn1', piece_image=IMAGES['wn'], set_up_loc = None, color='white')
wn2 = Ne((5,2), set_up_coord = None, piece_name = 'wn2', piece_image=IMAGES['wn'], set_up_loc = None, color='white')
wn3 = Ne((5,3), set_up_coord = None, piece_name = 'wn3', piece_image=IMAGES['wn'], set_up_loc = None, color='white')
wn4 = Ne((4,4), set_up_coord = None, piece_name = 'wn4', piece_image=IMAGES['wn'], set_up_loc = None, color='white')
wn5 = Ne((4,5), set_up_coord = None, piece_name = 'wn5', piece_image=IMAGES['wn'], set_up_loc = None, color='white')
wn6 = Ne((4,6), set_up_coord = None, piece_name = 'wn6', piece_image=IMAGES['wn'], set_up_loc = None, color='white')
wn7 = Ne((4,7), set_up_coord = None, piece_name = 'wn7', piece_image=IMAGES['wn'], set_up_loc = None, color='white')

bn0 = Ne((3,0), set_up_coord = None, piece_name = 'bn0', piece_image=IMAGES['bn'], set_up_loc = None, color='black')
bn1 = Ne((3,1), set_up_coord = None, piece_name = 'bn1', piece_image=IMAGES['bn'], set_up_loc = None, color='black')
bn2 = Ne((3,2), set_up_coord = None, piece_name = 'bn2', piece_image=IMAGES['bn'], set_up_loc = None, color='black')
bn3 = Ne((3,3), set_up_coord = None, piece_name = 'bn3', piece_image=IMAGES['bn'], set_up_loc = None, color='black')
bn4 = Ne((2,4), set_up_coord = None, piece_name = 'bn4', piece_image=IMAGES['bn'], set_up_loc = None, color='black')
bn5 = Ne((2,5), set_up_coord = None, piece_name = 'bn5', piece_image=IMAGES['bn'], set_up_loc = None, color='black')
bn6 = Ne((2,6), set_up_coord = None, piece_name = 'bn6', piece_image=IMAGES['bn'], set_up_loc = None, color='black')
bn7 = Ne((2,7), set_up_coord = None, piece_name = 'bn7', piece_image=IMAGES['bn'], set_up_loc = None, color='black')

# The pawns are the only pieces on the board at the start of the game.
# All other pieces are placed by the player at the start

# Yahhta (Rooks)
wy0 = Yahhta(None, set_up_coord = (0,8), piece_name='wy0', piece_image=IMAGES['wy'], set_up_loc = (HEIGHT+10, 10), color='white')
wy1 = Yahhta(None, set_up_coord = (1,8), piece_name='wy1', piece_image=IMAGES['wy'], set_up_loc = (HEIGHT+10, SQ_SIZE+10), color='white')

by0 = Yahhta(None, set_up_coord = (0,8), piece_name='by0', piece_image=IMAGES['by'], set_up_loc = (HEIGHT+10, 10), color='black')
by1 = Yahhta(None, set_up_coord = (1,8), piece_name='by1', piece_image=IMAGES['by'], set_up_loc = (HEIGHT+10, SQ_SIZE+10), color='black')

# Myin (Horse or knight)
wm0 = Myin(None, set_up_coord = (2,8), piece_name='wm0', piece_image=IMAGES['wm'], set_up_loc = (HEIGHT+10, SQ_SIZE*2+10), color='white')
wm1 = Myin(None, set_up_coord = (3,8), piece_name='wm1', piece_image=IMAGES['wm'], set_up_loc = (HEIGHT+10, SQ_SIZE*3+10), color='white')

bm0 = Myin(None, set_up_coord = (2,8), piece_name='bm0', piece_image=IMAGES['bm'], set_up_loc = (HEIGHT+10, SQ_SIZE*2+10),  color='black')
bm1 = Myin(None, set_up_coord = (3,8), piece_name='bm1', piece_image=IMAGES['bm'], set_up_loc = (HEIGHT+10, SQ_SIZE*3+10), color='black')

# Sin (Bishop)
ws0 = Sin(None, set_up_coord = (4,8), piece_name='ws0', piece_image=IMAGES['ws'], set_up_loc = (HEIGHT+10, SQ_SIZE*4+10), color='white')
ws1 = Sin(None, set_up_coord = (5,8), piece_name='ws1', piece_image=IMAGES['ws'], set_up_loc = (HEIGHT+10, SQ_SIZE*5+10), color='white')

bs0 = Sin(None, set_up_coord = (4,8), piece_name='bs0', piece_image=IMAGES['bs'], set_up_loc = (HEIGHT+10, SQ_SIZE*4+10), color='black')
bs1 = Sin(None, set_up_coord = (5,8), piece_name='bs1', piece_image=IMAGES['bs'], set_up_loc = (HEIGHT+10, SQ_SIZE*5+10), color='black')

# Min-Gyi (King)
wM = MinGyi(None, set_up_coord = (6,8), piece_name='wM0', piece_image=IMAGES['wM'], set_up_loc = (HEIGHT+10, SQ_SIZE*6+10), color='white')
bM = MinGyi(None, set_up_coord = (6,8), piece_name='bM0', piece_image=IMAGES['bM'], set_up_loc = (HEIGHT+10, SQ_SIZE*6+10), color='black')

# Sit-Ke (queen or general)
wS = SitKe(None, set_up_coord = (7,8), piece_name='wS0', piece_image=IMAGES['wS'], set_up_loc = (HEIGHT+10, SQ_SIZE*7+10), color='white')
bS = SitKe(None, set_up_coord = (7,8), piece_name='bS0', piece_image=IMAGES['bS'], set_up_loc = (HEIGHT+10, SQ_SIZE*7+10), color='black')

board = Board([wn0, wn1, wn2, wn3,
               wn4, wn5, wn6, wn7,
               wy0, wy1, wm0, wm1,
               ws0, ws1, wM, wS],
              [bn0, bn1, bn2, bn3,
               bn4, bn5, bn6, bn7,
               by0, by1, bm0, bm1,
               bs0, bs1, bM, bS], HEIGHT, WIDTH, DIMENSION)

high_squares = None

while running:
    if num_turns == 2:
        board.HEIGHT = 512
        board.WIDTH = 512

        screen = p.display.set_mode((board.WIDTH, board.HEIGHT))
        p.display.set_caption('Sittuyin')

        clock = p.time.Clock()
        screen.fill(p.Color('white'))

    for e in p.event.get():
        if e.type == p.QUIT:
            running = False

        if e.type == p.MOUSEBUTTONDOWN:
            location = p.mouse.get_pos()
            row = location[0]//SQ_SIZE
            col = location[1]//SQ_SIZE

            # If it is the first move of the game
            # White gets to place their pieces
            if num_turns == 0:
                if len(player_clicks) == 0:
                    if row < 8: # Only click in sidebar 
                        continue
                    else:
                        player_clicks.append((col, row))
                        piece_placement_opts = board.white_set_up_locs[(col, row)].place_piece(
                                board.white_piece_loc,
                                board.black_piece_loc,
                                board.name_obj_dict['bM0'])

                        high_squares = {(col, row)}|piece_placement_opts
                else:
                    if (col, row) in player_clicks: # Deselect piece
                        high_squares = None
                        player_clicks = []
                        continue
                    elif (col, row) not in piece_placement_opts:
                        continue
                    else:
                        # Update the location of the placed piece
                        # Change all of the setup variables to None
                        board.white_set_up_locs[player_clicks[0]].pos = (col, row)
                        board.white_set_up_locs[player_clicks[0]].set_up_coord = None
                        board.white_set_up_locs[player_clicks[0]].set_up_loc = None

                        board.white_piece_loc |= {(col, row)}
                        high_squares = None
                        player_clicks = []
                        num_placed_pieces += 1

                        if num_placed_pieces == 8:
                            num_turns += 1
                            num_placed_pieces = 0
                        else:
                            pass

            # Second move of the game
            # Black gets to place their pieces
            elif num_turns == 1:
                if len(player_clicks) == 0:
                    if row < 8: # Only click in sidebar 
                        continue
                    else:
                        player_clicks.append((col, row))
                        piece_placement_opts = board.black_set_up_locs[(col, row)].place_piece(
                                board.black_piece_loc,
                                board.white_piece_loc,
                                board.name_obj_dict['wM0'])

                        high_squares = {(col, row)}|piece_placement_opts
                else:
                    if (col, row) in player_clicks: # Deselect piece
                        high_squares = None
                        player_clicks = []
                        continue
                    elif (col, row) not in piece_placement_opts:
                        continue
                    else:
                        # Update the location of the placed piece
                        # Change all of the setup variables to None
                        board.black_set_up_locs[player_clicks[0]].pos = (col, row)
                        board.black_set_up_locs[player_clicks[0]].set_up_coord = None
                        board.black_set_up_locs[player_clicks[0]].set_up_loc = None

                        board.black_piece_loc |= {(col, row)}
                        high_squares = None
                        player_clicks = []
                        num_placed_pieces += 1

                        if num_placed_pieces == 8:
                            num_turns += 1
                            num_placed_pieces = 0
                        else:
                            pass
            # Normal game play
            else:
                pass


    board.drawGameState(screen, board.name_obj_dict, False, text, num, high_squares, None, num_turns)
    clock.tick(MAX_FPS)
    p.display.flip()