class qualitat:
    def __init__(self,stre = 10,mgc = 10,vlc = 10):
        self.__stre = stre    #força
        self.__mgc = mgc      #magia
        self.__vlc = vlc     #velocitat
    
    def __str__(self):
        return str(self.__stre)+","+str(self.__mgc)+","+str(self.__vlc)

    def __repr__(self):
        return str(self.__stre)+","+str(self.__mgc)+","+str(self.__vlc)

    def stre(self):
        return self.__stre
    
    def mgc(self):
        return self.__mgc
    
    def vlc(self):
        return self.__vlc

    def setForça(self,variacio):
        self.__stre += variacio
    def setMagia(self,variacio):
        self.__mgc += variacio
    def setVelocitat(self,variacio):
        self.__vlc += variacio