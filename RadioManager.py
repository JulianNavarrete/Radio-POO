import vlc


class RadioManager:

    def showRadios(self, library):
        print("\nRadios disponibles: ")
        count = 0
        for x in library.getRadios():
            count += 1
            print("\t" + str(count) + ". " + str(x.getName()) + "\n".strip("\n"))
        print("\n".strip("\n"))

    def showDetailedRadios(self, library):
        count = 0
        print("\nRadios disponibles: ")
        for x in library.getRadios():
            count += 1
            print("\t" + str(count) + ". " + str(x.getName()) + ", link: " + str(x.getURL()) + "\n".strip("\n"))
        print("\n".strip("\n"))

    def selectRadio(self, library):
        conditionExitWhile = False
        lines = []
        self.showRadios(library)
        for x in library.getRadios():
            lines.append(x)
        numSelectRadio = int(input("Seleccione la emisora desea escuchar: ")) - 1
        if 0 <= numSelectRadio < len(lines):
            try:
                volumeLevel = int(input("\nIngrese el nivel de volumen de reproducción\ndel 0 "
                                        "al 150 (por defecto será 40): "))
            except:
                volumeLevel = 40

            # Lógica de reproductor VLC
            Instance = vlc.Instance()
            player = Instance.media_player_new()
            Media = Instance.media_new(lines[numSelectRadio].getURL())
            print("\nReproduciendo:", lines[numSelectRadio].getName())
            Media.get_mrl()
            player.set_media(Media)
            player.play()
            player.audio_set_volume(volumeLevel)
            # Hasta acá la lógica del reproductor
            while not conditionExitWhile:
                try:
                    userStop = input("\nPara detener la reproducción y regresar al menú"
                                     "\nprincipal ingrese la letra " + '"' + "s" + '"' + ". Si desea"
                                     "cambiar el volumen\nde reproducción, ingrese el nuevo volumen "
                                     "deseado: ".strip("\n"))

                    if userStop == "s":
                        player.stop()
                        print("\nSe ha detenido la reproducción.\n")
                        conditionExitWhile = True

                    elif 0 <= int(userStop) <= 150:
                        player.audio_set_volume(int(userStop))
                        print("\nEl volumen de reproducción ha cambiado a:", int(userStop))

                    else:
                        print("\nNivel de volumen no válido.")

                except:
                    conditionExitWhile = False
                    print("\nOpción no existente. Ingrese una opción válida.")

        else:
            print("\nRadio no válida. Intente nuevamente.\n")

