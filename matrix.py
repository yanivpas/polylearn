from math import sqrt
from itertools import product
from copy import deepcopy

EPSILON = 0.00000001

# TODO: if we want to do this module nicely we need to add a vector object and implement scalar mul...
# TODO: refactor this all file.
def dot(vector_a, vector_b):
    result = 0
    for a, b in zip(vector_a, vector_b):
        result += a*b
    return result
        
def norm(a):
    return sqrt(dot(a, a))
            
            
class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        # TODO: check that the dim is correct...
        self.dim = (len(matrix), len(matrix[0]))

    def raws(self):
        return deepcopy(self.matrix)

    def colums(self):
        colums = []
        for i in range(self.dim[1]):
            colums.append([raw[i] for raw in self.raws()])
        return deepcopy(colums)
    
    def transpose(self):
        return Matrix(self.colums())

    def __mul__(self, other):
        if self.dim[0] != other.dim[1]:
            raise Exception("can't mul matrices")

        new_matrix = []
        for raw in self.raws():
            new_raw = []
            for colum in other.colums():
                new_raw.append(dot(raw, colum))
            new_matrix.append(new_raw)

        return Matrix(new_matrix)

    def mul(self, vector):
        new_vector = []
        for raw in self.raws():
            new_vector.append(dot(raw, vector))

        return new_vector

    def normaize(self):
        new_matrix = []
        for raw in self.raws():
            new_raw = []
            for value in raw:
                if abs(value) < EPSILON:
                    new_raw.append(0)
                else:
                    new_raw.append(value)
            new_matrix.append(new_raw)
        self.matrix = new_matrix


class Vector(object):
    def __init__(self, vector):
        self.vector = vector
        self.dim = len(vector)
    def __add__(self, other):
        new_vector = []
        for a, b in zip(self.vector, other.vector):
            new_vector.append(a+b)
        return Vector(new_vector)

    def __mul__(self, scalar):
        new_vector = []
        for a in self.vector:
            new_vector.append(scalar*a)
        return Vector(new_vector)

    def __iter__(self):
        return iter(self.vector)

def gramschmidt(vectors):
    bais = []
    vectors = [Vector(vector) for vector in vectors]
    for vector in vectors:
        proj = Vector([0]*vector.dim)
        for e in bais:
            proj += e*(-1*dot(vector, e))

        new_vector = vector + proj

        if norm(new_vector) < EPSILON:
            bais.append(Vector([0]*vector.dim))
        else:
            e = new_vector*(1/norm(new_vector))
            bais.append(e)

    return [e.vector for e in bais]

def QRdecomposition(matrix):
    Q = gramschmidt(matrix.colums())
    Q = Matrix(Q).transpose()

    R = Q.transpose()*matrix
    R.normaize()
    
    return (Q,R)
        

def psudorank(R):
    rank = 0
    for raw in R.raws():
        rank += 1 if norm(raw) != 0 else 0
    return rank

def solveQR(Q, R, y):
    y = Q.transpose().mul(y)
    dim = psudorank(R)

    y = y[:dim]
    y.reverse()
    raws = R.raws()[:dim]
    raws.reverse()
    b = []
    for raw, value in zip(raws, y):
        raw.reverse()
        raw_len = len([a for a in raw if a != 0])
        b += [1]*(raw_len-len(b)-1)
        if (raw[len(b)] != 0):
            b.append((value -dot(b, raw[:len(b)]))/raw[len(b)])
        else:
            b.append(0)

    b.reverse()
    return b
            

