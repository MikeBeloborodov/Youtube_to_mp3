import os
import pathlib
from moviepy.editor import AudioFileClip
from pytube import YouTube


PATH_TO_DOWNLOADS = str(pathlib.Path(__file__).parent.resolve()) + '\Downloads'
WELCOMING_MESSAGE = """
Hello, this is a youtube video to mp3 converter.
Commands:
/start - Shows this message.
/youtube <link to a youtube video> - Downloads and converts a youtube video into an mp3 format audio file,
and sends it back to you.
/delete - Deletes all previously downloaded files from the server.
"""


def convert_mp4_to_mp3(path_to_mp4: str, path_to_mp3: str) -> None:
    """
    Converts mp4 file to mp3 file.
    Arguments: 
        path_to_mp4 [str]: Path to mp4 file you want to convert.
        path_to_mp3 [str]: Path to save converted file in mp3 format.
    """

    file_to_convert = AudioFileClip(path_to_mp4) 
    file_to_convert.write_audiofile(path_to_mp3)
    file_to_convert.close()


def download_youtube_audio(url: str, path_to_file:str) -> str:
    """
    Downloads an audio file from youtube video. 
    Arguments:
        url [str]: A url string from a youtube video.
        path_to_file [str]: Path for saving the file.
    Return:
        file_name [str]: The name of a downloaded file.
    """

    youtube_video = YouTube(url)

    streams = youtube_video.streams.filter(only_audio=True, file_extension="mp4")
    best_quality_stream = streams[-1]
    best_quality_stream.download(output_path=path_to_file)
    file_name = youtube_video.title

    return file_name


def delete_files() -> None:
    """
    Deletes all files in Downloads folder.
    """

    file_names = os.listdir(PATH_TO_DOWNLOADS)
    for file in file_names:
        os.remove(PATH_TO_DOWNLOADS + "/" + file)
