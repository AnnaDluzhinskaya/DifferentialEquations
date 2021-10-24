from NumericalMethods import NumericalMethods


class ImprovedEuler(NumericalMethods):
    def solveTask(self):
        for i in range(0, self.numberOfSteps + 1):
            if i == 0:
                self.y_approx1.append(self.initialValueY)
                self.y_approx2.append(self.initialValueY)
            else:
                self.y_approx1.append(self.y_approx1[i - 1] + self.step * self.substituteDiff((self.x[i - 1] + self.step / 2),
                                     (self.y_approx1[i - 1] + self.step / 2 * self.substituteDiff(self.x[i - 1], self.y_approx1[i - 1]))))
                self.y_approx2.append(self.y_exact[i - 1] + self.step * self.substituteDiff((self.x[i - 1] + self.step / 2),
                                     (self.y_exact[i - 1] + self.step / 2 * self.substituteDiff(self.x[i-1],self.y_exact[i - 1]))))