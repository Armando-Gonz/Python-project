import tkinter
from tkinter import *
from tkinter import filedialog
import pygame
import os
from PIL import ImageTk, Image
# this block of codes initializes the music player with the emergent window
initializer = Tk()
initializer.title('Jose player')
initializer.geometry("500x300")
print(os.getcwd())
pygame.mixer.init()

# block of code that creates a list and fills it with music accessing the computer files
list_of_songs= []
current_song = ""
paused = False
def music_loader(): #function for creating a directory
     global current_song
     initializer.directory = filedialog.askdirectory()
     for song in os.listdir(initializer.directory):
         name, ext = os.path.splitext(song)
         if ext =='.mp3':
          list_of_songs.append(song)

     for song in list_of_songs:
          songList.insert("end", song)

     songList.selection_set(0) # set current song to the one selected in the list
     current_song = list_of_songs[songList.curselection()[0]]

# code functions so we can use the buttoms we created

def play():
    global current_song, paused # global allows us to work with variables outside the function
    song_path = os.path.join(initializer.directory, current_song)
    if paused:
        pygame.mixer.music.unpause()
        paused= False
    else:
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        paused = False

def pause():
    global paused
    pygame.mixer.music.pause()
    paused= True

def next():
    global current_song, paused
    try:
        current_index = songList.curselection()[0]
        next_index = current_index + 1 # moves the index one position
        if next_index < len(list_of_songs):
            songList.selection_clear(current_index) # starts from the current song until end of the list removes the previous sonng so we can go to the next one
            songList.selection_set(next_index)
            current_song = list_of_songs[next_index]
            play()
    except:
       pass

def previous():
    global current_song, paused
    try:
        current_index = songList.curselection()[0]
        previous_index = current_index -1 # does the inverse, takes an index and reduce it by one
        if previous_index >= 0:
            songList.selection_clear(current_index)
            songList.selection_set(previous_index)
            current_song = list_of_songs[previous_index]
        play()
    except:
        pass
#menu bar button for accesing the files inside computer
menu_bar = Menu(initializer) #creates menu bar
initializer.config(menu=menu_bar)
#block of code for adding images
organized_menu = Menu(menu_bar,tearoff=False) #creates menu called organized option 1
organized_menu.add_command(label='organized Option 1', command= music_loader) # adds items to the menu bar
menu_bar.add_cascade(label = 'organize',menu=organized_menu) # adds organize to the menu bar

songList = Listbox(initializer, bg="black", fg='white', width=100,  height=15)  # sets color and format to the emergent window
image_button = PhotoImage(file='images/play.png')
pause_button = PhotoImage(file='images/pause.png')
next_button = PhotoImage(file='images/next.png')
previus_button = PhotoImage(file='images/previous.png')

control_frame = Frame(initializer)
control_frame.pack()


play_btn = Button(control_frame, image=image_button, borderwidth=0, command=play)
pause_btn = Button(control_frame, image=pause_button, borderwidth=0, command= pause)
next_btn = Button(control_frame, image=next_button, borderwidth=0, command= next)
previous_btn = Button(control_frame, image=previus_button, borderwidth=0, command= previous)

play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
previous_btn.grid(row=0, column=0, padx=7, pady=10)

songList.pack()




initializer.mainloop()  # allows us to keep the emergent window and have user interaction

