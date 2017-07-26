import eyed3
import sys
import os
#import exifread
from shutil import copyfile
import json

source_path='Y:\\mp3'
#source_path='C:\\Users\\wolfg\\Pictures'
#dest_path='C:\\Users\\wolfg\\TMP\\'

audiofile = eyed3.load("Y:\\mp3\\Adel Tawil\\So schön anders (Deluxe Version)\\01-05- Worte.mp3")
processed_counter=0

mp3_list={}

for path, subdirs, files in os.walk(source_path):
    for name in files:
        if name.endswith(('.mp3', '.MP3')):
            processed_counter+=1
            ## source file for copy
            old_filename=os.path.join(path, name)
            #print(old_filename)
            try:
                audiofile = eyed3.load(old_filename)
                line = {'artist':audiofile.tag.artist,'album_artist':audiofile.tag.artist,
                        'album':audiofile.tag.album,'title':name}
                mp3_list[old_filename]=line
                
            except:
                line = {'artist':'unbekannt','album_artist':'unbekannt',
                        'album':'unbekannt','title':name}
                mp3_list[old_filename]=line

json.dump(mp3_list, open("mp3_liste.json",'w'))           
            
