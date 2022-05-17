#Samuel Enrique Velasquez i Oriol Vall
from typing import Text
from PyQt5.QtWidgets import *
from PyQt5 import uic
from modul1 import *

class secondWindow(QMainWindow):
    def __init__(self,parent):
        super().__init__()
        self.setGeometry(0,0,1000,1000)
        self.widgetP = QWidget()
        self.flayout = QHBoxLayout()
        self.flayout.setContentsMargins(0,0,100,0)
        self.flayout.setSpacing(0)
        self.widgetP.setLayout(self.flayout)
        self.setCentralWidget(self.widgetP)
        self.moduls = []
        self.actualitzats = []
        self.rellotge = QTimer(self)
        self.rellotge.timeout.connect(self.temporitzador) 
        self.rellotge.start(10)

    def temporitzador(self):
        self.rellotge.start(10)
        if len(self.actualitzats) > 0:
            for i in range(0,len(self.actualitzats)):
                self.flayout.itemAt(self.actualitzats[i]).widget().temporitzador()  
        self.conexio()
    
    def conexio(self):
        if len(self.moduls) > 0:
            for i in range(0,len(self.moduls)-1):
                self.flayout.itemAt(i+1).widget().entrada(self.flayout.itemAt(i).widget().value)    

    def crearModul1(self,nom):
        self.moduls.append(self.flayout.addWidget(Generador(self,nom))) 
        self.actualitzats.append(len(self.moduls)-1)

        
    def crearModul2(self,nom):
        self.moduls.append(self.flayout.addWidget(Visor(self,nom)))

    def crearModul3(self,nom):
        self.moduls.append(self.flayout.addWidget(Amplificador(self,nom)))
        self.actualitzats.append(len(self.moduls)-1)

    def crearModul4(self,nom):
        self.moduls.append(self.flayout.addWidget(Filtre(self,nom)))
        self.actualitzats.append(len(self.moduls)-1)
        
    

    def eliminarModul(self,index):
        self.moduls.pop(index)
        self.flayout.itemAt(index).widget().setParent(None)
        self.actualitzats.pop(index)

class thirdwindow(QMainWindow):
    indexEliminar = pyqtSignal(int)
    def __init__(self, parent):
        super().__init__()
        self.setGeometry(0,0,200,600)
        self.widgetList = QListWidget(self)
        self.widgetList.itemClicked.connect(self.eliminarElement)
        self.widgetList.setFixedHeight(600)

    def afegirElement(self,item):
        self.widgetList.addItem(item)
    
    def eliminarElement(self):
        index = self.widgetList.currentRow()
        self.widgetList.takeItem(index)
        self.indexEliminar.emit(index)

class FinPpal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pract4.ui',self)
        self.createWindows()
        self.segonafinestra.show()
        self.tercerafinestra.show()
        self.afegirGenerador.clicked.connect(self.nouGenerador)
        self.afegirVisor.clicked.connect(self.nouVisor)
        self.afegirAmplificador.clicked.connect(self.nouAmplificador)
        self.afegirFiltre.clicked.connect(self.nouFiltre)
        self.generadors = 0
        self.visors = 0
        self.filtres = 0
        self.amplificadors = 0
        self.tercerafinestra.indexEliminar.connect(self.eliminar)
        self.tancar.clicked.connect(self.sortir)

    

    def createWindows(self):
        self.segonafinestra = secondWindow(self)
        self.tercerafinestra = thirdwindow(self)

    def nouGenerador(self):
        self.segonafinestra.crearModul1("generador"+str(self.generadors))
        self.tercerafinestra.afegirElement("generador"+str(self.generadors))
        self.generadors += 1

    def nouVisor(self):
        self.segonafinestra.crearModul2("visor"+str(self.visors))
        self.tercerafinestra.afegirElement("visor"+str(self.visors))
        self.visors += 1

    def nouAmplificador(self):
        self.segonafinestra.crearModul3("amplificador"+str(self.amplificadors))
        self.tercerafinestra.afegirElement("amplificador"+str(self.amplificadors))
        self.amplificadors += 1

    def nouFiltre(self):
        self.segonafinestra.crearModul4("filtre"+str(self.filtres))
        self.tercerafinestra.afegirElement("filtre"+str(self.filtres))
        self.filtres += 1
        
    def eliminar(self):
        self.segonafinestra.eliminarModul(self.tercerafinestra.widgetList.currentRow())

    def sortir(self):
        self.segonafinestra.close()
        self.tercerafinestra.close()
        self.close()

app=QApplication([])
window=FinPpal()
window.show()
app.exec_()