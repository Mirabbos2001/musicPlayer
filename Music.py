from tkinter import filedialog
from tkinter import *
import pygame
import os

# Script fayl joylashgan manzil
script_directory = os.path.dirname(os.path.abspath(__file__))
# Rasm katalogi
image_directory = os.path.join(script_directory, "images")

root = Tk()
root.title("Musiqani ijro etuvchi")
root.geometry("500x300")

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

songs = []
current_song = ""
paused = False

def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == ".mp3" or ext == ".m4a":
            songs.append(song)
    for song in songs:
        songlist.insert("end", song)
    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]

def toggle_music():
    global current_song, paused

    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        play_btn.config(image=play_btn_image)
    else:
        song_file = os.path.join(root.directory, current_song)
        pygame.mixer.music.load(song_file)
        pygame.mixer.music.play()
        play_btn.config(image=stop_btn_image)

def next_music():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            play_btn.config(image=play_btn_image)
        play_music()
    except:
        pass

def prev_music():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            play_btn.config(image=play_btn_image)
        play_music()
    except:
        pass


organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label="Katalogni tanlash", command=load_music)
menubar.add_cascade(label="Tashkil etish", menu=organise_menu)

songlist = Listbox(root, bg="black", fg="white", width=100, height=13, border=5)
songlist.pack()

control_frame = Frame(root)
control_frame.pack()

play_btn_image = PhotoImage(file=os.path.join(image_directory, "rasm1.png")).subsample(10)
stop_btn_image = PhotoImage(file=os.path.join(image_directory, "rasm4.png")).subsample(10)
next_btn_image = PhotoImage(file=os.path.join(image_directory, "rasm2.png")).subsample(10)
prev_btn_image = PhotoImage(file=os.path.join(image_directory, "rasm3.png")).subsample(10)

play_btn = Button(control_frame, borderwidth=0, command=toggle_music, image=play_btn_image)
next_btn = Button(control_frame, borderwidth=0, command=next_music, image=next_btn_image)
prev_btn = Button(control_frame, borderwidth=0, command=prev_music, image=prev_btn_image)

prev_btn.grid(row=0, column=0, padx=3, pady=1)
play_btn.grid(row=0, column=1, padx=3, pady=1)
next_btn.grid(row=0, column=2, padx=3, pady=1)

root.mainloop()