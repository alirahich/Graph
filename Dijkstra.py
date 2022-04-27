from PyQt5 import QtCore, QtGui, QtWidgets


from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.pyplot as plt 
import networkx as nx
#
from dijkstrac import Dijkstra







class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(827, 720)
        self.graph_View = QtWidgets.QGraphicsView(Dialog)
        self.graph_View.setGeometry(QtCore.QRect(70, 10, 600, 350))
        self.graph_View.setObjectName("graph_View")
        self.newnode_text = QtWidgets.QTextEdit(Dialog)
        self.newnode_text.setGeometry(QtCore.QRect(20, 430, 71, 41))
        self.newnode_text.setObjectName("newnode_text")
        self.node1_text = QtWidgets.QTextEdit(Dialog)
        self.node1_text.setGeometry(QtCore.QRect(180, 430, 71, 41))
        self.node1_text.setObjectName("node1_text")
        self.node2_text = QtWidgets.QTextEdit(Dialog)
        self.node2_text.setGeometry(QtCore.QRect(270, 430, 71, 41))
        self.node2_text.setObjectName("node2_text")
        self.weight_text = QtWidgets.QTextEdit(Dialog)
        self.weight_text.setGeometry(QtCore.QRect(360, 430, 71, 41))
        self.weight_text.setObjectName("weight_text")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(490, 430, 61, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(580, 430, 61, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(30, 360, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 400, 51, 16))
        self.label.setObjectName("label")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(550, 360, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(260, 360, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(200, 400, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(290, 400, 51, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(380, 400, 51, 16))
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(500, 400, 51, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(590, 400, 51, 16))
        self.label_14.setObjectName("label_14")
        self.addnode_button = QtWidgets.QPushButton(Dialog)
        self.addnode_button.setGeometry(QtCore.QRect(30, 490, 56, 17))
        self.addnode_button.setObjectName("addnode_button")
        self.connect_button = QtWidgets.QPushButton(Dialog)
        self.connect_button.setGeometry(QtCore.QRect(240, 490, 131, 20))
        self.connect_button.setObjectName("connect_button")
        self.run_button = QtWidgets.QPushButton(Dialog)
        self.run_button.setGeometry(QtCore.QRect(540, 490, 71, 17))
        self.run_button.setObjectName("run_button")
        self.resetgraph_button = QtWidgets.QPushButton(Dialog)
        self.resetgraph_button.setGeometry(QtCore.QRect(690, 640, 111, 41))
        self.resetgraph_button.setObjectName("resetgraph_button")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(160, 610, 461, 91))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(350, 590, 51, 16))
        self.label_15.setObjectName("label_15")


# self.G = nx.Graph()
        self.plot_canvas = PlotCanvas(self.graph_View)
        self.plot_canvas.setGeometry(QtCore.QRect(190, 30, 461, 301))
        self.plot_canvas.setObjectName("plot_canvas")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_11.setText(_translate("Dialog", "New Node"))
        self.label.setText(_translate("Dialog", "Node Name"))
        self.label_12.setText(_translate("Dialog", "Run"))
        self.label_4.setText(_translate("Dialog", "Connect Nodes"))
        self.label_5.setText(_translate("Dialog", "Node 1"))
        self.label_6.setText(_translate("Dialog", "Node 2"))
        self.label_7.setText(_translate("Dialog", "Weight"))
        self.label_13.setText(_translate("Dialog", "Source"))
        self.label_14.setText(_translate("Dialog", "Destination"))
        self.addnode_button.setText(_translate("Dialog", "Add Node"))
        self.connect_button.setText(_translate("Dialog", "Connect"))
        self.run_button.setText(_translate("Dialog", "Run"))
        self.resetgraph_button.setText(_translate("Dialog", "Reset Graph"))
        self.label_15.setText(_translate("Dialog", "Reselt"))
        
class PlotCanvas(FigureCanvas): # By inheriting the FigureCanvas class, this class is both a PyQt5 Qwidget and a Matplotlib FigureCanvas, which is the key to connecting pyqt5 and matplotlib
    """A UI element to plotting networkx graph on window.
    """
    def __init__(self, parent=None):
        """Constructor of PlotCanvas class.

        Args:
            parent (optional): Parent should be Qt widget. Defaults to None.
        """
        FigureCanvas.__init__(self)
        self.setParent(parent)
        self.figure = plt.figure()
        FigureCanvas.updateGeometry(self)
       

    def plot(self, G):
        """Plotting all nodes and edges of graph with labels.

        Args:
            G (nx.Graph): Graph.
        """
        self.figure.clf()
        pos=nx.spring_layout(G, seed=42)

        #Drawing graph on canvas in UI.
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw(G, pos, with_labels=True, font_size=11, node_size=150, node_color="r", font_color="w")
        self.draw_idle()

##################################
class GUI(QtWidgets.QWidget):
    """Main GUI class to handle UI and controller functions.

    Args:
        QtWidgets.QMainWindow()
    """
    def __init__(self):
        """Constructor of GUI.
        """
        super(GUI, self).__init__()
        self.algo = None
        self.setup_gui()
        

    def setup_gui(self):
        """Initializer of GUI.
        """
        self.form = Ui_Dialog()
        self.form.setupUi(self)
        self.G = nx.Graph()
        

        #Controllers
        self.form.addnode_button.clicked.connect(self.add_new_node)
        self.form.connect_button.clicked.connect(self.connect_nodes)
        self.form.run_button.clicked.connect(self.run)
        self.form.resetgraph_button.clicked.connect(self.reset)
        
    def show_dialog(self, message):
        """Opening a new error window with a given error message.

        Args:
            message (string): error text.
        """
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def add_new_node(self):
        """ Adding a new node to the Graph. 
        """


        new_node = str(self.form.newnode_text.toPlainText())
        if not new_node:
            self.form.newnode_text.clear()
            self.show_dialog("Empty argument.")
            return
        
        self.form.newnode_text.clear()
        
        if self.G.has_node(new_node):
            self.show_dialog(f"{new_node} is already constructed.")
        
        else:
            self.G.add_node(new_node)
            self.form.plot_canvas.plot(self.G)
       
        

    def connect_nodes(self):
        """Connects two nodes with a given weight. 
        """
        node1 = str(self.form.node1_text.toPlainText())
        node2 = str(self.form.node2_text.toPlainText())
        weight = str(self.form.weight_text.toPlainText())
        self.form.node1_text.clear()
        self.form.node2_text.clear()
        self.form.weight_text.clear()

        if not node1 or not node2 or not weight:      
            self.show_dialog("Empty argument.")
            return
        
        try:
            weight = int(weight)
        except:
            self.show_dialog("Weight should be an integer.")
            return

        if self.G.has_edge(node1, node2):
            self.show_dialog(f"Edge: {node1, node2} is already constructed.")

        else:
            self.G.add_edge(node1, node2, weight=weight)
            self.form.plot_canvas.plot(self.G)

    def setAlgo(self, algo):
        self.algo = algo
        

    def run(self):
        """Takes source and destination from user and runs the Dijkstra algorithm to calculate shortest path.
        """

        source = str(self.form.textEdit.toPlainText())
        dest = str(self.form.textEdit_2.toPlainText())
        algos =  {  
                'Dijkstra': Dijkstra,
                'Prime': Dijkstra,
                'DFS': Dijkstra,
                'BFS': Dijkstra,
                'Kruskal': Dijkstra,
                'Bellman-Ford': Dijkstra,
                'Ford Fulkerson': Dijkstra
            }
        
        self.form.textEdit.clear()
        self.form.textEdit_2.clear()
        
        if not source or not dest:
            self.show_dialog("Empty argument.")
            return 

        if self.G.has_node(source) and self.G.has_node(dest):
            if source in nx.algorithms.descendants(self.G, dest):
                graph = nx.to_dict_of_dicts(self.G) # converting to dict based graph.
                currentAlgo = algos[self.algo](graph)
                parents,  visited = currentAlgo.find_route(source, dest)
                shortest_path = currentAlgo.generate_path(parents, source, dest)
                shortest_path = " -> ".join(shortest_path)
                result = f"Distance is {visited[dest]} units.\nShortest path from {source} to {dest} is {shortest_path}"
                self.form.textEdit_3.setText(result)
            else:
                self.show_dialog(f"There is no connection between {source} and {dest}.")
        else:
            self.show_dialog(f"Please check source and destination.")
        

    def reset(self):
        """Resets the existing graph.
        """
        self.G = nx.Graph()
        self.form.plot_canvas.plot(self.G)


      

#app = QtWidgets.QApplication([])
#run_app = GUI()
# run_app.show()

# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
# MainWindow.show()  


# sys.exit(app.exec_())





        
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())"""
