class ReplacementCtrl:
    def __init__(self, replacementList: list[tuple[str, str]]) -> None:
        self.__replacementList = replacementList
    
    def replace(self, data: str) -> str:
        for old, new in self.__replacementList:
            data = data.replace(old, new)
        return data