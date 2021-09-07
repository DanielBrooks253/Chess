import pygame as p

from Board import Board
from Pieces import Chuh, Ma, JiangShuai, Shi, Shiang, Pao, PingTsuh

p.init()

WIDTH = 576
HEIGHT = 576
DIMENSION = 9
MAX_FPS = 15
SQ_SIZE = HEIGHT//DIMENSION
PCT_SHRINK = .75

IMAGES = {}

num_turns = 0
game_over = False
text = ''
num = 1

for pieces in [('wpt', 'White-Solider'), ('wc', 'White-Chariot'), ('wm', 'White-Horse'), ('wJ', 'White-King'),
               ('wS', 'White-Advisor'), ('ws', 'White-Elephant'), ('wp', 'White-Cannon'), ('bpt', 'Black-Solider'), 
               ('bc', 'Black-Chariot'), ('bm', 'Black-Horse'), ('bJ', 'Black-King'),
               ('bS', 'Black-Advisor'), ('bs', 'Black-Elephant'), ('bp', 'Black-Cannon')]:
   IMAGES[pieces[0]] = p.transform.scale(p.image.load("Images/" + pieces[1] + ".jpg"), (int(SQ_SIZE*PCT_SHRINK), int(SQ_SIZE*PCT_SHRINK))) 

screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Xiangqi')

clock = p.time.Clock()
screen.fill(p.Color('white'))
running = True
player_clicks = []

wpingtshuh0 = PingTsuh((5,0), piece_name = 'wpt0', piece_image = IMAGES['wpt'], color = 'white')
wpingtshuh1 = PingTsuh((5,2), piece_name = 'wpt1', piece_image = IMAGES['wpt'], color = 'white')
wpingtshuh2 = PingTsuh((5,4), piece_name = 'wpt2', piece_image = IMAGES['wpt'], color = 'white')
wpingtshuh3 = PingTsuh((5,6), piece_name = 'wpt3', piece_image = IMAGES['wpt'], color = 'white')
wpingtshuh4 = PingTsuh((5,8), piece_name = 'wpt4', piece_image = IMAGES['wpt'], color = 'white')

bpingtshuh0 = PingTsuh((3,0), piece_name = 'bpt0', piece_image = IMAGES['bpt'], color = 'black')
bpingtshuh1 = PingTsuh((3,2), piece_name = 'bpt1', piece_image = IMAGES['bpt'], color = 'black')
bpingtshuh2 = PingTsuh((3,4), piece_name = 'bpt2', piece_image = IMAGES['bpt'], color = 'black')
bpingtshuh3 = PingTsuh((3,6), piece_name = 'bpt3', piece_image = IMAGES['bpt'], color = 'black')
bpingtshuh4 = PingTsuh((3,8), piece_name = 'bpt4', piece_image = IMAGES['bpt'], color = 'black')

wpao0 = Pao((6, 1), piece_name = 'wp0', piece_image = IMAGES['wp'], color = 'white')
wpao1 = Pao((6, 7), piece_name = 'wp1', piece_image = IMAGES['wp'], color = 'white')

bpao0 = Pao((2, 1), piece_name = 'bp0', piece_image = IMAGES['bp'], color = 'black')
bpao1 = Pao((2, 7), piece_name = 'bp1', piece_image = IMAGES['bp'], color = 'black')

wchuh0 = Chuh((8, 0), piece_name = 'wc0', piece_image = IMAGES['wc'], color = 'white')
wchuh1 = Chuh((8, 8), piece_name = 'wc1', piece_image = IMAGES['wc'], color = 'white')

bchuh0 = Chuh((0, 0), piece_name = 'bc0', piece_image = IMAGES['bc'], color = 'black')
bchuh1 = Chuh((0, 8), piece_name = 'bc1', piece_image = IMAGES['bc'], color = 'black')

wma0 = Ma((8, 1), piece_name = 'wm0', piece_image = IMAGES['wm'], color = 'white')
wma1 = Ma((8, 7), piece_name = 'wm1', piece_image = IMAGES['wm'], color = 'white')

bma0 = Ma((0, 1), piece_name = 'bm0', piece_image = IMAGES['bm'], color = 'black')
bma1 = Ma((0, 7), piece_name = 'bm1', piece_image = IMAGES['bm'], color = 'black')

wshiang0 = Shiang((8,2), piece_name = 'ws0', piece_image = IMAGES['ws'], color = 'white')
wshiang1 = Shiang((8,6), piece_name = 'ws1', piece_image = IMAGES['ws'], color = 'white')

bshiang0 = Shiang((0,2), piece_name = 'bs0', piece_image = IMAGES['bs'], color = 'black')
bshiang1 = Shiang((0,6), piece_name = 'bs1', piece_image = IMAGES['bs'], color = 'black')

wshi0 = Shi((8,3), piece_name = 'wS0', piece_image = IMAGES['wS'], color = 'white')
wshi1 = Shi((8,5), piece_name = 'wS1', piece_image = IMAGES['wS'], color = 'white')

bshi0 = Shi((0,3), piece_name = 'bS0', piece_image = IMAGES['bS'], color = 'black')
bshi1 = Shi((0,5), piece_name = 'bS1', piece_image = IMAGES['bS'], color = 'black')

wjiangshuai = JiangShuai((8,4), piece_name = 'wJ', piece_image = IMAGES['wJ'], color = 'white')
bjiangshuai = JiangShuai((0,4), piece_name = 'bJ', piece_image = IMAGES['bJ'], color = 'black')

board = Board([wpingtshuh0,wpingtshuh1,wpingtshuh2,wpingtshuh3,wpingtshuh4,
               wchuh0,wchuh1,wma0,wma1,wshi0,wshi1,
               wshiang0,wshiang1,wpao0,wpao1,wjiangshuai], 
              [bpingtshuh0,bpingtshuh1,bpingtshuh2,bpingtshuh3,bpingtshuh4,
               bchuh0,bchuh1,bma0,bma1,bshi0,bshi1,
               bshiang0,bshiang1,bpao0,bpao1,bjiangshuai],
              HEIGHT,WIDTH,DIMENSION)

high_squares = None
while running:
    pass