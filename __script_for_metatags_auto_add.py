# Script for placing meta tags in tracks from the filename
# Place in the directory with the music -> run
import mutagen
# from mutagen.mp3 import MP3
from os import scandir

from mutagen.easyid3 import EasyID3

root = './'
l_archivos = sorted([archivo.name for archivo in scandir(root) if archivo.is_file()])

mutagen.File(l_archivos[1])      # U: See the tags of the data
# print(mutagen)

def edit_Media_Data():

    for f in range(len(l_archivos[:-1])):                 # A: A range of all the fields exept the script
        
        
        if (l_archivos[f].endswith('mp3')):

            try:
                file = EasyID3(l_archivos[f])                         # A: Capture the file to edit
            except BaseException as err:
                print(f"Unexpected {err=}, {type(err)=}")

            filedata = l_archivos[f].replace('.mp3', '').split(' - ')
            file['artist'] = filedata[0]
            file['title'] = generate_title(filedata)
            print(f+1, file['artist'], file['title'])
            file.pprint()
            file.save()

def generate_title(filedata):
    title = ''
    for i in range(len(filedata)-1):
        title+= filedata[i+1] + ' '
    return title

edit_Media_Data()