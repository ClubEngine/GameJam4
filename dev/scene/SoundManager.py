import pygame
import threading
    
class SoundManager:

    INTRO_END = pygame.USEREVENT + 1
    JUMP   = 2
    MOVE   = 3
    DISTANT_ATTACK  = 4
    MELEE_ATTACK  = 5
    HURT  = 6
    DEATH  = 7
    
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 256)
        pygame.mixer.init()
        self._currentMusicName = ""
        
    def playMenuMusic(self):
        sound = pygame.mixer.music.load("music/maintheme.ogg")
        pygame.mixer.music.play()
        
    def playMusic(self, soundName):
        self._currentMusicName= soundName
        sound = pygame.mixer.music.load("music/" + self._currentMusicName + "-begin.ogg")
        sound = pygame.mixer.music.queue("music/" + self._currentMusicName + "-loop.ogg")     
        pygame.mixer.music.set_endevent(self.INTRO_END)
        pygame.mixer.music.play()
        
    def introEnd(self):
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_endevent()
        
    def stop(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.set_endevent()

    def playSoundFromEvent(self, event, typeName):
        sound = None
        if(event == self.MELEE_ATTACK):
            sound = pygame.mixer.Sound("sound/punch.ogg")
        elif(event == self.DISTANT_ATTACK):
            if typeName == "pirate":
                sound = pygame.mixer.Sound("sound/verybiggunshot.ogg")
            if typeName == "ninja":
                sound = pygame.mixer.Sound("sound/kunaithrow.ogg")
        elif(event == self.JUMP):
            if typeName == "pirate":
                sound = None
            if typeName == "ninja":
                sound = pygame.mixer.Sound("sound/ninjahop.ogg")
        elif(event == self.MOVE):
            sound = None
        elif(event == self.HURT):
            sound = pygame.mixer.Sound("sound/hurt.ogg")
        elif(event == self.DEATH):
            sound = pygame.mixer.Sound("sound/argh.ogg")
        if(sound != None):
            channel = pygame.mixer.find_channel(True)
            channel.set_volume(0.8)
            channel.play(sound)
