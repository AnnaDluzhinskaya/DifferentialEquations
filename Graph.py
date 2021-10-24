from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class Graph(QWidget):
    def __init__(self, parent=None, dpi=75):
        super(Graph, self).__init__(parent)
        self.labels = {'r': "Exact Solution", 'b': "Euler", 'g': "ImprovedEuler", 'y': "RungeKutta"}
        self.figure = Figure(dpi=dpi)
        self.canvas = Canvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def createGraph(self, x, y, color):
        self.figure.clear()
        ax = self.figure.add_subplot(1, 1, 1)

        ax.grid(which='minor')
        ax.grid(which='major')

        for i in range(len(y)):
            ax.plot(x, y[i], color[i], label=self.labels[color[i]])
        if len(y) != 0:
            ax.legend()

        self.canvas.draw()
