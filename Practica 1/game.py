from player import jugador
from element import el

class game:
    def __init__(self,p = [],ele = [] ,elA = []):
        self.__jugadors = p
        self.__elements = ele
        self.__elementsActuals = elA
        

    def __str__(self):
        return "Els jugadors disponibles són: "+self.__jugadors+"\n"+"Els elements a l'entorn són: "+self.__elementsA

    def afegirJugador(self,nomJugador,força,magia,velocitat):
        for jugadorAlmacenat in self.__jugadors:
            if nomJugador == jugadorAlmacenat.nom():
                return False
        self.__jugadors.append(jugador(nomJugador, 100, 50,força,magia,velocitat,[]))

    def eliminarJugador(self, nomJugador):
        for jugador in self.__jugadors:
            if nomJugador == jugador.nom():
                self.__jugadors.pop(self.__jugadors.index(jugador))
                return "Jugador eliminat correctament"
        return "Jugador no existent"

    def decrementarSalut(self, nomJugador, quantitat):
        for jugador in self.__jugadors:
            if nomJugador == jugador.nom():     
                jugador.sSalut(-int(quantitat))
                if jugador.salut() <= 0:
                    self.eliminarJugador(nomJugador)
                return jugador.salut()

    def comprarElement(self, nomJugador, nomElement):
        for jugadorEscogit in self.__jugadors:
            if nomJugador == jugadorEscogit.nom():
                for element in self.__elementsActuals:
                    if nomElement == element[0].nom() and element[1]!= 0:
                        if jugadorEscogit.riquesa() >= element[0].preu():
                            jugadorEscogit.sRiquesa(-element[0].preu())
                            jugadorEscogit.afegirElement(element[0].nom(),element[0].usos())
                            element[1] -= 1
                            if element[1] == 0:
                                self.__elementsActuals.pop(element)
                            return "El jugador "+nomJugador+" ha comprat l'element "+nomElement
                        return "No tens diners suficients"
        return "No hi ha aquest objecte a l'entorn"



    def usarElement(self, nomJugador, nomElement):
        for jugador in self.__jugadors:
            print(jugador)
            if nomJugador == jugador.nom():
                objecteEliminat = jugador.disminuirElement(nomElement)
                if objecteEliminat == True:
                    return "Element "+nomElement+" utilitzat per "+nomJugador+" i esgotat"
                else:
                    return "Element "+nomElement+" utilitzat per "+nomJugador
                        

    def modificarQualitat(self, nomJugador, qualitat, quantitat):
        for jugador in self.__jugadors:
            if nomJugador == jugador.nom():
                if qualitat == "força":
                    jugador.sForça(quantitat)
                    return "La força de "+nomjugador+" es ara de "+str(jugador.força())
                elif qualitat == "magia":
                    jugador.sMagia(quantitat)
                    return "La magia de "+nomjugador+" es ara de "+str(jugador.magia())
                elif qualitat == "velocitat":
                    jugador.sVelocitat(quantitat)
                    return "La velocitat de "+nomjugador+" es ara de "+str(jugador.velocitat())

    def mostrarPartida(self):
        return str(self.__jugadors)+str(self.__elementsActuals)

    def lluita(self, jugador1,jugador2):
        for jugadorLluita1 in self.__jugadors:
            if jugador1 == jugadorLluita1.nom():
                for jugadorLluita2 in self.__jugadors:
                    if jugador2 == jugadorLluita2.nom():
                        comparacioForça = int(jugadorLluita1.força()) - int(jugadorLluita2.força())
                        comparacioMagia = int(jugadorLluita1.magia()) - int(jugadorLluita2.magia())
                        comparacioVelocitat = int(jugadorLluita1.velocitat()) - int(jugadorLluita2.velocitat())
                        if 10> comparacioForça > 0:
                            jugadorLluita2.sSalut(-comparacioForça)
                        if -10 < comparacioForça < 0:
                            jugadorLluita1.sSalut(comparacioForça)
                        if 10> comparacioMagia > 0:
                            jugadorLluita2.sSalut(-comparacioMagia)
                        if -10 < comparacioMagia < 0:
                            jugadorLluita1.sSalut(comparacioMagia)
                        if 10> comparacioVelocitat > 0:
                            jugadorLluita2.sSalut(-comparacioVelocitat)
                        if -10 < comparacioVelocitat < 0:
                            jugadorLluita1.sSalut(comparacioVelocitat)
                        if jugadorLluita1.salut() <= 0:
                            self.eliminarJugador(jugador1)
                        if jugadorLluita2.salut() <= 0:
                            self.eliminarJugador(jugador2)
        

    def guardarPartida(self):
        fitxer = open("save.txt", mode = "w")
        llinea1 = ""
        llinea2 = ""
        for jugador in self.__jugadors:
            llinea1 += str(jugador)+";"
        fitxer.write(llinea1)
        fitxer.write("\n")
        for element in self.__elementsActuals:
            llinea2 += str(element[0])+","+str(element[1])+";"
        fitxer.write(llinea2)
        fitxer.close()

    def recuperarPartida(self):
        self.__jugadors.pop(0)
        fitxer = open("save.txt", mode = "r")
        jugadors = fitxer.readline()
        jugadors = jugadors.strip("\n")
        jugadors = jugadors.split(";")
        jugadors.pop(len(jugadors)-1)
        for jugadorGuardat in jugadors:
            jugadorGuardat = jugadorGuardat.split("/")
            elementsJugador = jugadorGuardat[1]
            jugadorGuardat = jugadorGuardat[0]
            jugadorGuardat = jugadorGuardat.split(",")
            elementsJugador = elementsJugador.split("*")
            llistaElementsJugador = []
            print(elementsJugador)
            for elements in elementsJugador:
                elements = elements.split(",")
                llistaElementsJugador.append(elements)
            if len(elementsJugador) < 2:
                elementsJugador = []
            else:
                for canviUsos in llistaElementsJugador:
                    canviUsos[1] = int(canviUsos[1])
                elementsJugador = llistaElementsJugador
            self.__jugadors.append(jugador(jugadorGuardat[0],int(jugadorGuardat[1]),int(jugadorGuardat[2]),int(jugadorGuardat[3]),int(jugadorGuardat[4]),int(jugadorGuardat[5]),elementsJugador))
        
        
        elementsGuardats = fitxer.readline()
        elementsGuardats = elementsGuardats.split(";")
        elementsGuardats.pop(len(elementsGuardats)-1)
        for elementGuardat in elementsGuardats:
            elementAlmacenat = False
            elementEntorn = False
            elementGuardat = elementGuardat.split(",")
            for element in self.__elements:
                if elementGuardat[0] == element.nom():
                    for elementActual in self.__elementsActuals:
                        if elementGuardat[0] == elementActual[0].nom():
                            elementActual[1] += int(elementGuardat[5])
                            elementEntorn = True

                    elementAlmacenat = True
            if elementAlmacenat == False:
                self.__elements.append(el(elementGuardat[0],elementGuardat[1],elementGuardat[2],elementGuardat[3]))
            if elementEntorn == False:
                self.__elementsActuals.append([el(elementGuardat[0],int(elementGuardat[1]),int(elementGuardat[2]),int(elementGuardat[3])),int(elementGuardat[4])])
        fitxer.close()

    def carregarPartida(self):
        fitxer = open("elements.txt", mode = "r")
        elementsGuardats = fitxer.readline()
        elementsGuardats = elementsGuardats.split(";")
        for elementGuardat in elementsGuardats:
            elementGuardat = elementGuardat.split(",")
            self.__elements.append(el(elementGuardat[0],elementGuardat[1],elementGuardat[2],elementGuardat[3]))
        fitxer.close()
        self.afegirJugador("jo",10,10,10)
