from polynomial import Polynomial

def squard_loss(h, point):
    (x, y) = point
    return (h(x) -y)**2

def mean_squared_err(h, sample):
    result = 0
    for point in sample:
        result = squard_loss(h, point)

    return result/len(sample)


class LinearMachine(object):
    def __init__(self, sample):
        self.sample = sample
        # TODO: check that all the vectors in the sample are in the same dimentation
        # FIXME:
        self.dim = len(sample[0][0])

class PolyMachine(object):
    def __init__(self, sample):
        pass
