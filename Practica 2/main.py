from atleta import *
from cursa import *

def main():
    cursa = 0
    curses = {}
    while cursa == 0:
        seleccio = input("1. Definir una cursa\n2. Inscriure un atleta\n3. Sortida\n4. Abandonament\n5. Arribada\n6. Mostrar cursa\n7. Mostrar participants\n8. Mostrar temps\n9. Clasificacio")  #crear cursa
        if seleccio == '1':
            cursa_actual = None
            indicador = input("indicador de la cursa\n")
            seleccio_cursa = input("cursa\n")
            distancia = input("distancia")
            max_participants = input("max participants\n")
            if seleccio_cursa == '1':     #peu
                cursa_actual = C_Peu(distancia,max_participants)

            elif seleccio_cursa == '2':   #pista
                ciutat = input("ciutat\n")
                estadi = input("estadi\n")
                cursa_actual = C_Pista(distancia,max_participants,ciutat,estadi)

            elif seleccio_cursa == '3':   #cross
                indret = input("indret")
                desnivell_pos = input("des pos\n")
                desnivell_neg = input("des neg\n")
                cursa_actual = C_Cross(distancia,max_participants,indret,desnivell_pos,desnivell_neg)

            elif seleccio_cursa == '4':   #bici
                permis_mossos = input("permis mossos\n")
                cursa_actual = C_Bici(distancia,max_participants,permis_mossos)

            elif seleccio_cursa == '5':   #carretera
                permis_mossos = input("permis mossos\n")
                origen = input("origen\n")
                arribada = input("arribada\n")
                cursa_actual = C_Carretera(distancia,max_participants,permis_mossos,origen,arribada)

            elif seleccio_cursa == '6':   #muntanya
                permis_mossos = input("permis mossos\n")
                indret = input("indret\n")
                desnivell_pos = input("des pos\n")
                desnivell_neg = input("des neg\n")
                cursa_actual = C_Muntanya(distancia,max_participants,permis_mossos,indret,desnivell_pos,desnivell_neg)

            elif seleccio_cursa == '7':   #esqui
                cursa_actual = C_Esqui(distancia,max_participants)
                
            elif seleccio_cursa == '8':   #fons
                cursa_actual = C_Fons(distancia,max_participants)

            elif seleccio_cursa == '9':   #alpi
                desnivell = input("desnivell\n")
                cursa_actual = C_Alpi(distancia,max_participants,desnivell)

            elif seleccio_cursa == '10':  #descens
                desnivell = input("desnivell\n")
                amplada = input("amplada\n")
                cursa_actual = C_Descens(distancia,max_participants,desnivell,amplada)

            elif seleccio_cursa == '11':  #slalom
                desnivell = input("desnivell\n")
                portes = input("portes\n")
                cursa_actual = C_Slalom(distancia,max_participants,desnivell,portes)
            else:
                print("Cursa no existent\n")
            if cursa_actual != None:
                curses[indicador] = cursa_actual
        elif seleccio == '2': #inscriure atleta
            indicador = input("indicador")
            if indicador in curses:
                tipus_atleta = input("tipus")   #1 amateur,2 federat,3 club
                if tipus_atleta == '1' or tipus_atleta == '2' or tipus_atleta == '3':
                    print (curses[indicador].inscriure(tipus_atleta))
                else:
                    print("tipus atleta mal\n")

        elif seleccio == '3': #sortida
            indicador = input("indicador cursa\n")
            mode = input("Conjunta o progressiva\n")
            if mode == '1':
                dorsal = 0
            elif mode == '2':
                dorsal = input("numero de dorsal\n")
            else:
                print("error")
            curses[indicador].sortida(mode,dorsal)
        elif seleccio == '4': #abandonament
            indicador = input("indicador cursa\n")
            dorsal_abandonament = input("dorsal\n")
            curses[indicador].abandonament(dorsal_abandonament)
        elif seleccio == '5': #arribada
            indicador = input("indicador\n")
            dorsal_arribada = input("dorsal\n")
            curses[indicador].arribada(dorsal_arribada)
        elif seleccio == '6': #mostrar cursa
            indicador = input("indicador cursa\n")
            print(str(curses[indicador]))
        elif seleccio == '7': #mostrar participants
            indicador = input("indicador cursa\n")
            print(curses[indicador].mostrar_participants())
        elif seleccio == '8': #mostrar temps
            indicador = input("indicador cursa\n")
            print(curses[indicador].mostrar_temps())
        elif seleccio == '9': #classificació
            indicador = input("indicador cursa")
            print(curses[indicador].classificacio())
        else:
            print("Introdueix un número vàlid")


if __name__ == '__main__':
    main()