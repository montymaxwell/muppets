import pygame

# Testing
pygame.mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)') # NO! it sounds like a nightmare
pygame.mixer.music.load('./music/Baton Road - Boruto OP (English Cover) TV SIZE【JubyPhonic】バトンロード.wav')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():  # wait for music to finish playing
    pygame.time.wait(1)