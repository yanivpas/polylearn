from math import sqrt 

# TODO: if we want to do this module nicely we need to add a vector object and implement scalar mul...
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
        return self.matrix

    def colums(self):
        colums = []
        for i in range(self.dim[1]):
            colums.append([raw[i] for raw in self.raws()])
        return colums
    
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

        bais.append(new_vector*(1/norm(new_vector)))
    return [e.vector for e in bais]

def QRdecomposition(matrix):
    '''
    for colum in matrix.colums():
        normal = norm(colum)
        Q.append([a/normal for a in colum])
        '''

    Q = gramschmidt(matrix.colums())
    Q = Matrix(Q).transpose()

    R = Q.transpose()*matrix

    return (Q,R)
        

