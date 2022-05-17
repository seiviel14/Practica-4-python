class el:
    def __init__(self,n,p,b,u):
        self.__nom = n
        self.__preu = p
        self.__ind = b
        self.__usos = u
    
    def __str__(self):
        return str(self.__nom)+","+str(self.__preu)+","+str(self.__ind)+","+str(self.__usos)
    
    def __repr__(self):
        return str(self.__nom)+","+str(self.__preu)+","+str(self.__ind)+","+str(self.__usos)

    def nom(self):
        return self.__nom

    def preu(self):
        return self.__preu

    def indicador(self):
        return self.__ind

    def usos(self):
        return self.__usos

