from instant import *
class Temps:
    def __init__(self):
        self.__abandonat = False

    def sortida(self):
        self.__sortida = Instant()
    
    def arribada(self):
        self.__arribada = Instant()

    def abandonament(self):
        self.__abandonament = Instant()
        self.__abandonat = True 
    
    def rsortida(self): #retorns
        return str(self.__sortida)

    def rarribada(self):
        return str(self.__arribada)

    def rabandonament(self):
        return str(self.__abandonament)
    
    def rsortidaint(self):
        return int(self.__sortida)

    def rarribadaint(self):
        return int(self.__arribada)

    def rabandonamentint(self):
        return int(self.__abandonament)

    def abandonat(self):
        return self.__abandonat

    def temps(self):
        return self.rarribadaint()-self.rsortidaint()

