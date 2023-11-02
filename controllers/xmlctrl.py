import xml.etree.ElementTree as et
from xmljson import badgerfish
import json

class XMLCtrl:
    def __init__(self, xmlFiles: dict[str, str]) -> None:
        self.xmls = xmlFiles

    
    def getInfo(self, name: str) -> dict[str, any]:
        xmlPath = self.xmls.get(name)
        if xmlPath == None:
            return None
        xml = et.parse(xmlPath)
        return dict(json.loads(json.dumps(badgerfish.data(xml.getroot()))))