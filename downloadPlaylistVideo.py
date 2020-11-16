from pytube import Playlist, YouTube
from termcolor import colored
from tqdm import tqdm
import re

print(colored("Please give us the link of the playlist:", 'yellow'), end=" ")
urlOfPlayList = input()

videosOfPlaylist = Playlist(urlOfPlayList)
videosOfPlaylist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
videosUrls = videosOfPlaylist.video_urls

print(colored("If you want the hight resolution or the lowerst resolution:(l/h)[l]", 'yellow'), end=' ')
chose = input()

k = 0
loop = tqdm(total = len(videosUrls), position = 0, leave = True)

for url in videosUrls:
	while True:
		try:
			if chose == "h":
				YouTube(url).streams.filter(type="video").get_highest_resolution().download()
			else:
				YouTube(url).streams.filter(type="video").get_lowest_resolution().download()
			loop.set_description("Downloading".format(k))
			loop.update(1)
			k += 1
			break
		except:
			pass

loop.close()