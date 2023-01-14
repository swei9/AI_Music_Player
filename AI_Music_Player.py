#imports
from playsound import playsound
from tkinter import *
from PIL import ImageTk,Image

print("\n~~~~~~Music~~~~~")
#playsound('songs/meow.wav')

#root window
root = Tk()
root.title("AI Music Player")
root.iconbitmap("images\gui\orangeSwirl.ico")
#Icon taken from Avanade @favicon.cc

#image declarations
play_img = ImageTk.PhotoImage(Image.open("images\gui\play_button.png").resize((60, 60), Image.ANTIALIAS))
pause_img = ImageTk.PhotoImage(Image.open("images\gui\pause_button.png").resize((60, 60), Image.ANTIALIAS))
skip_img = ImageTk.PhotoImage(Image.open("images\gui\skip_forward_button.png").resize((60, 60), Image.ANTIALIAS))
back_img = ImageTk.PhotoImage(Image.open("images\gui\skip_backward_button.png").resize((60, 60), Image.ANTIALIAS))

img1 = ImageTk.PhotoImage(Image.open("images\songs\\beatles.jpg").resize((600, 600), Image.ANTIALIAS))
img2 = ImageTk.PhotoImage(Image.open("images\songs\led-zepllin.jpg").resize((600, 600), Image.ANTIALIAS))
img3 = ImageTk.PhotoImage(Image.open("images\songs\\nico.jpg").resize((600, 600), Image.ANTIALIAS))
img4 = ImageTk.PhotoImage(Image.open("images\songs\\notorius-big.jpg").resize((600, 600), Image.ANTIALIAS))
img5 = ImageTk.PhotoImage(Image.open("images\songs\patti.jpg").resize((600, 600), Image.ANTIALIAS))
img6 = ImageTk.PhotoImage(Image.open("images\songs\pink-floyd.jpg").resize((600, 600), Image.ANTIALIAS))

song_image_list = [img1, img2, img3, img4, img5, img6]
number_of_songs = 6

#gui-functions

def play():
    global album_cover
    global play_button
    global pause_button
    global skip_button
    global back_button

    album_cover.grid_forget()

    assembly()

def pause():
    global album_cover
    global play_button
    global pause_button
    global skip_button
    global back_button

    album_cover.grid_forget()

    assembly()


def skip(current_image_number):
    global album_cover
    global play_button
    global pause_button
    global skip_button
    global back_button

    album_cover.grid_forget()

    album_cover = Label(root, image=song_image_list[current_image_number-1])
    play_button = Button(root, image=play_img, command=lambda: play)
    pause_button = Button(root, image=pause_img, command=lambda: pause)

    if current_image_number == 6:
        skip_button = Button(root, image=skip_img, state=DISABLED)
    else:
        skip_button = Button(root,  image=skip_img, command=lambda: skip(current_image_number+1))

    back_button = Button(root, image=back_img, command=lambda: back(current_image_number-1))

    assembly()

def back(image_number):
    global album_cover
    global play_button
    global pause_button
    global skip_button
    global back_button

    album_cover.grid_forget()

    album_cover = Label(root, image=song_image_list[image_number-1])
    play_button = Button(root, image=play_img, command=lambda: play)
    pause_button = Button(root, image=pause_img, command=lambda: pause)

    skip_button = Button(root,  image=skip_img, command=lambda: skip(image_number+1))

    if image_number == 1:
        back_button = Button(root, image=back_img, state=DISABLED)
    else:
        back_button = Button(root, image=back_img, command=lambda: back(image_number-1))

    assembly()


#Widget Initializations
album_cover = Label(image=img1)

play_button = Button(root, image=play_img, command=lambda: play)
pause_button = Button(root, image=pause_img, command=lambda: pause)
skip_button = Button(root,  image=skip_img, command=lambda: skip(2))
back_button = Button(root, image=back_img, state=DISABLED)

#Widget Assembly

def assembly():
    album_cover.grid(row=0, column=1, columnspan=3)

    back_button.grid(row=1, column=1)
    play_button.grid(row=1, column=2)
    skip_button.grid(row=1, column=3)

assembly()

#mainloop
root.mainloop()