import time


class Instant:
    def __init__(self):
        self.__time = time.gmtime()


    def __int__(self):
        return int(time.mktime(self.__time))
    
    def __str__(self):
        return time.strftime("%H"+"h"+"%M"+"m"+"%S"+"s",self.__time)

#time.gmtime(secs) para convertir de segundos a no segundos