import pygame as p

from Board import Board
from Pieces import Shah, Pil, Rukh, Asp, Pujada, Farzin

p.init()
WIDTH = HEIGHT = 512
DIMENSION = 8
MAX_FPS = 15
SQ_SIZE = HEIGHT//DIMENSION
PCT_SHRINK = .75

IMAGES = {} 

turn = 'white'
legal_moves=False
checkmate=False
stalemate=False

# Get all of the images loaded for the given pieces
for pieces in [('wp', 'pawn-w1'), ('wr', 'chariot-w1'), ('wa', 'knight-w1'),
               ('we', 'elephant-w1'), ('wS', 'king-w1'), ('wF', 'queen-w1'),
               ('bp', 'pawn-b1'), ('br', 'chariot-b1'), ('ba', 'knight-b1'),
               ('be', 'elephant-b1'), ('bS', 'king-b1'), ('bF', 'queen-b1')]:
            IMAGES[pieces[0]] = p.transform.scale(p.image.load("Images/" + pieces[1] + ".jpg"), (int(SQ_SIZE*PCT_SHRINK), int(SQ_SIZE*PCT_SHRINK)))

# Pygame initializations
screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Shatranj')

clock = p.time.Clock()
screen.fill(p.Color('white'))
running = True

sq_selected = () # no sqaure that is selected (row, col)
player_Clicks = [] # keep track of the number of clicks the user does

# Initialize all of the pieces on the board
# Pujada (Pawns)
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

high_squares = None
while running:
    for e in p.event.get():
        if e.type == p.QUIT:
            running = False
        elif e.type == p.MOUSEBUTTONDOWN: # code 1025
            location = p.mouse.get_pos() #(x, y) location of mouse
            row = location[0]//SQ_SIZE
            col = location[1]//SQ_SIZE

            # If first click
            if len(player_Clicks) == 0:
                # Check to make sure that is is a valid move (piece is on square)
                # Get available moves
                # Highlight moves

                if (col, row) not in board.loc_names.keys():
                    break
                else:
                    player_Clicks.append((col, row))
                    piece_name = board.loc_names[(col, row)]

                    if board.name_obj_dict[piece_name].color == 'white' and \
                    turn == 'white':
                        moves = board.name_obj_dict[piece_name].Available_Moves(
                            board.x_dim,
                            board.y_dim,
                            board.white_piece_loc,
                            board.black_piece_loc
                        )
                    elif board.name_obj_dict[piece_name].color == 'black' and \
                turn == 'black':
                        moves = board.name_obj_dict[piece_name].Available_Moves(
                            board.x_dim,
                            board.y_dim,
                            board.black_piece_loc,
                            board.white_piece_loc
                        )
                    else:
                        break
                
                if moves is None:
                    high_squares = ((col, row))
                else:
                    high_squares = {(col, row)} | moves

            # If second click
            else:
                pass
                # Check to see if click on in available moves
                # CHeck to see if click is the same position as before
                # Make the move
                # reset click list
            
            # Check if location has a piece on it 
            # if (col,row) not in board.loc_names.keys():
            #     break
            # else:
            #     # Gets the object name
            #     piece_name = board.loc_names[(col, row)]

            #     # Gets moves for the white and black pieces when it is their turn
            #     if board.name_obj_dict[piece_name].color == 'white' and \
            #     turn == 'white':
            #         moves = board.name_obj_dict[piece_name].Available_Moves(
            #             board.x_dim,
            #             board.y_dim,
            #             board.white_piece_loc,
            #             board.black_piece_loc
            #         )

            #         player_Clicks.append((col, row))

            #     elif board.name_obj_dict[piece_name].color == 'black' and \
            #     turn == 'black':
            #         moves = board.name_obj_dict[piece_name].Available_Moves(
            #             board.x_dim,
            #             board.y_dim,
            #             board.black_piece_loc,
            #             board.white_piece_loc
            #         )
            #         player_Clicks.append((col, row))
            #     else:
            #         break

            # if moves is None:
            #     if len(player_Clicks) < 2:
            #         high_squares = ((col, row))
            #     else:
            #         high_squares = None
            # else:
            #     if len(player_Clicks) < 2:
            #         high_squares = {(col, row)} | moves
            #     else:
            #         high_squares = None

    # Draw the pieces and tiles on the board
    board.drawGameState(screen, board.name_obj_dict, high_squares, False)
    clock.tick(MAX_FPS)
    p.display.flip()

    player_Clicks = []


