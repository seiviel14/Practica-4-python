from typing import Text
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import math

from PyQt5.uic.uiparser import QtCore, QtWidgets

class Modul(QWidget):
    sortida = pyqtSignal(float)
    def __init__(self,parent,nom_modul):
        super().__init__(parent)
        self.setGeometry(0,0,100,500)
        self.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(nom_modul,self) 
        self.value = 0.5
        self.maxValue = 1.0
        self.minValue = -1.0
    
    def entrada(self,valor):
        self.value = valor
    
    def sortidaValor(self):
        self.sortida.emit(self.value)

    def paintEvent(self,e):
        p = QPainter(self)
        p.drawRect(0,20,99,99)
        if self.value < 0:
            p.setPen(QColor(0,255,0,255))
        elif self.value >= 0:
            p.setPen(QColor(255,0,0,255))
        p.drawLine(50,70,50,(self.value*16)+70)


    
class Generador(Modul):
    def __init__(self,parent,nom_modul):
        super().__init__(parent,nom_modul)
        
        
        
        self.temps=0
        self.slider1 = QSlider(self)
        self.slider2 = QSlider(self)
        self.slider3 = QSlider(self)

        self.slider1.setGeometry(0,120,100,20)
        self.slider1.setOrientation(Qt.Horizontal)
        self.slider1.setMaximum(30)
        self.slider1.setValue(0)
        self.slider1.setSingleStep(1)

        self.slider2.setGeometry(0,140,100,20)
        self.slider2.setOrientation(Qt.Horizontal)
        self.slider2.setMaximum(400)
        self.slider2.setValue(0)
        self.slider2.setSingleStep(1)

        self.slider3.setGeometry(0,160,100,20)  
        self.slider3.setOrientation(Qt.Horizontal)
        self.slider3.setMaximum(628)
        self.slider3.setValue(0)
        self.slider3.setSingleStep(1)
        
    def calcul(self):
        self.amplitud = self.slider1.value()/10
        self.frecuencia = self.slider2.value()/100
        self.fase = self.slider3.value()/100
        self.value = self.amplitud*math.sin(self.temps*2*math.pi*self.frecuencia+self.fase)
        self.update()
        self.sortidaValor()
        
    def temporitzador(self):
        self.temps += 0.01
        self.calcul()
        
class Visor(Modul):
    def __init__(self, parent, nom_modul):
        super().__init__(parent, nom_modul)
        self.posicions = []
        for i in range(0,98):
            self.posicions.append(0)
        self.tipus = 0
        self.boto1 = QPushButton(self)
        self.boto1.setGeometry(0,120,50,20)
        self.boto1.setText('Punts')
        self.boto1.clicked.connect(self.punts)
        self.boto2 = QPushButton(self)
        self.boto2.setGeometry(0,140,50,20)
        self.boto2.setText('Linea')
        self.boto2.clicked.connect(self.linea)
        self.boto3 = QPushButton(self)
        self.boto3.setGeometry(0,160,50,20)
        self.boto3.setText('Ple')
        self.boto3.clicked.connect(self.ple)

    def punts(self):
        self.tipus = 0
    
    def linea(self):
        self.tipus = 1

    def ple(self):
        self.tipus = 2
        

    def paintEvent(self,e):
        self.posicions.append(self.value)
        if len(self.posicions) > 98:
            self.posicions.pop(0)
        p = QPainter(self)
        p.drawRect(0,20,99,99)
        if self.tipus == 0:
            for i in range(1,len(self.posicions)):
                if self.posicions[i] < 0:
                    p.setPen(QColor(0,255,0,255))
                elif self.posicions[i] >= 0:
                    p.setPen(QColor(255,0,0,255))
                p.drawPoint(i,self.posicions[i]*16+70)
        elif self.tipus == 1:
            for i in range(1,len(self.posicions)-1):
                if self.posicions[i] < 0:
                    p.setPen(QColor(0,255,0,255))
                elif self.posicions[i] >= 0:
                    p.setPen(QColor(255,0,0,255))
                p.drawLine(i,self.posicions[i]*16+70,i+1,self.posicions[i+1]*16+70)
        elif self.tipus == 2:
            for i in range(1,len(self.posicions)):
                if self.posicions[i] < 0:
                    p.setPen(QColor(0,255,0,255))
                elif self.posicions[i] >= 0:
                    p.setPen(QColor(255,0,0,255))
                p.drawLine(i,70,i,self.posicions[i]*16+70)
        self.update()

class Amplificador(Modul):
    def __init__(self, parent, nom_modul):
        super().__init__(parent, nom_modul)
        self.slider = QSlider(self)
        self.slider.setGeometry(0,120,100,20)
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setMaximum(30)
        self.slider.setMinimum(1)
        self.slider.setSingleStep(1)
        self.slider.setValue(10)

    
    def amplificacio(self): #Hem comprobat que la amplificació es dona en valors, però a l'hora de fer el dibuix, el painter no ho té en compte
        self.value = self.value*(self.slider.value()/10)
        self.update()
        self.sortidaValor()

    def temporitzador(self):
        self.amplificacio()



class Filtre(Modul):
    def __init__(self, parent, nom_modul):
        super().__init__(parent, nom_modul)
        self.slider1 = QSlider(self)
        self.slider2 = QSlider(self)

        self.slider1.setGeometry(0,120,100,20)
        self.slider1.setOrientation(Qt.Horizontal)
        self.slider1.setMaximum(30)
        self.slider1.setMinimum(1)
        self.slider1.setPageStep(1)
        self.slider1.setValue(10)

        self.slider2.setGeometry(0,140,100,20)
        self.slider2.setOrientation(Qt.Horizontal)
        self.slider2.setMaximum(30)
        self.slider2.setMinimum(0)
        self.slider2.setPageStep(1)
        self.slider2.setValue(10)
    
    def temporitzador(self):
        self.filtracio()

    def filtracio(self):    #Hem comprobat que la filtració es dona en valors, però a l'hora de fer el dibuix el painter tampoc ho té en compte
        if self.value > self.slider1.value()*1.6:
            self.value = self.slider1.value()*1.6
        elif self.value < -self.slider2.value()*1.6:
            self.value = -self.slider2.value()*1.6
        self.sortidaValor()
        self.update()