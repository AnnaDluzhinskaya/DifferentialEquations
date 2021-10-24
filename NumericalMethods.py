import numexpr as ne
from math import pi


class NumericalMethods:
    def __init__(self, eS, eq, y_0, a, b, n):
        self.y_exact = []
        self.y_approx1 = []
        self.y_approx2 = []
        self.LTE = []
        self.GTE = []
        self.diff_equation = eq
        self.exact_eq = eS.exact_eq
        self.step = (b - a) / n
        self.numberOfSteps = n
        self.initialValueY = y_0

        self.x = []
        temp = a
        i = 0
        while temp < b:
            temp = a + self.step * i
            i = i + 1
            if temp == 0:
                temp = 0.0000001
            self.x.append(temp)

        for i in range(0, self.numberOfSteps + 1):
            if i == 0:
                self.y_exact.append(self.initialValueY)
            else:
                self.y_exact.append(self.substituteEq(self.x[i]))

    def substituteEq(self, x):
        temp_eq = self.exact_eq
        temp_eq = temp_eq.replace('x', str(x), temp_eq.count('x'))
        return 1 * ne.evaluate(temp_eq)

    def substituteDiff(self, x, y):
        temp_diff = self.diff_equation
        temp_diff = temp_diff.replace('x', str(x), temp_diff.count('x'))
        temp_diff = temp_diff.replace('y', str(y), temp_diff.count('y'))
        return 1 * ne.evaluate(temp_diff)

    def calculateLTE(self):
        for i in range(0, self.numberOfSteps + 1):
            if i == 0:
                self.LTE.append(0)
            else:
                self.LTE.append(abs(self.y_exact[i] - self.y_approx2[i]))
        return self.LTE

    def calculateGTE(self):
        for i in range(0, self.numberOfSteps + 1):
            if i == 0:
                self.GTE.append(0)
            else:
                self.GTE.append(abs(self.y_exact[i] - self.y_approx1[i]))
        return self.GTE
