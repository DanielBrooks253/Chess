import pygame as p

from Board import Board
from Pieces import OSho, GinSho, Kyosha, KeiMa, Fuhyo, KinSho, Hisha, Kaku

p.init()

WIDTH = HEIGHT = 522
DIMENSION = 9
MAX_FPS = 15
SQ_SIZE = HEIGHT//DIMENSION
PCT_SHRINK = .75

IMAGES = {} 

num_turns = 0
num = 1
game_over = False
all_pieces_captured_turns = []
text = ''

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
wfuhyo0 = Fuhyo((6,0), piece_name='wf0', piece_image = IMAGES['Pawn'], promoted_image = IMAGES['prom_pawn'], color='white')
wfuhyo1 = Fuhyo((6,1), piece_name='wf1', piece_image = IMAGES['Pawn'], promoted_image = IMAGES['prom_pawn'], color='white')
wfuhyo2 = Fuhyo((6,2), piece_name='wf2', piece_image = IMAGES['Pawn'], promoted_image = IMAGES['prom_pawn'], color='white')
wfuhyo3 = Fuhyo((6,3), piece_name='wf3', piece_image = IMAGES['Pawn'], promoted_image = IMAGES['prom_pawn'], color='white')
wfuhyo4 = Fuhyo((6,4), piece_name='wf4', piece_image = IMAGES['Pawn'], promoted_image = IMAGES['prom_pawn'], color='white')
wfuhyo5 = Fuhyo((6,5), piece_name='wf5', piece_image = IMAGES['Pawn'], promoted_image = IMAGES['prom_pawn'], color='white')
wfuhyo6 = Fuhyo((6,6), piece_name='wf6', piece_image = IMAGES['Pawn'], promoted_image = IMAGES['prom_pawn'], color='white')
wfuhyo7 = Fuhyo((6,7), piece_name='wf7', piece_image = IMAGES['Pawn'], promoted_image = IMAGES['prom_pawn'], color='white')
wfuhyo8 = Fuhyo((6,8), piece_name='wf8', piece_image = IMAGES['Pawn'], promoted_image = IMAGES['prom_pawn'], color='white')

bfuhyo0 = Fuhyo((2,0), piece_name='bp0', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black')
bfuhyo1 = Fuhyo((2,1), piece_name='bp1', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black')
bfuhyo2 = Fuhyo((2,2), piece_name='bp2', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black')
bfuhyo3 = Fuhyo((2,3), piece_name='bp3', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black')
bfuhyo4 = Fuhyo((2,4), piece_name='bp4', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black')
bfuhyo5 = Fuhyo((2,5), piece_name='bp5', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black')
bfuhyo6 = Fuhyo((2,6), piece_name='bp6', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black')
bfuhyo7 = Fuhyo((2,7), piece_name='bp7', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black')
bfuhyo8 = Fuhyo((2,8), piece_name='bp8', piece_image = p.transform.rotate(IMAGES['Pawn'], 180), promoted_image = p.transform.rotate(IMAGES['prom_pawn'], 180), color='black')

# Kyosha (Lances)
wkyosha0 = Kyosha((8,0), piece_name='wl0', piece_image = IMAGES['Lance'], promoted_image = IMAGES['prom_lance'], color='white')
wkyosha1 = Kyosha((8,8), piece_name='wl1', piece_image = IMAGES['Lance'], promoted_image = IMAGES['prom_lance'], color='white')

bkyosha0 = Kyosha((0,0), piece_name='bl0', piece_image = p.transform.rotate(IMAGES['Lance'], 180), promoted_image = p.transform.rotate(IMAGES['prom_lance'], 180), color='black')
bkyosha1 = Kyosha((0,8), piece_name='bl1', piece_image = p.transform.rotate(IMAGES['Lance'], 180), promoted_image = p.transform.rotate(IMAGES['prom_lance'], 180), color='black')

# Kei-Ma (Knights)
wkeima0 = KeiMa((8,1), piece_name='wk0', piece_image = IMAGES['Knight'], promoted_image = IMAGES['prom_knight'], color='white')
wkeima1 = KeiMa((8,7), piece_name='wk1', piece_image = IMAGES['Knight'], promoted_image = IMAGES['prom_knight'], color='white')

bkeima0 = KeiMa((0,1), piece_name='bk0', piece_image = p.transform.rotate(IMAGES['Knight'], 180), promoted_image = p.transform.rotate(IMAGES['prom_knight'], 180), color='black')
bkeima1 = KeiMa((0,7), piece_name='bk1', piece_image = p.transform.rotate(IMAGES['Knight'], 180), promoted_image = p.transform.rotate(IMAGES['prom_knight'], 180), color='black')

# Gin-Sho (Silver Generals)
wginsho0 = GinSho((8,2), piece_name='wg0', piece_image = IMAGES['Silver_General'], promoted_image = IMAGES['prom_silver'], color='white')
wginsho1 = GinSho((8,6), piece_name='wg1', piece_image = IMAGES['Silver_General'], promoted_image = IMAGES['prom_silver'], color='white')

bginsho0 = GinSho((0,2), piece_name='bg0', piece_image = p.transform.rotate(IMAGES['Silver_General'], 180), promoted_image = p.transform.rotate(IMAGES['prom_silver'], 180), color='black')
bginsho1 = GinSho((0,6), piece_name='bg1', piece_image = p.transform.rotate(IMAGES['Silver_General'], 180), promoted_image = p.transform.rotate(IMAGES['prom_silver'], 180), color='black')

# Kin-Sho (Gold Generals)
wkinsho0 = KinSho((8,3), piece_name='wks0', piece_image = IMAGES['Gold_General'], promoted_image = None, color='white')
wkinsho1 = KinSho((8,5), piece_name='wks1', piece_image = IMAGES['Gold_General'], promoted_image = None, color='white')

bkinsho0 = KinSho((0,3), piece_name='bks0', piece_image = p.transform.rotate(IMAGES['Gold_General'], 180), promoted_image = None, color='black')
bkinsho1 = KinSho((0,5), piece_name='bks1', piece_image = p.transform.rotate(IMAGES['Gold_General'], 180), promoted_image = None, color='black')

# Kaku (Bishop)
wkaku = Kaku((7,1), piece_name = 'wk', piece_image = IMAGES['Bishop'], promoted_image = IMAGES['prom_bishop'], color='white')
bkaku = Kaku((1,1), piece_name = 'bk', piece_image = p.transform.rotate(IMAGES['Bishop'], 180), promoted_image = p.transform.rotate(IMAGES['prom_bishop'], 180), color='black')

# Hisha (Rook)
whisha = Hisha((7,7), piece_name = 'wh', piece_image = IMAGES['Rook'], promoted_image = IMAGES['prom_rook'], color='white')
bhisha = Hisha((1,7), piece_name = 'bh', piece_image = p.transform.rotate(IMAGES['Rook'], 180), promoted_image = p.transform.rotate(IMAGES['prom_rook'], 180), color='black')

# O-Sho/Gyuk (King)
wosho = OSho((8,4), piece_name = 'wO', piece_image = IMAGES['King'], promoted_image = None, color='white')
bosho = OSho((0,4), piece_name = 'bO', piece_image = p.transform.rotate(IMAGES['King'], 180), promoted_image = None, color='black')

# Set the pieces on the board for the start of the match
board = Board([wfuhyo0, wfuhyo1, wfuhyo2, wfuhyo3,
                wfuhyo4, wfuhyo5, wfuhyo6, wfuhyo7, wfuhyo8,
                wkyosha0, wkyosha1, wkeima0, wkeima1, wginsho0, wginsho1,
                wkinsho0, wkinsho1, wkaku, whisha, wosho], 
              [bfuhyo0, bfuhyo1, bfuhyo2, bfuhyo3,
                bfuhyo4, bfuhyo5, bfuhyo6, bfuhyo7, bfuhyo8,
                bkyosha0, bkyosha1, bkeima0, bkeima1, bginsho0, bginsho1,
                bkinsho0, bkinsho1, bkaku, bhisha, bosho], HEIGHT, WIDTH, DIMENSION)

while running:
    for e in p.event.get():
        if e.type == p.QUIT:
            running = False     

    board.drawGameState(screen, board.name_obj_dict, False, '', 0, None, (8,4))

    clock.tick(MAX_FPS)
    p.display.flip()