import pygame
import threading
    
class SoundManager:

    INTRO_END = pygame.USEREVENT + 1
    ATTACK = 1
    JUMP   = 2
    MOVE   = 3
    ATTACK  = 4
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 256)
        pygame.mixer.init()
        self._currentMusicName = ""
    
    def playMusic(self, soundName):
        self._currentMusicName= soundName
        sound = pygame.mixer.music.load("music/" + self._currentMusicName + "-begin.ogg")
        sound = pygame.mixer.music.queue("music/" + self._currentMusicName + "-loop.ogg")     
        pygame.mixer.music.set_endevent(self.INTRO_END)
        pygame.mixer.music.play()
        
    def introEnd(self):
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_endevent()
        
    def stopMusic(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.set_endevent()

    def playSoundFromEvent(self, event):
        sound = None
        if(event == self.ATTACK):
            sound = pygame.mixer.Sound("sound/punch.ogg")
        elif(event == self.JUMP):
            sound = None
        elif(event == self.MOVE):
            sound = None
        
        if(sound != None):
            channel = pygame.mixer.find_channel(True)
            channel.set_volume(0.7)
            channel.play(sound)
