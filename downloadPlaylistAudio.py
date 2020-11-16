from pytube import Playlist, YouTube
from termcolor import colored
from tqdm import tqdm
import re

print(colored("Please give us the link of the playlist:", 'yellow'), end=" ")
urlOfPlayList = input()

audiosOfPlaylist = Playlist(urlOfPlayList)
audiosOfPlaylist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
audiosUrls = audiosOfPlaylist.video_urls

k = 0
loop = tqdm(total = len(audiosUrls), position = 0, leave = True)

for url in audiosUrls:
	while True:
		try:
			YouTube(url).streams.filter(type="audio").first().download()
			loop.set_description("Downloading".format(k))
			loop.update(1)
			k += 1
			break
		except:
			pass

loop.close()