from pytube import YouTube
from termcolor import colored

# get the url of the video from the user
print(colored("Give us the link of the video:", 'yellow'), end=" ")
URL = input()

# video = YouTube('https://www.youtube.com/watch?v=-SgyhUdJ_TY')
# URL = 'https://www.youtube.com/watch?v=AnBQXaC1ulQ'

# to avoid the YouTube class error "KeyError: 'assets'"
while True:
	try:
		video = YouTube(URL)
		break
	except:
		pass

# print the title of the video
print(colored(f"video name: {video.title}", 'white'))

# to let the user chose if you want to download audio or video
while True:
	print(colored("if you want to download audio or video(a/v): ", 'yellow'), end=" ")
	chose = input()
	if chose == "a" or chose == "v":
		break

# index used to print available formats numbred
index = 1
# formats list used to stock the vailable formats of audio
formats = []
# result list used to stock the vailable formats of video
result = []

# if the user decide to download audio
if (chose == "a"):
	print(colored("This is the available audio format:", 'green'))
	# this loop to print available format of audio
	for i in video.streams.filter(type='audio'):
		# filter available format by audio to just get the audio
		for j in str(i).split():
			# to print if format mp3 or webm or something else
			if "mime_type" in j:
					print(colored(f"({index})", 'white'), end=" ")
					print(colored(j.split('"')[1].split("/")[1].ljust(4, " "), 'cyan'), end=" ")
			# to print abr like 120kb or something else
			if "abr" in j:
				formats.append(j.split('"')[1])
				print(colored(f"{formats[-1]}", 'cyan'))
				index += 1
	while True:
		try:
			print(colored(f"What the format you want (1..{len(formats)}):", 'yellow'), end=" ")
			audioFormat = int(input())
			while (audioFormat < 1 or audioFormat > len(formats)):
				print(colored(f"Please entre a number between 1 and {len(formats)}: ", 'red'), end=" ")
				try:
					audioFormat = int(input())
				except:
					pass
			break
		except:
			print(colored(f"Please entre a number between 1 and {len(formats)} Not a String..!!", 'red'))
	# to download audio with the chosed format
	video.streams.filter(type='audio')[audioFormat - 1].download()

else:
	print(colored("This is the available video format:", 'green'))
	for i in video.streams.filter(type='video'):
		mp4OrWebm = ''
		if 'None' not in str(i):
			for j in str(i).split():
				if "mime_type" in j:
					mp4OrWebm = j.split('"')[1].split("/")[1].ljust(4, " ")
				# to print the resolution link 1080p or 720p...
				if "res=" in j:
					result.append(mp4OrWebm + ' ' + j.split('"')[1])
	# to sort the available video format
	result.sort()
	for i in result:
		print(colored(f"({str(index).zfill(2)})", 'white'), end=" ")
		print(colored(f"{i}", 'cyan'))
		index += 1
	while True:
		try:
			print(colored(f"What the format you want (1..{len(result)}):", 'yellow'), end=" ")
			choseFormat = int(input())
			while (choseFormat < 1 or choseFormat > len(result)):
				print(colored(f"Please entre a number between 1 and {len(result)}: ", 'red'), end=" ")
				try:
					choseFormat = int(input())
					videoFormat = result[choseFormat - 1].split()[0]
					resolution = result[choseFormat - 1].split()[1]
					# we use first because some times we have duplicated format so the filter function return you an array
					video.streams.filter(res=resolution, file_extension=videoFormat).first().download()
				except:
					pass
			break
		except ValueError:
			print(colored(f"Please entre a number between 1 and {len(result)} Not a String..!!", 'red'))
