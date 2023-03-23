from dataclasses import dataclass
from json import dumps

@dataclass
class Track:
    _index: int
    _name: str
    _abspath: str
    _folderpath: str = ""
    _folderIndex: int = -1

    def __init__(self, index: int, name: str, abspath: str, folderpath: str, folderIndex: int):
        self._index = index
        self._name = name
        self._abspath = abspath
        self._folderpath = folderpath
        self._folderIndex = folderIndex

    def toJson(self):
        return dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

    # =======================
    # === GETTER ============
    # =======================

    @property
    def name(self):
        return self._name

    @property
    def absPath(self):
        return self._abspath

    @property
    def folderPath(self):
        return self._folderpath

    @property
    def folderIndex(self):
        return self._folderIndex

    @property
    def index(self):
        return self._index

    @property
    def folderIndex(self):
        return self._folderIndex

    # =======================
    # === SETTER ============
    # =======================

    @name.setter
    def name(self, name: str):
        self._name = name

    @index.setter
    def index(self, index: int):
        self._index = index