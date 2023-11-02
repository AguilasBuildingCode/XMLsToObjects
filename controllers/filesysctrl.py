from os import listdir
from os.path import isfile, join

class FileSystemCtrl:
    def __init__(self, folderPath: str) -> None:
        self.folder = folderPath
        self.files = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]