from game import game
import os

#Practica 1 Oriol Vall i Samuel Velasquez

def main():
    funcionament = 0
    partida = game()
    partida.carregarPartida()
    while funcionament == 0:
        print("Agafa estat")
        print("1: Afegir un nou jugador")
        print("2: Eliminar un jugador")
        print("3: Decrementar la salut d'un jugador")
        print("4: Comprar un element")
        print("5: Utilitzar un element")
        print("6: Modificar la qualitat d'un jugador")
        print("7: Mostrar entorn")
        print("8: Lluita entre jugadors")
        print("9: Guardar partida")
        print("10: Recuperar partida")
        print("11: Tancar")
        estat = int(input())
        if estat == 1:
            print("Nom del jugador a afegir")
            nomjugador = input()
            print("Força del jugador a afegir")
            força  = input()
            print("Magia del jugador a afegir")
            magia = input()
            print("Velocitat del jugador a afegir")
            velocitat = input()
            if partida.afegirJugador(nomjugador,força,magia,velocitat) == True:
                print("Jugador "+nomjugador+" creat correctament")
            else:
                print("El jugador "+nomjugador+" ja existeix")

        elif estat == 2:
            print("Nom del jugador a eliminar")
            nomjugador = input()
            print(partida.eliminarJugador(nomjugador))

        elif estat == 3:
            print("Nom del jugador a decrementar salut")
            nomjugador = input()
            print("Quantitat de la vida a decrementar")
            quantitat = input()
            salut = partida.decrementarSalut(nomjugador,quantitat)
            if salut >0:
                print("El jugador "+nomjugador+"té ara una salut de "+str(salut))
            else:
                print("El jugador "+nomjugador+" ha estat eliminat")

        elif estat == 4:
            print("Nom del jugador que comprará l'element")
            nomjugador = input()
            print("Nom de l'element a comprar")
            nomelement = input()
            text = partida.comprarElement(nomjugador,nomelement)
            print(text)

        elif estat == 5:
            print("Nom del jugador que utilitzará l'element")
            nomjugador = input()
            print("Nom de l'element a utilitzar")
            element = input()
            text = partida.usarElement(nomjugador,element)
            print(text)

        elif estat == 6:
            print("Nom del jugador a modificar la qualitat")
            nomjugador = input()
            print("Agafa la qualitat entre: força, magia o velocitat")
            qualitat = input()
            print("Quantitat de modificació de la qualitat tant en positiu com en negatiu")
            quantitat = int(input())
            text = partida.modificarQualitat(nomjugador, qualitat,quantitat)
            print(text)

        elif estat == 7:
            print(partida.mostrarPartida())
        elif estat == 8:
            print("Nom del primer jugador que lluitará")
            jugador1 = input()
            print("Nom del segón jugador que lluitará")
            jugador2 = input()
            partida.lluita(jugador1,jugador2)
            print(partida.mostrarPartida())
        elif estat == 9:
            partida.guardarPartida()
            print("Partida guardada")
        elif estat == 10:
            partida.recuperarPartida()
            print("Partida recuperada")
        elif estat == 11:
            funcionament = 1
            print("Sortint...")
        else:
            print("Error, introdueix un valor adequat")

if __name__ == "__main__":
    main()