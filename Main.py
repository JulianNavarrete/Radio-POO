from Library import *
from Radio import *
from RadioManager import *


class Main:

    def __init__(self):
        self.__exitProgram = False
        self.__exitMenu = False
        print("Bienvenido a Radio Streamer.\n"
              "Copyright ©2019. All rights reserved. Julián Software Foundation.\n")

    def menu(self):
        radioManager = RadioManager()
        library = Library() # Este es el objeto que contiene las radios
        library.addRadio(Radio("Truckers FM", "https://radio.truckers.fm/")) # Agrego una radio de prueba 1
        library.addRadio(Radio("Simulator Radio", "http://stream.simulatorradio.com:8002/stream.mp3")) # Agrego una radio de prueba 2
        library.addRadio(Radio("TruckSim FM", "http://radio.trucksim.fm:8000/stream")) # Agrego una radio de prueba 3
        while not self.__exitProgram:
            while not self.__exitMenu:
                try:
                    print("Menú Principal.\nSeleccione una acción:")
                    numMenu = int(input("\t1. Elegir emisora para reproducir\n"
                                        "\t2. Mostrar lista de emisoras disponibles\n"
                                        "\t3. Mostrar lista de emisoras detallada, con sus links\n"
                                        "\t4. Agregar emisora\n\t5. Eliminar emisora\n\t6. Salir del programa\n"
                                        "Su elección: "))

                    if numMenu == 1:
                        radioManager.selectRadio(library)

                    elif numMenu == 2:
                        radioManager.showRadios(library)

                    elif numMenu == 3:
                        radioManager.showDetailedRadios(library)

                    elif numMenu == 4:
                        print("\n".strip("\n"))
                        name = input("Ingrese nombre de la radio: ")
                        url = input("Ingrese URL: ")
                        if len(name) and len(url) != 0:
                            print("\n".strip("\n"))
                            print("Emisora agregada con éxito.")
                            print("\n".strip("\n"))
                            radio = Radio(name, url) # Creo un objeto con dos atributos que se los pido arriba al usuario
                            library.addRadio(radio) # Agrego una radio a la libreria
                        else:
                            print("\n".strip("\n"))
                            print("Error, no se ha podido agregar emisora. Nombre y/o URL no válidos.")
                            print("\n".strip("\n"))

                    elif numMenu == 5:
                        radioManager.showDetailedRadios(library)
                        position = int(input("Ingrese el índice de la radio que quiera eliminar.\nPara "
                                             "cancelar la operación solo presione Enter: "))
                        print("\n".strip("\n"))
                        if position > 0:
                            library.deleteRadio(position - 1)
                            print("Radio eliminada con éxito.")
                            print("\n".strip("\n"))
                        else:
                            print("Operación cancelada exitosamente.")
                            print("\n".strip("\n"))

                    elif numMenu == 6:
                        self.__exitProgram = True
                        self.__exitMenu = True
                        print("\nPrograma cerrado con éxito, ¡Hasta luego!\n", end="")

                    else:
                        print("\nError, opción no existente. Por favor elija una opción válida.\n")
                        self.__exitMenu = False

                except:
                    print("\nError, opción no existente. Por favor elija una opción válida.\n")
                    self.__exitMenu = False


menuPrincipal = Main()
menuPrincipal.menu()
