# Script for placing meta tags in tracks from the filename
# Place in the directory with the music -> run
import mutagen
# from mutagen.mp3 import MP3
from os import scandir

from mutagen.easyid3 import EasyID3

root = './'
l_archivos = sorted([archivo.name for archivo in scandir(root) if archivo.is_file() and archivo.name.endswith('.mp3')])

def generate_title(filedata):
    # Join all parts except the first (artist)
    return ' - '.join(filedata[1:])

def edit_Media_Data():
    for idx, filename in enumerate(l_archivos, start=1):
        try:
            file = EasyID3(filename)
        except mutagen.id3.ID3NoHeaderError:
            # If no ID3 tag, create one
            file = mutagen.File(filename, easy=True)
            file.add_tags()
        except Exception as err:
            print(f"Skipping {filename} due to error: {err}")
            continue

        filedata = filename.replace('.mp3', '').split(' - ')
        if len(filedata) < 2:
            print(f"Skipping {filename}: unexpected filename format")
            continue

        artist = filedata[0]
        title = generate_title(filedata)

        file['artist'] = artist
        file['title'] = title.strip()
        file.save()

        print(f"{idx}. ✅ Updated: {artist} - {title}")

if __name__ == "__main__":
    edit_Media_Data()