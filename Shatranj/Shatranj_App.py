import pygame as p

from Board import Board
from Pieces import Shah, Pil, Rukh, Asp, Pujada, Farzin

p.init()
WIDTH = HEIGHT = 512
DIMENSION = 8
MAX_FPS = 15
SQ_SIZE = HEIGHT//DIMENSION

IMAGES = {} 

for pieces in [('wp', 'pawn-w1'), ('wr', 'chariot-w1'), ('wa', 'knight-w1'),
               ('we', 'elephant-w1'), ('wS', 'king-w1'), ('wF', 'queen-w1'),
               ('bp', 'pawn-b1'), ('br', 'chariot-b1'), ('ba', 'knight-b1'),
               ('be', 'elephant-b1'), ('bS', 'king-b1'), ('bF', 'queen-b1')]:
            IMAGES[pieces[0]] = p.transform.scale(p.image.load("Images/" + pieces[1] + ".jpg"), (SQ_SIZE, SQ_SIZE))

# Pygame initializations
screen = p.display.set_mode((WIDTH, HEIGHT))
clock = p.time.Clock()
screen.fill(p.Color('white'))
running = True

# Initialize all of the pieces on the board
wp0 = Pujada((6,0), piece_name='wp0', piece_image = IMAGES['wp'], color='white')
wp1 = Pujada((6,1), piece_name='wp1', piece_image = IMAGES['wp'], color='white')
wp2 = Pujada((6,2), piece_name='wp2', piece_image = IMAGES['wp'], color='white')
wp3 = Pujada((6,3), piece_name='wp3', piece_image = IMAGES['wp'], color='white')
wp4 = Pujada((6,4), piece_name='wp4', piece_image = IMAGES['wp'], color='white')
wp5 = Pujada((6,5), piece_name='wp5', piece_image = IMAGES['wp'], color='white')
wp6 = Pujada((6,6), piece_name='wp6', piece_image = IMAGES['wp'], color='white')
wp7 = Pujada((6,7), piece_name='wp7', piece_image = IMAGES['wp'], color='white')

bp0 = Pujada((1,0), piece_name='bp0', piece_image = IMAGES['bp'], color='black')
bp1 = Pujada((1,1), piece_name='bp1', piece_image = IMAGES['bp'], color='black')
bp2 = Pujada((1,2), piece_name='bp2', piece_image = IMAGES['bp'], color='black')
bp3 = Pujada((1,3), piece_name='bp3', piece_image = IMAGES['bp'], color='black')
bp4 = Pujada((1,4), piece_name='bp4', piece_image = IMAGES['bp'], color='black')
bp5 = Pujada((1,5), piece_name='bp5', piece_image = IMAGES['bp'], color='black')
bp6 = Pujada((1,6), piece_name='bp6', piece_image = IMAGES['bp'], color='black')
bp7 = Pujada((1,7), piece_name='bp7', piece_image = IMAGES['bp'], color='black')

# Rukh (Rooks)
wr0 = Rukh((7,0), piece_name='wr0', piece_image = IMAGES['wr'], color='white')
wr1 = Rukh((7,7), piece_name='wr1', piece_image = IMAGES['wr'], color='white')

br0 = Rukh((0,0), piece_name='br0', piece_image = IMAGES['br'], color='black')
br1 = Rukh((0,7), piece_name='br1', piece_image = IMAGES['br'], color='black')

# Asp (Horses)
wa0 = Asp((7,1), piece_name='wa0', piece_image = IMAGES['wa'], color='white')
wa1 = Asp((7,6), piece_name='wa1', piece_image = IMAGES['wa'], color='white')

ba0 = Asp((0,1), piece_name='ba0', piece_image = IMAGES['ba'], color='black')
ba1 = Asp((0,6), piece_name='ba1', piece_image = IMAGES['ba'], color='black')

# Pil (Elephants)
we0 = Pil((7,2), piece_name='we0', piece_image = IMAGES['we'], color='white')
we1 = Pil((7,5), piece_name='we1', piece_image = IMAGES['we'], color='white')

be0 = Pil((0,2), piece_name='be0', piece_image = IMAGES['be'], color='black')
be1 = Pil((0,5), piece_name='be1', piece_image = IMAGES['be'], color='black')

# Shah (King) and Farzin (Queen)
wS = Shah((7,3), piece_name='wS0', piece_image = IMAGES['wS'], color='white')
wF = Farzin((7,4), piece_name='wF0', piece_image = IMAGES['wF'], color='white')

bS = Shah((0,3), piece_name='bS0', piece_image = IMAGES['bS'], color='black')
bF = Farzin((0,4), piece_name='bF0', piece_image = IMAGES['bF'], color='black')

# Set the pieces on the board for the start of the match
board = Board([wp0, wp1, wp2, wp3,
                wp4, wp5, wp6, wp7,
                wr0, wr1, wa0, wa1,
                we0, we1, wS, wF], 
              [bp0, bp1, bp2, bp3,
                bp4, bp5, bp6, bp7,
                br0, br1, ba0, ba1,
                be0, be1, bS, bF], HEIGHT, DIMENSION)

while running:
    for e in p.event.get():
        if e.type == p.QUIT:
            running = False

    board.drawGameState(screen, board.name_obj_dict)
    clock.tick(MAX_FPS)
    p.display.flip()



