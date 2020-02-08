from pygame import mixer  # Load the popular external library
from mutagen.mp3 import MP3
from eyed3 import id3
import models

def PlaySong(filePath):
    mixer.music.load(filePath)
    mixer.music.play()

def PauseSong(isPaused):
    if(isPaused):
        mixer.music.unpause()
    else:
        mixer.music.pause()

def GetSongData(filePath):
    tag = id3.Tag()
    tag.parse(filePath)
    song = MP3(filePath)
    return models.SongData(filePath, tag.title, tag.artist, tag.album, song.info.length * 1000)

def ParseTime(millis):
    millis = int(millis)
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    minutes = "0%s" % (minutes) if minutes < 10 else minutes
    seconds = "0%s" % (seconds) if seconds < 10 else seconds
    return "%s:%s" %  (minutes, seconds)
