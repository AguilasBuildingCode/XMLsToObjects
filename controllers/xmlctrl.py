import xml.etree.ElementTree as et
from xml.dom import minidom
from xmljson import badgerfish
import json
from controllers.replacementctrl import ReplacementCtrl

class XMLCtrl:
    def __init__(self, xmlFiles: dict[str, str], tagsAndAttrs: list[tuple[str, list[str]]] = []) -> None:
        self.xmls = xmlFiles
        self.__tagsAndAttrs = tagsAndAttrs

    def getAttributesByTagName(self, name: str, tag: str):
        xmlPath = self.xmls.get(name)
        if xmlPath == None:
            return None
        xmlMin = minidom.parse(xmlPath)
        elements = xmlMin.getElementsByTagName(tag)
        if len(elements) <= 0:
            return None
        return list(map(lambda el: dict(list(el.attributes.items())), elements))
    
    def __dynamicReplacementByXMLAttributes(self, name: str, data: str):
        for tag, attrs in self.__tagsAndAttrs:
            tagAttrs = self.getAttributesByTagName(name, tag)
            if tagAttrs != None:
                for attr in attrs:
                    for ta in tagAttrs:
                        taValue = ta.get(attr)
                        if taValue != None:
                            data = data.replace('{' + taValue + '}', '').replace(taValue, '')
        return data

    def getInfo(self, name: str, replacement: ReplacementCtrl = ReplacementCtrl([])) -> dict[str, any]:
        xmlPath = self.xmls.get(name)
        if xmlPath == None:
            return None
        xmlET = et.parse(xmlPath)
        data = json.dumps(badgerfish.data(xmlET.getroot()))
        data = replacement.replace(data)
        data = self.__dynamicReplacementByXMLAttributes(name, data)
        return dict(json.loads(data))