import pygame

pygame.init() #iniciar programa
pygame.mixer.music.load('volibear-morrendo.mp3') #acrecentar audio
pygame.mixer.music.play() #dar play
pygame.mixer.wait() #esperar a música tocar até o final