
import pygame

import mglobals

def draw_vertical_line(x):
    pygame.draw.line(mglobals.GD, mglobals.BLACK, (x, 0), (x, 1000))

def draw_horizontal_line(y):
    pygame.draw.line(mglobals.GD, mglobals.BLACK, (0, y), (1000, y))

def draw_debug_lines():
    for i in xrange(0, 1000, 100):
        draw_vertical_line(i)
        draw_horizontal_line(i)

def text_objects(msg, fontobj, color=None):
    if not color:
        color = mglobals.BLACK
    text_surf = fontobj.render(msg, True, color)
    return text_surf, text_surf.get_rect()

def message_display(msg, x=mglobals.DISPLAY_W/2, y=mglobals.DISPLAY_H/2, clear_color=None):
    if clear_color:
        mglobals.GD.fill(clear_color)
    large_text = pygame.font.Font('freesansbold.ttf', 50)
    text_surf, text_rect = text_objects(msg, large_text)
    text_rect.center = (x, y)
    mglobals.GD.blit(text_surf, text_rect)
    pygame.display.update()

def message_display_lines(lines, x=mglobals.DISPLAY_W/2, y=mglobals.DISPLAY_H/2):
    for line in lines:
        message_display(line, x, y)
        y += 50

def draw_background():
    mglobals.GD.fill(mglobals.WHITE)
    mglobals.GD.blit(mglobals.BACK_IMG, (0, 0))


