import openai
import tkinter as tk
from PIL import ImageTk, Image
from io import BytesIO
import requests

openai.api_key = "API_KEY"
root = tk.Tk()

def getImage(artist, song):
    response = openai.Image.create(
        prompt="Album Cover for {} by {}".format(song, artist),
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    response = requests.get(image)
    img_data = response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))

    return img

# image = getImage('Jay-Z', "Don't Knock tha Hustle")

# panel = tk.Label(root, image=img)
# panel.pack(side="bottom", fill="both", expand="yes")
# root.mainloop()