import tkinter as tk
from tkinter import messagebox, simpledialog, font
from bisect import bisect_left

# Initialize song list
song_list = sorted(["Drake - Marvins Room", "Lorde - Green Light","Kanye West - All of the lights", "Taylor Swift - Dress", 'The Weeknd - After Hours', "Nicki Minaj - Pink Friday", "Rihanna - Needed Me", "Frank Ocean - Pink + White", "Drake - Sticky"])

def add_song():
    song = song_entry.get().strip()
    if song:
        if song not in song_list:
            song_list.append(song)
            song_list.sort()
            song_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Info", "Song already exists.")
    else:
        messagebox.showinfo("Info", "Please enter a song name.")
    update_display()

def remove_song():
    song = simpledialog.askstring("Remove Song", "Enter song name:")
    if song in song_list:
        song_list.remove(song)
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
    

def update_display():
    song_display.delete(1.0, tk.END)
    for song in song_list:
        song_display.insert(tk.END, song + "\n")

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


root = tk.Tk()
root.title("Song Manager")

# Styling
root.configure(bg='light pink')
myFont = font.Font(family='Helvetica', size=12, weight='bold')

# Main frame
main_frame = tk.Frame(root, bg='light pink', padx=10, pady=10)
main_frame.pack(padx=10, pady=10)

# Input frame
input_frame = tk.Frame(main_frame, bg='light grey')
input_frame.pack(pady=5)

# Entry widget for adding songs
song_entry = tk.Entry(input_frame, width=40, font=myFont)
song_entry.grid(row=0, column=0, padx=5, pady=5)

# Button frame
button_frame = tk.Frame(main_frame, bg='black')
button_frame.pack(pady=5)

# Operation buttons
add_button = tk.Button(button_frame, text="Add Song", command=add_song, font=myFont)
add_button.grid(row=0, column=0, padx=5, pady=5)

remove_button = tk.Button(button_frame, text="Remove Song", command=remove_song, font=myFont)
remove_button.grid(row=0, column=1, padx=5, pady=5)

find_linear_button = tk.Button(button_frame, text="Find Song (Linear)", command=find_song_linear, font=myFont)
find_linear_button.grid(row=0, column=2, padx=5, pady=5)



find_artist_button = tk.Button(button_frame, text="Find Songs by Artist", command=find_songs_by_artist, font=myFont)
find_artist_button.grid(row=0, column=4, padx=5, pady=5)  # Adjust grid positioning as necessary


# Display frame
display_frame = tk.Frame(main_frame, bg='light grey')
display_frame.pack(pady=5)

# Song display
song_display = tk.Text(display_frame, height=10, width=50, font=myFont)
song_display.pack(padx=5, pady=5)

update_display()

root.mainloop()
