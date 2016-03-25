from polynomial import Polynomial
from matrix import Matrix, QRdecomposition, solveQR

MAX_DEGREE = 20
EPSILON = 0.0000001

def squard_loss(h, point):
    (x, y) = point
    return (h(x) -y)**2

def mean_squared_err(h, sample):
    result = 0
    for point in sample:
        result = squard_loss(h, point)

    return result/len(sample)




class PolyMachine(object):
    def __init__(self, sample):
        self.sample = sample

    def polynomial(self, degree):
        raws = []
        vector = []
        for (x, y) in self.sample:
            raws.append([x**i for i in range(0, degree)])
            vector.append(y)

        A = Matrix(raws)
        (Q, R) = QRdecomposition(A)
        result = solveQR(Q, R, vector)
        return Polynomial(result)

    def run(self):
        polynomials = []
        for degree in range(1, MAX_DEGREE):
            p = self.polynomial(degree)
            polynomials.append(p)
            print "polynomial: ", p.vector, " mean:", mean_squared_err(p, self.sample)
            if mean_squared_err(p, self.sample) < EPSILON:
                break

        return p

        

