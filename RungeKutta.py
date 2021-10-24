from NumericalMethods import NumericalMethods


class RungeKutta(NumericalMethods):
    def solveTask(self):
        for i in range(0, self.numberOfSteps + 1):
            if i == 0:
                self.y_approx1.append(self.initialValueY)
                self.y_approx2.append(self.initialValueY)
            else:
                k1 = self.substituteDiff(self.x[i-1], self.y_approx1[i - 1])
                k2 = self.substituteDiff((self.x[i-1] + self.step / 2), (self.y_approx1[i - 1] + self.step * k1 / 2))
                k3 = self.substituteDiff((self.x[i-1] + self.step / 2), (self.y_approx1[i - 1] + self.step * k2 / 2))
                k4 = self.substituteDiff((self.x[i-1] + self.step), (self.y_approx1[i - 1] + self.step * k3))

                self.y_approx1.append(self.y_approx1[i - 1] + self.step * (k1 + 2 * k2 + 2 * k3 + k4) / 6)

                k1 = self.substituteDiff(self.x[i-1], self.y_exact[i - 1])
                k2 = self.substituteDiff((self.x[i-1] + self.step / 2), (self.y_exact[i - 1] + self.step * k1 / 2))
                k3 = self.substituteDiff((self.x[i-1] + self.step / 2), (self.y_exact[i - 1] + self.step * k2 / 2))
                k4 = self.substituteDiff((self.x[i-1] + self.step), (self.y_exact[i - 1] + self.step * k3))

                self.y_approx2.append(self.y_exact[i - 1] + self.step * (k1 + 2 * k2 + 2 * k3 + k4) / 6)
