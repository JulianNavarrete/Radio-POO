from Radio import *
from Library import *
import vlc


class RadioManager:

    count = 0

    def addRadio(self):
        radio.setName()
        print(radio.getName())
        radio.setURL()
        print(radio.getURL())
        # Library.radiosNames.append(tmpRadioName)
        # Library.radiosURLs.append(tmpRadioURL)

    def deleteRadio(self):
        print("\n")
        for x in Library.radiosNames:
            self.count = 0
            self.count += 1
            print(self.count, ". ", x, "\n".strip("\n"))
        index = int(input("Ingrese el índice de la radio que desea eliminar: "))
        print("¿Está seguro que desea eliminar " + Library.radiosNames[index + 1])
        deleteOption = int(input("Para confirmar su desición, ingrese " + '"' + "SI" + '"' + " en mayúsculas.\n"
                                 "Para cancelar la operación, solo pulse " + '"' + "Enter" + '"' + ": "))
        if deleteOption == "SI":
            Library.radiosNames.pop(index - 1)
            Library.radiosURLs.pop(index - 1)
            print("\nSe ha eliminado exitosamente la radio.")
        else:
            print("\nLa operación fue cancelada.")

    def showRadios(self):
        self.count = 0
        print("\nRadios disponibles: ")
        for x in Library.radiosNames:
            self.count += 1
            print("\t" + str(self.count) + ". " + x + "\n".strip("\n"))
        print("\n".strip("\n"))

    def showDetailedRadios(self):
        self.count = 0
        print("\nRadios disponibles: ")
        for x in range(len(Library.radiosNames)):
            self.count += 1
            print(str(self.count) + ". " + Library.radiosNames[x] + "\n".strip("\n"))
            print("\t" + Library.radiosURLs[x] + "\n".strip("\n"))
        print("\n".strip("\n"))

    def selectRadio(self):
        RadioManager.showRadios(self)
        while True:
            indexReproduction = int(input("Ingrese el índice de la radio que desea escuchar: "))
            if indexReproduction < 1:
                print("Error, emisora no existente.\n")
            else:
                print("Reproduciendo emisora: ", Library.radiosNames[indexReproduction - 1])
                input("Presione " + '"' + "Enter" + '"' + " para salir.\n")
                break
        # player.play()

    def saveFile(self):
        # print()
        pass


radioManager = RadioManager()
