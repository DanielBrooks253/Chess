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

num_turns = 0
num = 1
game_over = False
all_pieces_captured_turns = []
text = ''

# Get all of the images loaded for the given pieces
for pieces in [('wp', 'pawn-w1'), ('wr', 'rukh-w1'), ('wa', 'knight-w1'),
               ('we', 'elephant-w1'), ('wS', 'shah-w1'), ('wF', 'firzan-w1'),
               ('bp', 'pawn-b1'), ('br', 'rukh-b1'), ('ba', 'knight-b1'),
               ('be', 'elephant-b1'), ('bS', 'shah-b1'), ('bF', 'firzan-b1')]:
            IMAGES[pieces[0]] = p.transform.scale(p.image.load("Images/" + pieces[1] + ".jpg"), (int(SQ_SIZE*PCT_SHRINK), int(SQ_SIZE*PCT_SHRINK)))

# Pygame initializations
screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Shatranj')

clock = p.time.Clock()
screen.fill(p.Color('white'))
running = True

# sq_selected = () # no sqaure that is selected (row, col)
player_Clicks = [] # keep track of the number of clicks the user does

# Initialize all of the pieces on the board
# Pujada (Pawns)
wpujada0 = Pujada((6,0), piece_name='wp0', piece_image = IMAGES['wp'], IMAGES = IMAGES, color='white')
wpujada1 = Pujada((6,1), piece_name='wp1', piece_image = IMAGES['wp'], IMAGES = IMAGES, color='white')
wpujada2 = Pujada((6,2), piece_name='wp2', piece_image = IMAGES['wp'], IMAGES = IMAGES, color='white')
wpujada3 = Pujada((6,3), piece_name='wp3', piece_image = IMAGES['wp'], IMAGES = IMAGES, color='white')
wpujada4 = Pujada((6,4), piece_name='wp4', piece_image = IMAGES['wp'], IMAGES = IMAGES, color='white')
wpujada5 = Pujada((6,5), piece_name='wp5', piece_image = IMAGES['wp'], IMAGES = IMAGES, color='white')
wpujada6 = Pujada((6,6), piece_name='wp6', piece_image = IMAGES['wp'], IMAGES = IMAGES, color='white')
wpujada7 = Pujada((6,7), piece_name='wp7', piece_image = IMAGES['wp'], IMAGES = IMAGES, color='white')

bpujada0 = Pujada((1,0), piece_name='bp0', piece_image = IMAGES['bp'], IMAGES = IMAGES, color='black')
bpujada1 = Pujada((1,1), piece_name='bp1', piece_image = IMAGES['bp'], IMAGES = IMAGES, color='black')
bpujada2 = Pujada((1,2), piece_name='bp2', piece_image = IMAGES['bp'], IMAGES = IMAGES, color='black')
bpujada3 = Pujada((1,3), piece_name='bp3', piece_image = IMAGES['bp'], IMAGES = IMAGES, color='black')
bpujada4 = Pujada((1,4), piece_name='bp4', piece_image = IMAGES['bp'], IMAGES = IMAGES, color='black')
bpujada5 = Pujada((1,5), piece_name='bp5', piece_image = IMAGES['bp'], IMAGES = IMAGES, color='black')
bpujada6 = Pujada((1,6), piece_name='bp6', piece_image = IMAGES['bp'], IMAGES = IMAGES, color='black')
bpujada7 = Pujada((1,7), piece_name='bp7', piece_image = IMAGES['bp'], IMAGES = IMAGES, color='black')

# Rukh (Rooks)
wrukh0 = Rukh((7,0), piece_name='wr0', piece_image = IMAGES['wr'], IMAGES = IMAGES, color='white')
wrukh1 = Rukh((7,7), piece_name='wr1', piece_image = IMAGES['wr'], IMAGES = IMAGES, color='white')

brukh0 = Rukh((0,0), piece_name='br0', piece_image = IMAGES['br'], IMAGES = IMAGES, color='black')
brukh1 = Rukh((0,7), piece_name='br1', piece_image = IMAGES['br'], IMAGES = IMAGES, color='black')

# Asp (Horses)
wasp0 = Asp((7,1), piece_name='wa0', piece_image = IMAGES['wa'], IMAGES = IMAGES, color='white')
wasp1 = Asp((7,6), piece_name='wa1', piece_image = IMAGES['wa'], IMAGES = IMAGES, color='white')

basp0 = Asp((0,1), piece_name='ba0', piece_image = IMAGES['ba'], IMAGES = IMAGES, color='black')
basp1 = Asp((0,6), piece_name='ba1', piece_image = IMAGES['ba'], IMAGES = IMAGES, color='black')

# Pil (Elephants)
welephant0 = Pil((7,2), piece_name='we0', piece_image = IMAGES['we'], IMAGES = IMAGES, color='white')
welephant1 = Pil((7,5), piece_name='we1', piece_image = IMAGES['we'], IMAGES = IMAGES, color='white')

belephant0 = Pil((0,2), piece_name='be0', piece_image = IMAGES['be'], IMAGES = IMAGES, color='black')
belephant1 = Pil((0,5), piece_name='be1', piece_image = IMAGES['be'], IMAGES = IMAGES, color='black')

# Shah (King) and Farzin (Queen)
wShah = Shah((7,3), piece_name='wS0', piece_image = IMAGES['wS'], IMAGES = IMAGES, color='white')
wFarzin = Farzin((7,4), piece_name='wF0', piece_image = IMAGES['wF'], IMAGES = IMAGES, color='white')

bShah = Shah((0,3), piece_name='bS0', piece_image = IMAGES['bS'], IMAGES = IMAGES, color='black')
bFarzin = Farzin((0,4), piece_name='bF0', piece_image = IMAGES['bF'], IMAGES = IMAGES, color='black')

# Set the pieces on the board for the start of the match
board = Board([wpujada0, wpujada1, wpujada2, wpujada3,
                wpujada4, wpujada5, wpujada6, wpujada7,
                wrukh0, wrukh1, wasp0, wasp1,
                welephant0, welephant1, wShah, wFarzin], 
              [bpujada0, bpujada1, bpujada2, bpujada3,
                bpujada4, bpujada5, bpujada6, bpujada7,
                brukh0, brukh1, basp0, basp1,
                belephant0, belephant1, bShah, bFarzin], HEIGHT, WIDTH, DIMENSION)

high_squares = None
while running:
    for e in p.event.get():
        if e.type == p.QUIT:
            running = False
        if not game_over:
            if e.type == p.MOUSEBUTTONDOWN: # code 1025
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
                        piece_name = board.loc_names[(col, row)]

                        # Get the available moves for the given color
                        if board.name_obj_dict[piece_name].color == 'white' and \
                        num_turns % 2 == 0:
                            moves = board.name_obj_dict[piece_name].Available_Moves(
                                board.x_dim,
                                board.y_dim,
                                board.white_piece_loc,
                                board.black_piece_loc
                            )
                        elif board.name_obj_dict[piece_name].color == 'black' and \
                    num_turns % 2 != 0:
                            moves = board.name_obj_dict[piece_name].Available_Moves(
                                board.x_dim,
                                board.y_dim,
                                board.black_piece_loc,
                                board.white_piece_loc
                            )
                        # Do not highlight anything if the place they click 
                        # doesn't have any piece or a piece of their color
                        else: 
                            break
                    
                    if moves is None:
                        player_Clicks.append((col, row))
                        high_squares = ((col, row))
                    else:
                        invalid_moves = board.name_obj_dict[piece_name].avail_move_check_check(
                                    moves, board)
                        # Removes all the moves that will not get you out
                        # of check
                        valid_moves = moves - invalid_moves
                        # If there are no valid moves, return none
                        if len(valid_moves) == 0:
                            moves = None
                            player_Clicks.append((col, row))
                        else:
                            moves = valid_moves.copy()
                            player_Clicks.append((col, row))

                        high_squares = {(col, row)} | valid_moves

                # If second click
                else:
                    # Check if the player clicked the sames square or not
                    # Unselect the piece
                    if (col, row) in player_Clicks:
                        high_squares = None
                        player_Clicks = []
                    else:
                        # If the piece has no available moves,
                        # ingore the clicks
                        if moves is None:
                            break
                        # If the second click is in the pieces available
                        # moves, make the move and update everything
                        elif (col,row) in moves:
                            board.name_obj_dict[piece_name].Make_Move(
                                (col, row),
                                board)

                            high_squares = None
                            player_Clicks = []

                            board.name_obj_dict['bS0'].in_check = board.name_obj_dict['bS0'].check_check(
                                board.white_name_obj_dict,
                                board.white_piece_loc,
                                board.black_piece_loc
                            )

                            board.name_obj_dict['wS0'].in_check = board.name_obj_dict['wS0'].check_check(
                                board.black_name_obj_dict,
                                board.black_piece_loc,
                                board.white_piece_loc
                            )

                            if num_turns % 2 == 0:
                                if board.game_over_chkmt_stlmt_check(
                                    board.black_name_obj_dict,
                                    num_turns
                                ) and bShah.in_check:

                                    text = 'Checkmate!! White Wins'
                                    game_over = True
                                    break

                                elif board.game_over_chkmt_stlmt_check(
                                    board.black_name_obj_dict,
                                    num_turns
                                ) and not bShah.in_check:

                                    text = 'Stalemate!! White Wins'
                                    game_over = True
                                    break
                                else:
                                    all_pieces_captured_turns.append(
                                board.game_over_lose_pieces(board.black_name_obj_dict)
                            )

                            else:
                                if board.game_over_chkmt_stlmt_check(
                                    board.white_name_obj_dict,
                                    num_turns
                                ) and wShah.in_check:

                                    text = '!! Checkmate Black Wins !!'
                                    game_over = True
                                    break

                                elif board.game_over_chkmt_stlmt_check(
                                    board.white_name_obj_dict,
                                    num_turns
                                ) and not wShah.in_check:

                                    text = '!! Stalemate Black Wins !!'
                                    game_over=True
                                    break
                                else:
                                    all_pieces_captured_turns.append(
                                board.game_over_lose_pieces(board.white_name_obj_dict)
                            )

                            if len(all_pieces_captured_turns) == 2 and \
                                sum(all_pieces_captured_turns) == 2:

                                text = "!! The Game Ends in a Draw !!"
                                game_over = True
                                break

                            elif len(all_pieces_captured_turns) == 2 and \
                                all_pieces_captured_turns[0] and \
                                num_turns % 2 == 0:
                                text = '!! Black Wins by Capturing all Whites Pieces !!'
                                num = 2
                                game_over = True
                                break

                            elif len(all_pieces_captured_turns) == 2 and \
                                all_pieces_captured_turns[0] and \
                                num_turns % 2 != 0:
                                text = '!! White Wins by Capturing all Blacks Pieces !!'
                                num = 2
                                game_over = True
                                break

                            elif all_pieces_captured_turns[0] == 0:
                                all_pieces_captured_turns = []
                            else:
                                pass
                            
                            num_turns +=1
                            
                        else:
                            break

    # Print out the gamestate of the board, depending on if the game
    # is eneded or not.
    if game_over:
        if board.name_obj_dict['wS0'].in_check:
            board.drawGameState(screen, board.name_obj_dict, True, text, num, high_squares,
                                board.name_obj_dict['wS0'].pos)
            clock.tick(MAX_FPS)
            p.display.flip()
        elif board.name_obj_dict['bS0'].in_check:
            board.drawGameState(screen, board.name_obj_dict, True, text, num, high_squares,
                                board.name_obj_dict['bS0'].pos)
            clock.tick(MAX_FPS)
            p.display.flip()
        else:
            board.drawGameState(screen, board.name_obj_dict, True, text, num, high_squares,
                                None)
            clock.tick(MAX_FPS)
            p.display.flip()
    else:
        if board.name_obj_dict['wS0'].in_check:
            board.drawGameState(screen, board.name_obj_dict, False, '', num, high_squares,
                                board.name_obj_dict['wS0'].pos)
            clock.tick(MAX_FPS)
            p.display.flip()

        elif board.name_obj_dict['bS0'].in_check:
            board.drawGameState(screen, board.name_obj_dict, False, '', num, high_squares,
                                board.name_obj_dict['bS0'].pos)
            clock.tick(MAX_FPS)
            p.display.flip()
        else:
            board.drawGameState(screen, board.name_obj_dict, False, '', num, high_squares, None)
            clock.tick(MAX_FPS)
            p.display.flip()


