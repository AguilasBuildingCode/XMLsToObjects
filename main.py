from controllers.filesysctrl import FileSystemCtrl
from controllers.xmlctrl import XMLCtrl
from envs.env import Environment
from models.filesystypes import FileSysTypes
from views.filesysview import FileSystemView
from views.xmlview import XMLView

environment = Environment()
fileSystemView = FileSystemView(FileSystemCtrl(environment.originPath))

xmlFilesNames = fileSystemView.getFilesNamesByExtention(FileSysTypes.XML)
xmlFilesDict = dict[str, str](map(lambda xmlFileName: [ xmlFileName, fileSystemView.getFile(xmlFileName) ], xmlFilesNames))
xmlView = XMLView(XMLCtrl(xmlFilesDict))

for xmlFileName in xmlFilesNames:
    print(xmlFileName)
    for key, value in xmlView.getXMLData(xmlFileName).items():
        print(key)
        print(value)
        print('------------------------------------------------')