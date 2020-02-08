import PySimpleGUI as sg
import winEvents
import utils
import MainWindowViewModel as viewModel
import os
from pygame import mixer  # Load the popular external library
import _thread

mixer.init()
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

layout = [
            [
                sg.Column([
                    [sg.Text("00:00", key="-TOTAL_TIME-", auto_size_text=True, size=(4,1)),
                        sg.ProgressBar(100, key='-PROGESS-', size=(30, 10)),
                        sg.Text("00:00", key="-CURRENT_TIME-", auto_size_text=True, size=(4,1))],
                    [sg.Text("Nothing Playing...", key="-SONG-", auto_size_text=True, size=(30,1))],
                    [sg.Button("PLAY", key='-PLAY-')], 
                ], pad=((1,1), (80,1))), 
                sg.Column([
                    [sg.Button('Music Folder', size=(15, 1), key="-FOLDER_SELECT-")], 
                    [sg.Listbox(values=viewModel.files, key="-SONGLIST-", enable_events=True, size=(30,10))]
                ])
            ],
        ]

# Create the Window
viewModel.window = window = sg.Window('PyMusicPlayer', layout)   


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    if event in (None, '-FOLDER_SELECT-'):
        viewModel.files = winEvents.FolderSelected(viewModel.files)
        window["-SONGLIST-"].update(viewModel.files)
    if event in (None, '-PLAY-'):
        viewModel.isPaused = winEvents.PlayPauseEvent(viewModel.isPaused)
    if event in (None, '-SONGLIST-'):
        winEvents.MusicChangedEvent(values["-SONGLIST-"])       

window.close()


