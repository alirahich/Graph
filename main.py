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
        self.w = None

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

        btn0.clicked.connect(self.openWindow)
        btn1.clicked.connect(self.openWindow)
        btn2.clicked.connect(self.openWindow)
        btn3.clicked.connect(self.openWindow)
        btn4.clicked.connect(self.openWindow)
        btn5.clicked.connect(self.openWindow)
        btn6.clicked.connect(self.openWindow)
        btn7.clicked.connect(self.openWindow)

        self.statusBar()

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Menu-Graphs')
        self.show()

    def openWindow(self):
        algo = self.sender().text()
        self.w = GUI()
        self.w.setAlgo(algo)
        self.w.show()

def main():
    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()