from tkinter import *
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, window ):
        window.geometry('400x350'); window.title('Swathi Music Player'); window.resizable(0,0)
        load_button = Button(window, text = 'Load song ',  width = 15, font = ('Times', 15), command = self.load)
        start_button = Button(window, text = 'start song ',  width = 15,font = ('Times', 15), command = self.play)
        pause_button = Button(window,text = 'Pause song',  width = 15, font = ('Times', 15), command = self.pause)
        stop_button = Button(window ,text = 'Stop song',  width = 15, font = ('Times', 15), command = self.stop)
        load_button.place(x=110,y=30);start_button.place(x=110,y=110);pause_button.place(x=110,y=190);stop_button.place(x=110,y=270)
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
root = Tk()
app= MusicPlayer(root)
root.mainloop()
