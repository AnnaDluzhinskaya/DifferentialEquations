import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from Euler import Euler
from ExactSolution import ExactSolution
from Graph import Graph
from ImprovedEuler import ImprovedEuler
from NumericalMethods import NumericalMethods
from RungeKutta import RungeKutta
from View import Window
import numexpr as ne
from math import pi


class MyApp(QMainWindow, Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Analyzing Differential Equation")

        self.graph_page1 = Graph(self.graph_page1)
        self.graph_page1.createGraph([], [], [])

        self.graph_page2 = Graph(self.graph_page2)
        self.graph_page2.createGraph([], [], [])

        self.graph_page3 = Graph(self.graph_page3)
        self.graph_page3.createGraph([], [], [])

        self.button_page1.clicked.connect(self.createPage1Graph)
        self.button_page2.clicked.connect(self.createPage2Graph)
        self.button_page3.clicked.connect(self.createPage3Graph)

        self.save_exact_eq = self.exact_equation.toPlainText()

    def createPage1Graph(self):
        
        if "c" in self.exact_equation.toPlainText():
            self.save_exact_eq = self.exact_equation.toPlainText()

        ex = ExactSolution(self.save_exact_eq, float(ne.evaluate(self.textEdit_2.toPlainText())),
                           float(ne.evaluate(self.textEdit.toPlainText())))

        self.exact_equation.setText(ex.exact_eq)
        self.textEdit.setText(str(ex.x))

        nm = NumericalMethods(ex, self.diff_equation.toPlainText(),
                              float(ne.evaluate(self.textEdit_2.toPlainText())),
                              float(ne.evaluate(self.textEdit.toPlainText())),
                              float(ne.evaluate(self.textEdit_3.toPlainText())),
                              int(self.textEdit_4.toPlainText()))
        color = ['r']
        list_x = nm.x
        list_y = [nm.y_exact]

        if self.checkBox.checkState():
            em = Euler(ex, self.diff_equation.toPlainText(),
                       float(ne.evaluate(self.textEdit_2.toPlainText())),
                       float(ne.evaluate(self.textEdit.toPlainText())),
                       float(ne.evaluate(self.textEdit_3.toPlainText())),
                       int(self.textEdit_4.toPlainText()))
            em.solveTask()
            list_y.append(em.y_approx1)
            color.append('b')
        if self.checkBox_2.checkState():
            ie = ImprovedEuler(ex, self.diff_equation.toPlainText(),
                              float(ne.evaluate(self.textEdit_2.toPlainText())),
                              float(ne.evaluate(self.textEdit.toPlainText())),
                              float(ne.evaluate(self.textEdit_3.toPlainText())),
                              int(self.textEdit_4.toPlainText()))
            ie.solveTask()
            list_y.append(ie.y_approx1)
            color.append('g')
        if self.checkBox_3.checkState():
            rk = RungeKutta(ex, self.diff_equation.toPlainText(),
                            float(ne.evaluate(self.textEdit_2.toPlainText())),
                            float(ne.evaluate(self.textEdit.toPlainText())),
                            float(ne.evaluate(self.textEdit_3.toPlainText())),
                            int(self.textEdit_4.toPlainText()))
            rk.solveTask()
            list_y.append(rk.y_approx1)
            color.append('y')

        self.graph_page1.createGraph(list_x, list_y, color)

    def createPage2Graph(self):
        ex = ExactSolution(self.save_exact_eq, float(ne.evaluate(self.textEdit_2.toPlainText())),
                           float(ne.evaluate(self.textEdit.toPlainText())))

        nm = NumericalMethods(ex, self.diff_equation.toPlainText(),
                              float(ne.evaluate(self.textEdit_2.toPlainText())),
                              float(ne.evaluate(self.textEdit.toPlainText())),
                              float(ne.evaluate(self.textEdit_3.toPlainText())),
                              int(self.textEdit_4.toPlainText()))
        color = []
        list_x = nm.x
        list_y = []


        if self.checkBox_4.checkState():
            em = Euler(ex, self.diff_equation.toPlainText(),
                       float(ne.evaluate(self.textEdit_2.toPlainText())),
                       float(ne.evaluate(self.textEdit.toPlainText())),
                       float(ne.evaluate(self.textEdit_3.toPlainText())),
                       int(self.textEdit_4.toPlainText()))
            em.solveTask()
            list_y.append(em.calculateLTE())
            color.append('b')
        if self.checkBox_5.checkState():
            ie = ImprovedEuler(ex, self.diff_equation.toPlainText(),
                              float(ne.evaluate(self.textEdit_2.toPlainText())),
                              float(ne.evaluate(self.textEdit.toPlainText())),
                              float(ne.evaluate(self.textEdit_3.toPlainText())),
                              int(self.textEdit_4.toPlainText()))
            ie.solveTask()
            list_y.append(ie.calculateLTE())
            color.append('g')
        if self.checkBox_6.checkState():
            rk = RungeKutta(ex, self.diff_equation.toPlainText(),
                            float(ne.evaluate(self.textEdit_2.toPlainText())),
                            float(ne.evaluate(self.textEdit.toPlainText())),
                            float(ne.evaluate(self.textEdit_3.toPlainText())),
                            int(self.textEdit_4.toPlainText()))
            rk.solveTask()
            list_y.append(rk.calculateLTE())
            color.append('y')

        self.graph_page2.createGraph(list_x, list_y, color)

    def createPage3Graph(self):
        ex = ExactSolution(self.save_exact_eq, float(ne.evaluate(self.textEdit_2.toPlainText())),
                           float(ne.evaluate(self.textEdit.toPlainText())))

        color = []
        list_x = [i for i in range(int(self.textEdit_9.toPlainText()), int(self.textEdit_10.toPlainText())+1)]
        list_y = []

        if self.checkBox_10.checkState():
            temp_y = []
            for i in list_x:
                em = Euler(ex, self.diff_equation.toPlainText(),
                           float(ne.evaluate(self.textEdit_2.toPlainText())),
                           float(ne.evaluate(self.textEdit.toPlainText())),
                           float(ne.evaluate(self.textEdit_3.toPlainText())), i)
                em.solveTask()
                temp_y.append(em.calculateGTE()[-1])
            list_y.append(temp_y)
            color.append('b')
        if self.checkBox_11.checkState():
            temp_y = []
            for i in list_x:
                ie = ImprovedEuler(ex, self.diff_equation.toPlainText(),
                                   float(ne.evaluate(self.textEdit_2.toPlainText())),
                                   float(ne.evaluate(self.textEdit.toPlainText())),
                                   float(ne.evaluate(self.textEdit_3.toPlainText())), i)
                ie.solveTask()
                temp_y.append(ie.calculateGTE()[-1])
            list_y.append(temp_y)
            color.append('g')
        if self.checkBox_12.checkState():
            temp_y = []
            for i in list_x:
                rk = RungeKutta(ex, self.diff_equation.toPlainText(),
                                float(ne.evaluate(self.textEdit_2.toPlainText())),
                                float(ne.evaluate(self.textEdit.toPlainText())),
                                float(ne.evaluate(self.textEdit_3.toPlainText())), i)
                rk.solveTask()
                temp_y.append(rk.calculateGTE()[-1])
            list_y.append(temp_y)
            color.append('y')

        self.graph_page3.createGraph(list_x, list_y, color)


def application():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()