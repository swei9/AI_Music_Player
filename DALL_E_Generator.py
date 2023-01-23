import openai
import urllib.request
import os

image_path_album_covers = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images/album-covers")

openai.api_key = ""

def getImage(song):
    response = openai.Image.create(
        prompt="Create a unique album cover for a song called {} that is 500 x 500 pixels. ".format(song),
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    urllib.request.urlretrieve(image_url, os.path.join(image_path_album_covers, "{}.jpg".format(song)))

    return "{}.jpg".format(song)