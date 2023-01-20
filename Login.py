# login gui
import customtkinter
from PIL import ImageTk,Image
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("BeatScape")
root.geometry("500x350")
root.iconbitmap("images/gui/favicon.ico")

def login():
    print("Test")
    
logo_image = customtkinter.CTkImage(light_image=Image.open(os.path.join("images\gui\\beatscape-highrez-dark.png")),
                                    dark_image=Image.open(os.path.join("images\gui\\beatscape-highrez-light.png")), size=(250, 61.75))

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

navigation_frame_label = customtkinter.CTkLabel(master=frame, text="", image=logo_image)
navigation_frame_label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry1.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()