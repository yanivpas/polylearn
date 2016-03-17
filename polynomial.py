def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    # or:
    # for i in range(1,n):
    #   result *= i

def binomial(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

def convolotion(a, b):
    # THIS IS NOT CONVOLOTION YET... JUST POLYNOMIAL PRODUCT
    # TODO: it would be faster to implement FFT
    c = [0*(len(a)+len(b))]
    for index_a, coefficient_a in enumerate(a):
        for index_b, coefficient_b in enumerate(b):
            c[index_a + index_b] += coefficient_a*coefficient_b
    return c;
            

class Polynomial(object):
    def __init__(self, coefficients_vector):
        self.vector = coefficients_vector

    def __mul__(self, other):
        return polynomial(convolotion(self.vector, other.vector))

    def eval(self, value):
        result = 0
        for index, coefficient in enumerate(self.vector):
            result += coefficient*(value**index)

        return result
            
    def __call__(self, value):
        self.eval(value)

