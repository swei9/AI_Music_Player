
pip install pygame
from pygame import mixer
    
def Play():
    mixer.music.load("meow.mp3")
    mixer.music.play()

def Pause():
    mixer.music.pause()

def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

def Resume():
    mixer.music.unpause()
