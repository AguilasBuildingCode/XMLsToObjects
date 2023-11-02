from controllers.filesysctrl import FileSystemCtrl
from os import path

class FileSystemView:
    def __init__(self, ctrl: FileSystemCtrl) -> None:
        self.folder = ctrl.folder
        self.files = ctrl.files

    def getFilesNamesByExtention(self, extentions: str) -> list[str]:
        return self.getFilesNamesByExtention([extentions])
    
    def getFilesNamesByExtention(self, extentions: tuple[str]) -> list[str]:
        return list(filter(lambda file: file.endswith(extentions), self.files))
    
    def getFile(self, name: str) -> str:
        return path.join(self.folder, name)