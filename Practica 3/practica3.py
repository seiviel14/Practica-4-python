
from typing import Text
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QTime

'''Les propietas modificades al designer són: Valors màxim i mínim de l'Slider (0-1439), els valors màxim i mínim dels dials (0-255), els colors de fons dels dials,
 el nombre de digits dels display LCD (digitCount) i la clasificació automàtica del widget de llista (sortingEnabled) '''

class FinPpal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('practica3.ui',self)
        self.marcarInstant.clicked.connect(self.Premut)                         #Quan fem un click al botó de marcar instant executem la funció Premut
        self.redDial.valueChanged['int'].connect(self.redNumber.display)        #Quan el valor del dial vermell canvia actualicem el display per que mostri el seu valor actual i així successivament amb el verd i blau
        self.greenDial.valueChanged['int'].connect(self.greenNumber.display)
        self.blueDial.valueChanged['int'].connect(self.blueNumber.display)
        self.grayDial.valueChanged['int'].connect(self.redDial.setValue)        #Quan el valor del dial vermell canvia actualicem el valor del display per tal que sigui el mateix del dial, el mateix amb el verd i blau
        self.grayDial.valueChanged['int'].connect(self.greenDial.setValue)
        self.grayDial.valueChanged['int'].connect(self.blueDial.setValue)
        self.redDial.valueChanged['int'].connect(self.canviBg)                  #Quan el valor del dial vermell canvia actualicem el color del fons del widget buit mitjançant la funció canviBg, el dial verd i blau funcionen de la mateixa manera
        self.greenDial.valueChanged['int'].connect(self.canviBg)
        self.blueDial.valueChanged['int'].connect(self.canviBg)
        self.tempsActual.timeChanged['QTime'].connect(self.canviSlider)         #Quan modifiquem l'hora també s'ha de modificar l'Slider i ho fem amb la funció canviSlider
        self.sliderTemps.valueChanged['int'].connect(self.canviTemps)           #Quan modifiquem l'Slider també s'ha de modificar l'hora i ho fem amb la funció canviTemps
        self.llistaHores.itemClicked.connect(self.eliminarHora)                 #Quan clickem un dels elements de la llista aquest s'ha d'esborrar i ho fem amb la funció eliminarHora
        self.temps = QTime(0,0,0)                                               #Variable de tipus QTime que utilitzarem per modificar el widget de temps i tenir com l'hora referenciada
        self.llistaTemps = []                                                   #Llista on guardarem les hores ya almacenades per tal de poder comparar i no tenir duplicats

    def canviBg(self):
        colorRed = self.redDial.value()                                         #Aquestes tres llinies següents son per asignar el valor de cada dial a una variable menys complexa
        colorGreen = self.greenDial.value()
        colorBlue = self.blueDial.value()
        self.displayColor.setStyleSheet("background-color: rgb("+str(colorRed)+", "+str(colorGreen)+", "+str(colorBlue)+");")   #Seguidament amb la funció setStyleSheet introduim una string amb les dades de color que s'haurà de posar el fons del widget buit
    
    def canviTemps(self):
        valorSlider = self.sliderTemps.value()                                  #Aquí asignem el valor de l'slider (int) a una variable menys complexa, cada unitat d'aquesta variable representa 1 minut, per tan 90 minutos equivaldria a 1h i 30min
        tempsM = 0                                                              #Inicialitzem les variables tempsM i tempsH que maracarán els minuts i hores respectivament
        tempsH = 0
        while valorSlider % 60 != 0:                                            #Per tal de no obtenir errors el funcionament del codi a continuació és el següent:
            tempsM += 1                                                         #primer comprovem que el valor de l'slider es multiple de 60 (minuts d'una hora), en cas afirmatiu sabem que no hi ha minuts sobrants, només hores
            valorSlider -= 1                                                    #en cas negatiu sumarem un dels minuts i restarem un dels minuts a l'slider, seguidament tornariem a fer la comprovació fins que els minuts siguin multiples de 60 per no obtenir errors de calcul
        tempsH = int(valorSlider/60)                                            #Asignem a la variable tempsH les hores corresponents
        self.temps = QTime(tempsH,tempsM,0)                                     #Utilitzem les variables int de hores i minuts per pasarla a tipus QTime doncs es el tipus que accepta el widget de temps i no ints
        self.tempsActual.setTime(self.temps)                                    #Finalment utilitzem la funció setTime per introduir la variable QTime amb l'hora adequada

    def canviSlider(self):
        self.temps = self.tempsActual.time()                                    #Pel cas contrari, quan modifiquem el widget d'hora, primer asignem el temps "actual" al widget, a l'hora referenciada
        temps = self.temps.hour()   *60+self.temps.minute()                     #Seguidament, amb les funcions hour() i minute() obtenim les hores i minuts corresponents, en int, de l'hora actual
        self.sliderTemps.setValue(temps)                                        #les hores les multipliquem per 60 doncs el valor a asignar son minuts, sumem els minuts solts i asignem el valor amb setValue() a l'slider

    def Premut(self):
        valorTemps = self.temps.toString()                                      #Amb aquesta funció pasem directament de variable QTime a variable string
        if valorTemps not in  self.llistaTemps:                                 #en cas el temps estigui ja dins del widget llista, fem una comprovació
            self.llistaHores.addItem(valorTemps)                                #si el valor no está dins la llista l'introduïm tant dins del widget com la llista de valors
            self.llistaTemps.append(valorTemps)
            self.llistaTemps.sort()                                             #Amb el sort() fem que la llista tant de widget com d'estructura siguin equivalents en ordre per tal que si eliminem un index al widget facilment ho podem fer a la llista (ho veurem després)

    def eliminarHora(self):                                                     
        lineaActual = self.llistaHores.currentRow()                             #Amb la funció currentRow() obtenim l'index de l'item de la llista que haurém seleccionat previament
        self.llistaHores.takeItem(lineaActual)                                  #Amb la funció takeItem() treiem la linea amb index indicat
        self.llistaTemps.pop(lineaActual)                                       #I com hem dit abans, el widget i la llista son equivalents en organització per tant utilitzem la mateixa variable d'index per treure l'hora desitjada
        
app=QApplication([])
window=FinPpal()
window.show()
app.exec_()