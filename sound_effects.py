import pygame

def play_correct_sound():
    pygame.mixer.Sound("sounds/correct.wav").play()

def play_wrong_sound():
    pygame.mixer.Sound("sounds/wrong.wav").play()
