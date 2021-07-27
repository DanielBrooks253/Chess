import pygame as p

class Board:

    def __init__(self, white_pieces, black_pieces, height, width, dimension, y_dim=8, x_dim=8):
        # get all of the location of the white and black pieces
        self.black_piece_loc = set([i.pos for i in black_pieces])
        self.white_piece_loc = set([i.pos for i in white_pieces])

        # map the setup locations to their respective objects
        self.white_set_up_locs = {i.set_up_coord:i for i in white_pieces}
        self.black_set_up_locs = {i.set_up_coord:i for i in black_pieces}

        # Dictionary that takes the piece name and maps it to the object
        # One for each color and an overall dictionary
        self.white_name_obj_dict = {i.piece_name:i for i in white_pieces}
        self.black_name_obj_dict = {i.piece_name:i for i in black_pieces}

        self.loc_names = {i.pos:i.piece_name for i in white_pieces + black_pieces}
        self.name_obj_dict = {i.piece_name:i for i in white_pieces + black_pieces}

        # Dimensions of the chess board
        self.y_dim=y_dim
        self.x_dim=x_dim

        self.HEIGHT = height
        self.WIDTH = width
        self.SQ_SIZE = (width-68) //dimension

        # Promotion squares for the ne (pawns)
        self.promotion_sq_white = ((0,0), (1,1), (2,2), (3,3), (7,0), (6,1), (5,2), (4,3))
        self.promotion_sq_black = ((4,4), (5,5), (6,6), (7,7), (3,4), (2,5), (1,6), (0,7))

    def drawGameState(self, screen, names_obj, game_over, text, num, *args):
        if game_over:
            Board.drawBoard(self, screen, args) # Draw board first so pieces do not get overwritten
            # Board.drawPieces(self, screen, names_obj)
            # Board.drawText(self, screen, text, num)
        else:
            Board.drawBoard(self, screen, args) # Draw board first so pieces do not get overwritten
            Board.drawPieces(self, screen, names_obj, args)

    def drawBoard(self, screen, args):
        # Red check; darkolivegreen moves
        # Draw the tiles on the board
        for r in range(self.x_dim):
            for c in range(self.y_dim):
                p.draw.rect(screen, p.Color('wheat1'), 
                   p.Rect(r*self.SQ_SIZE, c*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
                p.draw.rect(screen, p.Color('black'),
                   p.Rect((r*self.SQ_SIZE-1), (c*self.SQ_SIZE-1), 
                           (self.SQ_SIZE+1), (self.SQ_SIZE+1)),1)
        
        p.draw.line(screen, p.Color('black'), (0 ,0), (512, 512))
        p.draw.line(screen, p.Color('black'), (0, 512), (512, 0))

        p.draw.rect(screen, p.Color('wheat1'), p.Rect(512, 0, 68, 512))
        p.draw.rect(screen, p.Color('black'), p.Rect(512, 0, 68, 512),1)

        # Check to see if a place has been clicked 
        # Highlight the space and the pieces moves in grey
        if args[0] is not None:
            if type(args[0]) is tuple: 
                if args[0] in self.loc_names.keys() or args[0] in self.white_set_up_locs or args[0] in self.black_set_up_locs:
                    p.draw.rect(screen, p.Color('darkolivegreen'), 
                        p.Rect(args[0][1]*self.SQ_SIZE, args[0][0]*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
                    p.draw.rect(screen, p.Color('black'),
                        p.Rect((args[0][1]*self.SQ_SIZE-1), (args[0][0]*self.SQ_SIZE-1), 
                                (self.SQ_SIZE+1), (self.SQ_SIZE+1)),1)
            else:
                for i in args[0]:
                    p.draw.rect(screen, p.Color('darkolivegreen'), 
                       p.Rect(i[1]*self.SQ_SIZE, i[0]*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
                    p.draw.rect(screen, p.Color('black'),
                       p.Rect((i[1]*self.SQ_SIZE-1), (i[0]*self.SQ_SIZE-1), 
                               (self.SQ_SIZE+1), (self.SQ_SIZE+1)),1)
        if args[1] is not None:
            p.draw.rect(screen, p.Color('red'), 
                        p.Rect(args[1][1]*self.SQ_SIZE, args[1][0]*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
            p.draw.rect(screen, p.Color('black'),
                        p.Rect((args[1][1]*self.SQ_SIZE-1), (args[1][0]*self.SQ_SIZE-1), 
                           (self.SQ_SIZE+1), (self.SQ_SIZE+1)),1)

    def drawPieces(self, screen, names_obj, args):
        # Draw the pieces on the board
        # x and y axis are flipped when drawing the pieces
        for piece in names_obj.values():
            if piece.pos is None:
                if args[2] == 0:
                    if piece.color == 'white':
                        screen.blit(piece.piece_image,
                            p.Rect(piece.set_up_loc[0], piece.set_up_loc[1], self.SQ_SIZE, self.SQ_SIZE))
                elif args[2] == 1:
                    if piece.color == 'black':
                        screen.blit(piece.piece_image,
                             p.Rect(piece.set_up_loc[0], piece.set_up_loc[1], self.SQ_SIZE, self.SQ_SIZE))
                else:
                    pass
            else:
                screen.blit(piece.piece_image, 
                        p.Rect(piece.pos[1]*self.SQ_SIZE+8, piece.pos[0]*self.SQ_SIZE+8, 
                            self.SQ_SIZE, self.SQ_SIZE))