import pygame as p
from pygame.constants import MOUSEBUTTONDOWN

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
num_turns = 0

# Instantiate all the pieces
# Ne (Pawns or soliders)
wn0 = Ne((5,0), piece_name = 'wn0', piece_image=IMAGES['wn'], color='white')
wn1 = Ne((5,1), piece_name = 'wn1', piece_image=IMAGES['wn'], color='white')
wn2 = Ne((5,2), piece_name = 'wn2', piece_image=IMAGES['wn'], color='white')
wn3 = Ne((5,3), piece_name = 'wn3', piece_image=IMAGES['wn'], color='white')
wn4 = Ne((4,4), piece_name = 'wn4', piece_image=IMAGES['wn'], color='white')
wn5 = Ne((4,5), piece_name = 'wn5', piece_image=IMAGES['wn'], color='white')
wn6 = Ne((4,6), piece_name = 'wn6', piece_image=IMAGES['wn'], color='white')
wn7 = Ne((4,7), piece_name = 'wn7', piece_image=IMAGES['wn'], color='white')

bn0 = Ne((3,0), piece_name = 'bn0', piece_image=IMAGES['bn'], color='black')
bn1 = Ne((3,1), piece_name = 'bn1', piece_image=IMAGES['bn'], color='black')
bn2 = Ne((3,2), piece_name = 'bn2', piece_image=IMAGES['bn'], color='black')
bn3 = Ne((3,3), piece_name = 'bn3', piece_image=IMAGES['bn'], color='black')
bn4 = Ne((2,4), piece_name = 'bn4', piece_image=IMAGES['bn'], color='black')
bn5 = Ne((2,5), piece_name = 'bn5', piece_image=IMAGES['bn'], color='black')
bn6 = Ne((2,6), piece_name = 'bn6', piece_image=IMAGES['bn'], color='black')
bn7 = Ne((2,7), piece_name = 'bn7', piece_image=IMAGES['bn'], color='black')

# The pawns are the only pieces on the board at the start of the game.
# All other pieces are placed by the player at the start

# Yahhta (Rooks)
wy0 = Yahhta(None, piece_name='wy0', piece_image=IMAGES['wy'], color='white')
wy1 = Yahhta(None, piece_name='wy1', piece_image=IMAGES['wy'], color='white')

by0 = Yahhta(None, piece_name='by0', piece_image=IMAGES['by'], color='black')
by1 = Yahhta(None, piece_name='by1', piece_image=IMAGES['by'], color='black')

# Myin (Horse or knight)
wm0 = Myin(None, piece_name='wm0', piece_image=IMAGES['wm'], color='white')
wm1 = Myin(None, piece_name='wm1', piece_image=IMAGES['wm'], color='white')

bm0 = Myin(None, piece_name='bm0', piece_image=IMAGES['bm'], color='black')
bm1 = Myin(None, piece_name='bm1', piece_image=IMAGES['bm'], color='black')

# Sin (Bishop)
ws0 = Sin(None, piece_name='ws0', piece_image=IMAGES['ws'], color='white')
ws1 = Sin(None, piece_name='ws1', piece_image=IMAGES['ws'], color='white')

bs0 = Sin(None, piece_name='bs0', piece_image=IMAGES['bs'], color='black')
bs1 = Sin(None, piece_name='bs1', piece_image=IMAGES['bs'], color='black')

# Min-Gyi (King)
wM = MinGyi(None, piece_name='wM0', piece_image=IMAGES['wM'], color='white')
bM = MinGyi(None, piece_name='bM0', piece_image=IMAGES['bM'], color='black')

# Sit-Ke (queen or general)
wS = SitKe(None, piece_name='wS0', piece_image=IMAGES['wS'], color='white')
bS = SitKe(None, piece_name='bS0', piece_image=IMAGES['bS'], color='black')

board = Board([wn0, wn1, wn2, wn3,
               wn4, wn5, wn6, wn7,
               wy0, wy1, wm0, wm1,
               ws0, ws1, wM, wS],
              [bn0, bn1, bn2, bn3,
               bn4, bn5, bn6, bn7,
               by0, by1, bm0, bm1,
               bs0, bs1, bM, bS], HEIGHT, WIDTH, DIMENSION)

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

        if e.type == MOUSEBUTTONDOWN:
            num_turns += 1


    board.drawGameState(screen, board.name_obj_dict, False, '', 22, None, None, num_turns)
    clock.tick(MAX_FPS)
    p.display.flip()