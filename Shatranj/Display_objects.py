import pygame as p

class MessageBox:
    def __init__(self, window_rect, fonts, message):
        self.window_rect = window_rect
        self.fonts = fonts
        self.background_color = p.Color('gray')
        self.text_color = p.Color('black')

        self.window_title_str = '!! Game Over !!'
        self.title_text_render = self.fonts[1].render(self.window_title_str, 
                                                      True, self.text_color)