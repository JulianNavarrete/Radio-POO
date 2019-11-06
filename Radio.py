from RadioManager import *
from Library import *


class Radio:

    def __init__(self, name, url):
        self.__name = name
        self.__url = url

    def setName(self, name):
        # radioName = input("Para agregar una radio, ingrese el nombre: ")
        # self.__name = radioName

    def getName(self):
        return self.__name

    def setURL(self):
        self.__url = input("Ahora ingrese el link de la radio: ")

    def getURL(self):
        return self.__url


radio1 = Radio()
radio2 = Radio()

'''
radio.setName()
radio.setURL()
print(radio.getName())
print(radio.getURL())
'''
