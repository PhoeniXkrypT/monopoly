
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

def text_objects(msg, fontobj, color='black'):
    color = mglobals.color_map[color]
    text_surf = fontobj.render(msg, True, color)
    return text_surf, text_surf.get_rect()

def message_display(msg, x=mglobals.DISPLAY_W/2, y=mglobals.DISPLAY_H/2, clear_color=None,
                    color='black', fntsize='big'):
    if clear_color:
        mglobals.GD.fill(mglobals.color_map[clear_color])

    textfont = pygame.font.Font('freesansbold.ttf', mglobals.fontsize_map[fntsize])
    text_surf, text_rect = text_objects(msg, textfont, color)
    text_rect.center = (x, y)
    mglobals.GD.blit(text_surf, text_rect)
    pygame.display.update()

def message_display_lines(lines, x=mglobals.DISPLAY_W/2, y=mglobals.DISPLAY_H/2,
                          y_inc=50, color='black', fntsize='big'):
    for line in lines:
        message_display(line, x, y, color=color, fntsize=fntsize)
        y += y_inc

def draw_board():
    mglobals.GD.blit(mglobals.BACK_IMG, (0, 0))
    print type(mglobals.GD)

def clear_p1_info():
    mglobals.P_INFO_CLRSCR.fill(mglobals.color_map['white'])
    mglobals.GD.blit(mglobals.P_INFO_CLRSCR, (808, 0))

def clear_p2_info():
    mglobals.P_INFO_CLRSCR.fill(mglobals.color_map['white'])
    mglobals.GD.blit(mglobals.P_INFO_CLRSCR, (808, 390))

def draw_player_menu(ocolor1, ocolor2):
    mglobals.GD.fill(mglobals.WHITE)
    message_display("Monopoly !!!")
    message_display("PvP", x=(mglobals.DISPLAY_W/2)-100,
                           y=(mglobals.DISPLAY_H/2)+100,
                           color=ocolor1)
    message_display("PvAI", x=(mglobals.DISPLAY_W/2)+100,
                            y=(mglobals.DISPLAY_H/2)+100,
                            color=ocolor2)


