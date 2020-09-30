import pygame
import math

def update_fps(a_game):
	fps = str(int(a_game.clock.get_fps()))
	fps_text = a_game.font.render(fps, 1, pygame.Color("yellow"))
	return fps_text

def log_message(a_game, message, color):
    log_text = a_game.font.render(message, 1, pygame.Color(color))
    return log_text

def return_distance(object1, object2):
    #passed objects must have rects
    x1 = object1.rect.x
    x2 = object2.rect.x
    y1 = object1.rect.y
    y2 = object2.rect.y
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def return_angle(object1, object2):
    delta_x = object2.rect.x - object1.rect.x
    delta_y = object2.rect.y - object1.rect.y
    return math.degrees(math.atan2(delta_y, delta_x))
