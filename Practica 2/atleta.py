class Atleta:
    def Omplir(self):
        self.__nom = input("Nom de l'atleta: ")
        self.__categoria = input("Categoría: ")

    def __str__(self):
        return self.__nom+", categoría "+self.__categoria

class A_Amateur(Atleta):
    def Omplir(self):
        super().Omplir()
        self.__municipi = input("Nom del municipi: ")

    def __str__(self):
        return super().__str__()+". Amateur, "+self.__municipi

class A_Federat(Atleta):
    def Omplir(self):
        super().Omplir()
        self.__num_federat = input("Número de federat: ")
    
    def __str__(self):
        return super().__str__()+". #"+self.__num_federat

class A_Club(A_Federat):
    def Omplir(self):
        super().Omplir()
        self.__nom_club = input("Nom del club: ")
    
    def __str__(self):
        return super().__str__()+" del club "+self.__nom_club