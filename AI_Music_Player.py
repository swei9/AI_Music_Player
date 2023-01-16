#print("\n~~~~~~Music~~~~~")
#playsound('songs/meow.wav')

#imports
from playsound import playsound
import tkinter
from PIL import ImageTk,Image
import customtkinter
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("BeatScape")
        self.geometry(f"{1100}x{580}")
        self.iconbitmap("images/gui/favicon.ico")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path_gui = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images/gui")
        image_path_album_covers = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images/album-covers")

        self.playbutton_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path_gui, "play_dark.png")),
                                                       dark_image=Image.open(os.path.join(image_path_gui, "play_light.png")), size=(30, 30))
        self.pausebutton_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path_gui, "pause_dark.png")),
                                                        dark_image=Image.open(os.path.join(image_path_gui, "pause_light.png")), size=(30, 30))
        self.skipbutton_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path_gui, "skip_dark.png")),
                                                       dark_image=Image.open(os.path.join(image_path_gui, "skip_light.png")), size=(30, 30))
        self.backbutton_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path_gui, "back_dark.png")),
                                                       dark_image=Image.open(os.path.join(image_path_gui, "back_light.png")), size=(30, 30))

        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path_gui, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path_gui, "home_light.png")), size=(20, 20))
        self.playlist_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path_gui, "playlist_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path_gui, "playlist_light.png")), size=(20, 20))
        self.settings_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path_gui, "settings_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path_gui, "settings_light.png")), size=(20, 20))

        self.logo_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path_gui, "beatscape-highrez-dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path_gui, "beatscape-highrez-light.png")), size=(26, 26))

        self.album_cover_img1 = customtkinter.CTkImage(Image.open(os.path.join(image_path_album_covers, "beatles.jpg")), size=(500, 500))
        self.album_cover_img2 = customtkinter.CTkImage(Image.open(os.path.join(image_path_album_covers, "led-zepllin.jpg")), size=(500, 500))
        self.album_cover_img3 = customtkinter.CTkImage(Image.open(os.path.join(image_path_album_covers, "nico.jpg")), size=(500, 500))
        self.album_cover_img4 = customtkinter.CTkImage(Image.open(os.path.join(image_path_album_covers, "notorius-big.jpg")), size=(500, 500))
        self.album_cover_img5 = customtkinter.CTkImage(Image.open(os.path.join(image_path_album_covers, "patti.jpg")), size=(500, 500))
        self.album_cover_img6 = customtkinter.CTkImage(Image.open(os.path.join(image_path_album_covers, "pink-floyd.jpg")), size=(500, 500))

        self.song_image_list = [self.album_cover_img1, self.album_cover_img2, self.album_cover_img3, self.album_cover_img4, self.album_cover_img5, self.album_cover_img6]
        number_of_songs = len(self.song_image_list)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, image=self.logo_image, compound="left")
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

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        album_cover = customtkinter.CTkLabel(self, image=self.album_cover_img1)
        album_cover.grid(row=0, column=1, columnspan=3)

        play_button = customtkinter.CTkButton(self, image=self.playbutton_image, command=lambda: play)
        play_button.grid(row=1, column=2)

        skip_button = customtkinter.CTkButton(self,  image=self.skipbutton_image, command=lambda: skip(2))
        skip_button.grid(row=1, column=3)

        back_button = customtkinter.CTkButton(self, image=self.backbutton_image)
        back_button.grid(row=1, column=1)


        status_button = customtkinter.CTkLabel(self, text="Song 1 of " + str(number_of_songs))
        status_button.grid(row=2, column=1, columnspan=3)


        #self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        #self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        #self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.image_icon_image)
        #self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)

        #self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        #self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)

        #self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        #self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)

        #self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        #self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create playlist frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create settings frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        def login():
            print("Test")

        def play():
            global album_cover
            global play_button
            global pause_button
            global skip_button
            global back_button

            album_cover.grid_forget()

        def pause():
            global album_cover
            global play_button
            global pause_button
            global skip_button
            global back_button

            album_cover.grid_forget()

        def skip(image_number):
            global album_cover
            global play_button
            global pause_button
            global skip_button
            global back_button

            album_cover.grid_forget()

            album_cover = customtkinter.CTkLabel(self, image=self.song_image_list[image_number-1])
            play_button = customtkinter.CTkButton(self, image=self.playbutton_image, command=lambda: play)
            pause_button = customtkinter.CTkButton(self, image=self.pausebutton_image, command=lambda: pause)

            if image_number == number_of_songs:
                skip_button = customtkinter.CTkButton(self, image=self.skipbutton_image)
            else:
                skip_button = customtkinter.CTkButton(self,  image=self.skipbutton_image, command=lambda: skip(image_number+1))

            back_button = customtkinter.CTkButton(self, image=self.backbutton_image, command=lambda: back(image_number-1))

            status_button = customtkinter.CTkLabel(self, text="Song " + str(image_number) + " of " + str(number_of_songs), bd=1)
            status_button.grid(row=2, column=1, columnspan=3)

        def back(image_number):
            global album_cover
            global play_button
            global pause_button
            global skip_button
            global back_button

            album_cover.grid_forget()

            album_cover = customtkinter.CTkLabel(self, image=self.song_image_list[image_number-1])
            play_button = customtkinter.CTkButton(self, image=self.playbutton_image, command=lambda: play)
            pause_button = customtkinter.CTkButton(self, image=self.pausebutton_image, command=lambda: pause)

            skip_button = customtkinter.CTkButton(self,  image=self.skipbutton_image, command=lambda: skip(image_number+1))

            if image_number == 1:
                back_button = customtkinter.CTkButton(self, image=self.backbutton_image)
            else:
                back_button = customtkinter.CTkButton(self, image=self.backbutton_image, command=lambda: back(image_number-1))

            status_button = customtkinter.CTkLabel(self, text="Song " + str(image_number) + " of " + str(number_of_songs), bd=1)
            status_button.grid(row=2, column=1, columnspan=3)

        
        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.playlist_button.configure(fg_color=("gray75", "gray25") if name == "playlist" else "transparent")
        self.settings_button.configure(fg_color=("gray75", "gray25") if name == "settings" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "playlist":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "settings":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

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