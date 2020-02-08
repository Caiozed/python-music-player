import PySimpleGUI as sg
import os
import utils
from os import walk
import _thread
from pygame import mixer  # Load the popular external library
import MainWindowViewModel as viewModel

def FolderSelected(files):
    mypath = sg.popup_get_folder("Mp3's Folder")
    files = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        for file in filenames:
            if file.endswith(".mp3"):
                files.append(utils.GetSongData(os.path.join(dirpath, file)))
        
    return files

def PlayPauseEvent(isPaused):
    if(isPaused):
        utils.PauseSong(isPaused)
        viewModel.window['-PLAY-'].update("PAUSE")
        StartProgressBarThread()  
    else:
        utils.PauseSong(isPaused)
        viewModel.window['-PLAY-'].update("PLAY")  
    
    return not isPaused

def PlayEvent(currentSong):
    viewModel.window["-SONG-"].update('Playing - ' + currentSong[0].name + ' - ' + currentSong[0].artist)
    viewModel.window['-PLAY-'].update("PAUSE")
    utils.PlaySong(currentSong[0].path)

def MusicChangedEvent(selectedSong):
    viewModel.isPlaying = True
    viewModel.isPaused = False
    viewModel.currentSong = selectedSong
    if(len(viewModel.currentSong) > 0):
        viewModel.currentSongLength = viewModel.currentSong[0].length
        viewModel.window["-TOTAL_TIME-"].update(utils.ParseTime(viewModel.currentSongLength))
        PlayEvent(viewModel.currentSong)
        StartProgressBarThread()

def StartProgressBarThread():
    if(viewModel.barThread == 0):
        viewModel.barThread = _thread.start_new_thread( UpdateProgressBar, () )

def UpdateProgressBar():
    while(True):
        viewModel.window["-PROGESS-"].update_bar((mixer.music.get_pos() / viewModel.currentSongLength)*100)
        viewModel.window["-CURRENT_TIME-"].update(utils.ParseTime(mixer.music.get_pos()))
        print((mixer.music.get_pos() / viewModel.currentSongLength) *100)
