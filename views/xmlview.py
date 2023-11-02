from controllers.xmlctrl import XMLCtrl

class XMLView:
    def __init__(self, xmlCtrl: XMLCtrl) -> None:
        self.ctrl = xmlCtrl

    def getXMLData(self, name: str):
        return self.ctrl.getInfo(name)