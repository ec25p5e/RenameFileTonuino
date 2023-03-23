# IMPORTS
from controller.fileController import manageFile, moveTrack
from controller.folderController import generateFolder
from controller.csvController import generateCsv

def inputdata():
    path = input("Path: ")
    outfile = [str(j) for j in input("File di output (keep, tmp) --> senza .csv: ").split(' ')]

    return path, outfile


if __name__ == '__main__':
    refPath, outFileName = inputdata()
    tracks = manageFile(refPath)
    generateCsv(tracks, refPath, outFileName)
    generateFolder(tracks)
    moveTrack(tracks)