from controllers.filesysctrl import FileSystemCtrl
from controllers.replacementctrl import ReplacementCtrl
from controllers.xmlctrl import XMLCtrl
from envs.env import Environment
from models.filesystypes import FileSysTypes
from views.filesysview import FileSystemView
from views.replacementview import ReplacementView
from views.xmlview import XMLView

environment = Environment()
fileSystemView = FileSystemView(FileSystemCtrl(environment.originPath))

xmlFilesNames = fileSystemView.getFilesNamesByExtention(FileSysTypes.XML)
xmlFilesDict = dict[str, str](map(lambda xmlFileName: [ xmlFileName, fileSystemView.getFile(xmlFileName) ], xmlFilesNames))
xmlView = XMLView(XMLCtrl(xmlFilesDict))

class XMLsToObjs:
    def __init__(self) -> None:
        self.__replaceData = []
    
    def setReplaceData(self, replaceData: list[tuple[str, str]]):
        self.__replaceData = replaceData
    
    def dynamicReplacementByXMLAttributes(self, tagsAndAttrs: list[tuple[str, list[str]]]):
        global xmlView
        xmlView = XMLView(XMLCtrl(xmlFilesDict, tagsAndAttrs))
    
    def getXMLsObjs(self):
        # for xmlFileName in xmlFilesNames:
        #     print(xmlView.getAttributesByTagName(xmlFileName, 'cfdi:Comprobante'))
        #     print(xmlView.getAttributesByTagName(xmlFileName, 'tfd:TimbreFiscalDigital'))
        return list(map(lambda xmlFileName: xmlView.getXMLData(xmlFileName, ReplacementView(ReplacementCtrl(self.__replaceData))), xmlFilesNames))