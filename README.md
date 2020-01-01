
# Yt-music-downloader
<center><b>Python3 script to download mmp3 files from YouTube service.</b></center>
You can add links to many videos on yt to file (all of them in separate line) and this sxript download all files to current directory (You may change it) and - owing to <i>FFmpeg </i> codecs it converts all files into *.mp3.

## Requirements
<ul>
<li> Python 3.x.x </li>
<li><a href = ""> youtube-dl</a></li>
<li> FFmpeg codecs (for conversion to mp3) </il>
</ul>

## How to usage

 1. Add links to file (names e.g. <i>list.txt</i>):
 `https://youtube.com/aaaaa` 
` https://youtube.com/bbbbb`
 2. Open terminal and run this code:
   `python3 ytdown.py list.txt`
 3.   Or if you can download file into other directory:
 `python3 ytdown.py -d /path/to/dir/ list.txt`

  







