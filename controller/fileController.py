# IMPORTS
from os import path, rename, listdir
from pathlib import Path
from fleep import get as fleepGet
from utils import composeIndex
from model.Track import Track
from model.Tracks import Tracks
from utils import MAX_TRACK_FOLDER

def listfile(refPath):
    files = listdir(refPath)
    files = [f for f in files if path.isfile(refPath + '\\' + f)]
    results = []

    # Filtra i file audio
    for e in files:
        with open(refPath + '\\' + e, 'rb') as file:
            if fleepGet(file.read(128)).type == ['audio']:
                results.append(e)

    return results

def manageFile(path):
    files = listfile(path)
    tracks = Tracks(path)
    folderIndex = 1
    fileIndex = 1

    for i in range(len(files)):
        # Componi tutti i dati necessari
        try:
            folderPath = path + str("\\") + composeIndex(folderIndex) + str("\\") + composeIndex(fileIndex) + Path(files[i]).suffix.lower()
        except Exception:
            print(files[i])

        singleTrack = Track(
            index = composeIndex(fileIndex),
            name = files[i],
            abspath = path + "\\" + files[i],
            folderpath = folderPath,
            folderIndex = composeIndex(folderIndex)
        )

        # Aggiungi il brano alla collezione
        tracks.addTrack(singleTrack)

        if (i + 1) % MAX_TRACK_FOLDER == 0:
            folderIndex += 1
            fileIndex = 1
        else:
            fileIndex += 1

    return tracks

def moveTrack(tracks):
    for track in tracks.getTracks():
        rename(track.absPath, track.folderPath)