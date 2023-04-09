from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

playlist = Playlist("https://www.youtube.com/playlist?list=PLeg_cM4Xd2vPgSvlBE8CaZFEUutUHIwUU")



for url in playlist: # check for url in the playlist
    print(url)

for vid in playlist.videos: # go to vids in playlist.vids
    print(vid)

for url in playlist: # go to url in playlist
   YouTube(url).streams.filter(only_audio=True).first().download() # select that the audio only

for url in playlist:## go to url in playlist and download in the given directory
    YouTube(url).streams.first().download(" C:\\Users\\LENOVO\\Desktop")

folder = " C:\\Users\\LENOVO\\Desktop" # Destination of download


for file in os.listdir(folder): # go to file in listed directory folder
  if re.search('mp4', file): # check for mp4 file fromat
    mp4_pa = os.path.join(folder,file)
    mp3_pa = os.path.join(folder,os.path.splitext(file)[0]+'.mp3') # describe to add the fiel to path
    fil = mp.AudioFileClip(mp4_pa) # describe the fiel
    fil.write_audiofile(mp3_pa) # write the file instead of mp4
    os.remove(mp4_path) # remove the old mp4 file
