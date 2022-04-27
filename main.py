#!/usr/bin/python

"""
ZetCode PyQt5 tutorial

In this example, we determine the event sender
object.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from Dijkstra import GUI
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Menu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.algos = {  
                        'Dijkstra': GUI(),
                        'Prime': GUI(),
                        'DFS': GUI(),
                        'BFS':  GUI(),
                        'Kruskal': GUI(),
                        'Bellman-Ford': GUI(),
                        'Ford Fulkerson': GUI()
                    }

        self.initUI()
    def initUI(self):

        btn0 = QPushButton("Dijkstra", self)
        btn0.move(50, 50)

        btn1 = QPushButton("Prime", self)
        btn1.move(50, 100)

        btn2 = QPushButton("DFS", self)
        btn2.move(50, 150)
        
        btn3 = QPushButton("BFS", self)
        btn3.move(50, 200)

        btn4 = QPushButton("Kruskal", self)
        btn4.move(150, 50)

        btn5 = QPushButton("Bellman-Ford", self)
        btn5.move(150, 100)
        
        btn6 = QPushButton("Ford Fulkerson", self)
        btn6.move(150, 150)

        btn7 = QPushButton("Warshall", self)
        btn7.move(150, 200)

        btn0.clicked.connect(self.buttonClicked)
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        btn3.clicked.connect(self.buttonClicked)
        btn4.clicked.connect(self.buttonClicked)
        btn5.clicked.connect(self.buttonClicked)
        btn6.clicked.connect(self.buttonClicked)
        btn7.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Menu-Graphs')
        self.show()

    def openWindow(self, algo):
        self.w = self.algos[algo]
        self.w.show()
    
    def buttonClicked(self):
        sender = self.sender()
        for algo in self.algos.keys():
            if sender.text() == algo:
                self.openWindow(algo)


def main():
    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()