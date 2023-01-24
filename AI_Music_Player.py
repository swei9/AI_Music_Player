#imports
from playsound import playsound
import tkinter
from tkinter import filedialog
from PIL import ImageTk,Image
import customtkinter
import os
import pygame
from pygame import mixer
import DALL_E_Generator as imageGen
import time
from mutagen.mp3 import MP3

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# ============= Music Credit ============= #

# Bensound: https://www.bensound.com
# - "All That" by Benjamin Tissot
# - "Creative Minds" by Benjamin Tissot
# - "Dreams" by Benjamin Tissot
# - "Elevate" by Benjamin Tissot
# 
# BreakingCopyright: https://youtu.be/BH-SnQ8J1VU
# - "Artificial.Music - And So It Begins [Lo-fi]" is under a Creative Commons license (CC-BY) 3.0
# - "Artificial.Music - Faithful Mission" is under a Creative Commons (CC BY 3.0) license.
# - "Tokyo Music Walker  - Way Home" is under a Creative Commons (CC-BY) license.

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()

        # ============= Initialize Window ============= #

        self.title("BeatScape")
        self.geometry(f"{1150}x{640}")
        self.iconbitmap("images/gui/favicon.ico")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        # ============= Initialize Images ============= #

        # Load GUI Images (light & dark)

        image_path_gui = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images/gui")
        image_path_album_covers = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images/album-covers")

        self.logo_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path_gui, "beatscape-highrez-dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path_gui, "beatscape-highrez-light.png")), size=(250, 61.75))

        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path_gui, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path_gui, "home_light.png")), size=(20, 20))
        self.playbutton_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path_gui, "play_dark.png")),
                                                       dark_image=Image.open(os.path.join(image_path_gui, "play_light.png")), size=(30, 30))
        self.pausebutton_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path_gui, "pause_dark.png")),
                                                        dark_image=Image.open(os.path.join(image_path_gui, "pause_light.png")), size=(30, 30))
        self.skipbutton_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path_gui, "skip_dark.png")),
                                                       dark_image=Image.open(os.path.join(image_path_gui, "skip_light.png")), size=(30, 30))
        self.backbutton_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path_gui, "back_dark.png")),
                                                       dark_image=Image.open(os.path.join(image_path_gui, "back_light.png")), size=(30, 30))

        self.playlist_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path_gui, "playlist_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path_gui, "playlist_light.png")), size=(20, 20))

        self.settings_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path_gui, "settings_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path_gui, "settings_light.png")), size=(20, 20))

        # Generate & Load AI Song Images 

        self.album_cover_img1 = customtkinter.CTkImage(Image.open(os.path.join(image_path_album_covers, imageGen.getImage("all that.mp3"))), size=(500, 500))
        self.album_cover_img2 = customtkinter.CTkImage(Image.open(os.path.join(image_path_album_covers, imageGen.getImage("and so it begins.mp3"))), size=(500, 500))
        self.album_cover_img3 = customtkinter.CTkImage(Image.open(os.path.join(image_path_album_covers, imageGen.getImage("creative minds.mp3"))), size=(500, 500))
        self.album_cover_img4 = customtkinter.CTkImage(Image.open(os.path.join(image_path_album_covers, imageGen.getImage("dreams.mp3"))), size=(500, 500))
        self.album_cover_img5 = customtkinter.CTkImage(Image.open(os.path.join(image_path_album_covers, imageGen.getImage("elevate.mp3"))), size=(500, 500))
        self.album_cover_img6 = customtkinter.CTkImage(Image.open(os.path.join(image_path_album_covers, imageGen.getImage("faithful mission.mp3"))), size=(500, 500))
        self.album_cover_img7 = customtkinter.CTkImage(Image.open(os.path.join(image_path_album_covers, imageGen.getImage("meow.mp3"))), size=(500, 500))
        self.album_cover_img8 = customtkinter.CTkImage(Image.open(os.path.join(image_path_album_covers, imageGen.getImage("santa.mp3"))), size=(500, 500))
        self.album_cover_img9 = customtkinter.CTkImage(Image.open(os.path.join(image_path_album_covers, imageGen.getImage("way home.mp3"))), size=(500, 500))

        self.song_image_list = [self.album_cover_img1, self.album_cover_img2, self.album_cover_img3, self.album_cover_img4, self.album_cover_img5, self.album_cover_img6,
                                self.album_cover_img7, self.album_cover_img8, self.album_cover_img9]
        number_of_songs = len(self.song_image_list)

        # ============= Create Navigation Frame ============= #

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="", image=self.logo_image)
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.playlist_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Playlist",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.playlist_image, anchor="w", command=self.playlist_button_event)
        self.playlist_button.grid(row=2, column=0, sticky="ew")

        self.settings_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Settings",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.settings_image, anchor="w", command=self.settings_button_event)
        self.settings_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Dark", "Light", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # ============= Create Home Frame ============= #

        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        global album_cover
        album_cover = customtkinter.CTkLabel(self.home_frame, text="", image=self.album_cover_img1)
        album_cover.grid(row=0, column=1, columnspan=4, padx=10, pady=10)

        global back_button
        back_button = customtkinter.CTkButton(self.home_frame, text="", image=self.backbutton_image, command=lambda: back(), state='disabled')
        back_button.grid(row=2, column=1, padx=10, pady=10)

        global play_button
        play_button = customtkinter.CTkButton(self.home_frame, text="", image=self.playbutton_image, command=lambda: play())
        play_button.grid(row=2, column=2, padx=10, pady=10)

        global pause_button
        pause_button = customtkinter.CTkButton(self.home_frame, text="", image=self.pausebutton_image, command=lambda: pause(paused))
        pause_button.grid(row=2, column=3, padx=10, pady=10)

        global skip_button
        skip_button = customtkinter.CTkButton(self.home_frame, text="",  image=self.skipbutton_image, command=lambda: skip(2))
        skip_button.grid(row=2, column=4, padx=10, pady=10)

        global song_number
        song_number = customtkinter.CTkLabel(self.home_frame, text="Song 1 of " + str(number_of_songs))
        song_number.grid(row=3, column=1, sticky='w')

        global song_status
        song_status = customtkinter.CTkLabel(self.home_frame, text='', anchor='e')
        song_status.grid(row=3, column=4, sticky='e')

        # ============= Create Playlist Frame ============= #

        self.playlist_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        paddingx = customtkinter.CTkLabel(self.playlist_frame, text='', width=110)
        paddingx.grid(row=0, column=0)

        song_box = tkinter.Listbox(self.playlist_frame, bg="#1a1a1a", width=100, height=25, border="1", foreground="white")
        song_box.grid(padx=20, pady=20, row=0, column=1, columnspan=2, sticky='we')

        add_song_btn = customtkinter.CTkButton(self.playlist_frame, text="Add song", command=lambda: add_song())
        add_song_btn.grid(padx=10, pady=10, row=1, column=1, sticky='we')

        add_many_songs_btn = customtkinter.CTkButton(self.playlist_frame, text="Add many songs", command=lambda: add_many_songs())
        add_many_songs_btn.grid(padx=10, pady=10, row=2, column=1, sticky='we')

        remove_song_btn = customtkinter.CTkButton(self.playlist_frame, text="Remove song", command=lambda: remove_song())
        remove_song_btn.grid(padx=10, pady=10, row=1, column=2, sticky='we')

        remove_all_songs_btn = customtkinter.CTkButton(self.playlist_frame, text="Remove all songs", command=lambda: remove_all_songs())
        remove_all_songs_btn.grid(padx=10, pady=10, row=2, column=2, sticky='we')

        # ============= Create Settings Frame ============= #

        self.settings_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # ============= Music Player Functions ============= #

        global paused
        paused = False

        def play():
            song = song_box.get('active')
            song = f'C:/Users/bsaen/develop/AI_Music_Player/songs/{song}.mp3'
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)

            play_time()

        def pause(is_paused):
            global paused
            paused = is_paused

            if paused:
                pygame.mixer.music.pause()
                paused = False
            else:
                pygame.mixer.music.unpause()
                paused = True

        def skip(image_number):

            # Get current song index number
            next_one = song_box.curselection()

            # Add one to the current song selection
            next_one = next_one[0] + 1
            song = song_box.get(next_one)

            # Add directory structure to song title
            song = f'C:/Users/bsaen/develop/AI_Music_Player/songs/{song}.mp3'
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)

            # Move active in playlist
            song_box.selection_clear(0, 'end')
            song_box.activate(next_one)
            song_box.select_set(next_one, last=None)

            global album_cover
            global play_button
            global pause_button
            global skip_button
            global back_button

            album_cover.grid_forget()

            album_cover = customtkinter.CTkLabel(self.home_frame, text="", image=self.song_image_list[image_number-1])
            album_cover.grid(row=0, column=1, columnspan=4, padx=10, pady=10)

            play_button = customtkinter.CTkButton(self.home_frame, text="", image=self.playbutton_image, command=lambda: play)
            play_button.grid(row=2, column=2, padx=10, pady=10)

            pause_button = customtkinter.CTkButton(self.home_frame, text="", image=self.pausebutton_image, command=lambda: pause(paused))
            pause_button.grid(row=2, column=3, padx=10, pady=10)

            if image_number == number_of_songs:
                skip_button = customtkinter.CTkButton(self.home_frame, text="", image=self.skipbutton_image, state='disabled')
            else:
                skip_button = customtkinter.CTkButton(self.home_frame, text="", image=self.skipbutton_image, command=lambda: skip(image_number+1))
            skip_button.grid(row=2, column=4, padx=10, pady=10)

            back_button = customtkinter.CTkButton(self.home_frame, text="", image=self.backbutton_image, command=lambda: back(image_number-1))
            back_button.grid(row=2, column=1, padx=10, pady=10)

            song_number = customtkinter.CTkLabel(self.home_frame, text="Song " + str(image_number) + " of " + str(number_of_songs))
            song_number.grid(row=3, column=1, sticky='w')

            self.home_frame.grid(row=0, column=1, sticky="nsew", padx=100)

        def back(image_number):
            
            # Get current song index number
            next_one = song_box.curselection()

            # Add one to the current song selection
            next_one = next_one[0] - 1
            song = song_box.get(next_one)

            # Add directory structure to song title
            song = f'C:/Users/bsaen/develop/AI_Music_Player/songs/{song}.mp3'
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)

            # Move active in playlist
            song_box.selection_clear(0, 'end')
            song_box.activate(next_one)
            song_box.select_set(next_one, last=None)

            global album_cover
            global play_button
            global pause_button
            global skip_button
            global back_button

            album_cover.grid_forget()

            album_cover = customtkinter.CTkLabel(self.home_frame, text="", image=self.song_image_list[image_number-1])
            album_cover.grid(row=0, column=1, columnspan=4, padx=10, pady=10)

            play_button = customtkinter.CTkButton(self.home_frame, text="", image=self.playbutton_image, command=lambda: play)
            play_button.grid(row=2, column=2, padx=10, pady=10)

            pause_button = customtkinter.CTkButton(self.home_frame, text="", image=self.pausebutton_image, command=lambda: pause(paused))
            pause_button.grid(row=2, column=3, padx=10, pady=10)

            skip_button = customtkinter.CTkButton(self.home_frame, text="", image=self.skipbutton_image, command=lambda: skip(image_number+1))
            skip_button.grid(row=2, column=4, padx=10, pady=10)

            if image_number == 1:
                back_button = customtkinter.CTkButton(self.home_frame, text="", image=self.backbutton_image, state='disabled')
            else:
                back_button = customtkinter.CTkButton(self.home_frame, text="", image=self.backbutton_image, command=lambda: back(image_number-1))
                
            back_button.grid(row=2, column=1, padx=10, pady=10)

            song_number = customtkinter.CTkLabel(self.home_frame, text="Song " + str(image_number) + " of " + str(number_of_songs))
            song_number.grid(row=3, column=1, sticky='w')

            self.home_frame.grid(row=0, column=1, sticky="nsew", padx=100)

        # ============= Playlist Functions ============= #

        def add_song():
            song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
        
            #strip out the directory info and .mp3 extension from the song name
            song = song.replace("C:/Users/bsaen/develop/AI_Music_Player/songs/", "")
            song = song.replace(".mp3", "")

            # Add song to listbox
            song_box.insert('end', song)

        def add_many_songs():
            songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))

            #Loop through song list and replace directory info and mp3 paths then insert into playlist
            for song in songs:
                song = song.replace("C:/Users/bsaen/develop/AI_Music_Player/songs/", "")
                song = song.replace(".mp3", "")
                song_box.insert('end', song)
        
        def remove_song():
            song_box.delete('anchor')
            pygame.mixer.music.stop
        
        def remove_all_songs():
            song_box.delete(0, 'end')
            pygame.mixer.music.stop

        # ============= Misc. Functions ============= #

        def play_time():
            current_time = pygame.mixer.music.get_pos() / 1000
            converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

            # Get current song
            current_song = song_box.curselection()
            song = song_box.get(current_song)
            song = f'C:/Users/bsaen/develop/AI_Music_Player/songs/{song}.mp3'

            # Get song length
            song_mut = MP3(song)
            song_length = song_mut.info.length
            converted_current_song_length = time.strftime('%M:%S', time.gmtime(song_length))

            song_status.configure(text=f'  {converted_current_time} of {converted_current_song_length}  ')

            song_status.after(1000, play_time)

        def slide(x):
            pass

        # Select Default Frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.playlist_button.configure(fg_color=("gray75", "gray25") if name == "playlist" else "transparent")
        self.settings_button.configure(fg_color=("gray75", "gray25") if name == "settings" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew", padx=100)
        else:
            self.home_frame.grid_forget()
        if name == "playlist":
            self.playlist_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.playlist_frame.grid_forget()
        if name == "settings":
            self.settings_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.settings_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def playlist_button_event(self):
        self.select_frame_by_name("playlist")

    def settings_button_event(self):
        self.select_frame_by_name("settings")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()