import tkinter as tk
from tkinter import messagebox, simpledialog, font, PhotoImage
from bisect import bisect_left
import json
import os

# File path
file_path = "song_list.json"

# Load song list from file
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        song_list = sorted(json.load(file))
else:
    song_list = sorted([])

def save_song_list():
    with open(file_path, "w") as file:
        json.dump(song_list, file)

def add_song():
    song = song_entry.get().strip()
    if song:
        if song not in song_list:
            song_list.append(song)
            song_list.sort()
            song_entry.delete(0, tk.END)
            save_song_list()
        else:
            messagebox.showinfo("Info", "Song already exists.")
    else:
        messagebox.showinfo("Info", "Please enter a song name.")
    update_display()

def remove_song():
    song = simpledialog.askstring("Remove Song", "Enter song name:")
    if song in song_list:
        song_list.remove(song)
        save_song_list()
    else:
        messagebox.showinfo("Info", "Song not found.")
    update_display()

def find_song_linear():
    song_query = simpledialog.askstring("Find Song (Linear)", "Enter part of the song name or artist:")
    matches = [song for song in song_list if song_query.lower() in song.lower()]
    if matches:
        messagebox.showinfo("Info", "Songs found:\n" + "\n".join(matches))
    else:
        messagebox.showinfo("Info", "Song not found.")

def find_song_binary():
    song_query = simpledialog.askstring("Find Song (Binary)", "Enter song name:")
    if song_query:
        index = bisect_left(song_list, song_query)
        if index < len(song_list) and song_list[index] == song_query:
            messagebox.showinfo("Info", f"Song found: {song_list[index]}")
        else:
            messagebox.showinfo("Info", "Song not found.")
    else:
        messagebox.showinfo("Info", "Please enter a song name.")

def find_songs_by_artist():
    artist_name = simpledialog.askstring("Find Songs by Artist", "Enter artist name:")
    if not artist_name:
        messagebox.showinfo("Info", "Please enter an artist name.")
        return
    
    artist_name = artist_name.lower()
    found_songs = [song for song in song_list if artist_name in song.lower().split(' - ')[0]]

    if found_songs:
        message = "Songs found:\n" + "\n".join(found_songs)
    else:
        message = "No songs found by that artist."
    
    messagebox.showinfo("Search Results", message)

def update_display():
    song_display.delete(1.0, tk.END)
    for song in song_list:
        song_display.insert(tk.END, song + "\n")

root = tk.Tk()
root.title("Song Manager")

# Styling
root.configure(bg='#f0c3cc')
myFont = font.Font(family='Helvetica', size=12)

# Load an icon image for the window (optional)
# root.iconphoto(False, PhotoImage(file='icon.png'))

# Main frame
main_frame = tk.Frame(root, bg='#f0c3cc', padx=10, pady=10)
main_frame.pack(padx=10, pady=10)

# Header image (optional)
# header_img = PhotoImage(file='header.png')
# header_label = tk.Label(main_frame, image=header_img, bg='#f0c3cc')
# header_label.pack(pady=5)

# Input frame
input_frame = tk.Frame(main_frame, bg='#ffffff')
input_frame.pack(pady=5)

# Entry widget for adding songs
song_entry = tk.Entry(input_frame, width=40, font=myFont, bd=2, relief='solid')
song_entry.grid(row=0, column=0, padx=5, pady=5)

# Button frame
button_frame = tk.Frame(main_frame, bg='#000000')
button_frame.pack(pady=5)

# Operation buttons with rounded corners
button_style = {"font": myFont, "bg": "#ffffff", "fg": "#000000", "relief": "solid", "bd": 2}

add_button = tk.Button(button_frame, text="Add Song", command=add_song, **button_style)
add_button.grid(row=0, column=0, padx=5, pady=5)

remove_button = tk.Button(button_frame, text="Remove Song", command=remove_song, **button_style)
remove_button.grid(row=0, column=1, padx=5, pady=5)

find_linear_button = tk.Button(button_frame, text="Find Song (Linear)", command=find_song_linear, **button_style)
find_linear_button.grid(row=0, column=2, padx=5, pady=5)

find_binary_button = tk.Button(button_frame, text="Find Song (Binary)", command=find_song_binary, **button_style)
find_binary_button.grid(row=0, column=3, padx=5, pady=5)

find_artist_button = tk.Button(button_frame, text="Find Songs by Artist", command=find_songs_by_artist, **button_style)
find_artist_button.grid(row=0, column=4, padx=5, pady=5)

# Display frame
display_frame = tk.Frame(main_frame, bg='#f0c3cc')
display_frame.pack(pady=5)

# Song display with scroll bar
song_display = tk.Text(display_frame, height=10, width=50, font=myFont, bg='#000000', bd=2, relief='solid')
song_display.pack(side=tk.LEFT, padx=5, pady=5)

scrollbar = tk.Scrollbar(display_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
song_display.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=song_display.yview)

update_display()

root.mainloop()
