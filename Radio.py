
class Radio:

    def __init__(self, name, url):
        self.__name = name
        self.__url = url

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setURL(self, url):
        self.__url = url

    def getURL(self):
        return self.__url

