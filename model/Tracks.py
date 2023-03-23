class Tracks:

    def __init__(self, basePath):
        self._tracks = list()
        self._basePath = basePath
        self._numFolder = 1
        self._numTracks = self.getNumTracks()

    def getNumTracks(self):
        return len(self._tracks)

    @property
    def basePath(self):
        return self._basePath

    def getTracks(self):
        return list(self._tracks)

    def getNumFolder(self):
        self._numFolder = 0
        before = 0

        for track in self._tracks:
            if track.folderIndex != before:
                self._numFolder += 1
            before = track.folderIndex

        return self._numFolder


    def addTrack(self, track):
        self._tracks.append(track)