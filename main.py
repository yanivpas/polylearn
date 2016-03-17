from machine_learning import PolyMachine

def polylearn(points):
    '''
    This function try to find a polynomial 
    which is close to the given points.
    '''
    bla = PolyMachine(points)
    p = bla.run()
    return p

def usage():
    # TODO
    return ""

def main():
    print usage()

if __name__ == '__main__':
    main()
