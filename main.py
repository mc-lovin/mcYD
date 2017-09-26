from __future__ import unicode_literals
import youtube_dl
import sys
import os.path
import re

from download import fetch_url_for_song

YOUTUBE_PREFIX = 'http://www.youtube.com/watch?v='
DEVELOPER_KEY = ''

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def download_from_youtube(url):
	ydl_opts = {
	    'format': 'bestaudio/best',
	    'postprocessors': [{
	        'key': 'FFmpegExtractAudio',
	        'preferredcodec': 'mp3',
	        'preferredquality': '192',
	    }],
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download([url])

def process_request_for_song(song_name):
	print bcolors.HEADER + 'Starting: ' + song_name + bcolors.ENDC
	id, name = fetch_url_for_song(song_name + ' song', DEVELOPER_KEY)
	url = YOUTUBE_PREFIX + id
	file_name = name + '-' + id + '.mp3'
	file_name = re.sub('\|+','_', file_name)

	if os.path.isfile(file_name):
		print bcolors.OKBLUE + 'Song already downloaded' + bcolors.ENDC
		return
	try:
		download_from_youtube(url)
		print bcolors.OKGREEN + 'Downloaded: ' + song_name + bcolors.ENDC
	except:
		pass


def read_from_file(file_name):
	print bcolors.WARNING + 'Reading from file: ' + file_name + bcolors.ENDC
	f = open(file_name, 'r')
	for line in f:
		song_name = line.strip()
		process_request_for_song(song_name)


if __name__ == '__main__':
	args = sys.argv

	if len(args) <= 3:
		print "Usage:-"
		print "python manage.py APIKEY --file file_name"
		print "python manange.py APIKEY --song song_name"
		exit()

	DEVELOPER_KEY = args[1]

	if args[2] == '--file':
		read_from_file(args[3])
	else:
		song_name = ' '.join(args[3:])
		process_request_for_song(song_name)
