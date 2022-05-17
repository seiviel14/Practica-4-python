from atleta import *
from temps import *
class Cursa:
    def __init__(self,distancia,max_participants):
        self.__distancia = distancia
        self.__max_participants = max_participants
        self.__dorsal = 100
        self.__atletas = {}
        self.__temps = {}
        self.__classificacio = {}

    def __str__(self):
        return "Cursa "+str(self.__distancia)+", "+str(self.__max_participants)+" màx"

    def inscriure(self,tipus_atleta):
        if self.limit_participants() == False:
            self.__tipus_atleta = tipus_atleta
            self.__nou_atleta = None
            comprovacio = False
            if tipus_atleta == '1':
                self.__nou_atleta = A_Amateur()
            elif tipus_atleta == '2':
                self.__nou_atleta = A_Federat()
            elif tipus_atleta == '3':
                self.__nou_atleta = A_Club()
            for atleta in self.__atletas:
                if self.__nou_atleta == self.__atletas[atleta]:
                    self.__comprovacio = True
            if comprovacio == True:
                return "Atleta ja inscrit"
            else:
                self.__atletas[str(self.__dorsal)] = self.__nou_atleta
                self.__atletas[str(self.__dorsal)].Omplir()
                self.__temps[str(self.__dorsal)] = Temps()
                self.__dorsal += 1
                return "Atleta inscrit"
        else:
            return "Llimit superat"
    
    def limit_participants(self):
        if len(self.__atletas) < self.__max_participants:
            return False
        else:
            return True

    def mostrar_participants(self):
        llista_participants = ""
        for keys in self.__atletas:
            llista_participants += "   "+str(keys)+" : "+str(self.__atletas[keys])+"\n"
        return  "Atletes participants\n"+ llista_participants

    def sortida(self,mode,dorsal_sortida):
        if mode == '1':
            for dorsal in self.__atletas:
                self.__temps[dorsal].sortida()
        elif mode == '2':
            self.__temps[dorsal_sortida].sortida()

    def arribada(self,dorsal_arribada):
        self.__temps[dorsal_arribada].arribada()
    
    def abandonament(self,dorsal_abandonament):
        self.__temps[dorsal_abandonament].abandonament()

    def mostrar_temps(self):
        temps_mostrar = ""
        for dorsals in self.__temps:
            if self.__temps[dorsals].rsortida() != None:
                temps_mostrar += dorsals+": "+self.__temps[dorsals].rsortida()+" - "+self.__temps[dorsals].rarribada()+"  "+str(self.__temps[dorsals].temps())+"\n"
            elif self.__temps[dorsals].abandonat() == True:
                temps_mostrar += dorsals+": "+self.__temps[dorsals].rsortida()+" - "+" XXX"
            else:
                temps_mostrar += dorsals+": "+self.__temps[dorsals].rsortida()+" - "
        return "Temps\n"+temps_mostrar

    def classificacio(self):
        classificacions = ""
        ranking = 1
        for dorsal in self.__temps:
            self.__classificacio[dorsal] = self.__temps[dorsal].temps()
        valors_ordenats = sorted(self.__classificacio.values())
        for valor in valors_ordenats:
            for dorsal in self.__classificacio:    
                if valor == self.__classificacio[dorsal]:
                    classificacions = classificacions+str(ranking)+": "+dorsal+"\n"
                    ranking += 1
        return "Classificació\n"+classificacions

        

class C_Peu(Cursa):
    def __init__(self,distancia,max_participants):
        super().__init__(distancia,max_participants)
    
    def __str__(self):
        return super().__str__()+" a peu"

class C_Pista(C_Peu):
    def __init__(self,distancia,max_participants,ciutat,estadi):
        super().__init__(distancia,max_participants)
        self.__ciutat = ciutat
        self.__estadi = estadi

    def __str__(self):
        return super().__str__()+", "+self.__ciutat+", "+self.__estadi

class C_Cross(C_Peu):
    def __init__(self,distancia,max_participants,indret,desnivell_pos,desnivell_neg):
        super().__init__(distancia,max_participants)
        self.__indret = indret
        self.__desnivell_pos = desnivell_pos
        self.__desnivell_neg = desnivell_neg

    def __str__(self):
        return super().__str__()+" a "+self.__indret+", amb desnivells +"+str(self.__desnivell_pos)+"/-"+str(self.__desnivell_neg)

class C_Bici(Cursa):
    def __init__(self,distancia,max_participants,permis_mossos):
        super().__init__(distancia,max_participants)
        self.__permis_mossos = permis_mossos

    def __str__(self):
        if self.__permis_mossos == False:
            return super().__str__()+", en bici, alegal"
        elif self.__permis_mossos == True:
            return super().__str__()+", en bici, legal"
        else:
            return "Permís mal introduit"

class C_Carretera(C_Bici):
    def __init__(self,distancia,max_participants,permis_mossos,origen,arribada):
        super().__init__(distancia,max_participants,permis_mossos)
        self.__origen = origen
        self.__arribada = arribada

    def __str__(self):
        return super().__str__()+", de "+self.__origen+" a "+self.__arribada

class C_Muntanya(C_Bici):
    def __init__(self,distancia,max_participants,permis_mossos,indret,desnivell_pos,desnivell_neg):
        super().__init__(distancia,max_participants,permis_mossos)
        self.__indret = indret
        self.__desnivell_pos = desnivell_pos
        self.__desnivell_neg = desnivell_neg

    def __str__(self):
        return super().__str__()+" a "+self.__indret+", amb desnivells +"+str(self.__desnivell_pos)+"/-"+str(self.__desnivell_neg)

class C_Esqui(Cursa):
    def __init__(self,distancia,max_participants):
        super().__init__(distancia,max_participants)
    def __str__(self):
        return super().__str__()+", d'esquí"

class C_Fons(C_Esqui):
    def __init__(self,distancia,max_participants):
        super().__init__(distancia,max_participants)
    def __str__(self):
        return super().__str__()+" de fons"

class C_Alpi(C_Esqui):
    def __init__(self,distancia,max_participants,desnivell):
        super().__init__(distancia,max_participants)
        self.__desnivell = desnivell

    def __str__(self):
        return super().__str__()+", amb "+str(self.__desnivell)+"m de desnivell"

class C_Descens(C_Alpi):
    def __init__(self,distancia,max_participants,desnivell,amplada):
        super().__init__(distancia,max_participants,desnivell)
        self.__amplada = amplada

    def __str__(self):
        return super().__str__()+", amb "+str(self.__amplada)+" i amplada de "+str(self.__amplada)+"m"

class C_Slalom(C_Alpi):
    def __init__(self,distancia,max_participants,desnivell,portes):
        super().__init__(distancia,max_participants,desnivell)
        self.__portes = portes

    def __str__(self):
        return super().__str__()+" i "+str(self.__portes)+" portes"