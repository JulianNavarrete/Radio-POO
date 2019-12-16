
class Library:

    __radios = []

    def addRadio(self, radio): # Este metodo agrega una radio
        self.__radios.append(radio)

    def getRadios(self): # Este metodo obtiene la lista de radios
        return self.__radios

    def deleteRadio(self, position): # Elimina una radio en una posicion específica
        return self.__radios.pop(position)

