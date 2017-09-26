Youtube Downloader
===================

Download bundle of songs in mp3 format easily.

You would need to register below to get a google developer API key

https://developers.google.com/api-client-library/python/guide/aaa_apikeys

Installation
============

Use `./install.sh` or `./install_mac.sh` depending on your os


Usage
=====
```
python main.py dev_key --file file_name
python main.py dev_key -- song song_name
```


Example file `(songs.txt)`
```
armin van buuren dominator
vini vici tribe
mr robot where is my mind
```

and run `python main.py dev_key --file songs.txt`

To download a single song you can do `python main.py dev_key --song all of me`
