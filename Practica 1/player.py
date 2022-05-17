from quality import qualitat

class jugador:
    def __init__(self,n,s,r,stre,mgc,vlc,ele):
        self.__nom = n
        self.__salut = s
        self.__riquesa = r
        self.__qualitats = qualitat(stre,mgc,vlc)
        self.__elements = ele
    
    def __str__(self):
        qualit = str(self.__qualitats)
        qualit = qualit.split(",")
        llistaElements = ""
        for element in self.__elements:
            print(self.__elements)
            llistaElements = llistaElements+element[0]+","+str(element[1])+"*"
        llistaElements = llistaElements.strip("*")
        return str(self.__nom)+","+str(self.__salut)+","+str(self.__riquesa)+","+qualit[0]+","+qualit[1]+","+qualit[2]+"/"+llistaElements
        
    def guardar(self):
        qualit = str(self.__qualitats)
        qualit = qualit.split(",")
        llistaElements = ""
        for element in self.__elements:
            llistaElements = llistaElements+element[0]+","+str(element[1])+"*"
        llistaElements = llistaElements.strip("*")
        return str(self.__nom)+","+str(self.__salut)+","+str(self.__riquesa)+","+qualit[0]+","+qualit[1]+","+qualit[2]+"/"+llistaElements

        '''
        return "El personatge "+self.__nom+" té:\n"
        +str(self.__salut)+" punts de salut\n"
        +"Una riquesa de "+str(self.__riquesa)+"\n"
        +"Una força de "+str(self.__força)+"\n"
        +"Una magia de "+str(self.__magia)+"\n"
        +"Una velocitat de "+str(self.__velocitat)+"\n"
        +"I els elements "+self.__elements
        '''


    def __repr__(self):
        qualit = str(self.__qualitats)
        qualit = qualit.split(",")
        return str(self.__nom)+","+str(self.__salut)+","+str(self.__riquesa)+","+qualit[0]+","+qualit[1]+","+qualit[2]+","+str(self.__elements)

    def afegirElement(self, nomElement, usos):
        print(nomElement,usos)
        self.__elements.append([nomElement,usos])

    def disminuirElement(self, nomElement):
        for element in self.__elements:
            if element[0] == nomElement:
                element[1] -= 1
                if element[1] <= 0:
                    self.__elements.pop(self.__elements.index(element))
                    return True
        return False

    def nom(self):
        return self.__nom
    def salut(self):
        return self.__salut
    def riquesa(self):
        return self.__riquesa
    def força(self):
        return self.__qualitats.stre()
    def magia(self):
        return self.__qualitats.mgc()
    def velocitat(self):
        return self.__qualitats.vlc()
    def elements(self):
        return self.__elements

    def sSalut(self,variacio):
        self.__salut += variacio
    def sRiquesa(self,variacio):
        self.__riquesa += variacio
    def sForça(self,variacio):
        self.__qualitats.setForça(variacio)
    def sMagia(self,variacio):
        self.__qualitats.setMagia(variacio)
    def sVelocitat(self,variacio):
        self.__qualitats.setVelocitat(variacio)
    def sElements(self,element):
        self.__elements = element