import pygame

# Testing
pygame.mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)') # NO! it sounds like a nightmare
pygame.mixer.music.load('./music/Elvis Presley - Unchained Melody (Live at Ann Arbor, MI - Official Audio).mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():  # wait for music to finish playing
    pygame.time.wait(1)