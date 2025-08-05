import pygame

pygame.mixer.init()

def play_sleep_alert():
    pygame.mixer.music.load("sleep_alert.mp3")
    pygame.mixer.music.play()

def play_yawn_alert():
    pygame.mixer.music.load("yawn_alert.mp3")
    pygame.mixer.music.play()
