import numexpr as ne
from math import pi


class ExactSolution:
    def __init__(self, eq, y0, x0):
        self.exact_eq = eq
        if x0 != 0:
            self.x = x0
            if x0 == float(pi) and y0 == 1.0:
                self.x = "pi"
                self.exact_eq = eq.replace("c", '(1/pi)', eq.count("c"))
            elif x0 != 0:
                c = "(y-x*sin(x))/x"
                c = c.replace("x", str(x0), c.count("x"))
                c = c.replace("y", str(y0), c.count("y"))
                c = 1 * ne.evaluate(c)
                self.x = round(self.x, 4)
                self.exact_eq = eq.replace("c", "("+str(round(c, 4))+")", eq.count("c"))
        elif x0 == 0:
            x0 = 0.0000001
            self.x = x0
            c = "(y-x*sin(x))/x"
            c = c.replace("x", str(x0), c.count("x"))
            c = c.replace("y", str(y0), c.count("y"))
            c = 1 * ne.evaluate(c)
            self.x = round(self.x, 7)
            self.exact_eq = eq.replace("c", str(round(c, 4)), eq.count("c"))



