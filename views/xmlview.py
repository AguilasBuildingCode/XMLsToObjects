from controllers.xmlctrl import XMLCtrl
from views.replacementview import ReplacementView

class XMLView:
    def __init__(self, xmlCtrl: XMLCtrl) -> None:
        self.ctrl = xmlCtrl

    def getXMLData(self, name: str, replacement: ReplacementView):
        return self.ctrl.getInfo(name, replacement.replacementCtrl)
    
    def getAttributesByTagName(self, name: str, tag: str):
        return self.ctrl.getAttributesByTagName(name, tag)