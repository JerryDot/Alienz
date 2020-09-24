import pygame

def update_fps(a_game):
	fps = str(int(a_game.clock.get_fps()))
	fps_text = a_game.font.render(fps, 1, pygame.Color("yellow"))
	return fps_text

def log_message(a_game, message, color):
    log_text = a_game.font.render(message, 1, pygame.Color(color))
    return log_text
