from utils import composeIndex
from os import path, makedirs

def generateFolder(tracks):
    for i in range(tracks.getNumFolder()):
        completePath = str(tracks.basePath) + str("\\") + str(composeIndex(i + 1))

        try:
            if not path.exists(completePath):
                makedirs(completePath)
        except OSError as e:
            print(e)