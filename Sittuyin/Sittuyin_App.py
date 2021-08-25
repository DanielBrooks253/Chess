import pygame as p
from pygame.constants import WINDOWHITTEST

from Pieces import MinGyi, Yahhta, Myin, Ne, SitKe, Sin
from Board import Board

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

black_queen = {}
white_queen = {}

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

# Inititalize all the pieces
# Ne (Pawns or soliders)
wne0 = Ne((5,0), set_up_coord = None, piece_name = 'wn0', piece_image=IMAGES['wn'], set_up_loc = None, color='white')
wne1 = Ne((5,1),  set_up_coord = None, piece_name = 'wn1', piece_image=IMAGES['wn'], set_up_loc = None, color='white')
wne2 = Ne((5,2),  set_up_coord = None, piece_name = 'wn2', piece_image=IMAGES['wn'], set_up_loc = None, color='white')
wne3 = Ne((5,3),  set_up_coord = None, piece_name = 'wn3', piece_image=IMAGES['wn'], set_up_loc = None, color='white')
wne4 = Ne((4,4),  set_up_coord = None, piece_name = 'wn4', piece_image=IMAGES['wn'], set_up_loc = None, color='white')
wne5 = Ne((4,5),  set_up_coord = None, piece_name = 'wn5', piece_image=IMAGES['wn'], set_up_loc = None, color='white')
wne6 = Ne((4,6),  set_up_coord = None, piece_name = 'wn6', piece_image=IMAGES['wn'], set_up_loc = None, color='white')
wne7 = Ne((4,7),  set_up_coord = None, piece_name = 'wn7', piece_image=IMAGES['wn'], set_up_loc = None, color='white')

bne0 = Ne((3,0),  set_up_coord = None, piece_name = 'bn0', piece_image=IMAGES['bn'], set_up_loc = None, color='black')
bne1 = Ne((3,1),  set_up_coord = None, piece_name = 'bn1', piece_image=IMAGES['bn'], set_up_loc = None, color='black')
bne2 = Ne((3,2),  set_up_coord = None, piece_name = 'bn2', piece_image=IMAGES['bn'], set_up_loc = None, color='black')
bne3 = Ne((3,3),  set_up_coord = None, piece_name = 'bn3', piece_image=IMAGES['bn'], set_up_loc = None, color='black')
bne4 = Ne((2,4),  set_up_coord = None, piece_name = 'bn4', piece_image=IMAGES['bn'], set_up_loc = None, color='black')
bne5 = Ne((2,5),  set_up_coord = None, piece_name = 'bn5', piece_image=IMAGES['bn'], set_up_loc = None, color='black')
bne6 = Ne((2,6),  set_up_coord = None, piece_name = 'bn6', piece_image=IMAGES['bn'], set_up_loc = None, color='black')
bne7 = Ne((2,7),  set_up_coord = None, piece_name = 'bn7', piece_image=IMAGES['bn'], set_up_loc = None, color='black')

# The pawns are the only pieces on the board at the start of the game.
# All other pieces are placed by the player at the start

# Yahhta (Rooks)
wyahhta0 = Yahhta(None,  set_up_coord = (0,8), piece_name='wy0', piece_image=IMAGES['wy'], set_up_loc = (HEIGHT+10, 10), color='white')
wyahhta1 = Yahhta(None,  set_up_coord = (1,8), piece_name='wy1', piece_image=IMAGES['wy'], set_up_loc = (HEIGHT+10, SQ_SIZE+10), color='white')

byahhta0 = Yahhta(None,  set_up_coord = (0,8), piece_name='by0', piece_image=IMAGES['by'], set_up_loc = (HEIGHT+10, 10), color='black')
byahhta1 = Yahhta(None,  set_up_coord = (1,8), piece_name='by1', piece_image=IMAGES['by'], set_up_loc = (HEIGHT+10, SQ_SIZE+10), color='black')

# Myin (Horse or knight)
wmyin0 = Myin(None,  set_up_coord = (2,8), piece_name='wm0', piece_image=IMAGES['wm'], set_up_loc = (HEIGHT+10, SQ_SIZE*2+10), color='white')
wmyin1 = Myin(None,  set_up_coord = (3,8), piece_name='wm1', piece_image=IMAGES['wm'], set_up_loc = (HEIGHT+10, SQ_SIZE*3+10), color='white')

bmyin0 = Myin(None,  set_up_coord = (2,8), piece_name='bm0', piece_image=IMAGES['bm'], set_up_loc = (HEIGHT+10, SQ_SIZE*2+10),  color='black')
bmyin1 = Myin(None,  set_up_coord = (3,8), piece_name='bm1', piece_image=IMAGES['bm'], set_up_loc = (HEIGHT+10, SQ_SIZE*3+10), color='black')

# Sin (Bishop)
wsin0 = Sin(None,  set_up_coord = (4,8), piece_name='ws0', piece_image=IMAGES['ws'], set_up_loc = (HEIGHT+10, SQ_SIZE*4+10), color='white')
wsin1 = Sin(None,  set_up_coord = (5,8), piece_name='ws1', piece_image=IMAGES['ws'], set_up_loc = (HEIGHT+10, SQ_SIZE*5+10), color='white')

bsin0 = Sin(None,  set_up_coord = (4,8), piece_name='bs0', piece_image=IMAGES['bs'], set_up_loc = (HEIGHT+10, SQ_SIZE*4+10), color='black')
bsin1 = Sin(None,  set_up_coord = (5,8), piece_name='bs1', piece_image=IMAGES['bs'], set_up_loc = (HEIGHT+10, SQ_SIZE*5+10), color='black')

# Min-Gyi (King)
wMinGyi = MinGyi(None,  set_up_coord = (6,8), piece_name='wM0', piece_image=IMAGES['wM'], set_up_loc = (HEIGHT+10, SQ_SIZE*6+10), color='white')
bMinGyi = MinGyi(None,  set_up_coord = (6,8), piece_name='bM0', piece_image=IMAGES['bM'], set_up_loc = (HEIGHT+10, SQ_SIZE*6+10), color='black')

# Sit-Ke (queen or general)
wSitKe = SitKe(None, set_up_coord = (7,8), piece_name='wS0', piece_image=IMAGES['wS'], set_up_loc = (HEIGHT+10, SQ_SIZE*7+10), color='white')
bSitKe = SitKe(None, set_up_coord = (7,8), piece_name='bS0', piece_image=IMAGES['bS'], set_up_loc = (HEIGHT+10, SQ_SIZE*7+10), color='black')

board = Board([wne0, wne1, wne2, wne3,
               wne4, wne5, wne6, wne7,
               wyahhta0, wyahhta1, wmyin0, wmyin1,
               wsin0, wsin1, wMinGyi, wSitKe],
              [bne0, bne1, bne2, bne3,
               bne4, bne5, bne6, bne7,
               byahhta0, byahhta1, bmyin0, bmyin1,
               bsin0, bsin1, bMinGyi, bSitKe], HEIGHT, WIDTH, DIMENSION)

high_squares = None

# Flags to move the messgae boxes around depending on which turn it is
white_promote = False 
black_promote = False

# Keep track of the number of pawns that had been ask for promotion
white_promotion_count = 0
black_promotion_count = 0

did_pawn_promote_white = False # Check to see if a pawn promotion went through or not
did_pawn_promote_black = False # Check to see if a pawn promotion went through or not

while running:
    if num_turns == 2:
        board.HEIGHT = 512
        board.WIDTH = 512

        screen = p.display.set_mode((board.WIDTH, board.HEIGHT))
        p.display.set_caption('Sittuyin')

        clock = p.time.Clock()
        screen.fill(p.Color('white'))

        board = Board([wne0, wne1, wne2, wne3,
               wne4, wne5, wne6, wne7,
               wyahhta0, wyahhta1, wmyin0, wmyin1,
               wsin0, wsin1, wMinGyi, wSitKe],
              [bne0, bne1, bne2, bne3,
               bne4, bne5, bne6, bne7,
               byahhta0, byahhta1, bmyin0, bmyin1,
               bsin0, bsin1, bMinGyi, bSitKe], 
                    HEIGHT, WIDTH, DIMENSION)

        # Clean up items that are not needed anymore
        del board.white_set_up_locs
        del board.black_set_up_locs

        black_queen = {'bS0': bSitKe.pos}
        white_queen = {'wS0': wSitKe.pos}

        # Check to see if paw can promote
        # if pawn cannot promote continue with logic
        # else promotion equals true and promotion logic ensues

    # Odd turns check for white promote
    if num_turns % 2 == 0 and not did_pawn_promote_white:
        if len(white_queen) == 0:
            white_prom_pawns = [board.name_obj_dict[pawns].piece_name for pawns in  \
                            ['wn0', 'wn1', 'wn2', 'wn3', 'wn4', 'wn5', 'wn6', 'wn7'] \
                            if board.name_obj_dict[pawns].pos in board.promotion_sq_white and \
                                board.name_obj_dict[pawns].promoted == False]
            if len(white_prom_pawns) == 0: # See if any pawns are able to promote
                white_promote = False
            else:
                # For loops do not work while in pygame, so need to index the list instead.
                pawns = white_prom_pawns[white_promotion_count]

                if board.name_obj_dict[pawns].promotion_count == 0 and \
                    board.name_obj_dict[pawns].promoted == False:
                    board.name_obj_dict[pawns].promotion_count += 1
                else:
                    # Change the promotion flag to print out the message box
                    white_promote = True
                    high_squares = board.name_obj_dict[pawns].pos

                    # Get the click event for the message box
                    for e in p.event.get():
                        if e.type == p.QUIT:
                            running = False
                            break

                        if e.type == p.MOUSEBUTTONDOWN:
                            location = p.mouse.get_pos()

                            raw_row = location[0]
                            raw_col = location[1]

                            # Click the yes button
                            if 150 <= raw_row <= 200 and 350 <= raw_col <= 380:
                                board.promotion_selection_white = True
                                high_squares = {}
                                break
                            # Click the no button
                            elif 275 <= raw_row <= 325 and 350 <= raw_col <= 380:
                                board.promotion_selection_white = False
                                high_squares = {}
                                break
                            else:
                                pass
                        else:
                            continue # Look for a click/quit action

                    # If yes is selected, change promotion flag, piece image 
                    # and update the queen dictionary
                    if board.promotion_selection_white:
                        board.name_obj_dict[pawns].Promote_pawn()
                        board.name_obj_dict[pawns].piece_image = IMAGES['wS']
                        white_queen = {pawns: board.white_name_obj_dict[pawns].pos}

                        # Move onto the next turn 
                        white_promote = False
                        did_pawn_promote_white = True
                        board.promotion_selection_white = None
                        num_turns += 1
                        
                    # If no selected, change the did_pawn_promotion flag to True
                    # This will allow white to continue on with their turn as usual
                    elif board.promotion_selection_white == False:
                        if len(white_prom_pawns) == 1:
                            white_promote = False
                            board.promotion_selection_white = None
                            did_pawn_promote_white = True
                            white_promotion_count = 0
                        else:
                            # Once all the pawns have been exhausted, reset all the flags
                            # an continue on with the game
                            if white_promotion_count == (len(white_prom_pawns)-1):
                                white_promote = False
                                did_pawn_promote_white = True
                                board.promotion_selection_white = None
                                white_promotion_count = 0
                                continue
                            else: # add to the index for each pawn
                                board.promotion_selection_white = None
                                white_promotion_count += 1
                    else:
                        pass
                
     
        # white promotion check
        else:
            if board.name_obj_dict[list(white_queen.keys())[0]].pos is None and \
                num_turns > 2:
                white_queen = {}
            else:
                pass

    elif num_turns % 2 != 0 and not did_pawn_promote_black:
        if len(black_queen) == 0:
            black_prom_pawns = [board.name_obj_dict[pawns].piece_name for pawns in  \
                            ['bn0', 'bn1', 'bn2', 'bn3', 'bn4', 'bn5', 'bn6', 'bn7'] \
                            if board.name_obj_dict[pawns].pos in board.promotion_sq_black and \
                                board.name_obj_dict[pawns].promoted == False]
            if len(black_prom_pawns) == 0: # See if any pawns are able to promote
                black_promote = False
            else:
                # For loops do not work while in pygame, so need to index the list instead.
                pawns = black_prom_pawns[black_promotion_count]

                if board.name_obj_dict[pawns].promotion_count == 0 and \
                    board.name_obj_dict[pawns].promoted == False:
                    board.name_obj_dict[pawns].promotion_count += 1
                else:
                    # Change the promotion flag to print out the message box
                    black_promote = True
                    high_squares = board.name_obj_dict[pawns].pos

                    # Get the click event for the message box
                    for e in p.event.get():
                        if e.type == p.QUIT:
                            running = False
                            break

                        if e.type == p.MOUSEBUTTONDOWN:
                            location = p.mouse.get_pos()

                            raw_row = location[0]
                            raw_col = location[1]

                            # Click the yes button
                            if 150 <= raw_row <= 200 and 90 <= raw_col <= 120:
                                board.promotion_selection_black = True
                                high_squares = {}
                                break
                            # Click the no button
                            elif 275 <= raw_row <= 325 and 90 <= raw_col <= 120:
                                board.promotion_selection_black = False
                                high_squares = {}
                                break
                            else:
                                pass
                        else:
                            continue # Look for a click/quit action

                    # If yes is selected, change promotion flag, piece image 
                    # and update the queen dictionary
                    if board.promotion_selection_black:
                        board.name_obj_dict[pawns].Promote_pawn()
                        board.name_obj_dict[pawns].piece_image = IMAGES['bS']
                        black_queen = {pawns: board.black_name_obj_dict[pawns].pos}

                        # Move onto the next turn 
                        black_promote = False
                        did_pawn_promote_black = True
                        board.promotion_selection_black = None
                        num_turns += 1
                        
                    # If no selected, change the did_pawn_promotion flag to True
                    # This will allow black to continue on with their turn as usual
                    elif board.promotion_selection_black == False:
                        if len(black_prom_pawns) == 1:
                            black_promote = False
                            board.promotion_selection_black = None
                            did_pawn_promote_black = True
                            black_promotion_count = 0
                        else:
                            # Once all the pawns have been exhausted, reset all the flags
                            # an continue on with the game
                            if black_promotion_count == (len(black_prom_pawns)-1):
                                black_promote = False
                                did_pawn_promote_black = True
                                board.promotion_selection_black = None
                                black_promotion_count = 0
                                continue
                            else: # add to the index for each pawn
                                board.promotion_selection_black = None
                                black_promotion_count += 1
                    else:
                        pass
                
     
        # black promotion check
        else:
            if board.name_obj_dict[list(black_queen.keys())[0]].pos is None \
                and num_turns > 2:
                black_queen = {}
            else:
                pass
    else:
        pass

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
                    if row < 8 or (col, row) not in board.white_set_up_locs.keys(): # Only click in sidebar 
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
                        # Delete the space from the dictionary so it cannot be selected
                        # for the next iteration

                        del board.white_set_up_locs[player_clicks[0]]

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
                    if row < 8 or (col, row) not in board.black_set_up_locs.keys(): # Only click in sidebar 
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

                        del board.black_set_up_locs[player_clicks[0]]

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
                if not game_over:
                    # First click
                    if len(player_clicks) == 0:
                        # Check to make sure that is is a valid move (piece is on square)
                        # Get available moves
                        # Highlight moves
                        if (col, row) not in board.loc_names.keys():
                            break
                        else:
                            piece_name = board.loc_names[(col, row)]

                            if board.name_obj_dict[piece_name].color == 'white' and  \
                                num_turns % 2 == 0:
                                moves = board.name_obj_dict[piece_name].Available_Moves(
                                    board.x_dim,
                                    board.y_dim,
                                    board.white_piece_loc,
                                    board.black_piece_loc
                                )
                            elif board.name_obj_dict[piece_name].color == 'black' and  \
                                num_turns % 2 != 0:
                                moves = board.name_obj_dict[piece_name].Available_Moves(
                                    board.x_dim,
                                    board.y_dim,
                                    board.black_piece_loc,
                                    board.white_piece_loc
                                )
                            else:
                                # Do not highlight anything if the place they click 
                                # doesn't have any piece or a piece of their color 
                                break
                        
                        if moves is None:
                            player_clicks.append((col, row))
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
                                player_clicks.append((col, row))
                            else:
                                moves = valid_moves.copy()
                                player_clicks.append((col, row))

                            high_squares = {(col, row)} | valid_moves
                    
                    # second click
                    else:
                        if (col, row) in player_clicks:
                            # If the player selects the same square that was previously
                            # selected, deselect the piece.
                            high_squares = None
                            player_clicks = []
                        else:
                            # If the piece has no available moves,
                            # ignore the clicks
                            if moves is None:
                                break
                            # If the second click is in the pieces available
                            # moves. make the move and update everything.
                            elif (col, row) in moves:
                                board.name_obj_dict[piece_name].Make_Move(
                                    (col, row),
                                    board
                                )

                                high_squares = None
                                player_clicks = []
                                
                                # Check to see if the move as resulted in the king being in 
                                # check or not
                                board.name_obj_dict['bM0'].in_check = board.name_obj_dict['bM0'].check_check(
                                    board.white_name_obj_dict,
                                    board.white_piece_loc,
                                    board.black_piece_loc
                                )

                                board.name_obj_dict['wM0'].in_check = board.name_obj_dict['wM0'].check_check(
                                    board.black_name_obj_dict,
                                    board.black_piece_loc,
                                    board.white_piece_loc
                                )

                                if num_turns % 2 == 0:
                                    if board.game_over_check(
                                        board.black_name_obj_dict,
                                        num_turns
                                    ) and bMinGyi.in_check:

                                        text = 'Checkmate!! White Wins'
                                        game_over = True
                                        break

                                    elif board.game_over_check(
                                        board.black_name_obj_dict,
                                        num_turns
                                    ) and not bMinGyi.in_check:

                                        text = 'Stalemate!! Draw Game'
                                        game_over = True
                                        break
                                    else:
                                        pass
                                else:
                                    if board.game_over_check(
                                        board.white_name_obj_dict,
                                        num_turns
                                    ) and wMinGyi.in_check:

                                        text = 'Checkmate!! Black Wins'
                                        game_over = True
                                        break

                                    elif board.game_over_check(
                                        board.white_name_obj_dict,
                                        num_turns
                                    ) and not wMinGyi.in_check:

                                        text = 'Stalemate!! Draw Game'
                                        game_over = True
                                        break
                                    else:
                                        pass

                                num_turns += 1
                                # Change flag back to False to look for promotion again
                                did_pawn_promote_white = False
                                did_pawn_promote_black = False 
                            
                            else:
                                break

    if board.name_obj_dict['wM0'].in_check:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares,
                                board.name_obj_dict['wM0'].pos, num_turns)
        clock.tick(MAX_FPS)
        p.display.flip()

    elif board.name_obj_dict['bM0'].in_check:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares,
                                board.name_obj_dict['bM0'].pos, num_turns)
        clock.tick(MAX_FPS)
        p.display.flip()

    else:
        board.drawGameState(screen, board.name_obj_dict, game_over, text, num, high_squares, None, num_turns, 
                            white_promote, black_promote)
        clock.tick(MAX_FPS)
        p.display.flip()