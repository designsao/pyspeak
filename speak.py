import os
import tempfile
from gtts import gTTS
import pygame
from pygame import mixer

def speak(words):
    tts = gTTS(words, lang='en')

    # using block for temp file 
    f = tempfile.NamedTemporaryFile()
    tts.write_to_fp(f)
    # playing the temp file
    pygame.init()
    mixer.music.load(f.name)
    SONG_END = pygame.constants.USEREVENT + 1
    mixer.music.set_endevent(SONG_END)
    mixer.music.play()

    waiting = True
    while waiting :
        for event in pygame.event.get():
            if event.type == pygame.constants.QUIT:
                waiting = False
            elif event.type == SONG_END:
                waiting = False
    f.close()

speak("Hello World!")