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
        while not self.__exitProgram:

            while not self.__exitMenu:
                # try:
                print("Menú Principal.\nSeleccione una acción:")
                numMenu = int(input("\t1. Elegir emisora para reproducir\n"
                                    "\t2. Mostrar lista de emisoras disponibles\n"
                                    "\t3. Mostrar lista de emisoras detallada, con sus links\n"
                                    "\t4. Agregar emisora\n\t5. Eliminar emisora\n\t6. Salir del programa\n"
                                    "Su elección: "))

                if numMenu == 1:
                    radioManager.selectRadio()

                elif numMenu == 2:
                    radioManager.showRadios()

                elif numMenu == 3:
                    radioManager.showDetailedRadios()

                elif numMenu == 4:
                    radioManager.addRadio()

                elif numMenu == 5:
                    # radioManager.deleteRadio()
                    pass

                elif numMenu == 6:
                    self.__exitProgram = True
                    self.__exitMenu = True
                    print("\nPrograma cerrado con éxito, ¡Hasta luego!")

                else:
                    print("\nError, opción no existente. Por favor elija una opción válida. (While menu)\n")
                    self.__exitMenu = False

                # except:
                    # print("\nError, opción no existente. Por favor elija una opción válida. (While programa)\n")
                    # self.__exitMenu = False


menuPrincipal = Main()
menuPrincipal.menu()
