import math

class assets:
    number_coof = 4
    delta_x = 0.001

    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

    Lamda = 1j

    formula = ''

    def __init__(self, number_coof):
        self.number_coof = number_coof
        self.coof = [0j+0] * self.number_coof
    
    def f(self, x):
        '''
        ans = 0
        for i in range(len(self.coof)):
            ans += (x ** (i)) * self.coof[i]
        return ans
        '''
        #return x**4 + x**3 - x**2 - 5
        return eval(self.formula)

    def complex_derivative_f(self, x):
        z = complex(x.real + self.delta_x, x.imag + self.delta_x)
        derivative = (self.f(z) - self.f(x)) / (z - x)

        return derivative
    
    def real_derivative_f(self, x):
        answer = (self.f(x + self.delta_x) - self.f(x)) / (self.delta_x)

        return answer

    def magnitude(self, x):
        return math.sqrt(x.real ** 2 + x.imag ** 2)