import pygame as p

class Board:
    '''
        Class to define the chess board
    '''
    def __init__(self, white_pieces, black_pieces, height, width, dimension, y_dim=9, x_dim=9):
        '''
        Initializes the Board class

        :param white_pieces (list): list of objects that belong to the white pieces 
        :param black_pieces (list): list of objects that belong to the black pieces
        :param height (int): The height of the pygame window
        :param width (int): The width of the pygame window
        :param dimension (int): the size of the squares for the chess board

        :param y_dim (int): the number of squares in the y direction (up/down)
            :default value: 8
        :param x_dim (int): the number of squares in the x direction (left/right) 
            :default value: 8

        :return: Null (Nothing)
        '''
        # get all of the location of the white and black pieces
        self.black_piece_loc = set([i.pos for i in black_pieces])
        self.white_piece_loc = set([i.pos for i in white_pieces])

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
        self.SQ_SIZE = height //dimension

    def drawGameState(self, screen, names_obj, game_over, text, num, *args):
        '''
        Responsible for drawing the game board, pieces and end of game text

        :param screen (pygame obj): Pygame game object that houses all of the "drawings" and images
            rendered for the chess game (Basically the pygame window and board)
        :param name_obj (dict): all of the piece objects that are on the board
            :key piece_name
            :value class associated with the piece
        :param game_over (Bool): Flag to determine if the game is over or not
            :True draw the end if game text
            : False draw the game baord and pieces
        :param text (str): The text to display after the game is over
        :param num (int): The size of the font to display the text

        :param args (list): THis is the catch all parameter. This is used to color the square for
            the king in red and highlught the available moves for the pieces. 
            :args[0]: 
                list of available moves for the piece
            :args[1]:
                None if king is not in check
                king pos if the king is in check

        return: Null (Nothing)
        '''
        if game_over:
            Board.drawBoard(self, screen, args) # Draw board first so pieces do not get overwritten
            Board.drawPieces(self, screen, names_obj)
            Board.drawText(self, screen, text, num)
        else:
            Board.drawBoard(self, screen, args) # Draw board first so pieces do not get overwritten
            Board.drawPieces(self, screen, names_obj)

    def drawBoard(self, screen, args):
        # Red check; darkolivegreen moves
        # Draw the tiles on the board
        colors = [p.Color("wheat1"), p.Color("darkkhaki")]

        for r in range(self.x_dim):
            for c in range(self.y_dim):
                p.draw.rect(screen, 'wheat1', 
                   p.Rect(r*self.SQ_SIZE, c*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
                p.draw.rect(screen, p.Color('black'),
                   p.Rect((r*self.SQ_SIZE-1), (c*self.SQ_SIZE-1), 
                           (self.SQ_SIZE+1), (self.SQ_SIZE+1)),1)

        # Check to see if a place has been clicked 
        # Highlight the space and the pieces moves in grey
        if args[0] is not None:
            if type(args[0]) is tuple: 
                if args[0] in self.loc_names.keys():
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

    def drawPieces(self, screen, names_obj):
        '''
        Responsible for drawing the piece images of the board

        :param screen (pygame obj): Pygame game object that houses all of the "drawings" and images
            rendered for the chess game (Basically the pygame window and board)
        :param name_obj (dict): all of the piece objects that are on the board
            :key piece_name
            :value class associated with the piece

        :return Null (Nothing)
        '''
        # Draw the pieces on the board
        # x and y axis are flipped when drawing the pieces
        for piece in names_obj.values():
            if piece.pos is None:
                continue
            else:
                screen.blit(piece.piece_image, 
                    p.Rect(piece.pos[1]*self.SQ_SIZE+8, piece.pos[0]*self.SQ_SIZE+8, 
                            self.SQ_SIZE, self.SQ_SIZE))
                
    def drawText(self, screen, text, num):
        '''
        Responsible for drawing the end of the game text across the screen

        :param screen (pygame obj): Pygame game object that houses all of the "drawings" and images
            rendered for the chess game (Basically the pygame window and board)
        :param text (str): The text that will show once the game is over
        :param num (int): The size of the font to show on the screen

        :return Null (Nothing)
        '''
        # Draw the text at the end of the game
        p.font.init()

        if num == 1:
            size = 32
        else:
            size = 22


        font = p.font.SysFont('Comic Sans MS', size, True, False)
        textObject = font.render(text, 0, p.Color('white'))
        textLocation = p.Rect(0,0, self.WIDTH, self.HEIGHT) \
                        .move(self.WIDTH//2-textObject.get_width()//2, 
                              self.HEIGHT//2-textObject.get_height()//2)
        screen.blit(textObject, textLocation)
        textObject = font.render(text, 0, p.Color('gray2'))
        screen.blit(textObject, textLocation.move(2,2))