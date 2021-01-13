import numpy as np

def get_big_numpy_kern(params):
    outer = params[0]
    middle = params[1]
    inner = params[2]
    kernel = [[outer, outer, outer, outer, outer],
              [outer, middle, middle, middle, outer],
              [outer, middle, inner, middle, outer],
              [outer, middle, middle, middle, outer],
              [outer, outer, outer, outer, outer]]
    return np.array(kernel)

def get_biggest_numpy_kern(params):
    veryVeryOuterEdge = params[0]
    veryOuterEdge = params[1]
    outerEdge = params[2]
    edge = params[3]
    outer = params[4]
    middle = params[5]
    inner = params[6]

    kernel = [[veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge],
              [veryVeryOuterEdge, veryOuterEdge, veryOuterEdge, veryOuterEdge, veryOuterEdge, veryOuterEdge, veryOuterEdge, veryOuterEdge, veryOuterEdge, veryOuterEdge, veryOuterEdge, veryOuterEdge, veryVeryOuterEdge],
              [veryVeryOuterEdge, veryOuterEdge, outerEdge, outerEdge, outerEdge, outerEdge, outerEdge, outerEdge, outerEdge, outerEdge, outerEdge, veryOuterEdge, veryVeryOuterEdge],
              [veryVeryOuterEdge, veryOuterEdge, outerEdge, edge, edge, edge, edge, edge, edge, edge, outerEdge, veryOuterEdge, veryVeryOuterEdge],
              [veryVeryOuterEdge, veryOuterEdge, outerEdge, edge, outer, outer, outer, outer, outer, edge, outerEdge, veryOuterEdge, veryVeryOuterEdge],
              [veryVeryOuterEdge, veryOuterEdge, outerEdge, edge, outer, middle, middle, middle, outer, edge, outerEdge, veryOuterEdge, veryVeryOuterEdge],
              [veryVeryOuterEdge, veryOuterEdge, outerEdge, edge, outer, middle, inner, middle, outer, edge, outerEdge, veryOuterEdge, veryVeryOuterEdge],
              [veryVeryOuterEdge, veryOuterEdge, outerEdge, edge, outer, middle, middle, middle, outer, edge, outerEdge, veryOuterEdge, veryVeryOuterEdge],
              [veryVeryOuterEdge, veryOuterEdge, outerEdge, edge, outer, outer, outer, outer, outer, edge, outerEdge, veryOuterEdge, veryVeryOuterEdge],
              [veryVeryOuterEdge, veryOuterEdge, outerEdge, edge, edge, edge, edge, edge, edge, edge, outerEdge, veryOuterEdge, veryVeryOuterEdge],
              [veryVeryOuterEdge, veryOuterEdge, outerEdge, outerEdge, outerEdge, outerEdge, outerEdge, outerEdge, outerEdge, outerEdge, outerEdge, veryOuterEdge, veryVeryOuterEdge],
              [veryVeryOuterEdge, veryOuterEdge, veryOuterEdge, veryOuterEdge, veryOuterEdge, veryOuterEdge, veryOuterEdge, veryOuterEdge, veryOuterEdge, veryOuterEdge, veryOuterEdge, veryOuterEdge, veryVeryOuterEdge],
              [veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge, veryVeryOuterEdge]]
    return np.array(kernel)

def get_kern(size):
    return np.ones((size, size))