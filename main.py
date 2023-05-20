from fastapi import FastAPI
import os
import utils

# create Downloads folder
if not os.path.exists(utils.PATH_TO_DOWNLOADS):
    os.mkdir(utils.PATH_TO_DOWNLOADS)


# initiate FastAPI app
app = FastAPI()


@app.get("/")
def home():
    message = "Welcome to youtube to mp3 conerter!"
    return message


@app.get("/youtube_downloader")
def youtube_downloader():
    url = "https://www.youtube.com/watch?v=V66PMeImkxI"
    file_name = utils.download_youtube_audio(url, utils.PATH_TO_DOWNLOADS)
    path_to_mp4 = utils.PATH_TO_DOWNLOADS + "/" + file_name + ".mp4"
    path_to_mp3 = utils.PATH_TO_DOWNLOADS + "/" + file_name + ".mp3"
    utils.convert_mp4_to_mp3(path_to_mp4, path_to_mp3)


@app.get("/delete_files")
def delete_downloaded_files():
    utils.delete_files()
