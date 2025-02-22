import sys
import networkx as nx 
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

G = nx.DiGraph()

grafo = {"A":["C","B","D"],
        "B":["C","E"]}

for vertex, edges in grafo.items():
    G.add_node("%s"%vertex)
    for edge in edges:
        G.add_node("%s"%edge)
        G.add_edge("%s" %vertex,"%s"%edge,weight=15)
        #print("'%s' se conecta con '%s'"%(vertex,edge))

nx.draw(G, with_labels=True, node_size = 4000, node_color = "darkgray", edge_weight = 300)
plt.savefig("image.png", dpi = 55)

class ChildWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("ChildWindow.ui",self)
        self.setFocus()
        self.showGraph()
        
    def showGraph(self):
        label = QLabel(self)
        pixmap = QPixmap('image.png')#.scaled(390,320)
        label.resize(pixmap.width(),pixmap.height())       
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())